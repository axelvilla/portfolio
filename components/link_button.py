import reflex as rx

def link_button(text: str, url: str, logo:str) -> rx.Component:
    return rx.link(
        
        rx.button(
            rx.image(
            src=logo,
            max_width=["1.5em", "2em"],
            alt=logo
        ),
            text,
            size="4",
            font_size=["2em", "1.5em"],
            bg="black",
            border="solid",
            border_color="rgb(90, 51, 163)",
            _hover = {
                "background_color": "rgba(90, 51, 163, 0.2)"
            },
            padding=["1em", "1em"],
        ),
        is_external=True,
        href=url,
        underline="none",
        color="white",
        
    )