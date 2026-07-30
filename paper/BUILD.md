# Building the Core Edition PDF

**Current source:** `RTT_Core_Edition_4.0.1.tex`  
**Legacy:** `RTT_Core_Edition_4.0.tex` is a pointer only — do not submit it.

## Compile locally

```bash
cd paper
pdflatex RTT_Core_Edition_4.0.1.tex
pdflatex RTT_Core_Edition_4.0.1.tex   # second pass for TOC
```

Requires a standard TeX distribution (`texlive-latex-base` + recommended packages: booktabs, hyperref, lmodern, microtype).

## Commit the PDF (manual)

Binary PDF is not committed by the automated tooling used in this project. After compiling:

```bash
git add paper/RTT_Core_Edition_4.0.1.pdf
git commit -m "Add compiled Core Edition 4.0.1 PDF"
git push
```

## arXiv

Upload **both** the `.tex` source and the compiled PDF. See `../SUBMISSION_NOTES.md` and `../ARXIV_CHECKLIST.md`.
