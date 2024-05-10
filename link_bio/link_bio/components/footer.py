import reflex as rx
import datetime
import link_bio.constants as constants
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/Nombre.png",
            width="150px",
            height="auto",
            alt="Logotipo de DevsDav. Se lee DevsDav"
            ),
        rx.link(
            rx.box(
                f"© 2024 - {datetime.date.today().year} ",
                rx.text(
                    "DevsDav",
                    as_="span",
                    color=TextColor.FOOTER.value
                ),
                " v0.",
                padding_top=Size.DEFAULT.value
            ),
            href=constants.GITHUB_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    weidth=Size.LARGE.value,
                    alt="Logotipo de GitHub"
                ),
                rx.text(
                    "Building with reflex",
                    font_size=Size.MEDIUM.value
                ),
            ),
            href=constants.REPO_URL,
            is_external=True
        ),
        spacing=Size.SMALL_SPACING.value,
        padding_bottom=Size.VERY_BIG.value,
        align_items="center",
        color=TextColor.FOOTER.value,
        display="flex"
    )
