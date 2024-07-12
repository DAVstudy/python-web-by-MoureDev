import reflex as rx
import datetime
import link_bio.constants as constants
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size
from link_bio.styles.colors import TextColor, Color
from link_bio.components.link_button import link_button


def header(details=True, live=False, live_title="") -> rx.Component:
    return rx.vstack(
        rx.hstack(
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
                    color=TextColor.SUBTITLE.value
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
                    info_text(f"+{experience()}", "de ingeniero electrónico"),
                    rx.spacer(),
                    info_text(f"+3", "cursos de programación"),
                    rx.spacer(),
                    info_text("+100", "seguidores"),
                    width="100%"
                ),
                rx.cond(
                    live,
                    link_button(
                        "En directo",
                        live_title,
                        "/icons/twitch.svg",
                        constants.TWITCH_URL,
                        highlight_color=Color.BORDER.value,
                        animated=True
                    )
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


def experience() -> int:
    return datetime.date.today().year - 2021
