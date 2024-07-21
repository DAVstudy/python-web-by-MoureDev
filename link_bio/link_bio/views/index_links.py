import reflex as rx
import link_bio.constants as constants
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.routes import Route
from link_bio.components.featured_link import featured_link
from link_bio.state.PageState import PageState
from link_bio.styles.styles import Color, Size


def index_links() -> rx.Component:
    return rx.vstack(
        title("Proyectos y Cursos Realizados"),
        link_button(
            "Cursos Realizados",
            "Revisa los contenidos educativos que me han ayudado",
            "/icons/book.svg",
            Route.COURSES.value,
            is_external=False,
            highlight_color=Color.BORDER.value
        ),
        link_button(
            "Github",
            "Revisa mis proyectos :)",
            "/icons/github.svg",
            constants.GITHUB_URL
        ),

        rx.cond(
            PageState.featured_info,
            rx.vstack(
                title("Destacado"),
                rx.flex(
                    rx.foreach(
                        PageState.featured_info,
                        featured_link
                    ),
                    flex_direction=["column", "row"],
                    spacing=Size.DEFAULT_SPACING.value
                ),
                spacing=Size.DEFAULT_SPACING.value
            )
        ),

        title("Contenido de Video"),
        link_button(
            "Twitch",
            "Directos realizando proyectos de desarrollo.",
            "/icons/twitch.svg",
            constants.TWITCH_URL,
            True,
            Color.BORDER.value
        ),
        link_button(
            "Youtube",
            "Pronto subire video",
            "/icons/youtube.svg",
            constants.YOUTUBE_URL
        ),
        title("Contacto"),
        link_button(
            "Email",
            "devsdav@devsdav.com",
            "/icons/envelope-regular.svg",
            f"mailto:{constants.EMAIL}",
            True,
            Color.BORDER.value
            ),
        width="100%",
        spacing=Size.DEFAULT_SPACING.value,
        on_mount=PageState.featured_links
    )
