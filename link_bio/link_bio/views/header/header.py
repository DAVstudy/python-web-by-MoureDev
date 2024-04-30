import reflex as rx
import link_bio.constants as constants
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="DAV",
                size=Size.DEFAULT_SPACING.value,
                color_scheme="violet",
                bg=TextColor.BODY.value,
                variant="solid",
                radius="full",
                margin_top=Size.SMALL.value
            ),
            rx.vstack(
                rx.heading(
                    "Hola! soy DevsDav",
                    size=Size.DEFAULT_SPACING.value
                    ),
                rx.text(
                    "@devsdav",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                    ),
                rx.hstack(
                    link_icon(constants.INSTAGRAM_URL),
                    link_icon(constants.TIKTOK_URL),
                    link_icon(constants.TWITTER_X_URL),
                    padding_top=Size.SMALL.value,
                    spacing=Size.DEFAULT_SPACING.value
                ),
                width="100%",
                spacing=Size.SMALL_SPACING.value
            ),
            align="end",
            spacing=Size.DEFAULT_SPACING.value
        ),
        rx.flex(
            info_text("+3", "años de experiencia como ingeniero electrónico"),
            rx.spacer(),
            info_text("+3", "cursos de programación con Python realizados"),
            rx.spacer(),
            info_text("+100", "seguidores"),
            width="100%"
        ),
        rx.text("""Soy un Ingeniero Electrónico que ha encontrado su pasión en
                programar, me encuentro aprendiendo sobre el mundo del
                desarrollo y quisiera compartir mi experiencia con ustedes,
                espero aportar para bien, un abrazo.
                """,
                font_size=Size.DEFAULT.value,
                color=TextColor.HEADER.value
                ),
        spacing=Size.BIG_SPACING.value
    )
