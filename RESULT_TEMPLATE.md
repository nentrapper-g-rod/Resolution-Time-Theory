# Result Provenance Template

**ID:** (e.g. N-07)
**Artifact:** (path)
**Claim (one sentence):**
**Status:** proven-analytically / shown-numerically / assumed / withdrawn

## How to regenerate
```bash
# exact command
python simulations/XX.py
```
**Environment:** see requirements.txt  
**Seed:** (if any)  
**Printed output (verbatim):**
```
(paste)
```

## Analytic target
(what exact relation or density the number is supposed to support)

## Metric used and why
(e.g. L¹ distance to normalized I; why not correlation)

## Pass / Fail criterion
(tolerance and whether it passed)

## Convergence / negative controls
(dt→0, N→∞, or a case that must *not* lock)

## Notes / limitations
