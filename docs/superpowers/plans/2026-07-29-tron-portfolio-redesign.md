# TRON Portfolio Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reskin the Reflex portfolio site with a TRON-inspired HUD visual system (corner-bracket cards, cyan/orange accents, grid motifs, 8 approved animations), refresh all content from the user's current CV and four new live project links, and fix the bugs found during exploration.

**Architecture:** No behavioral/state logic changes — this is a Reflex (Python→Next.js) static content site. Work centralizes design tokens into one module, adds a hand-written global CSS file for anything Python style-dicts can't express (pseudo-elements, keyframes, `prefers-reduced-motion`), adds one tiny vanilla-JS scroll-reveal script, and touches each content view (`views/*`) plus the shared card/button components (`components/*`) to apply the new classes and refreshed copy.

**Tech Stack:** Reflex 0.5.8 (Python → Next.js/React), Radix-based components, hand-authored CSS (no Tailwind/build step for styles), vanilla JS for the one IntersectionObserver script. No test framework exists in this repo — verification is manual, via the Reflex dev server viewed in the browser (desktop + mobile widths), matching the spec's own Testing/Verification section.

**Spec:** `docs/superpowers/specs/2026-07-29-tron-portfolio-redesign-design.md`

---

## Notes for the executor

- This repo has no automated tests. Every task's "verify" step is a manual visual/functional check via the Reflex dev server — do the check, don't skip it.
- Reflex compiles Python to a Next.js app on `reflex run`. The first run downloads Node/Bun and frontend deps and can take several minutes — this only happens once (Task 1).
- Use the project's Browser/preview tool (not a bare `Bash` background process) to keep the dev server running across tasks and to actually look at the page.
- Two real bugs beyond the ones already listed in the spec were found while reading the exact current file contents (not just summaries) — both are fixed in Task 3 / Task 4:
  - `stack_card.py` and `experience_card.py` currently end their `return rx.card(...)` statement with a trailing comma, which makes the function return a 1-tuple `(Component,)` instead of a `Component`. The rewrites in this plan drop that trailing comma.
  - The contact email is inconsistent: `header.py` and `footer.py` use `axelvilla745@gmail.com`, but the user's CV lists `axelvilla746@gmail.com`. This plan treats the CV as the source of truth and fixes both call sites to `746`.

---

### Task 1: Environment setup and dev server smoke test

**Files:**
- Create: `.claude/launch.json`

- [ ] **Step 1: Create a virtual environment and install dependencies**

Run:
```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
Expected: Reflex 0.5.8 and its dependencies install without error.

- [ ] **Step 2: Add a launch config so the dev server can be previewed in the browser**

Create `.claude/launch.json`:

```json
{
  "version": "0.0.1",
  "configurations": [
    {
      "name": "portfolio-dev",
      "runtimeExecutable": "venv/Scripts/python.exe",
      "runtimeArgs": ["-m", "reflex", "run"],
      "port": 3000
    }
  ]
}
```

- [ ] **Step 3: Start the dev server and confirm the current (unmodified) site loads**

Start the `portfolio-dev` preview server and open it in the browser pane. First boot compiles the Next.js app and can take a few minutes — wait for it to finish.

Expected: the existing purple/green-gradient portfolio loads at the preview URL with no console errors. Leave the server running for the rest of the tasks (Reflex hot-reloads on file save).

- [ ] **Step 4: Commit**

```bash
git add .claude/launch.json
git commit -m "chore: add dev server launch config for portfolio preview"
```

---

### Task 2: Design tokens, global stylesheet, and scroll-reveal script

**Files:**
- Create: `portfolio/theme.py`
- Create: `assets/styles/tron.css`
- Create: `assets/scripts/scroll-reveal.js`
- Create: `components/hud_frame.py`
- Create: `components/grid_background.py`
- Modify: `portfolio/portfolio.py`

- [ ] **Step 1: Create the design tokens module**

Create `portfolio/theme.py`:

```python
"""Centralized design tokens for the TRON-inspired visual theme."""

BG = "#000000"
BG_PANEL = "#0A0A0A"

CYAN = "#5CF6FF"
CYAN_BORDER = "rgba(92, 246, 255, 0.25)"
ORANGE = "#F2994A"

TEXT_PRIMARY = "#EAF6F6"
TEXT_MUTED = "#8FA3A3"

FONT_DISPLAY = "'Orbitron', sans-serif"
FONT_BODY = "'Space Grotesk', sans-serif"
FONT_MONO = "'JetBrains Mono', monospace"
```

- [ ] **Step 2: Create the global stylesheet**

Create `assets/styles/tron.css`:

```css
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800&family=Space+Grotesk:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --tron-bg: #000000;
  --tron-bg-panel: #0A0A0A;
  --tron-cyan: #5CF6FF;
  --tron-orange: #F2994A;
  --tron-text: #EAF6F6;
  --tron-text-muted: #8FA3A3;
  --tron-border: rgba(92, 246, 255, 0.25);
}

