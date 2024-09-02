import reflex as rx
from Web_Compras.components.title import title 
from Web_Compras.styles.styles import Size, Image_Size
from Web_Compras.styles import styles

# Ultimas Novedades
def header() -> rx.Component:
    return rx.vstack(
            rx.image(
                src="bicicleta.jpg",
                height=Image_Size.STANDAR.value,
                width="auto"
            ),
            width="100%",
            style=styles.header_style
    )
