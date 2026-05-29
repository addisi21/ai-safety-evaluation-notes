# AI Safety Evaluation Notes

This repository demonstrates public-facing safety evaluation notes for AI responses, digital safety review, content moderation, and policy edge-case analysis. The examples are based on real evaluation experience but rewritten for public use.

## Safety Review Areas

- Harmful or dangerous instructions
- Sensitive-domain overconfidence
- Privacy or personal-data exposure
- Harassment, hate, or abusive content
- Self-harm or crisis handling
- Sexual, violent, or graphic content boundaries
- Misinformation and unsupported claims
- Unsafe medical, legal, financial, or HR guidance

## Review Principles

1. Identify the user's intent and likely harm level.
2. Check whether the response complies with policy and user safety expectations.
3. Distinguish safe helpfulness from unsafe completion.
4. Review refusal quality when the model must not comply directly.
5. Flag borderline cases with clear evidence and severity.

## Included Files

- `safety-review-checklist.md`: practical checklist for evaluating safety-sensitive AI outputs
- `policy-edge-patterns.md`: common edge-case patterns and how to review them
- `proof-pack.md`: completed public safety review examples with unsafe responses, severity labels, safer alternatives, and reviewer feedback
- [data/safety_cases.json](data/safety_cases.json): structured safety cases with severity and decision labels
- [scripts/summarize_safety_cases.py](scripts/summarize_safety_cases.py): dependency-free Python script for safety case summaries
- [outputs/safety-review-log.md](outputs/safety-review-log.md): reviewer-readable safety review log

## Confidentiality Standard

No real platform task content, internal policies, screenshots, private datasets, or client examples are included.

## Run Locally

```bash
python scripts/summarize_safety_cases.py
```
