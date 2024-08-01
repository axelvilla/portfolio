import reflex as rx

def experience_card(title:str, body:str, img) -> rx.Component:
    return rx.card(
        rx.flex(
            rx.image(
                src=img,
                max_width=["10%","7%"],
                object_fit="cover",
                alt=img
            ),
            rx.box(
                rx.heading(
                    title,
                    font_size=["2em", "1em"],
                ),
                rx.text(
                    body,
                    font_size=["1.5em", "1em"],
                ),
            ),
            spacing="2",
            align="center"    
        ),
        width="100%",
        padding_top="1em"
    ),