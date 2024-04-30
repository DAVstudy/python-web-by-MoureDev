import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(src="/favicon.ico"),
            rx.link(
                f"© 2024 - {datetime.date.today().year} Devsdav ",
                href="https://devsdav.com",
                is_external=True,
                font_size=Size.MEDIUM.value,
                color=TextColor.FOOTER.value,
                margin_top=Size.DEFAULT.value
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
