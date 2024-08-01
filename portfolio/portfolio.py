import reflex as rx
from views.header.header import header
from components.navbar import navbar
from views.stack.stack import stack
from views.projects.projects import projects
from views.experience.experience import experience
from views.education.education import education
from views.footer.footer import footer

from rxconfig import config


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.center(
            header(),
            ##width="100%",
            ##align="center",
            ##justify="center"
        ),
        stack(
            "HABILIDADES", 
            "Algunas de mis habilidades destacadas",
        ),
        projects(
            "PROYECTOS", 
            "Algunos de mis proyectos"
        ),
        experience(
            "EXPERIENCIA", 
            "Estas son algunas de mis experiencias profesionales"
        ),
        education(
            "FORMACIÓN", 
            "Estos son mis estudios y otras formaciones complementarias"
        ),
        footer(),
        spacing="6",
        width=["200%", "100%"],
        background="linear-gradient(100deg, rgba(131,58,180,0.2) 0%, rgba(139,69,109,0.2) 50%, rgba(40,102,46,0.2) 100%)",
        text_align="center"
        )


app = rx.App()
app.add_page(index)
