import reflex as rx

def experience_card(title:str, body:str, img) -> rx.Component:
    return rx.card(
        rx.flex(
            rx.image(
                src=img,
                max_width="7%",
                object_fit="cover"
            ),
            rx.box(
                rx.heading(title),
                rx.text(
                    body
                ),
            ),
            spacing="2",
            align="center"    
        ),
        width="100%",
    ),