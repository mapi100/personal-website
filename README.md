# Marco Antonio Peña Ibarra — personal website

A minimal static academic website with selected software and data projects. It preserves the original beige background (`#f5f5dc`), system font, black text, blue links, centered homepage, Rubik's cubes photo, and white buttons with black outlines. HTML and CSS only; no installation or build step.

## Run locally

From the repository root:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

On Windows, use `py -m http.server 8000 --bind 127.0.0.1` if Python is installed through the Python launcher. Open `http://127.0.0.1:8000` in your own browser and refresh after editing. Stop with Ctrl+C. Use this HTTP workflow for review; the managed browser blocks direct `file:` navigation.

## Apply the ZIP

Extract `personal-website-minimalista.zip` outside your clone. Copy its **contents** into the repository root next to `index.html`, merge folders, and replace supplied files. There is no enclosing project folder in the ZIP. Preserve the rest of the clone, including `documents/`, original images, `CNAME`, `robots.txt`, and `.git`. The ZIP includes every new or changed file relative to original commit `2130e11`, so it can be applied directly to a clone of the original site or over the earlier portfolio delivery. It requires no deletion of existing files. Review `git diff` before publishing.

## Structure

- `index.html`: original-style homepage, brief software/data introduction, summer 2027 internship search, Projects/GitHub/ORCID/About/CV buttons, and original contact email.
- `about.html`: original portrait-and-biography layout, personal interests, and an optional native “Education & teaching” disclosure.
- `projects.html`: three selected projects as plain text and links, with the academic portal first.
- `seminary-portal.html`: a single-column case study covering context, roles, architecture, authentication/authorization, decisions, tests, and limitations.
- `style.css`: shared original palette and layout rules, responsive behavior, and keyboard focus styles.
- `images/math-and-cubes.webp`, `images/marco-portrait.webp`: optimized copies of the existing photos; originals remain available at their unchanged paths.
- `documents/`: existing PDFs, unchanged by this update. Main CV: `documents/cv_Marco.pdf`.
- `docs/content-sources.md`: source revisions and evidence behind the project descriptions.
- `tools/check_site.py`: dependency-free local-reference, fragment, document-structure, and metadata checks.

## Maintain content

Keep the homepage brief. Put project descriptions and technology lists in `projects.html`; keep the detailed portal explanation in `seminary-portal.html`. Preserve the original visual style when editing: no decorative cards, hero redesigns, new palette, oversized headings, or external fonts are needed.

Use the current CV for education, experience, and contribution claims. Keep education and teaching details in the About disclosure. Update the homepage's summer 2027 internship search when appropriate. The coffee project is a collaborative academic study with 20 labeled samples and limited holdout validation, not a production classifier. Keep implementation, deployment, and institutional adoption distinct. Refresh `docs/content-sources.md` when reviewing newer source.

For CV updates, replace the PDF at the existing path `documents/cv_Marco.pdf`; preserve other shared document URLs. This task does not regenerate or edit the CV. Update contact and verified profile links consistently, and add other profiles only after confirming ownership.

Every page has a title, description, canonical URL, Open Graph metadata, and Twitter card metadata. Sharing uses the original `images/marco.jpg`. If the domain changes, update absolute metadata URLs, `CNAME`, `robots.txt`, and `sitemap.xml` together. All ordinary page and asset links are relative.

Images have explicit dimensions and alt text. Navigation uses native links; the About disclosure uses native `details`/`summary` and works without JavaScript. Keyboard focus remains visible. There are no animations or external runtime resources.

## Verify

```sh
python3 tools/check_site.py
```

Also inspect all four pages in a browser on desktop and mobile. Check homepage buttons, About's disclosure, case-study navigation, the CV PDF, contact email, image loading, keyboard access, focus, and overflow. The delivery was checked at 320, 375, 390, 768, 1024, and 1440 px. Screenshots and the delivery report are provided separately from the site ZIP.

Local checks do not establish that external services are reachable or that the portal's production setup matches its repository. The environment's proxy blocked the non-GitHub public destinations during the prior source review; those live checks remain unverified. No other project's test suite was run. Nothing here performs a push or deployment.
