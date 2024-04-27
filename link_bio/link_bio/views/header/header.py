import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="DAV",
                size="5",
                color_scheme="purple",
                variant="solid",
                radius="full",
                margin_top="10px"
            ),
            rx.vstack(
                rx.heading(
                    "Hola! me presento soy DevsDav",
                    size="7"
                    ),
                rx.text(
                    "@devsdav",
                    margin_top="0px !important"
                    ),
                rx.hstack(
                    link_icon("https://x.com/devsdav"),
                    link_icon("https://x.com/devsdav"),
                    link_icon("https://x.com/devsdav")
                ),
                width="100%",
            ),
            spacing="5"
        ),
        rx.flex(
            info_text("+3", "años de experiencia como ingeniero electrónico"),
            rx.spacer(),
            info_text("+3", "años de experiencia como ingeniero electrónico"),
            rx.spacer(),
            info_text("+3", "años de experiencia como ingeniero electrónico"),
            width="100%"
        ),
        rx.text("""Ingeniero Electrónico que ha encontrado su pasión en
                programar, me encuentro aprendiendo sobre el mundo del
                desarrollo y quisiera compartir mi experiencia con ustedes,
                espero aportar para bien, un abrazo y espero te guste."""),
        spacing="2"
    )
