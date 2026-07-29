import reflex as rx
from portfolio.theme import TEXT_PRIMARY, FONT_BODY

def link_bio(text: str, url: str) -> rx.Component:
    return rx.button(
        text,
        bg="transparent",
        _hover = {
                "background_color": "rgba(92, 246, 255, 0.08)"
            },
        color=TEXT_PRIMARY,
        font_family=FONT_BODY,
        letter_spacing="0.05em",
        font_size=["1.5em", "1em"],
        class_name="nav-link",
        on_click=(rx.scroll_to(url))
    )
