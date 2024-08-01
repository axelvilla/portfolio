import reflex as rx
from components.link_button import link_button

def projects_card(title:str, body:str, stack:str, image:str, repo:str) -> rx.Component:
    return rx.card(
            rx.flex(
                rx.image(
                    src=image,
                    ##max_width="5em",
                    border_radius= "8px",
                    max_width= "38%",
                    max_height= "12em",
                    object_fit= "cover",
                    opacity="0.8"
                ),
                rx.box(
                    rx.heading(
                        title,
                        size="6",
                        as_="bold",
                        color="white"
                    ),
                    rx.text(
                        body,
                        size="3",
                        margin_bottom="1em",
                        color="white"
                    ),
                    rx.text(
                        stack,
                        size="3",
                        margin_bottom="1em",
                        color="white",
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
        width=["80%", "45%"]    ,
        margin_right="0.5em",
    )