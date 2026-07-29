import reflex as rx
from components.experience_card import experience_card
from portfolio.theme import TEXT_PRIMARY

def experience(title:str, body: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            color=TEXT_PRIMARY,
            font_size=["2em", "1.5em"],
            as_="bold"
        ),
        rx.text(
            body,
            font_size=["1.5em", "1em"],
        ),
        rx.vstack(
            rx.grid(
                experience_card(
                    "Login App",
                    "Sistema de autenticación con React.js + Flask + MySQL, validación de credenciales, sesiones seguras y arquitectura modular. Freelance / Proyectos de GitHub (2025).",
                    "icon-login.svg",
                    ),
                experience_card(
                    "Filter App",
                    "Gestión y filtrado de datos con backend en FastAPI y frontend en React.js. Freelance / Proyectos de GitHub (2025).",
                    "icon-filter.svg",
                    ),
                experience_card(
                    "Sistema de Laboratorio de Análisis Clínicos",
                    "Backend en Node.js, frontend en Next.js/React, y persistencia con MySQL + Prisma; incluye autenticación, gestión de pacientes y carga de resultados. Freelance / Proyectos de GitHub (2025).",
                    "icon-lab.svg",
                    ),
                experience_card(
                    "Punto de Venta para Verdulería",
                    "Backend en Java (Spring Boot), frontend en Next.js, MySQL y Docker, para gestionar productos, stock y ventas. Freelance / Proyectos de GitHub (2025).",
                    "icon-store.svg",
                    ),
                experience_card(
                    "Instructor de Java",
                    "Escuela Superior de Comercio N° 43",
                    "teacher-icon.svg",
                    ),
                width=["90%","70%"],
                spacing="4",
            ),
            width="100%",
            align="center"
        ),
        align="center",
        width="100%",
        id="experience",
        class_name="reveal",
    )
