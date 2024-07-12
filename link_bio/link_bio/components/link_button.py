import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size


def link_button(title: str,
                body: str,
                image: str,
                url: str,
                is_external=True,
                highlight_color=None,
                animated=False) -> rx.Component:
    return rx.button(
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
        border=f"{'4px' if highlight_color != None else '0px'} solid {highlight_color}",
        class_name=styles.BOUNCEIN_ANIMATION if animated else None,
        on_click=rx.redirect(path=url, external=is_external)
        )
