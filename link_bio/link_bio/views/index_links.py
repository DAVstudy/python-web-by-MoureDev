import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.routes import Route
import link_bio.constants as constants


def index_links() -> rx.Component:
    return rx.vstack(
        title("Redes Sociales"),
        link_button(
            "Instagram",
            "Contenido educativo",
            "/icons/instagram.svg",
            constants.INSTAGRAM_URL
            ),
        link_button(
            "LinkedIN",
            "Mi perfil profesional",
            "/icons/linkedin.svg",
            constants.LINKEDIN_URL
            ),
        link_button(
            "X",
            "Sigueme!",
            "/icons/x-twitter.svg",
            constants.TWITTER_X_URL
        ),
        link_button(
            "TikTok",
            "Contenido rapido!",
            "/icons/tiktok.svg",
            constants.TIKTOK_URL
        ),
        title("Contenido de Video"),
        link_button(
            "Twitch",
            "Directos realizando proyectos de desarrollo.",
            "/icons/twitch.svg",
            constants.TWITCH_URL
            ),
        link_button(
            "Youtube",
            "Pronto subire video",
            "/icons/youtube.svg",
            constants.YOUTUBE_URL
            ),
        title("Proyectos y Cursos Realizados"),
        link_button(
            "Github",
            "Revisa mis proyectos :)",
            "/icons/github.svg",
            constants.GITHUB_URL
            ),
        link_button(
            "Cursos Realizados",
            "Revisa los contenidos educativos que me han ayudado",
            "/icons/book.svg",
            Route.COURSES.value,
            is_external=False
            ),
        title("Contacto"),
        link_button(
            "Email",
            "devsdav@devsdav.com",
            "/icons/envelope-regular.svg",
            f"mailto:{constants.EMAIL}"
            ),
        width="100%"
    )
