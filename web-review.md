# Authorized web security review worksheet

## Rules of engagement

Document the written authorization, exact target environments, allowed techniques, test identities, maintenance window, rate limits, excluded systems, stop conditions and emergency contact before any testing.

## Review areas

| Area | Verification | Evidence | Remediation owner |
|---|---|---|---|
| Authentication | Session lifecycle, MFA where appropriate, recovery flow | | |
| Authorization | Server-side object and function access controls | | |
| Input handling | Parameterized queries, contextual output encoding | | |
| Browser controls | CSP, MIME handling, cookies, clickjacking protection | | |
| Transport | Valid TLS and secure redirects | | |
| Secrets | No secrets in source, logs or client bundles | | |
| Dependencies | Inventory, provenance, vulnerability review | | |
| Operations | Logging, recovery exercises, least privilege | | |

For each finding record: scope, reproducible evidence without sensitive data, impact, severity rationale, recommended fix, owner, due date and retest outcome. Link the issue to a risk-register entry where applicable. Do not label an untested system as secure.
