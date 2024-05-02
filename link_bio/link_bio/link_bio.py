
import reflex as rx
import link_bio.constants as constants
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.links import links
import link_bio.styles.styles as styles


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
               header(),
               links(),
               max_width=styles.MAX_WIDTH,
               width="100%",
               margin_y=styles.Size.BIG.value,
               padding=styles.Size.BIG.value
            )
        ),
        footer()
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={constants.G_TAG}"),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{constants.G_TAG}');
"""
        ),
    ]
)


title = "DevsDav | Aprendiendo a Programar"
description = "Hola soy DevsDav, Ingeniero Electrónico que esta aprendiendo a programar"
preview = "avatar.png"

app.add_page(
    index,
    title=title,
    description=description,
    image=preview,
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@devsdav"}
    ]
)
