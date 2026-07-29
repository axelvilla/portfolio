# TRON Portfolio Redesign — Design

Date: 2026-07-29

## Context

The portfolio (`axelvilla` personal site) is built with [Reflex](https://reflex.dev) 0.5.8, a Python framework that compiles to a Next.js/React app. Current state: dark Radix theme, a purple/mauve/green gradient wash, no centralized design tokens (accent colors are copy-pasted literal strings across 4 component files), and content that has fallen behind the author's current CV and project list.

Goal: reskin the site with a distinctive TRON-inspired visual language (validated with the user via visual mockups — see below), refresh content from the user's current CV and four new live project links, and fix several pre-existing bugs discovered during exploration.

## Visual Design System

Validated direction: a hybrid of two mockup directions the user approved — "Circuit HUD" (corner-bracket frames, dual cyan/orange accent, technical feel) combined with "Grid Arena Minimal" (restrained, large confident type, perspective grid floor, low visual noise). Rejected direction: "Neon Grid Classic" (heavy uniform cyan bloom) — flagged as the most clichéd/AI-generic take on a dark-neon aesthetic.

**Palette**
- Background: `#000000` base, `#050607`/`#0A0A0A` for slightly-raised panels/cards
- Primary accent (cyan): `#5CF6FF`
- Secondary accent (orange): `#F2994A` — used sparingly (secondary corner brackets, one focal CTA), a nod to TRON: Legacy's dual-faction color scheme
- Text primary: `#EAF6F6` (near-white, cool tint)
- Text muted/secondary: `#8FA3A3`
- Hairline borders: `rgba(92,246,255,0.25)` resting, full opacity cyan on hover/focus

**Typography**
- Display (hero name, section headings): **Orbitron** (700/800) — geometric, technical, used sparingly (large sizes only) so it doesn't tip into novelty-font territory
- Body/UI (paragraphs, nav links, buttons): **Space Grotesk** (400/500) — modern and geometric without being the default "Inter" look
- Mono (tags, dates, stack badges, small labels): **JetBrains Mono** (400/500)
- Fonts loaded via Google Fonts `@import`/`<link>` in the global stylesheet (see Technical Approach)

**Structural motifs**
- Corner-bracket "HUD frame": reusable style applied to project/experience/education/stack cards — a 2px cyan bracket top-left + 2px orange bracket bottom-right (14px arm length), replacing default rounded Radix card borders
- Perspective grid floor: a masked, rotated CSS grid (cyan hairlines, low opacity, fading via gradient mask) behind the hero section only — evokes the light-cycle arena without covering the whole page
- Faint full-page grid: much lower opacity, non-perspective, behind body content for texture without competing with cards

## Animations

All animations respect `prefers-reduced-motion: reduce` (looping/decorative motion is disabled or reduced to a simple opacity fade under that media query). None of the demoed loops run infinitely in production except where noted — the brainstorming mockups auto-looped purely so the user could preview them without hovering/scrolling.

1. **Hero decode-in** — the name "digitizes" into place (blur + letter-spacing + opacity keyframes) once on page load, ~1.2s ease-out. Not repeated.
2. **Card border trace** — a light segment travels the card perimeter. Runs only while the card is hovered/focused (`animation-play-state` tied to `:hover`/`:focus-within`), not continuously.
3. **Grid floor drift** — the hero's perspective grid slowly scrolls (background-position animation), continuous but slow and low-opacity; paused under reduced-motion.
4. **Nav underline trace** — width 0→100% transition on hover/focus per nav link (a transition, not an infinite keyframe, since it's an interaction response, not ambient motion).
5. **Section scan-line divider** — a thin bright segment sweeps across the hairline divider between major sections, slow (4–6s) continuous loop; paused under reduced-motion.
6. **Button power-up glow** — pulsing glow on hover/focus for all buttons; the primary CV-download CTA additionally gets a slow, subtle persistent pulse to draw the eye (also paused under reduced-motion).
7. **Scroll-reveal** — each major section (Skills/Projects/Experience/Education/Footer) fades + translates up 16px into place the first time it enters the viewport (IntersectionObserver-driven class toggle), one-time per section, no replay on scroll-up.
8. **Hover-lift** — project/experience/education/stack cards lift ~4px with intensified border glow and soft shadow on hover/focus, ~150–200ms transition.

Hover/focus-triggered effects must also fire on `:focus-visible` (not just `:hover`) so keyboard navigation gets equivalent feedback.

## Content Changes

### Hero / Header
- Rewrite bio paragraph using the CV's professional summary (full-stack dev across Java/Spring Boot, Python/Flask/FastAPI, JS-TS/React/Node/Next; leadership, GitHub best practices, agile).
- Fix subtitle typo: "Desarrollador Full Stack - Pyhton" → "Desarrollador Full Stack".
- Fix CV download link: point to the actual file `public/CV_Gomez_Axel.pdf` (currently linked as `/CV_Gomex_Axel.pdf`, a typo causing a broken download).

### Projects (full replacement of the current 3 entries)
| Title | Description | Stack | Link |
|---|---|---|---|
| Tienda Informática | E-commerce de componentes y periféricos de PC, con filtros por categoría/marca y configurador "Armá tu PC" | React, Tailwind | https://informatica-sepia.vercel.app/ |
| 1step | Plataforma de software a medida para automatizar y centralizar operaciones de negocios de servicios | React, Tailwind | https://1stepservice.vercel.app/ |
| Inmobiliaria Reconquista | Portal inmobiliario con búsqueda filtrada de propiedades en venta/alquiler | React, Tailwind | https://inmobiliaria-reconquista.vercel.app/ |
| La Cumbre | Sitio de la verdulería La Cumbre: catálogo de ofertas, galería de productos y pedidos por WhatsApp | React, Tailwind | https://lacumbre.netlify.app/ |

All four are live-demo-only (no public repo to link), so each project card drops the "Ver código" repo link and keeps only the live-site link.

### Experience (add one entry, keep the existing one)
- **New:** "Desarrollador Full Stack y Líder de Proyecto — Freelance / Proyectos de GitHub (2025)", body listing the four CV sub-projects: Login App (React + Flask + MySQL, auth system), Filter App (FastAPI + React, data management/filtering), Sistema de Laboratorio de Análisis Clínicos (Node.js + Next.js/React + MySQL/Prisma, patient/results management), Punto de Venta para Verdulería (Spring Boot + Next.js + MySQL + Docker, internal management system — distinct from the public `lacumbre.netlify.app` site above).
- **Kept as-is:** "Instructor de Java — Escuela Superior de Comercio N° 43".

### Education (replace with CV's exact 4 entries)
1. Técnico Superior en Desarrollo de Software — Escuela Superior de Comercio N° 43
2. Full Stack Python — Codo a Codo 4.0
3. Full Stack Java — Codo a Codo 4.0
4. Full Stack Javascript — Bootcamp: JSCamp InfoJobs

("Programación Inicial - Codo a Codo" is dropped — not present in the current CV.)

### Stack / Skills (add CV technologies, keep existing ones)
Add: JavaScript, TypeScript, React, Next.js, FastAPI, Spring Boot, MongoDB, Prisma, Docker.
Keep: HTML, CSS, Bootstrap, Tailwind, Python, Flask, Java, Hibernate, MySQL, Vercel, GitHub.

## Bug Fixes (bundled into this redesign)

1. CV download href typo (`/CV_Gomex_Axel.pdf` → `/CV_Gomez_Axel.pdf`).
2. Header subtitle typo: "Desarrollador Full Stack - Pyhton" → "Desarrollador Full Stack".
3. Root `rx.vstack` in `portfolio/portfolio.py` has `width=["260%", "100%"]`, which (Reflex's mobile-first responsive arrays) applies 260% width at the smallest breakpoint — likely causing horizontal overflow/zoom-out on mobile. Fix to a sane responsive value (e.g. `"100%"`).
4. Remove dead component `components/stack_projects.py` (unused, superseded by `stack_card`).

## Technical Approach (Reflex specifics)

- **Centralize design tokens:** new `portfolio/theme.py` (or `components/theme.py`) module exporting the color constants, font family names, and shared spacing/radius values. Replace the repeated literal `rgba(90, 51, 163, ...)` strings in `link_bio.py`, `link_button.py`, `footer_links.py`, and card components with references to this module.
- **Global stylesheet:** add a CSS file (e.g. `assets/styles/tron.css`) holding the `@font-face`/Google Fonts import, `@keyframes` for all animations, the grid-background utility classes, and the HUD corner-bracket classes (`::before`/`::after` pseudo-elements aren't expressible via Reflex's Python style dicts, so these live in real CSS and get applied via `class_name` on `rx.box`). Register it on the app (Reflex's `rx.App` supports a `stylesheets` list).
- **New shared components:**
  - `components/hud_frame.py` — wraps card content and applies the corner-bracket class.
  - `components/grid_background.py` — renders the perspective grid floor (for the hero) and the fainter full-page grid.
- **Updated existing components:** `navbar.py`, `link_bio.py`, `link_button.py`, `footer_links.py`, `projects_card.py`, `stack_card.py`, `experience_card.py` — swap inline literal colors for theme tokens, add hover-lift/trace/underline classes.
- **Updated content-only files:** `views/header/header.py`, `views/projects/projects.py`, `views/experience/experience.py`, `views/education/education.py`, `views/stack/stack.py`, `portfolio/portfolio.py` (width fix).

## Testing / Verification

- Run the Reflex dev server locally and visually inspect every section (hero, skills, projects, experience, education, footer) at desktop (1280px) and mobile (375px) widths, confirming no horizontal overflow (validates bug fix #3).
- Confirm the CV download button successfully downloads `CV_Gomez_Axel.pdf` (validates bug fix #1).
- Confirm each of the 4 new project cards links to the correct live URL and that no stale project (Amazing Jobs, Sistema Veterinaria, Citador APA) remains.
- Emulate `prefers-reduced-motion: reduce` in devtools and confirm looping/decorative animations (grid drift, scan-line, decode-in, power-up pulse) are disabled or reduced.
- Tab through the page with keyboard only and confirm hover-equivalent effects (underline trace, hover-lift, border trace, button glow) also trigger on focus.
