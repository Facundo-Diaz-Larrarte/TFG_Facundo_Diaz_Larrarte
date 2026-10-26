# Presentation: AI adoption and labor productivity

## Goal
Create a polished Spanish Beamer defense presentation in `Facundo_Diaz_Larrarte_TFG/presentacion_tfg.tex`, using `presentacion_unc (1).tex` as a structural/style reference while replacing its blue palette and adapting the content to `trabajo_final.tex`.

## Acceptance criteria
- Follow the thesis table of contents: introduction/problem, theoretical framework, data and methodology, results, discussion, conclusions.
- Present enough evidence for an academic defense, emphasizing balanced panel coverage, model specification, main result and caveats.
- Use a professional non-blue palette and consistent typography/layout.
- Keep claims associative and disclose key limits; distinguish nominal main results from real-productivity robustness.
- Compile with available LaTeX tooling, resolving errors where possible.

## Tasks
1. Extract thesis structure, verified findings, and presentation constraints (done through source reading).
2. Create the Beamer presentation as a separate file; do not modify the thesis or reference presentation (done; 20 frames, 6 sections, green/gold/charcoal identity).
3. Compile and inspect build output; fix observed TikZ compile error, malformed spacing, and missing sector M; compile again (done).

## Evidence
- Source: `Facundo_Diaz_Larrarte_TFG/trabajo_final.tex`
- Style reference: `Facundo_Diaz_Larrarte_TFG/presentacion_unc (1).tex`
- Output: `Facundo_Diaz_Larrarte_TFG/presentacion_tfg.tex`
- Initial verification found TikZ compile failure, a malformed spacing construct, overfull frame and missing sector M; these were addressed.
- Final verification: latexmk passed, generated 20-page PDF in `/tmp/presentacion_tfg_verify.3vWt75`; no errors. Remaining non-fatal overfull vbox warnings at source lines 311, 347 and 377, plus font substitution at line 98. Build outputs stayed outside repository.
