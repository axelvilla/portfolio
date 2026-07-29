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
