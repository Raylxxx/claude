---
name: serenity-posts
description: Archive of posts by Serenity (@aleabitoreddit on X, 用户称她「白毛股神」), an AI and semiconductor supply-chain account. Use when the user asks what Serenity / @aleabitoreddit / 白毛股神 said about a stock, theme or event, wants her views over time, or wants to check how her past calls played out.
---

# Serenity (@aleabitoreddit) post archive

Posts are stored as Markdown in `posts/`:

- `posts/index.md`: post count per month, plus the most-mentioned tickers ($cashtags) with first and last mention dates. Read this first.
- `posts/YYYY-MM.md`: every post from that month, oldest first. Each entry has the UTC time, type (原创 / 回复 / 引用), a link to the original, engagement counts, cashtags, the replied-to or quoted text, and the full post text.

## How to answer

1. To find posts about a company, grep `posts/` for both forms of the ticker (`\$MRVL` and `MRVL`) and for the company name, since she does not always use cashtags.
2. Quote her briefly, give the date and the link to the original, and lay several posts out as a timeline so the user can see how her view changed.
3. Keep apart what she said and what actually happened. When checking a past call, get prices for the post date and today from the IBKR connector if it is available, and say plainly when a call did not work out.
4. Her bio says "Nothing is investment advice" and that she may hold the names she discusses. Pass that on when it matters, and do not present her views as recommendations.
5. Report and analyse her views. Do not write new posts or opinions in her voice.

## When posts/ is empty or out of date

The posts are collected with the official X API, not by logging into an account. To update:

```bash
export X_BEARER_TOKEN=...   # from developer.x.com; keep it out of the repo
cd .claude/skills/serenity-posts
python3 scripts/x_archive.py fetch --since 2025-07-01            # recent ~3,200 posts
python3 scripts/x_archive.py fetch --since 2025-07-01 --mode search   # full history, higher API tier
python3 scripts/x_archive.py render
```

`fetch` merges into `data/raw.jsonl` (not committed), so re-running it only adds new posts. `render` rebuilds every file in `posts/`.
