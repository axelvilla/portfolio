import reflex as rx

def stack_card(text:str, url:str) -> rx.Component:
    return rx.card(
            rx.center(
                rx.vstack(
                    rx.avatar(
                        src=url,
                        max_width="10em",
                        size="6"
                    ),
                    rx.text(
                        text,
                        width="100%",
                        align="center",
                        font_size=["2.5em", "1em"],
                    ),
                    align="center",
                ),
            ),
            size="6",
            padding="1.5em",
        ),