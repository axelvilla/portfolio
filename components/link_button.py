import reflex as rx
from portfolio.theme import TEXT_PRIMARY, BG_PANEL, CYAN_BORDER, FONT_BODY

def link_button(text: str, url: str, logo:str) -> rx.Component:
    return rx.link(

        rx.button(
            rx.image(
            src=logo,
            max_width=["1.5em", "1em"],
            alt=logo
        ),
            text,
            size="4",
            font_family=FONT_BODY,
            font_size=["2em", "1.5em"],
            bg=BG_PANEL,
            border="solid",
            border_color=CYAN_BORDER,
            class_name="btn-power",
            padding=["1em", "1em"],
        ),
        is_external=True,
        href=url,
        underline="none",
        color=TEXT_PRIMARY,
        rel="noopener noreferrer",

    )
