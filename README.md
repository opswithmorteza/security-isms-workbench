# Security & ISMS Workbench

A practical portfolio lab by Morteza Rajabi for asset-based risk assessment and remediation tracking. It includes a runnable risk-register validator and a scoped web security review worksheet. It is not certification evidence, legal advice or a complete ISMS implementation.

## Run

```sh
python -m unittest -v
python risk_register.py sample-risks.csv
```

Scores are likelihood × impact on a 1–5 scale. This is a sample policy, not an ISO-mandated scoring system: low 1–5, medium 6–12, high 13–19, critical 20–25. Agree criteria with the organization before real use.

The sample register contains synthetic assets, example risks, proposed controls and owners. None are claims about a real client. Map controls and applicability using a licensed standard and your organization's actual risk context; no ISO standard text is reproduced here.

## Workflow

Identify scope → inventory assets → assess likelihood and impact → choose treatment → assign owner and deadline → collect evidence → review residual risk → obtain acceptance from the accountable owner.

The security worksheet is for systems you own or are explicitly authorized to assess. It contains review criteria rather than exploit automation.
