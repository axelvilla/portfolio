import reflex as rx
from components.stack_card import stack_card

def stack(title:str, body: str) -> rx.Component:
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
        rx.hstack(
            rx.flex(
                stack_card("HTML", "html-icon.svg"),
                stack_card("CSS", "css-icon.svg"),
                stack_card("BootStrap", "bootstrap-icon.svg"),
                stack_card("Tailwind", "tailwind-icon.svg"),
                stack_card("Python", "python-icon.svg"),
                stack_card("Flask", "flask-svgrepo-com.svg"),
                stack_card("Java", "java-icon.svg"),
                stack_card("MySQL", "mysql-icon.svg"),
                stack_card("Vercel", "vercel-logo.svg"),
                stack_card("GitHub", "github-white-icon.svg"),
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
        id="habilidades"
    )