/* HUD corner-bracket frame used by components/hud_frame.py */
.hud-frame {
  position: relative;
  border-radius: 0 !important;
  background: var(--tron-bg-panel) !important;
  border: 1px solid var(--tron-border) !important;
}
.hud-frame::before,
.hud-frame::after {
  content: "";
  position: absolute;
  width: 14px;
  height: 14px;
  pointer-events: none;
}
.hud-frame::before {
  top: -1px;
  left: -1px;
  border-top: 2px solid var(--tron-cyan);
  border-left: 2px solid var(--tron-cyan);
}
.hud-frame::after {
  bottom: -1px;
  right: -1px;
  border-bottom: 2px solid var(--tron-orange);
  border-right: 2px solid var(--tron-orange);
}
.hud-frame .trace-runner {
  position: absolute;
  top: -1px;
  left: -1px;
  width: 26px;
  height: 2px;
  background: var(--tron-cyan);
  box-shadow: 0 0 8px var(--tron-cyan);
  animation: hudTrace 2.4s linear infinite;
  animation-play-state: paused;
  pointer-events: none;
}
.hud-frame:hover .trace-runner,
.hud-frame:focus-within .trace-runner {
  animation-play-state: running;
}
@keyframes hudTrace {
  0%   { top: -1px; left: -1px; width: 26px; height: 2px; }
  24%  { top: -1px; left: calc(100% - 25px); width: 26px; height: 2px; }
  25%  { top: -1px; left: calc(100% - 1px); width: 2px; height: 26px; }
  49%  { top: calc(100% - 25px); left: calc(100% - 1px); width: 2px; height: 26px; }
  50%  { top: calc(100% - 1px); left: calc(100% - 25px); width: 26px; height: 2px; }
  74%  { top: calc(100% - 1px); left: -1px; width: 26px; height: 2px; }
  75%  { top: calc(100% - 25px); left: -1px; width: 2px; height: 26px; }
  99%  { top: -1px; left: -1px; width: 2px; height: 26px; }
  100% { top: -1px; left: -1px; width: 26px; height: 2px; }
}

/* Hover-lift, combined with .hud-frame on every card */
.hover-lift {
  transition: transform 0.2s ease-out, box-shadow 0.2s ease-out;
}
.hover-lift:hover,
.hover-lift:focus-within {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(92, 246, 255, 0.15);
}

/* Perspective grid floor behind the hero (light-cycle arena motif) */
.grid-bg-perspective {
  position: absolute;
  left: -20%;
  right: -20%;
  bottom: -10%;
  height: 70%;
  background-image:
    linear-gradient(rgba(92, 246, 255, 0.35) 1px, transparent 1px),
    linear-gradient(90deg, rgba(92, 246, 255, 0.35) 1px, transparent 1px);
  background-size: 26px 26px;
  transform: rotateX(58deg);
  transform-origin: bottom;
  mask-image: linear-gradient(to top, black, transparent 75%);
  -webkit-mask-image: linear-gradient(to top, black, transparent 75%);
  animation: gridDrift 3s linear infinite;
  pointer-events: none;
  z-index: 0;
}
@keyframes gridDrift {
  from { background-position: 0 0; }
  to   { background-position: 0 26px; }
}

/* Scroll-reveal, toggled by assets/scripts/scroll-reveal.js */
.reveal {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}
.reveal.revealed {
  opacity: 1;
  transform: translateY(0);
}

/* Navbar link underline trace */
.nav-link {
  position: relative;
}
.nav-link::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 2px;
  height: 1px;
  width: 0;
  background: var(--tron-cyan);
  box-shadow: 0 0 6px var(--tron-cyan);
  transition: width 0.25s ease-out;
}
.nav-link:hover::after,
.nav-link:focus-visible::after {
  width: 100%;
}

/* Scan-line section divider (available for use between sections) */
.scan-divider {
  position: relative;
  width: 100%;
  height: 1px;
  background: rgba(92, 246, 255, 0.15);
  overflow: hidden;
  margin: 24px 0;
}
.scan-divider::after {
  content: "";
  position: absolute;
  top: -1px;
  left: -10%;
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, transparent, var(--tron-cyan), transparent);
  box-shadow: 0 0 10px var(--tron-cyan);
  animation: scanMove 5s ease-in-out infinite;
}
@keyframes scanMove {
  0%   { left: -10%; }
  100% { left: 100%; }
}

