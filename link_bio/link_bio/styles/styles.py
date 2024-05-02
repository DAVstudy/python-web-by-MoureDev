import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "560px"


# Sizes
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap"
]


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    SMALL_SPACING = "0"
    MEDIUM_SPACING = "3"
    DEFAULT_SPACING = "6"
    BIG_SPACING = "9"


# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUDN.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.BODY,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": Color.SECUNDARY.value,
            "color": TextColor.HEADER
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.BOLD.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    font_size=Size.LARGE.value,
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.DEFAULT.value
)
