# Security Floor (the common lower bound for every project)

Last reviewed: 2026-07-06 / Index: [INDEX.md](../INDEX.md)

The additional floor generalized from real leaks. Layer it on top of your own security rules.

## 1. Secrets floor

- Never put secret values (passwords, tokens, API keys) in governance documents (constitution, agent files,
  README, handoffs).
- Keep mentions of where secrets are stored to the minimum (exposing the location is a map for an attacker).
- For an exposed secret: stop use → rotate → check for similar occurrences across the codebase. Keep it an
  open task until rotation is complete (don't mark it done).

## 2. Internal-sensitive floor

- Don't put margins, cost, purchase prices, or negotiation stance in files an agent loads by default
  (the agent files an agent always reads).
- Reason: the contents of default-loaded files are a leak path into client-facing deliverables.
- If needed, isolate them in an explicitly-loaded file (e.g. `docs/internal/`) and put only a reference in the
  governance file.

## 3. PII publication gate

- Deciding to include personal data (names, faces, contact details, location-identifying information) in
  public output (a site, social post, report) requires confirming the person's explicit consent first.
- Record the consent (date, method, scope of OK) so the gate is auditable.

## 4. Vocabulary discipline floor

- Project-specific client-facing vocabulary rules (e.g. "don't write 'AI' or 'automation' in deliverables")
  are absolute constraints.
- State them in the project agent file's "absolute rules" section and check them in the pre-publish review.

## 5. Pre-publish checklist (minimum)

- [ ] No secret values or needless mention of where they're stored
- [ ] No internal-sensitive information (amounts, margins, negotiation stance) mixed in
- [ ] PII only where consent is confirmed
- [ ] No violation of the project's vocabulary rules

Related: [constitution.md](constitution.md) Article 10.
