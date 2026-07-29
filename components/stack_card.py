import reflex as rx
from components.hud_frame import hud_frame
from portfolio.theme import CYAN, FONT_MONO


def stack_card(text: str) -> rx.Component:
    return hud_frame(
        rx.text(
            text,
            font_family=FONT_MONO,
            letter_spacing="0.08em",
            text_transform="uppercase",
            font_size=["1.4em", "0.85em"],
            color=CYAN,
        ),
        padding="1em 1.5em",
    )
