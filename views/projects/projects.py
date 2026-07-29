import reflex as rx
from components.projects_card import projects_card

def projects(title:str, body: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            color="white",
            size="5",
            font_size=["2em", "1.5em"],
            as_="bold"
        ),
        rx.text(
            body,
            font_size=["1.5em", "1em"],
        ),
        rx.hstack(
            rx.flex(
                projects_card(
                    "Tienda Informática",
                    "E-commerce de componentes y periféricos de PC, con filtros por categoría y marca, y un configurador \"Armá tu PC\".",
                    "React, Tailwind",
                    "https://informatica-sepia.vercel.app/",
                    ),
                projects_card(
                    "1step",
                    "Plataforma de software a medida para automatizar y centralizar las operaciones de negocios de servicios.",
                    "React, Tailwind",
                    "https://1stepservice.vercel.app/",
                    ),
                projects_card(
                    "Inmobiliaria Reconquista",
                    "Portal inmobiliario con búsqueda filtrada de propiedades en venta y alquiler.",
                    "React, Tailwind",
                    "https://inmobiliaria-reconquista.vercel.app/",
                    ),
                projects_card(
                    "La Cumbre",
                    "Sitio de la verdulería La Cumbre: catálogo de ofertas, galería de productos y pedidos por WhatsApp.",
                    "React, Tailwind",
                    "https://lacumbre.netlify.app/",
                    ),
                flex_wrap="wrap",
                spacing="2",
                width="100%",
                justify="center",
            ),
            width="100%",
            justify="center",
        ),
    align="center",
    width="100%",
    id="projects",
    class_name="reveal",
    )
