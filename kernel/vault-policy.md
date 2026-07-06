# Vault Policy (knowledge discipline)

Last reviewed: 2026-07-06 / Index: [INDEX.md](../INDEX.md)

How agents write to the knowledge base so it gets stronger with size instead of noisier. Based on the
"second brain" pattern (see [README.md](../README.md) attribution).

## 1. Two layers (don't create a third home for knowledge)

| Layer | Where | Role | Writers |
|---|---|---|---|
| raw (inbox) | your capture area | Landing zone for source material: articles, transcripts, notes | capture agents / you |
| compiled (canon) | this vault | Distilled notes + index; the source of truth | the main agent (with an approval flow) |

- Don't keep a copy of the same knowledge in both layers. Compiled holds a distillation plus a reference (path
  or URL) into raw. Extract and reference — don't duplicate.
- The raw layer may live in a runtime you don't fully control (a scheduler, an agent framework). Note that
  asymmetry and audit its modification times periodically.

## 2. The four writing rules

1. **One lesson per file.** Put a one-line summary at the top.
2. **Update an existing page instead of creating a duplicate.**
3. **A page found to be wrong is deprecated, not deleted** (see [../maintenance/deprecation-rules.md](../maintenance/deprecation-rules.md); actual deletion needs owner approval).
4. **Keep raw and compiled separate, always** (don't edit raw in place; don't paste raw source into compiled).

## 3. Source-receipt duty

Every new statement in the compiled layer carries "claim + source (path or URL) + date." A page with no
source is quarantined at the next review as untrusted.

## 4. Raw intake rules

- OK to store: public articles, your own notes, research results, sensitivity-scrubbed transcripts.
- **Never store: secret values, PII (names + contact details), internal-sensitive info (margins, cost,
  negotiation stance)** — not even in raw. Isolate those in a per-project `docs/internal/` (extends
  [security-floor.md](security-floor.md) §2).

## 5. Entity pages: start frozen

Don't create named-person / named-client entity pages by default (the leak surface is large). Keep such
context in the per-project repository. Expand to non-sensitive entities (tools, your own projects) only after
you have decision-log evidence that it earns its keep.

## 6. Decisions log

Record business / product / architecture decisions as `maintenance/decisions/D-YYYY-MM-DD-NN-slug.md`
(format: [../templates/decision.template.md](../templates/decision.template.md); a light 4-field entry).

## 7. Retreat criteria

1. A full quarter with zero maintenance-review records → freeze appends and consolidate back to one home.
2. A content contradiction that stays unruled for a week → stop writing.
3. One confirmed leak of sensitive info into client-facing output → immediately freeze default-loading of the
   offending layer.

Related: [constitution.md](constitution.md) Articles 7–10.