/* Button power-up glow */
.btn-power {
  transition: box-shadow 0.2s ease-out;
}
.btn-power:hover,
.btn-power:focus-visible {
  box-shadow: 0 0 18px rgba(92, 246, 255, 0.65), inset 0 0 10px rgba(92, 246, 255, 0.3);
}
.btn-power-primary {
  animation: powerPulse 2.6s ease-in-out infinite;
}
@keyframes powerPulse {
  0%, 100% { box-shadow: 0 0 0 rgba(92, 246, 255, 0); }
  50%      { box-shadow: 0 0 16px rgba(92, 246, 255, 0.5); }
}

/* Hero name decode-in, runs once on load */
.hero-name-decode {
  animation: decodeIn 1.2s ease-out forwards;
}
@keyframes decodeIn {
  0%   { opacity: 0; filter: blur(4px); letter-spacing: 0.4em; }
  60%  { opacity: 1; filter: blur(0); letter-spacing: 0.02em; }
  100% { opacity: 1; filter: blur(0); letter-spacing: 0.02em; }
}

@media (prefers-reduced-motion: reduce) {
  .hud-frame .trace-runner,
  .grid-bg-perspective,
  .scan-divider::after,
  .btn-power-primary,
  .hero-name-decode {
    animation: none !important;
  }
  .reveal {
    transition: none !important;
    opacity: 1 !important;
    transform: none !important;
  }
  .hover-lift {
    transition: none !important;
  }
}
```

- [ ] **Step 3: Create the scroll-reveal script**

Create `assets/scripts/scroll-reveal.js`:

```javascript
(function () {
  function initReveal() {
    var els = document.querySelectorAll(".reveal");
    var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!("IntersectionObserver" in window) || prefersReduced) {
      els.forEach(function (el) {
        el.classList.add("revealed");
      });
      return;
    }
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("revealed");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );
    els.forEach(function (el) {
      observer.observe(el);
    });
  }

  if (document.readyState === "complete") {
    initReveal();
  } else {
    window.addEventListener("load", initReveal);
  }
})();
```

- [ ] **Step 4: Create the HUD frame component**

Create `components/hud_frame.py`:

```python
import reflex as rx


def hud_frame(*children: rx.Component, **props) -> rx.Component:
    """A box styled as a TRON HUD panel: corner brackets, a hover
    light-trace, and hover-lift motion (see .hud-frame / .hover-lift
    in assets/styles/tron.css). Drop-in replacement for rx.card on
    project/experience/education/stack cards."""
    extra_class = props.pop("class_name", "")
    class_name = f"hud-frame hover-lift {extra_class}".strip()
    return rx.box(
        rx.box(class_name="trace-runner"),
        *children,
        class_name=class_name,
        **props,
    )
```

- [ ] **Step 5: Create the grid background component**

Create `components/grid_background.py`:

```python
import reflex as rx


def grid_background() -> rx.Component:
    """Perspective grid floor rendered behind the hero section
    (see .grid-bg-perspective in assets/styles/tron.css)."""
    return rx.box(class_name="grid-bg-perspective")
```

- [ ] **Step 6: Wire everything into the app and fix the mobile-overflow width bug**

Modify `portfolio/portfolio.py` (full file):

```python
import reflex as rx
from views.header.header import header
from components.navbar import navbar
from components.grid_background import grid_background
from views.stack.stack import stack
from views.projects.projects import projects
from views.experience.experience import experience
from views.education.education import education
from views.footer.footer import footer
from portfolio.theme import BG

