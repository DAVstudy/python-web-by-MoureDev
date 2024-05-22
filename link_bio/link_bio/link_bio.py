
import reflex as rx
import link_bio.constants as constants
import link_bio.styles.styles as styles
from link_bio.pages.index import index
from link_bio.pages.courses import courses
from link_bio.api.api import hello


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

app.api.add_api_route("/hello", hello)
