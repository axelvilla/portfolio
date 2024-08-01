import reflex as rx
from components.projects_card import projects_card
from components.stack_projects import stack_projects

def projects(title:str, body: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            color="white",
            size="5",
            as_="bold"
        ),
        rx.text(
            body,
        ),
        rx.hstack(
            rx.flex(
                projects_card(
                    "Amanzing Jobs", 
                    "Página dedicada a la busqueda de empleo",
                    "HTML, CSS, JavaScript",
                    "work_page.png",
                    "https://github.com/axelvilla/Empleos_FrontEnd",
                    ),
                projects_card(
                    "Sistema de Gestión Veterinaria", 
                    "Sistema de manejo de clientes",
                    "HTML, Bootstrap, Python, Flask", 
                    "back.png",
                    "https://github.com/axelvilla/BackEnd_Python",
                    ),
                projects_card(
                    "Citador de Bibliografía", 
                    "Página para citar bibliografía con normas APA", 
                    "HTML, Bootstrap, Python, Flask",
                    "apa.jpg",
                    "https://github.com/axelvilla/ReferenciasApa",
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
    id="projects"
    )