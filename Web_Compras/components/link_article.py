import reflex as rx
from Web_Compras.styles.styles import Size, Image_Size
from Web_Compras.styles.colors import Color, Color_Text

def link_article(image: str, name: str, description: str, url: str) -> rx.Component:
    return rx.box(
        rx.image(
            src=image,
            alt=name,
            width="auto",
            height=Image_Size.STANDAR.value,
            display="block",  # Centra la imagen horizontalmente
            margin="0 auto"   # Ajusta el margen para centrar
        ),
        rx.text(name, font_size="xl", font_weight="bold", mt=2),
        rx.text(description, mt=1),
        rx.link(
            "Ver más detalles",
            href=url,
            color="blue.500",
            font_weight="medium",
            mt=2,
            is_external=True,
        ),
        padding=4,
        border="1px solid #ccc",
        border_radius="8px",
        width="300px",
        margin="auto",
        text_align="center",
        spacing="5px",
        bg=Color.CONTENT.value
    )
