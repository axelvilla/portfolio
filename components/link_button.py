import reflex as rx

def link_button(text: str, url: str, logo:str) -> rx.Component:
    return rx.link(
        
        rx.button(
            rx.image(
            src=logo,
            max_width="2em"
        ),
            text,
            size="4",
            bg="black",
            border="solid",
            border_color="rgb(90, 51, 163)",
            _hover = {
                "background_color": "rgba(90, 51, 163, 0.2)"
            },
        ),
        is_external=True,
        href=url,
        underline="none",
        color="white",
        
    )