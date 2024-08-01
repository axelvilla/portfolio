import reflex as rx
from components.footer_links import footer_links

def footer() -> rx.Component:
    return rx.vstack(
        
        rx.text(
            "Axel Benjamin Villa",
            font_size=["1.5em", "1em"],
        ),
        rx.hstack(
            footer_links("https://www.linkedin.com/in/axel-villa-a00a06318/", "/linkedin-icon.svg"),
            footer_links("https://github.com/axelvilla", "/github-icon.svg"),
            footer_links("mailto:axelvilla745@gmail.com", "/email-icon.svg"),
        ),
        width="100%",
        align="center",
        margin_bottom="2em",
    )