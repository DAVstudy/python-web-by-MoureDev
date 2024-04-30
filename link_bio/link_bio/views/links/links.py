import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
import link_bio.constants as constants


def links() -> rx.Component:
    return rx.vstack(
        title("Redes Sociales"),
        link_button(
            "Instagram",
            "Contenido educativo",
            constants.INSTAGRAM_URL
            ),
        link_button(
            "LinkedIN",
            "Mi perfil profesional",
            constants.LINKEDIN_URL
            ),
        link_button(
            "X",
            "Sigueme!",
            constants.TWITTER_X_URL
        ),
        link_button(
            "TikTok",
            "Contenido rapido!",
            constants.TIKTOK_URL
        ),
        title("Contenido de Video"),
        link_button(
            "Twitch",
            "Directos realizando proyectos de desarrollo.",
            constants.TWITCH_URL
            ),
        link_button(
            "Youtube",
            "Pronto subire video",
            constants.YOUTUBE_URL
            ),
        title("Proyectos"),
        link_button(
            "Github",
            "Revisa mis proyectos :)",
            constants.GITHUB_URL
            ),
        title("Contacto"),
        link_button(
            "Email",
            "respuesta rapida y con preferencia",
            constants.EMAIL
            ),
        width="100%"
    )
