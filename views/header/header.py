import reflex as rx
from components.link_button import link_button

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Hola, soy Axel Villa 👋",
            font_size=["3em", "3.5em"],
            width="100%",
            margin_bottom="0.5em"
            ),
        rx.text(
            "Desarrollador de Software",
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
                "mailto:axelvilla745@gmail.com", 
                "/email-icon.svg"
                ),
            width=["90%", "70%"],
            align="center"
        ),
        ##rx.heading(
            ##"Soy Axel Villa, futuro desarrollador de software",
            ##size="9",
            ##font_size=["3em", "2.5em"],
            ##margin_top="1em",
            ##width=["90%", "100%"]
        ##),
        rx.text(
            """
            Como desarrollador de software, me especializo en crear 
            soluciones digitales personalizadas para cada cliente. Mi 
            objetivo es transformar tus ideas en proyectos innovadores y 
            efectivos. Explora mis proyectos anteriores para ver cómo puedo 
            ayudarte a desarrollar y perfeccionar tus propuestas. 
            ¡Construyamos el futuro de tu visión digital!
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
            on_click=rx.download(url="/CV_Gomex_Axel.pdf"),
            bg="black",
            color="white",
            border="solid",
            border_color="grey",
            size="4",
            font_size=["2em", "1em"],
            padding_x="3em",
            padding_y=["1.5em", "1em"],
            _hover = {
                "background_color": "rgba(255, 255, 255, 0.1)"
            },
            
        ),
        align="center",
        spacing="5",
        margin_bottom="4em",
        width="100%",
        justify="center"
    )
    