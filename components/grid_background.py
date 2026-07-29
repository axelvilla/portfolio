import reflex as rx


def grid_background() -> rx.Component:
    """Perspective grid floor rendered behind the hero section
    (see .grid-bg-perspective in assets/styles/tron.css)."""
    return rx.box(class_name="grid-bg-perspective")
