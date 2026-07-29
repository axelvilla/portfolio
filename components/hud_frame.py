import reflex as rx


def hud_frame(*children: rx.Component, **props) -> rx.Component:
    """A box styled as a TRON HUD panel: corner brackets, a hover
    light-trace, and hover-lift motion (see .hud-frame / .hover-lift
    in assets/styles/tron.css). Drop-in replacement for rx.card on
    project/experience/education/stack cards."""
    extra_class = props.pop("class_name", "")
    class_name = f"hud-frame hover-lift {extra_class}".strip()
    return rx.box(
        rx.box(class_name="trace-runner"),
        *children,
        class_name=class_name,
        **props,
    )
