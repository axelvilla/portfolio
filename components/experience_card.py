import reflex as rx
from components.hud_frame import hud_frame
from portfolio.theme import TEXT_PRIMARY, TEXT_MUTED, FONT_DISPLAY


def experience_card(title: str, body: str, img: str) -> rx.Component:
    body_content = rx.text(
        body,
        font_size=["1.5em", "1em"],
        color=TEXT_MUTED,
    )
    return hud_frame(
        rx.flex(
            rx.image(
                src=img,
                max_width=["10%", "7%"],
                object_fit="cover",
                alt=img,
            ),
            rx.box(
                rx.heading(
                    title,
                    font_size=["2em", "1em"],
                    font_family=FONT_DISPLAY,
                    color=TEXT_PRIMARY,
                ),
                body_content,
            ),
            spacing="2",
            align="center",
        ),
        width="100%",
        padding="1em",
    )
