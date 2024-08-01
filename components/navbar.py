import reflex as rx
from components.link_bio import link_bio

def navbar() -> rx.Component:
    return rx.hstack(
        link_bio("HABILIDADES", "habilidades"),
        link_bio("PROYECTOS", "projects"),
        rx.spacer(),
        link_bio("EXPERIENCIA", "experience"),
        link_bio("FORMACION", "education"),
        width="100%",
        padding="2em",
    )