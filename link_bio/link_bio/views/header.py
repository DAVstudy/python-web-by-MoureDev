import reflex as rx
import link_bio.constants as constants
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor, Color


def header(details=True, live=False) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.cond(
                live,
                rx.text("is_live", color=TextColor.BODY.value)
            ),
            rx.avatar(
                src="/avatar.png",
                size=Size.DEFAULT_SPACING.value,
                bg=TextColor.BODY.value,
                color=TextColor.BODY.value,
                radius="full",
                margin_top=Size.SMALL.value,
                padding="2px",
                border=f"4px solid {Color.CONTENT.value}"
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
                    link_icon(
                        "/icons/instagram.svg",
                        constants.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "/icons/tiktok.svg",
                        constants.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "/icons/x-twitter.svg",
                        constants.TWITTER_X_URL,
                        "X"
                    ),
                    padding_top=Size.SMALL.value,
                    spacing=Size.DEFAULT_SPACING.value
                ),
                width="100%",
                spacing=Size.SMALL_SPACING.value,
                align_items="start"
            ),
            align="end",
            spacing=Size.DEFAULT_SPACING.value
        ),
        rx.cond(
            details,
            rx.vstack(
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
                        color=TextColor.HEADER.value,
                        text_align="justify"),
                width="100%",
                spacing=Size.DEFAULT_SPACING.value
            )
        ),
        spacing=Size.DEFAULT_SPACING.value
    )