from rxconfig import config

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.box(
            grid_background(),
            rx.center(header(), position="relative", width="100%"),
            position="relative",
            overflow="hidden",
            width="100%",
        ),
        rx.box(class_name="scan-divider"),
        stack(
            "HABILIDADES",
            "Algunas de mis habilidades destacadas",
        ),
        rx.box(class_name="scan-divider"),
        projects(
            "PROYECTOS",
            "Algunos de mis proyectos"
        ),
        rx.box(class_name="scan-divider"),
        experience(
            "EXPERIENCIA",
            "Estas son algunas de mis experiencias profesionales"
        ),
        rx.box(class_name="scan-divider"),
        education(
            "FORMACIÓN",
            "Estos son mis estudios y otras formaciones complementarias"
        ),
        rx.box(class_name="scan-divider"),
        footer(),
        rx.script(src="/scripts/scroll-reveal.js"),
        spacing="6",
        width="100%",
        background=BG,
        text_align="center"
        )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
    ),
    stylesheets=["/styles/tron.css"],
)
app.add_page(index)
```

This replaces the old `width=["260%", "100%"]` (the mobile-overflow bug) and the purple/green gradient `background` with the flat TRON black, and registers the new stylesheet.

- [ ] **Step 7: Verify**

With the dev server still running (Task 1), reload the preview. Confirm:
- The page background is solid black (no more purple/green gradient).
- A faint cyan grid is visible behind the hero area, angled like a floor, slowly drifting.
- Thin dividers with a traveling light sweep appear between each major section (scan-line dividers).
- No console errors about the missing `/styles/tron.css` or `/scripts/scroll-reveal.js` (check the Network tab — both should return 200).
- Load the page at a 375px-wide viewport and confirm there is no horizontal scrollbar/overflow (this validates the width-bug fix).

- [ ] **Step 8: Commit**

```bash
git add portfolio/theme.py assets/styles/tron.css assets/scripts/scroll-reveal.js components/hud_frame.py components/grid_background.py portfolio/portfolio.py
git commit -m "feat: add TRON design tokens, global stylesheet, and grid/HUD foundation"
```

---

### Task 3: Hero/header content, typo fixes, and broken CV link

**Files:**
- Modify: `views/header/header.py`

- [ ] **Step 1: Rewrite the header with fixed content and the decode-in / power-up classes**

Replace the full contents of `views/header/header.py`:

```python
import reflex as rx
from components.link_button import link_button
from portfolio.theme import TEXT_PRIMARY

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Hola, soy Axel Villa 👋",
            font_size=["3em", "3.5em"],
            width="100%",
            margin_bottom="0.5em",
            class_name="hero-name-decode",
            ),
        rx.text(
            "Desarrollador Full Stack",
            font_size=["2em", "2em"],
            width="100%"
            ),
        rx.hstack(
            link_button(
                "Github",
                "https://github.com/axelvilla",
                "/github-icon.svg",

                ),
            rx.spacer(),
            link_button(
                "Linkedin",
                "https://www.linkedin.com/in/axel-villa-a00a06318/",
                "/linkedin-icon.svg"
                ),
            rx.spacer(),
            link_button(
                "Email",
                "mailto:axelvilla746@gmail.com",
                "/email-icon.svg"
                ),
            width=["90%", "70%"],
            align="center"
        ),
        rx.text(
            """
            Desarrollador Full Stack con experiencia en proyectos web
            utilizando Java (Spring Boot), Python (Flask, FastAPI) y
            JavaScript/TypeScript (React, Node.js, Next.js). Apasionado
            por la construcción de aplicaciones escalables y bien
            estructuradas, con experiencia liderando proyectos en GitHub
            y aplicando buenas prácticas de programación, control de
            versiones y metodologías ágiles.
            """,
            size="7",
            font_size=["1.5em", "1.3em"],
            width=["80%", "90%"],
            text_align="center",
            margin_bottom="1em"
        ),
        rx.button(
            rx.image(
                src="/downloadicon.svg",
                max_width="2em",
                alt="download icon"
                ),
            "Descargar CV",
            on_click=rx.download(url="/CV_Gomez_Axel.pdf"),
            bg="black",
            color=TEXT_PRIMARY,
            border="solid",
            border_color="grey",
            size="4",
            font_size=["2em", "1em"],
            padding_x="3em",
            padding_y=["1.5em", "1em"],
            class_name="btn-power btn-power-primary",

        ),
        align="center",
        spacing="5",
        margin_bottom="4em",
        width="100%",
        justify="center"
    )
```

This fixes: the "Pyhton" typo (subtitle is now just "Desarrollador Full Stack"), the CV download link (`/CV_Gomex_Axel.pdf` → `/CV_Gomez_Axel.pdf`, matching the real file in `public/`), the email typo (`axelvilla745` → `axelvilla746`, matching the CV), and rewrites the bio paragraph using the CV's professional summary. It also adds the once-on-load decode-in animation to the name and a persistent subtle glow pulse to the primary CV button.

- [ ] **Step 2: Verify**

Reload the preview. Confirm:
- On page load, the name "Hola, soy Axel Villa 👋" animates in once (blur/tracking resolving), not looping.
- The subtitle reads "Desarrollador Full Stack" with no typo.
- The bio paragraph matches the new CV-based text.
- The "Descargar CV" button has a slow, subtle glowing pulse.
- Click "Descargar CV" and confirm it downloads `CV_Gomez_Axel.pdf` (not a 404).
- Hover the Email button in the header and confirm the mailto link is `axelvilla746@gmail.com` (inspect the link href, or check `views/header/header.py`).

- [ ] **Step 3: Commit**

```bash
git add views/header/header.py
git commit -m "fix: correct CV download link, subtitle typo, and email; refresh hero bio from CV"
```

---

### Task 4: Navbar links, buttons, and footer styling

**Files:**
- Modify: `components/link_bio.py`
- Modify: `components/link_button.py`
- Modify: `components/footer_links.py`
- Modify: `views/footer/footer.py`

- [ ] **Step 1: Update the nav link component**

Replace the full contents of `components/link_bio.py`:

```python
import reflex as rx
from portfolio.theme import TEXT_PRIMARY, FONT_BODY

