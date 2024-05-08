import reflex as rx
import link_bio.constants as constants
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size


def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos Gratis"),
        link_button(
            "Coursera - Universidad Católica de Chile",
            "Introducción a la programación en Python I: Aprendiendo a programar con Python",
            "/icons/python.svg",
            constants.COURSERA_PYTHON
            ),
        link_button(
            "Coursera - Universidad Católica de Chile",
            "Programación en Python II: aprendiendo a estructurar datos",
            "/icons/python.svg",
            constants.COURSERA_PYTHON_II
            ),
        link_button(
            "MoureDev - Curso Hello-Python ",
            "Curso de +37h: Fundamentos, frontend, backend, testing...",
            "/icons/python.svg",
            constants.MOURE_PYTHON_COURSE_URL
        ),
        width="100%"
    )
