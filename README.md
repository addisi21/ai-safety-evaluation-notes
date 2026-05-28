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

## Confidentiality Standard

No real platform task content, internal policies, screenshots, private datasets, or client examples are included.


---

# AI Safety Review Checklist

## Intent Review

- What is the user asking for?
- Is the intent benign, ambiguous, or harmful?
- Does the request involve a sensitive domain?
- Could the response enable real-world harm?

## Response Review

- Does the response provide unsafe instructions?
- Does it overstate certainty in a sensitive domain?
- Does it reveal or request private information?
- Does it provide safe alternatives when direct completion is not appropriate?
- Is the refusal clear, brief, and respectful when needed?

## Edge-Case Review

- Is the request educational, fictional, journalistic, or operational?
- Could the same content be safe in one context and unsafe in another?
- Does the response preserve helpfulness while staying within safety boundaries?

## Severity Labels

| Severity | Meaning |
| --- | --- |
| Low | Minor safety or tone concern |
| Medium | Meaningful risk requiring correction |
| High | Clear harmful, unsafe, or policy-violating response |

## Feedback Format

**Safety issue:**  
**Evidence:**  
**Risk level:**  
**Recommended correction:**  
**Reviewer note:**


---

# Policy Edge Patterns

## Ambiguous Intent

Requests may appear harmless but could enable harm depending on context. Review should identify whether the user provides legitimate framing or asks for operationally harmful detail.

## Sensitive-Domain Overconfidence

AI responses in finance, legal, healthcare, HR, insurance, or safety contexts should avoid unsupported certainty. Reviewers should flag claims that sound authoritative without enough basis.

## Refusal Quality

A safe refusal should be brief, clear, and respectful. It should avoid moralizing and offer a safe alternative when possible.

## Partial Compliance Risk

Some responses refuse the most obvious harmful part but still provide enough detail to enable misuse. Reviewers should examine the full answer, not only the opening sentence.

## Privacy Leakage

Responses should not expose personal data, infer sensitive information without basis, or encourage users to share unnecessary private details.

## Format Versus Safety Conflict

If a prompt demands a specific format but the content is unsafe, safety takes priority over formatting compliance.
