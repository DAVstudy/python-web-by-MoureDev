import reflex as rx
import datetime
import link_bio.constants as constants
from link_bio.styles.styles import Size
from link_bio.styles.colors import TextColor, Color
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.link_button import link_button
from link_bio.state.PageState import PageState


def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.cond(
                    PageState.live_status.live,
                    rx.link(
                        rx.image(
                            src="/icons/twitch_purple.svg",
                            height=Size.MEDIUM.value,
                            width=Size.MEDIUM.value
                        ),
                        href=constants.TWITCH_URL,
                        is_external=True,
                        class_name="blink",
                        border_radius="50%",
                        padding=Size.SMALL.value,
                        bg=Color.BORDER.value,
                        position="absolute",
                        bottom="0",
                        right="0"
                    )
                ),
                rx.avatar(
                    name="Diego Arenas",
                    src="/avatar.png",
                    size=Size.BIG_SPACING.value,
                    bg=TextColor.BODY.value,
                    color=TextColor.BODY.value,
                    radius="full",
                    margin_top=Size.SMALL.value,
                    padding="2px",
                    border=f"4px solid {Color.CONTENT.value}"
                ),
                position="relative"
            ),
            rx.vstack(
                rx.heading(
                    "Hola! soy DevsDav",
                    size=Size.BIG_SPACING.value
                    ),
                rx.text(
                    "@devsdav",
                    margin_top=Size.ZERO.value,
                    color=TextColor.SUBTITLE.value
                    ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        constants.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "/icons/x-twitter.svg",
                        constants.TWITTER_X_URL,
                        "Twitter/X"
                    ),
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
                        "/icons/linkedin.svg",
                        constants.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    padding_top=Size.SMALL.value,
                    spacing=Size.DEFAULT_SPACING.value
                ),
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
                    info_text(
                        f"+{experience()}",
                        "de ingeniero electrónico"
                    ),
                    rx.spacer(),
                    info_text(
                        "+3",
                        "cursos de programación"
                        ),
                    rx.spacer(),
                    info_text(
                        "+100",
                        "seguidores"
                        ),
                    width="100%"
                ),
                rx.cond(
                    PageState.live_status.live,
                    link_button(
                        "En directo",
                        PageState.live_status.title,
                        "/icons/twitch.svg",
                        constants.TWITCH_URL,
                        highlight_color=Color.BORDER.value,
                        animated=True
                    ),
                    rx.box(
                        rx.cond(
                            PageState.next_live,
                            link_button(
                                "Próximo directo",
                                PageState.next_live,
                                "/icons/twitch.svg",
                                constants.TWITCH_URL,
                                highlight_color=Color.BORDER.value,
                                animated=True
                            ),
                        ),
                        width="100%",
                        on_mount=PageState.check_schedule
                    )
                ),
                rx.text(
                    """
                    Soy un Ingeniero Electrónico que ha encontrado su pasión en
                    programar, me encuentro aprendiendo sobre el mundo del
                    desarrollo y quisiera compartir mi experiencia con ustedes,
                    espero aportar para bien, un abrazo.
                    """,
                    font_size=Size.DEFAULT.value,
                    color=TextColor.HEADER.value,
                    text_align="justify"
                ),
                width="100%",
                spacing=Size.DEFAULT_SPACING.value
            )
        ),
        spacing=Size.DEFAULT_SPACING.value,
        width="100%",
        align_items="start",
        on_mount=PageState.check_live
    )


def experience() -> int:
    return datetime.date.today().year - 2021
