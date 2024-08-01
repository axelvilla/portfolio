import reflex as rx

def link_bio(text: str, url: str) -> rx.Component:
    return rx.button(
        text,
        bg="transparent", 
        _hover = {
                "background_color": "rgba(90, 51, 163, 0.2)"
            }, 
        color="white",
        padding_x="1em",
        on_click=(rx.scroll_to(url))
    )