def link_bio(text: str, url: str) -> rx.Component:
    return rx.button(
        text,
        bg="transparent",
        _hover = {
                "background_color": "rgba(92, 246, 255, 0.08)"
            },
        color=TEXT_PRIMARY,
        font_family=FONT_BODY,
        letter_spacing="0.05em",
        font_size=["1.5em", "1em"],
        class_name="nav-link",
        on_click=(rx.scroll_to(url))
    )
```

- [ ] **Step 2: Update the external link-button component**

Replace the full contents of `components/link_button.py`:

```python
import reflex as rx
from portfolio.theme import TEXT_PRIMARY, BG_PANEL, CYAN_BORDER, FONT_BODY

def link_button(text: str, url: str, logo:str) -> rx.Component:
    return rx.link(

        rx.button(
            rx.image(
            src=logo,
            max_width=["1.5em", "1em"],
            alt=logo
        ),
            text,
            size="4",
            font_family=FONT_BODY,
            font_size=["2em", "1.5em"],
            bg=BG_PANEL,
            border="solid",
            border_color=CYAN_BORDER,
            class_name="btn-power",
            padding=["1em", "1em"],
        ),
        is_external=True,
        href=url,
        underline="none",
        color=TEXT_PRIMARY,

    )
```

- [ ] **Step 3: Update the footer icon-button component**

Replace the full contents of `components/footer_links.py`:

```python
import reflex as rx
from portfolio.theme import TEXT_PRIMARY

def footer_links(url: str, image:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.image(
                src=image,
                max_width=["3em","2em"],
                alt=image
            ),
            bg="transparent",
            class_name="btn-power",
        ),
        href=url,
        underline="none",
        color=TEXT_PRIMARY,
        is_external=True,
        margin_y="1em"
    )
```

- [ ] **Step 4: Fix the footer's email typo and add scroll-reveal**

Replace the full contents of `views/footer/footer.py`:

```python
import reflex as rx
from components.footer_links import footer_links

def footer() -> rx.Component:
    return rx.vstack(

        rx.text(
            "Axel Benjamin Villa",
            font_size=["1.5em", "1em"],
        ),
        rx.hstack(
            footer_links("https://www.linkedin.com/in/axel-villa-a00a06318/", "/linkedin-icon.svg"),
            footer_links("https://github.com/axelvilla", "/github-icon.svg"),
            footer_links("mailto:axelvilla746@gmail.com", "/email-icon.svg"),
        ),
        width="100%",
        align="center",
        margin_bottom="2em",
        class_name="reveal",
    )
```

- [ ] **Step 5: Verify**

Reload the preview. Confirm:
- Hovering a navbar link (HABILIDADES/PROYECTOS/EXPERIENCIA/FORMACION) shows a cyan underline trace filling left-to-right.
- Hovering the Github/Linkedin/Email buttons in the hero and the footer shows a cyan glow.
- Tab (keyboard-only) through the navbar and header buttons — the same underline/glow effects should appear on focus, not just mouse hover.
- The footer's email icon links to `mailto:axelvilla746@gmail.com`.
- Scroll down to the footer and confirm it fades/slides into view the first time it enters the viewport.

- [ ] **Step 6: Commit**

```bash
git add components/link_bio.py components/link_button.py components/footer_links.py views/footer/footer.py
git commit -m "style: apply TRON theme tokens and hover/focus effects to nav, buttons, and footer"
```

---

### Task 5: Stack/skills section

**Files:**
- Modify: `components/stack_card.py`
- Modify: `views/stack/stack.py`

- [ ] **Step 1: Convert the stack card to a mono text HUD chip**

Replace the full contents of `components/stack_card.py`:

```python
import reflex as rx
from components.hud_frame import hud_frame
from portfolio.theme import CYAN, FONT_MONO


def stack_card(text: str) -> rx.Component:
    return hud_frame(
        rx.text(
            text,
            font_family=FONT_MONO,
            letter_spacing="0.08em",
            text_transform="uppercase",
            font_size=["1.4em", "0.85em"],
            color=CYAN,
        ),
        padding="1em 1.5em",
    )
