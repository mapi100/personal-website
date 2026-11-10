# Content evidence — reviewed November 10, 2026

This is an editorial record, not a deployment audit. Repository copies were inspected read-only. No other project's source was changed and no authenticated student records were accessed.

## Identity, education, experience, and contributions

The existing public [`documents/cv_Marco.pdf`](../documents/cv_Marco.pdf) supports the M.S. expected May 2028; B.S. May 2026 with a Computer Science minor and Cum Laude; Graduate Teaching Assistant 2026–present; PLTL Leader & Mentor 2023–2026; and the 2026 p-adic numbers undergraduate project with Dr. Wilson Zúñiga-Galindo. Its project entries describe Marco's development and testing contributions. The PDF was read, not changed. The summer 2027 internship goal comes directly from the owner.

The existing About page supports the running, chess, and Rubik's cubes interests. Its personal profile URLs and the existing ORCID URL are retained. No LinkedIn or immigration/work-authorization claims were added.

## Seminary Academic Management Portal

Repository: <https://github.com/mapi100/seminario-matamoros-reynosa>

Reviewed revision: [`b066fa6fa7fe2eb05c06b3c6c1232b7b9cfcc388`](https://github.com/mapi100/seminario-matamoros-reynosa/tree/b066fa6fa7fe2eb05c06b3c6c1232b7b9cfcc388).

Evidence at that revision:

- `portal/README.md`, `portal/auth.js`, `portal/panel.html`, and `portal/panel.js`: static HTML/CSS/JavaScript, Supabase SDK, session verification, and active profiles. No React or Next.js frontend.
- `docs/aula-virtual.md` and `docs/campus-autonomo.md`: student, professor, and `control_escolar` workflows, coursework, enrollment, assignments, and publication of grades.
- `supabase/migrations/20261021020000_create_enrollment_grades.sql`: published-grade reads with owner/activity/role checks, RLS, score constraints, and denied direct writes.
- `supabase/migrations/20261021040000_enable_grade_capture.sql` and `docs/capturar-calificaciones.md`: separate drafts, guarded SQL functions, revisions, and audit events. Later migrations extend the system; the case study describes these foundational decisions, not an exhaustive schema inventory.
- `supabase/functions/invite-person/handler.ts`: TypeScript server-side invitation handler. This does not make the browser frontend TypeScript.
- `tests/portal_grade_capture.py`, `tests/portal_subjects.py`, and `portal/README.md`: Python/Playwright frontend checks with a simulated API.
- `supabase/tests/run_grades_local.py` and `supabase/tests/grades_rls.sql`: disposable PostgreSQL/Docker fixtures testing isolation, draft hiding, roles, direct-write restrictions, and grade constraints. Minimal local Auth fixtures do not exercise hosted Supabase Auth, HTTP, or PostgREST.

The CV supports the personal contribution claim; the source corroborates the implementation. Neither establishes exclusive authorship of every file. No portal tests were executed for this portfolio task. No full security audit, live authenticated verification, institutional adoption, or performance measurement is claimed.

Public destinations retained: <https://seminariomr.org> and <https://seminariomr.org/portal/>. The source requires applying SQL migrations and configuring Supabase separately from publishing static files.

## Coffee Origin Classification

Repository: <https://github.com/mapi100/Coffee-Pour-Over-Origin-Classification>

Reviewed revision: [`95f71afd8f3d13055eccd676ea071cabbf67b780`](https://github.com/mapi100/Coffee-Pour-Over-Origin-Classification/tree/95f71afd8f3d13055eccd676ea071cabbf67b780).

The actual notebook is `CSCI_final_project_Marco_and_Iris.ipynb`; the README's `coffee_project.ipynb` filename does not match the checked-in filename. The portfolio links to the repository to avoid repeating that broken path.

Read-only inspection of `coffee_combined_data.npz` confirmed 20 labeled samples with 1,995 values per curve. `test_data.npz` contains four unlabeled curves. Notebook cells implement numerical feature extraction, logistic regression with gradient descent, polynomial-feature expansion, a 70/30 holdout (14 training / 6 holdout), and a 60/40 tuning split (12 training / 8 validation). This is holdout validation, despite the README's broader use of “cross-validation.”

Saved notebook outputs include 0.75 **training** accuracy on all 20 samples; 0.3333 on the six-sample polynomial-model holdout; and 0.625 linear / 0.25 stacked accuracy on the eight-sample tuning-validation set. Those are stored outputs, not results reproduced in this task. The tuning-validation set is used for model selection, not an independent final benchmark. Four unlabeled predictions cannot establish accuracy. The public portfolio intentionally omits headline accuracy metrics and identifies the dataset and limited validation instead. The CV supports Marco's collaboration; no per-cell authorship is inferred.

## Parish website

Repository: <https://github.com/mapi100/parroquia-guadalupe-matamoros>

Reviewed revision: [`5d5e677aeb960cf8e79519af3e82e4b2edb09209`](https://github.com/mapi100/parroquia-guadalupe-matamoros/tree/5d5e677aeb960cf8e79519af3e82e4b2edb09209).

`index.html` contains Mass schedules, parish services, and practical information. `style.css` contains responsive breakpoints at 1300, 900, 620, and 360 px, plus print styles. The CV supports development of this responsive public information site. No database-backed application or measured usage is claimed.

Public destination retained: <https://guadalupematamoros.org>.

## Verification boundaries and follow-up facts

GitHub profile access returned HTTP 200 and the three repository reads succeeded. This environment's outbound proxy returned `403 Forbidden` for the personal domain, seminary domain, parish domain, ORCID, Chess.com, and Lichess. That restriction does **not** establish whether the destinations are up or down. Their current live responses, the deployed portal feature set, and authenticated production behavior remain unverified. No public screenshot could be obtained from those destinations; the portfolio uses an original architecture diagram rather than a simulated product screenshot.

The original contact `mailto:` address, CV path, profile URLs, original image paths, `CNAME`, and all existing PDF paths are preserved. Local files and browser behavior were checked separately. Actual email delivery and account ownership at external destinations were not tested by sending messages.

Useful future confirmations: currently deployed migrations and invitation configuration; permission to show a sanitized portal demo; any documented adoption or impact measurements. None is required for the conservative public descriptions delivered here.
