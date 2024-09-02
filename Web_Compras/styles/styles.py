import reflex as rx
from enum import Enum
from Web_Compras.styles.fonts import Font, FontWeight
from Web_Compras.styles.colors import Color, Color_Text


# Constants
MAX_WIDTH = "1400px"

# Ponemos los estilos de fuente de texto
STYLESHEETSS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@300;500&display=swap"
]

# Sizes
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

class Image_Size(Enum):
    SOPONSORS = "400px"
    STANDAR = "200px"
    FOOTER = "50px"
    BODY = "100px"
    NAVBAR = "150px"



# Style
BASE_STYLE={
    "font_family":Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color":Color.BACKGROUND.value,
    "background_image": "url(fondo2.jpg)",  # Aquí se define la imagen de fondo
    "background_size": "cover",  # Asegura que la imagen cubra todo el fondo
    "background_repeat": "no-repeat",  # Evita que la imagen se repita
    "background_position": "center center",  # Centra la imagen
    
}

header_style ={
    "background_image": "url(fondo1.JPG)",  # Aquí se define la imagen de fondo
    "background_color":Color.SECONDARY.value,
    "background_size": "cover",  # Asegura que la imagen cubra todo el fondo
    "background_repeat": "no-repeat",  # Evita que la imagen se repita
    "background_position": "center center",  # Centra la imagen
}

stock_style ={
    #"background_image": "url(fondo2.jpg)",  # Aquí se define la imagen de fondo
    "background_color":Color.SECONDARY.value,
    "background_size": "cover",  # Asegura que la imagen cubra todo el fondo
    "background_repeat": "no-repeat",  # Evita que la imagen se repita
    "background_position": "center center",  # Centra la imagen
    "display": "flex",
    "flexDirection": "column",
    "alignItems": "center",  # Centra horizontalmente
    "justifyContent": "center",  # Centra verticalmente (opcional, si quieres centrar en el contenedor)
    "textAlign": "center",  # Centra el texto dentro del contenedor
}

accessories_style ={
    #"background_image": "url(fondo3.jpg)",  # Aquí se define la imagen de fondo
    "background_color":Color.SECONDARY.value,
    "background_size": "cover",  # Asegura que la imagen cubra todo el fondo
    "background_repeat": "no-repeat",  # Evita que la imagen se repita
    "background_position": "center center",  # Centra la imagen
    "display": "flex",
    "flexDirection": "column",
    "alignItems": "center",  # Centra horizontalmente
    "justifyContent": "center",  # Centra verticalmente (opcional, si quieres centrar en el contenedor)
    "textAlign": "center",  # Centra el texto dentro del contenedor
}