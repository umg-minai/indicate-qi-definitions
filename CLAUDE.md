## Pull request reviews

### Assess the definition change

- Establish the intended change from the PR description, commit messages,
  referenced issues, and relevant discussion. Read earlier PR comments and
  review threads concerning the affected definitions, including resolutions
  and the reasoning behind accepted or rejected proposals. Distinguish
  agreed decisions from suggestions, earlier AI findings, and open questions.
- Compare the previous and proposed definitions. Check whether the change
  implements the agreed requirements completely and without unexplained
  changes in meaning.
- Check internal consistency, including population, counting unit,
  numerator, denominator, exclusions, timing, and aggregation.
- Assess whether the change is logically coherent and clinically plausible
  in its stated context. Explain concrete counterexamples when applicable.
  Do not invent clinical requirements.
- Separate introduced or worsened problems from unrelated pre-existing issues.
- Before reopening a previously resolved concern, establish what new evidence
  or changed requirement makes another correction necessary. Explain that
  difference and link the earlier decision.

### Report only actionable findings

- Start with the corrections or decisions the author needs to make, ordered
  by consequence. Omit praise, successful checks, confirmations of compliance,
  harmless differences, and a retelling of the PR's changes.
- Give each finding a short title stating the requested correction. Explain
  the discrepancy, its effect on the QI definition, and the smallest suitable
  correction or precise question to resolve it. Use a concrete example when
  needed to make the consequence clear.
- Do not leave neutral observations for the reader to interpret as good or
  bad. An edit that preserves the intended meaning needs no comment; if a
  requested semantic change is absent, say which requirement remains unmet
  and what must change.
- Use absolute GitHub URLs with descriptive link text. Link the affected
  definition at the reviewed commit with line anchors, and link the specific
  issue comment or PR discussion that establishes the requirement. Use actual
  permalinks; never invent line numbers, comment IDs, or source revisions.
- Put the evidence needed to understand each finding beside that finding.
  If findings are posted inline, keep the summary short and link them instead
  of repeating their full explanations. If nothing actionable remains, use
  only a brief completion statement rather than a list of passed checks.

### Put review context last

- End the summary with a compact, collapsed `<details>` block titled
  `Review context`. Place the reviewed commit, additional source references,
  scope, and verification limitations there. Omit empty subsections and do
  not lead the review with sources or limitations. A source gap that requires
  an author decision must still be raised as an actionable clarification above.
