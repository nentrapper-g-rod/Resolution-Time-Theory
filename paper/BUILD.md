# Building the Core Edition PDF

**Current source:** `RTT_Core_Edition_4.1.tex`  
**Previous:** `RTT_Core_Edition_4.0.1.tex`  
**Legacy:** `RTT_Core_Edition_4.0.tex` is a pointer only — do not submit it.

## Figures

```bash
pip install -r requirements.txt
python paper/generate_figures.py   # writes paper/figures/*.pdf
```

## Compile locally

```bash
cd paper
python generate_figures.py         # if figures/ missing
pdflatex RTT_Core_Edition_4.1.tex
pdflatex RTT_Core_Edition_4.1.tex  # second pass for TOC / refs
```

Requires a standard TeX distribution (booktabs, hyperref, graphicx, lmodern, microtype).

## Commit the PDF

The compiled PDF is not stored as a binary in source control by default. After compiling:

```bash
git add paper/RTT_Core_Edition_4.1.pdf paper/figures/
git commit -m "Add compiled Core Edition 4.1 PDF and figures"
git push
```

## arXiv

Upload **both** the `.tex` source (and figures) and the compiled PDF. See `../SUBMISSION_NOTES.md` and `../ARXIV_CHECKLIST.md`.
