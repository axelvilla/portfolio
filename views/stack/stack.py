import reflex as rx
from components.stack_card import stack_card

def stack(title:str, body: str) -> rx.Component:
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
                stack_card("Java", "java-icon.svg"),
                stack_card("MySQL", "mysql-icon.svg"),
                stack_card("HTML", "html-icon.svg"),
                stack_card("CSS", "css-icon.svg"),
                stack_card("Python", "python-icon.svg"),
                stack_card("Flask", "flask-svgrepo-com.svg"),
                flex_wrap="wrap",
                spacing="2",
                width="100%",
                justify="center"
            ),
        ),
        align="center",
        width="100%",
        spacing="4",
        id="habilidades"
    )