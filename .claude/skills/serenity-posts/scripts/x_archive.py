#!/usr/bin/env python3
"""Archive an X account's posts through the official X API v2 and render them as Markdown.

Needs a bearer token from developer.x.com in the X_BEARER_TOKEN environment variable.
Uses only the Python standard library.

  python3 x_archive.py fetch --user aleabitoreddit --since 2025-07-01
  python3 x_archive.py fetch --user aleabitoreddit --since 2025-07-01 --mode search
  python3 x_archive.py render

fetch merges new posts into data/raw.jsonl (safe to re-run for updates).
render rebuilds posts/YYYY-MM.md and posts/index.md from data/raw.jsonl.

--mode timeline (default) works on lower API tiers but only reaches the
~3,200 most recent posts. --mode search uses full-archive search, which needs
a higher API tier but has no such cap.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

API = "https://api.x.com/2"
SKILL_DIR = Path(__file__).resolve().parent.parent
RAW = SKILL_DIR / "data" / "raw.jsonl"
META = SKILL_DIR / "data" / "meta.json"
POSTS = SKILL_DIR / "posts"
TWEET_FIELDS = ",".join([
    "created_at", "public_metrics", "conversation_id", "referenced_tweets",
    "entities", "note_tweet", "in_reply_to_user_id", "lang",
])


def api_get(path, params, token):
    url = f"{API}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "User-Agent": "x-archive/1.0",
    })
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                reset = int(e.headers.get("x-rate-limit-reset", time.time() + 60))
                wait = max(5, reset - int(time.time()) + 2)
                print(f"rate limited, waiting {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            if e.code >= 500:
                time.sleep(2 ** attempt)
                continue
            body = e.read().decode(errors="replace")
            sys.exit(f"HTTP {e.code} on {path}: {body}")
        except urllib.error.URLError as e:
            if attempt == 5:
                sys.exit(f"network error on {path}: {e.reason}")
            time.sleep(2 ** attempt)
    sys.exit(f"giving up on {path} after repeated failures")


def load_raw():
    posts = {}
    if RAW.exists():
        with RAW.open(encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    t = json.loads(line)
                    posts[t["id"]] = t
    return posts


def fetch(args):
    token = os.environ.get("X_BEARER_TOKEN")
    if not token:
        sys.exit("X_BEARER_TOKEN is not set")

    user = api_get(f"/users/by/username/{args.user}", {"user.fields": "created_at,name"}, token)["data"]
    print(f"user: {user['name']} (@{user['username']}), id {user['id']}")

    params = {
        "max_results": 100,
        "start_time": f"{args.since}T00:00:00Z",
        "tweet.fields": TWEET_FIELDS,
        "expansions": "referenced_tweets.id",
    }
    if args.mode == "timeline":
        path, page_key = f"/users/{user['id']}/tweets", "pagination_token"
        params["exclude"] = "retweets" if args.include_replies else "retweets,replies"
    else:
        path, page_key = "/tweets/search/all", "next_token"
        query = f"from:{args.user} -is:retweet"
        if not args.include_replies:
            query += " -is:reply"
        params["query"] = query

    posts = load_raw()
    before = len(posts)
    pages = 0
    while True:
        page = api_get(path, params, token)
        refs = {t["id"]: t for t in page.get("includes", {}).get("tweets", [])}
        for t in page.get("data", []):
            t["_refs"] = [
                {"type": r["type"], "id": r["id"], "text": refs.get(r["id"], {}).get("text")}
                for r in t.get("referenced_tweets", [])
            ]
            posts[t["id"]] = t
        pages += 1
        print(f"page {pages}: {len(page.get('data', []))} posts, total {len(posts)}")
        token_next = page.get("meta", {}).get("next_token")
        if not token_next:
            break
        params[page_key] = token_next
        if args.mode == "search":
            time.sleep(1.1)  # full-archive search allows about one request per second

    RAW.parent.mkdir(parents=True, exist_ok=True)
    with RAW.open("w", encoding="utf-8") as f:
        for pid in sorted(posts, key=int):
            f.write(json.dumps(posts[pid], ensure_ascii=False) + "\n")
    META.write_text(json.dumps({
        "username": user["username"], "name": user["name"], "id": user["id"],
        "since": args.since, "mode": args.mode, "include_replies": args.include_replies,
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"done: {len(posts) - before} new, {len(posts)} total in {RAW}")
    if args.mode == "timeline" and len(posts) >= 3000:
        print("note: the timeline endpoint stops near 3,200 posts; use --mode search for older ones")


def full_text(t):
    return (t.get("note_tweet") or {}).get("text") or t["text"]


def kind(t):
    types = {r["type"] for r in t.get("_refs", [])}
    if "replied_to" in types:
        return "回复"
    if "quoted" in types:
        return "引用"
    return "原创"


def cashtags(t):
    ent = (t.get("note_tweet") or {}).get("entities") or t.get("entities") or {}
    return {c["tag"].upper() for c in ent.get("cashtags", [])}


def render(args):
    posts = sorted(load_raw().values(), key=lambda t: int(t["id"]))
    if not posts:
        sys.exit(f"no posts in {RAW}; run fetch first")
    meta = json.loads(META.read_text(encoding="utf-8")) if META.exists() else {}
    handle = meta.get("username", "aleabitoreddit")
    name = meta.get("name", "Serenity")

    by_month = defaultdict(list)
    for t in posts:
        by_month[t["created_at"][:7]].append(t)

    POSTS.mkdir(parents=True, exist_ok=True)
    for old in POSTS.glob("*.md"):
        old.unlink()

    for month, items in sorted(by_month.items()):
        lines = [
            f"# {name} (@{handle}) · {month}",
            "",
            f"{len(items)} 条帖子。来源：X API，仅供个人研究，不构成投资建议。",
            "",
        ]
        for t in items:
            m = t.get("public_metrics", {})
            when = t["created_at"][:16].replace("T", " ")
            tags = " ".join(f"${c}" for c in sorted(cashtags(t)))
            lines += [
                f"## {when} UTC · {kind(t)} · [原帖](https://x.com/{handle}/status/{t['id']})",
                "",
                f"❤ {m.get('like_count', 0)} · 🔁 {m.get('retweet_count', 0)} · "
                f"💬 {m.get('reply_count', 0)} · 👁 {m.get('impression_count', 0)}"
                + (f" · {tags}" if tags else ""),
                "",
            ]
            for r in t.get("_refs", []):
                if r.get("text"):
                    label = "回复的帖子" if r["type"] == "replied_to" else "引用的帖子"
                    quoted = r["text"].replace("\n", "\n> ")
                    lines += [f"> **{label}：** {quoted}", ""]
            lines += [full_text(t), "", "---", ""]
        (POSTS / f"{month}.md").write_text("\n".join(lines), encoding="utf-8")

    tag_count, first_seen, last_seen = Counter(), {}, {}
    for t in posts:
        day = t["created_at"][:10]
        for c in cashtags(t):
            tag_count[c] += 1
            first_seen.setdefault(c, day)
            last_seen[c] = day

    index = [
        f"# {name} (@{handle}) 帖子索引",
        "",
        f"共 {len(posts)} 条，时间 {posts[0]['created_at'][:10]} 至 {posts[-1]['created_at'][:10]}。"
        f"抓取于 {meta.get('fetched_at', '未知')}。",
        "",
        "## 按月份",
        "",
        "| 月份 | 帖子数 | 文件 |",
        "|---|---|---|",
    ]
    index += [f"| {mo} | {len(it)} | [{mo}.md]({mo}.md) |" for mo, it in sorted(by_month.items())]
    index += [
        "",
        "## 提到最多的股票代码（$cashtag）",
        "",
        "| 代码 | 次数 | 第一次提到 | 最近一次提到 |",
        "|---|---|---|---|",
    ]
    index += [
        f"| ${c} | {n} | {first_seen[c]} | {last_seen[c]} |"
        for c, n in tag_count.most_common(80)
    ]
    (POSTS / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"rendered {len(posts)} posts into {len(by_month)} month files under {POSTS}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch", help="download posts into data/raw.jsonl")
    f.add_argument("--user", default="aleabitoreddit")
    f.add_argument("--since", default="2025-07-01", help="YYYY-MM-DD, UTC")
    f.add_argument("--mode", choices=["timeline", "search"], default="timeline")
    f.add_argument("--no-replies", dest="include_replies", action="store_false",
                   help="skip replies (default keeps them)")
    sub.add_parser("render", help="build posts/*.md from data/raw.jsonl")
    args = p.parse_args()
    fetch(args) if args.cmd == "fetch" else render(args)


if __name__ == "__main__":
    main()
