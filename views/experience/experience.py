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
                    "En busca de experiencia", 
                    "Aún no cuento con experiencia en un trabajo formal, pero estoy en busca de poder adquirirla y usar todo el conocimiento que poseo",
                    "portfolio-icon.svg",
                    ),
                width=["90%","70%"],
                
            ),
            width="100%",
            align="center"
        ),
        align="center",
        width="100%",
        id="experience"
    )