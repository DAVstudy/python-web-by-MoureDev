import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Redes Sociales"),
        link_button(
            "Twitch",
            "Pronto volvere",
            "https://www.twitch.tv/devsdav"),
        link_button(
            "Youtube",
            "Pronto subire video",
            "https://www.youtube.com/channel/UCDGPEVysmSob0MqdfhjCBtw"),
        link_button(
            "Instagram",
            "Pronto volvere",
            "https://www.instagram.com/devsdav?igsh=MWtvd3J3NDd5eThmMA%3D%3D"),
        link_button(
            "Github",
            "Revisa mis proyectos :)",
            "https://github.com/DAVstudy"),
        title("Redes Sociales"),
        link_button(
            "Twitch",
            "Pronto volvere",
            "https://www.twitch.tv/devsdav"),
        link_button(
            "Youtube",
            "Pronto subire video",
            "https://www.youtube.com/channel/UCDGPEVysmSob0MqdfhjCBtw"),
        link_button(
            "Instagram",
            "Pronto volvere",
            "https://www.instagram.com/devsdav?igsh=MWtvd3J3NDd5eThmMA%3D%3D"),
        link_button(
            "Github",
            "Revisa mis proyectos :)",
            "https://github.com/DAVstudy"),
        width="100%"
    )
