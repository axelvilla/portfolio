import reflex as rx
from components.link_button import link_button
from portfolio.theme import TEXT_PRIMARY, BG_PANEL, CYAN_BORDER

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Hola, soy Axel Villa 👋",
            font_size=["3em", "3.5em"],
            line_height="1.2",
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
            align="center",
            wrap="wrap",
            justify="center",
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
            bg=BG_PANEL,
            color=TEXT_PRIMARY,
            border="solid",
            border_color=CYAN_BORDER,
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
