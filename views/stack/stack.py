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
