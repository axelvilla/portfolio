import reflex as rx
from components.experience_card import experience_card

def experience(title:str, body: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            color="white",
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
                    "Desarrollador Full Stack y Líder de Proyecto — Freelance (2025)",
                    [
                        "Login App: sistema de autenticación con React.js + Flask + MySQL, validación de credenciales, sesiones seguras y arquitectura modular.",
                        "Filter App: gestión y filtrado de datos con backend en FastAPI y frontend en React.js.",
                        "Sistema de Laboratorio de Análisis Clínicos: backend en Node.js, frontend en Next.js/React, y persistencia con MySQL + Prisma; incluye autenticación, gestión de pacientes y carga de resultados.",
                        "Punto de Venta para Verdulería: backend en Java (Spring Boot), frontend en Next.js, MySQL y Docker, para gestionar productos, stock y ventas.",
                    ],
                    "github-icon.svg",
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