```

This drops the per-icon-image approach (previously `stack_card(text, url)` rendered an `rx.avatar` from a logo file). None of the new CV technologies below have a matching icon asset in `assets/`, and mixing colorful brand-logo SVGs with the restrained cyan/orange HUD palette would clash with the approved visual direction — so every skill is now a uniform mono-font chip. This is a implementation-level refinement of the spec's "Stack / Skills" section, not a change to which technologies are listed.

- [ ] **Step 2: Update the stack section with the full CV technology list**

Replace the full contents of `views/stack/stack.py`:

```python
import reflex as rx
from components.stack_card import stack_card

def stack(title:str, body: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            color="white",
            size="5",
            font_size=["2em", "1.5em"],
            as_="bold"
        ),
        rx.text(
            body,
            font_size=["1.5em", "1em"],
        ),
        rx.hstack(
            rx.flex(
                stack_card("HTML"),
                stack_card("CSS"),
                stack_card("BootStrap"),
                stack_card("Tailwind"),
                stack_card("JavaScript"),
                stack_card("TypeScript"),
                stack_card("Python"),
                stack_card("Java"),
                stack_card("React"),
                stack_card("NextJS"),
                stack_card("Flask"),
                stack_card("FastAPI"),
                stack_card("Spring Boot"),
                stack_card("Hibernate"),
                stack_card("MySQL"),
                stack_card("MongoDB"),
                stack_card("Prisma"),
                stack_card("Docker"),
                stack_card("Vercel"),
                stack_card("GitHub"),
                flex_wrap="wrap",
                spacing="2",
                width="100%",
                justify="center",
            ),
        ),
        align="center",
        width="100%",
        padding_x="5em",
        spacing="4",
        justify="center",
        id="habilidades",
        class_name="reveal",
    )
```

- [ ] **Step 3: Verify**

Reload the preview and scroll to the Habilidades section. Confirm:
- 20 mono-font, uppercase, cyan-text chips render in a wrapped grid, each with cyan/orange corner brackets.
- Hovering a chip lifts it slightly and its border light-traces around the perimeter.
- No broken image icons (there shouldn't be any `<img>` in this section anymore).

- [ ] **Step 4: Commit**

```bash
git add components/stack_card.py views/stack/stack.py
git commit -m "feat: redesign stack section as TRON HUD chips with full CV tech list"
```

---

### Task 6: Projects section (full content replacement)

**Files:**
- Modify: `components/projects_card.py`
- Modify: `views/projects/projects.py`
- Delete: `components/stack_projects.py`

- [ ] **Step 1: Rewrite the project card (no screenshot image, no repo link — all 4 new projects are live-only)**

Replace the full contents of `components/projects_card.py`:

```python
import reflex as rx
from components.hud_frame import hud_frame
from portfolio.theme import CYAN, TEXT_PRIMARY, TEXT_MUTED, FONT_DISPLAY, FONT_MONO


def projects_card(title: str, body: str, stack: str, web: str) -> rx.Component:
    return hud_frame(
        rx.vstack(
            rx.heading(
                title,
                font_size=["2em", "1.2em"],
                font_family=FONT_DISPLAY,
                color=TEXT_PRIMARY,
            ),
            rx.text(
                body,
                font_size=["1.5em", "1em"],
                color=TEXT_MUTED,
            ),
            rx.text(
                stack,
                font_family=FONT_MONO,
                letter_spacing="0.05em",
                text_transform="uppercase",
                font_size=["1.2em", "0.85em"],
                color=CYAN,
            ),
            rx.link(
                "Ver sitio en vivo →",
                href=web,
                is_external=True,
                color=CYAN,
                font_family=FONT_MONO,
                font_size=["1.3em", "0.9em"],
                underline="none",
                margin_top="0.5em",
            ),
            align="start",
            spacing="2",
            width="100%",
        ),
        width=["90%", "45%"],
        margin_right="0.5em",
        padding="1.5em",
    )
```

- [ ] **Step 2: Delete the dead `stack_projects` component**

```bash
git rm components/stack_projects.py
```

- [ ] **Step 3: Replace the project list with the 4 new live projects**

Replace the full contents of `views/projects/projects.py`:

```python
import reflex as rx
from components.projects_card import projects_card

