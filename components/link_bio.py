import reflex as rx

def link_bio(text: str, url: str) -> rx.Component:
    return rx.button(
        text,
        bg="transparent", 
        _hover = {
                "background_color": "rgba(90, 51, 163, 0.2)"
            }, 
        color="white",
        font_size=["1.5em", "1em"],
        on_click=(rx.scroll_to(url))
    )