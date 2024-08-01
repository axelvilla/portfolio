import reflex as rx
from components.experience_card import experience_card

def education(title:str, body: str) -> rx.Component:
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
        rx.vstack(
            rx.grid(
                experience_card(
                    "Técnico Superior en Desarrollo de Software", 
                    "Escuela Superior de Comercio N° 43", 
                    "escuela-icon.png"
                ),
                experience_card(
                    "Programación Inicial", 
                    "Codo a Codo 4.0", 
                    "cac-icon.png"
                ),
                experience_card(
                    "Full Stack Python", 
                    "Codo a Codo 4.0", 
                    "cac-icon.png"
                ),
                width="70%",
                spacing="4"
            ),
            width="100%",
            align="center",
        ),
        align="center",
        width="100%",
        id="education"
    )