import reflex as rx
import datetime
import link_bio.constants as constants
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(src="/Nombre.png", width="150px", height="auto"),
            rx.link(
                f"© 2024 - {datetime.date.today().year} Devsdav ",
                href=constants.GITHUB_URL,
                is_external=True,
                font_size=Size.MEDIUM.value,
                color=TextColor.FOOTER.value,
                margin_top=Size.DEFAULT.value,
                alt="Logotipo de DevsDav. Se lee DevsDav"
            ),
            rx.text(
                "Building with reflex",
                font_size=Size.MEDIUM.value
                ),
            spacing=Size.SMALL_SPACING.value,
            margin_bottom=Size.BIG.value,
            align_items="center",
            color=TextColor.FOOTER.value
        )
    )
