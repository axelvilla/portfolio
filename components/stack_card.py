import reflex as rx

def stack_card(text:str, url:str) -> rx.Component:
    return rx.card(
            rx.center(
                rx.vstack(
                    rx.avatar(
                        src=url,
                        max_width="10em",
                    ),
                    rx.text(
                        text,
                        width="100%",
                        align="center"
                    ),
                    align="center",
                ),
            ),
            size="6",
            padding="1.5em",
        ),