# Models

canon-os is model-agnostic. The kernel and playbooks refer to three **tiers** — `top`, `mid`, `cheap` —
so the norms don't rot when models change. Map the tiers to whatever models you use.

## Tiers

| Tier | Use for | Reasoning effort |
|---|---|---|
| **top** | design, rulings, unknown-unknown discovery, hard trade-offs | highest available |
| **mid** | bounded implementation, reviews, structured research | high |
| **cheap** | build/lint fixes, enumeration, summarization, recon | default |

## Example mapping (edit for your setup)

This is only an example. Substitute your provider's line-up.

```
top:   your provider's strongest reasoning model
mid:   your provider's balanced model
cheap: your provider's fastest/cheapest model
```

For Anthropic's Claude line-up, a reasonable mapping is an Opus-class model for `top`, a Sonnet-class model for
`mid`, and a Haiku-class model for `cheap`. Adjust as the line-up evolves.

## Why tiers, not names

The behavioral style ([behavior/operating-style.md](behavior/operating-style.md)) lets a `mid`-tier model
*behave* with the discipline of a `top`-tier one — but it does not transfer raw capability (first-shot
correctness, long-horizon autonomy, hard-problem depth). So the routing table
([kernel/delegation-policy.md](kernel/delegation-policy.md)) still sends the judgment-heavy work to `top`.
Reproduce quality with **structure**, and reserve the expensive tier for what only it can do.
