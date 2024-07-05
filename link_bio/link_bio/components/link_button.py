import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


def link_button(title: str,
                body: str,
                image: str,
                url: str,
                is_live=False,
                is_external=True) -> rx.Component:
    return rx.link(
        rx.cond(
            is_live,
            rx.button(
                rx.hstack(
                    rx.image(
                        src=image,
                        width=Size.BIG.value,
                        height=Size.BIG.value,
                        margin=Size.MEDIUM.value,
                        alt=title
                        ),
                    rx.vstack(
                        rx.text(
                            title,
                            style=styles.button_title_style
                        ),
                        rx.text(
                            body,
                            style=styles.button_body_style
                        ),
                        align_items="start",
                        spacing=Size.SMALL_SPACING.value,
                        padding_y=Size.SMALL.value,
                        padding_right=Size.SMALL.value
                    ),
                    align="center",
                    width="100%"
                ),
                border_style="solid",
                border_width="5px",
                border_radius="20px",
                border_color="#B600FF"
            ),
            rx.button(
                rx.hstack(
                    rx.image(
                        src=image,
                        width=Size.BIG.value,
                        height=Size.BIG.value,
                        margin=Size.MEDIUM.value,
                        alt=title
                        ),
                    rx.vstack(
                        rx.text(
                            title,
                            style=styles.button_title_style
                        ),
                        rx.text(
                            body,
                            style=styles.button_body_style
                        ),
                        align_items="start",
                        spacing=Size.SMALL_SPACING.value,
                        padding_y=Size.SMALL.value,
                        padding_right=Size.SMALL.value
                    ),
                    align="center",
                    width="100%"
                )
            )
        ),
        href=url,
        is_external=is_external,
        width="100%"
    )
