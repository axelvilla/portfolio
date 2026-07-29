import reflex as rx
from components.hud_frame import hud_frame
from portfolio.theme import CYAN, TEXT_PRIMARY, TEXT_MUTED, FONT_DISPLAY, FONT_MONO


def projects_card(title: str, body: str, stack: str, web: str) -> rx.Component:
    return hud_frame(
        rx.vstack(
            rx.heading(
                title,
                font_size=["2em", "1.2em"],
                font_family=FONT_DISPLAY,
                color=TEXT_PRIMARY,
            ),
            rx.text(
                body,
                font_size=["1.5em", "1em"],
                color=TEXT_MUTED,
            ),
            rx.text(
                stack,
                font_family=FONT_MONO,
                letter_spacing="0.05em",
                text_transform="uppercase",
                font_size=["1.2em", "0.85em"],
                color=CYAN,
            ),
            rx.link(
                "Ver sitio en vivo →",
                href=web,
                is_external=True,
                rel="noopener noreferrer",
                color=CYAN,
                font_family=FONT_MONO,
                font_size=["1.3em", "0.9em"],
                underline="none",
                margin_top="0.5em",
            ),
            align="start",
            spacing="2",
            width="100%",
        ),
        width=["90%", "45%"],
        margin_right="0.5em",
        padding="1.5em",
    )
