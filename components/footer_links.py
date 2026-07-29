import reflex as rx
from portfolio.theme import TEXT_PRIMARY

def footer_links(url: str, image:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.image(
                src=image,
                max_width=["3em","2em"],
                alt=image
            ),
            bg="transparent",
            class_name="btn-power",
        ),
        href=url,
        underline="none",
        color=TEXT_PRIMARY,
        is_external=True,
        margin_y="1em"
    )
