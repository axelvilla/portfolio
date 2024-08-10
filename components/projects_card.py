import reflex as rx
from components.link_button import link_button

def projects_card(title:str, body:str, stack:str, image:str, repo:str, web:str) -> rx.Component:
    return rx.card(
            rx.flex(
                rx.image(
                    src=image,
                    ##max_width="5em",
                    border_radius= "8px",
                    max_width= "38%",
                    max_height= "12em",
                    object_fit= "cover",
                    opacity="0.8",
                    alt=image
                ),
                rx.box(
                    rx.link(
                        rx.heading(
                            title,
                            font_size=["2em", "1em"],
                            as_="bold",
                            color="white"
                        ),
                        rx.text(
                            body,
                            font_size=["1.5em", "1em"],
                            margin_bottom="1em",
                            color="white"
                        ),
                        rx.text(
                            stack,
                            font_size=["1.5em", "1em"],
                            margin_bottom="1em",
                            color="white",
                        ),
                        href=web,
                        is_external=True
                    ),
                    link_button(
                        "Ver más",
                        repo,
                        "link-icon.svg"
                    ),
                    margin_left="1em"
                ),
                spacing="2",
            ),
        width=["90%", "45%"],
        margin_right="0.5em",
    )