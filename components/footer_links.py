import reflex as rx

def footer_links(url: str, image:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.image(
                src=image,
                max_width="2em"
            ),
            
            bg="transparent",
            _hover = {
                "background_color": "rgba(90, 51, 163, 0.2)"
            },
        ),
        href=url,
        underline="none",
        color="white",
        is_external=True,
    )