def projects(title:str, body: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            color="white",
            size="5",
            font_size=["2em", "1.5em"],
            as_="bold"
        ),
        rx.text(
            body,
            font_size=["1.5em", "1em"],
        ),
        rx.hstack(
            rx.flex(
                projects_card(
                    "Tienda Informática",
                    "E-commerce de componentes y periféricos de PC, con filtros por categoría y marca, y un configurador \"Armá tu PC\".",
                    "React, Tailwind",
                    "https://informatica-sepia.vercel.app/",
                    ),
                projects_card(
                    "1step",
                    "Plataforma de software a medida para automatizar y centralizar las operaciones de negocios de servicios.",
                    "React, Tailwind",
                    "https://1stepservice.vercel.app/",
                    ),
                projects_card(
                    "Inmobiliaria Reconquista",
                    "Portal inmobiliario con búsqueda filtrada de propiedades en venta y alquiler.",
                    "React, Tailwind",
                    "https://inmobiliaria-reconquista.vercel.app/",
                    ),
                projects_card(
                    "La Cumbre",
                    "Sitio de la verdulería La Cumbre: catálogo de ofertas, galería de productos y pedidos por WhatsApp.",
                    "React, Tailwind",
                    "https://lacumbre.netlify.app/",
                    ),
                flex_wrap="wrap",
                spacing="2",
                width="100%",
                justify="center",
            ),
            width="100%",
            justify="center",
        ),
    align="center",
    width="100%",
    id="projects",
    class_name="reveal",
    )
```

- [ ] **Step 4: Verify**

Reload the preview and scroll to the Proyectos section. Confirm:
- Exactly 4 project cards render: Tienda Informática, 1step, Inmobiliaria Reconquista, La Cumbre. The old 3 (Amazing Jobs, Sistema Veterinaria, Citador APA) are gone.
- Each card's "Ver sitio en vivo →" link opens the correct URL in a new tab (check all 4 hrefs).
- No console error about a missing `stack_projects` import.

- [ ] **Step 5: Commit**

```bash
git add components/projects_card.py views/projects/projects.py
git commit -m "feat: replace project list with 4 current live projects and redesign the card"
```

---

### Task 7: Experience section

**Files:**
- Modify: `components/experience_card.py`
- Modify: `views/experience/experience.py`

- [ ] **Step 1: Rewrite the experience card to support a list of sub-bullets and fix the tuple-return bug**

Replace the full contents of `components/experience_card.py`:

```python
import reflex as rx
from components.hud_frame import hud_frame
from portfolio.theme import TEXT_PRIMARY, TEXT_MUTED, FONT_DISPLAY


def experience_card(title: str, body, img: str) -> rx.Component:
    if isinstance(body, list):
        body_content = rx.vstack(
            *[
                rx.text(
                    f"▸ {item}",
                    font_size=["1.4em", "0.95em"],
                    color=TEXT_MUTED,
                    text_align="left",
                )
                for item in body
            ],
            align="start",
            spacing="1",
        )
    else:
        body_content = rx.text(
            body,
            font_size=["1.5em", "1em"],
            color=TEXT_MUTED,
        )
    return hud_frame(
        rx.flex(
            rx.image(
                src=img,
                max_width=["10%", "7%"],
                object_fit="cover",
                alt=img,
            ),
            rx.box(
                rx.heading(
                    title,
                    font_size=["2em", "1em"],
                    font_family=FONT_DISPLAY,
                    color=TEXT_PRIMARY,
                ),
                body_content,
            ),
            spacing="2",
            align="center",
        ),
        width="100%",
        padding="1em",
    )
```

Note this previously ended with `),` after the closing `rx.card(...)` call, which made the function return a 1-tuple instead of a `Component` — the rewrite above removes that trailing comma. `body` now accepts either a `str` (single-line entries, e.g. "Instructor de Java") or a `list[str]` (sub-bullets, used for the freelance entry below).

- [ ] **Step 2: Add the CV freelance experience entry and keep the existing instructor entry**

Replace the full contents of `views/experience/experience.py`:

```python
import reflex as rx
from components.experience_card import experience_card

def experience(title:str, body: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            color="white",
            font_size=["2em", "1.5em"],
            as_="bold"
        ),
        rx.text(
            body,
            font_size=["1.5em", "1em"],
        ),
        rx.vstack(
            rx.grid(
                experience_card(
                    "Desarrollador Full Stack y Líder de Proyecto — Freelance (2025)",
                    [
                        "Login App: sistema de autenticación con React.js + Flask + MySQL, validación de credenciales, sesiones seguras y arquitectura modular.",
                        "Filter App: gestión y filtrado de datos con backend en FastAPI y frontend en React.js.",
                        "Sistema de Laboratorio de Análisis Clínicos: backend en Node.js, frontend en Next.js/React, y persistencia con MySQL + Prisma; incluye autenticación, gestión de pacientes y carga de resultados.",
                        "Punto de Venta para Verdulería: backend en Java (Spring Boot), frontend en Next.js, MySQL y Docker, para gestionar productos, stock y ventas.",
                    ],
                    "github-icon.svg",
                    ),
                experience_card(
                    "Instructor de Java",
                    "Escuela Superior de Comercio N° 43",
                    "teacher-icon.svg",
                    ),
                width=["90%","70%"],
                spacing="4",
            ),
            width="100%",
            align="center"
        ),
        align="center",
        width="100%",
        id="experience",
        class_name="reveal",
    )
