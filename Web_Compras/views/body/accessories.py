import reflex as rx
from Web_Compras.components.link_article import link_article
from Web_Compras.components.title import title 
from Web_Compras.styles import styles
from Web_Compras.styles.styles import Size, Image_Size

def accessories() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="accesorios.png",
            height=Image_Size.BODY.value,
            width="auto"
        ),
        # Primera fila de artículos
        rx.hstack(
            link_article("casco.jpeg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
            link_article("casco.jpeg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
            link_article("casco.jpeg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
            link_article("casco.jpeg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
            width="100%"
        ),
        rx.hstack(
            link_article("llantas.jpg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
            link_article("llantas.jpg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
            link_article("llantas.jpg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
            link_article("llantas.jpg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
            width="100%"
        ),
        width="100%",
        style=styles.accessories_style
    )