# Models

canon-os is model-agnostic. The kernel and playbooks refer to three **tiers** — `top`, `mid`, `cheap` —
so the norms don't rot when models change. Map the tiers to whatever models you use.

## Tiers

| Tier | Use for | Reasoning effort |
|---|---|---|
| **top** | design, rulings, unknown-unknown discovery, hard trade-offs | highest available |
| **mid** | bounded implementation, reviews, structured research | high |
| **cheap** | build/lint fixes, enumeration, summarization, recon | default |

## Effort (optional annotation)

Some hosts expose a per-call **reasoning-effort** control (e.g. low / medium / high / xhigh / max). Where the
routing table or a pattern needs it, write `tier@effort` — for example `mid@max` (a mid-tier model at maximum
effort) or `top@high`. Tier is primary; effort is a secondary dial. On a provider with no effort control, read
`tier@effort` as just the tier and ignore the suffix — the norm still parses.

Economic principle: judgment-dense but short-output work (review, adjudication) suits a **high tier at moderate
effort**; long-output generation suits a **mid tier at maximum effort**. Spend effort where the tokens are few
and the stakes are high, not where the output is long.

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
