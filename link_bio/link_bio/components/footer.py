import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size


def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(src="/favicon.ico"),
            rx.link(
                f"© 2024 - {datetime.date.today().year} Devsdav ",
                href="https://devsdav.com",
                is_external=True,
                font_size=Size.MEDIUM.value
            ),
            rx.text(
                "Building with reflex",
                font_size=Size.MEDIUM.value,
                margin_top="0px !important"
                ),
            margin_bottom=Size.BIG.value,
            align_items="center"
            
        )
    )
