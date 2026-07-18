# Whole-manuscript structure contract

## Classify {#classify}

Record `study_family`, optional specialty `profile`, target journal, primary question, primary endpoint,
top-level claim, and reporting standard before editing.

## Skeleton {#skeleton}

| Unit | Required job |
|---|---|
| Title | Name clinical object, population, and evidence level when material |
| Abstract | Reconstruct question, design, cohort, principal numbers, harms, and calibrated answer |
| Introduction | Clinical state → unresolved decision → exact aim |
| Methods | Cohort/design → measurements/intervention → endpoints → analysis |
| Results | Flow → primary result → supporting analyses → harms/sensitivity |
| Discussion | Principal findings → evidence comparison → explanation → clinical meaning → limitations |
| Conclusion | Answer the aim without exceeding the Discussion claim |

## Claim gradient {#claim-gradient}

Require monotonic restraint: title ≤ abstract conclusion ≤ discussion interpretation ≤ what design and
analysis support. A secondary analysis never inherits the parent trial's full claim strength by default.

## Cross-section pass {#cross-section}

Verify all of the following before delivery:

1. The Introduction aim, Methods endpoint, Results hierarchy, and Conclusion answer the same question.
2. Sample sizes, group counts, event counts, percentages, time points, estimates, intervals, and P values
   reconcile across abstract, text, tables, figures, and supplement.
3. Every reported analysis has a method; every promised method has a result or an explicit reason.
4. Terminology, abbreviations, group names, endpoint labels, and reference categories remain stable.
5. Causal, diagnostic, prognostic, and practice claims stay within the selected study family.
6. All table, figure, registry, appendix, and supplement references point to existing items.
7. The conclusion retains material safety findings and limitations relevant to its claim.

Record unresolved discrepancies as author queries; never silently choose a value.
