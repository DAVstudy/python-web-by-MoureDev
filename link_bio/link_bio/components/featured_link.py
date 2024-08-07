import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size, Color
from link_bio.model.Featured import Featured


def featured_link(featured: Featured) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=featured.image,
                border_radius=Size.DEFAULT.value,
                background=Color.NAVBAR.value,
                width="100%",
                height="auto",
                alt=f"Imagen destacada para: {featured.title}"
            ),
            rx.text(
                featured.title,
                size=Size.MEDIUM_SPACING.value,
                style=styles.button_body_style,
                color=styles.TextColor.HEADER
            ),
            spacing=Size.SMALL_SPACING.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        ),
        href=featured.url,
        is_external=True
    )