import reflex as rx
from enum import Enum

from .fonts import Font

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap"
    ]

#"assets/css/styles.css"

#STYLESHEETS = [
#    "https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700#;1,400..700&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900#;1,100#;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap",
#]


MAX_WIDTH = "1280px"
#MAX_WIDTH = "1200px"
MAX_WIDTH_TABLET = "1024px"
MAX_WIDTH_MOBILE = "768px"

#imagenes de proyectos
IMAGE_HEIGHT = "220px"
IMAGE_WIDTH = "280px"

class SizeEM(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "1.3em"
    BIG = "2em"
    VERY_BIG = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    SMALL_BIG = "3"
    DEFAULT = "4"  # 1em
    MEDIUM = "6"
    BIG = "7"
    MEDIUM_VERY_BIG = "8"
    VERY_BIG = "9"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    #"font_weight": FontWeight.REGULAR.value,
    #"color": Color.LIGHT.value,
    #"background": Color.DARK.value,
    #rx.heading: {
    #    "font_family": Font.HEADER.value,
    #    "font_weight": FontWeight.BOLD.value,
    #},
    rx.button: {
        "cursor": "pointer",
        #"color": Color.CYAN_TEXT.value,
        #"background": Color.CYAN.value,
        #"_hover": {
        #    "color": Color.LIGHT.value,
        #    "background": Color.HOVER_CYAN.value
        #}
    },
    #rx.link: {
    #    "font_weight": FontWeight.BOLD.value
    #}

}

max_width_style = dict(
    #padding_x="3.5em",
    #margin="56px",
    #adding="2em",
    #padding_x=SizeEM.BIG.value,
    #padding_y=SizeEM.VERY_BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)

max_width_style_tablet = dict(
    margin="40px",
    #padding_x=SizeEM.BIG.value,
    #padding_y=SizeEM.VERY_BIG.value,
    #width="100%",
    max_width=MAX_WIDTH_TABLET
)

max_width_style_mobile = dict(
    #padding="1.5em",
    margin="24px",
    #padding_y=SizeEM.VERY_BIG.value,
    #padding_x=SizeEM.BIG.value,
    #width="100%",
    max_width=MAX_WIDTH_MOBILE
)

# styles.py
header_style = {
    #"background": "transparent",
    "@keyframes header-blur-scroll": {
        "0%": {
            "backdrop_filter": "blur(0px)",
            "background": "transparent"
        },
        "100%": {
            #"backdrop_filter": "blur(10px)",
            "background": "#fff",
            "border_bottom_color": "#e8e8e8"
        }
    },
    "animation": "header-blur-scroll 0.3s linear both",
    "animation_timeline": "scroll()",
    "animation_range": "0 250px",
    "border_bottom": "1px solid transparent"
}