```

- [ ] **Step 3: Verify**

Reload the preview and scroll to the Experiencia section. Confirm:
- Two cards render: the new "Desarrollador Full Stack y Líder de Proyecto" card (4 sub-bullets: Login App, Filter App, Sistema de Laboratorio de Análisis Clínicos, Punto de Venta para Verdulería) and the existing "Instructor de Java" card.
- The new card's icon is the GitHub icon.
- Both cards show the HUD corner brackets and hover-lift.

- [ ] **Step 4: Commit**

```bash
git add components/experience_card.py views/experience/experience.py
git commit -m "feat: add CV freelance experience entry, fix tuple-return bug in experience_card"
```

---

### Task 8: Education section

**Files:**
- Modify: `views/education/education.py`

- [ ] **Step 1: Replace the education list with the CV's exact 4 entries**

Replace the full contents of `views/education/education.py`:

```python
import reflex as rx
from components.experience_card import experience_card

def education(title:str, body: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            color="white",
            font_size=["2em", "1.5em"],
            as_="bold"
        ),
        rx.text(
            body,
            font_size=["1.5em", "1em"],
        ),
        rx.vstack(
            rx.grid(
                experience_card(
                    "Técnico Superior en Desarrollo de Software",
                    "Escuela Superior de Comercio N° 43",
                    "escuela-icon.png"
                ),
                experience_card(
                    "Full Stack Python",
                    "Codo a Codo 4.0",
                    "cac-icon.png"
                ),
                experience_card(
                    "Full Stack Java",
                    "Codo a Codo 4.0",
                    "cac-icon.png"
                ),
                experience_card(
                    "Full Stack Javascript",
                    "Bootcamp: JSCamp InfoJobs",
                    "javascript-icon.svg"
                ),
                width=["90%", "70%"],
                spacing="4"
            ),
            width="100%",
            align="center",
        ),
        align="center",
        width="100%",
        id="education",
        class_name="reveal",
    )
```

This drops "Programación Inicial - Codo a Codo" (not present in the current CV) and adds "Full Stack Java" (Codo a Codo 4.0) and "Full Stack Javascript" (Bootcamp: JSCamp InfoJobs), reusing the existing `cac-icon.png` and `javascript-icon.svg` assets so no new icon files are needed.

- [ ] **Step 2: Verify**

Reload the preview and scroll to the Formación section. Confirm exactly 4 cards render, in this order: Técnico Superior en Desarrollo de Software, Full Stack Python, Full Stack Java, Full Stack Javascript — and "Programación Inicial" is gone.

- [ ] **Step 3: Commit**

```bash
git add views/education/education.py
git commit -m "content: update education section to match current CV"
```

---

### Task 9: Full-site verification pass

**Files:** none (verification only; fix forward in this task if something fails)

- [ ] **Step 1: Desktop pass**

At a 1280px-wide viewport, scroll through the entire page top to bottom. Confirm: navbar → hero (grid floor + decode-in name + bio + social buttons + CV button) → Habilidades (20 chips) → Proyectos (4 cards) → Experiencia (2 cards) → Formación (4 cards) → footer, each section fading/sliding into view once as it's scrolled to.

- [ ] **Step 2: Mobile pass**

At a 375px-wide viewport, repeat the same scroll-through. Confirm there is no horizontal overflow/scrollbar anywhere on the page (this is the width-bug regression check) and that all cards/chips reflow to a single column or wrap sensibly.

- [ ] **Step 3: Reduced-motion pass**

Emulate `prefers-reduced-motion: reduce` in the browser devtools (Rendering tab → Emulate CSS media feature) and reload. Confirm the hero decode-in, grid floor drift, section scan-line dividers, and the CV button's persistent pulse are all disabled or static, while content is still fully visible (no permanently-hidden `.reveal` elements stuck at `opacity: 0`).

- [ ] **Step 4: Keyboard pass**

Starting from the top of the page, press Tab repeatedly through every interactive element (navbar links, social buttons, CV button, project "Ver sitio en vivo" links, footer icons). Confirm each one shows a visible focus effect (underline trace, glow, or lift — whichever it uses on hover) and that focus order follows the visual top-to-bottom order.

- [ ] **Step 5: Link pass**

Click through all 4 project live-site links and the CV download button one more time end-to-end to confirm nothing regressed from earlier per-task checks.

- [ ] **Step 6: Stop the dev server**

Stop the `portfolio-dev` preview server once verification is complete.
