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
            link_article(
                "accessories/casco.jpeg", 
                "Casco",
                "Accesorio de alta calidad con garantia incluida",
                "https://instagram.com"
                ),
            link_article(
                "accessories/anteojos.JPG",
                "Anteojos",
                "Accesorio de alta calidad con garantia incluida",
                "https://instagram.com"
                ),
            link_article(
                "accessories/guantes.JPG",
                "Guantes",
                "Accesorio de alta calidad con garantia incluida",
                "https://instagram.com"
                ),
            link_article(
                "accessories/campera.jpg",
                "Campera",
                "Accesorio de alta calidad con garantia incluida", 
                "https://instagram.com"
                ),
            width="100%"
        ),
        rx.hstack(
            link_article(
                "accessories/llantas.jpg",
                "Llantas",
                "Accesorio de alta calidad con garantia incluida",
                "https://instagram.com"
                ),
            link_article(
                "accessories/cadena.JPG",
                "Cadena",
                "Accesorio de alta calidad con garantia incluida",
                "https://instagram.com"),
            link_article(
                "accessories/suspension.JPG",
                "Suspension",
                "Accesorio de alta calidad con garantia incluida",
                "https://instagram.com"
                ),
            link_article(
                "accessories/botas.JPG",
                "Botas",
                "Accesorio de alta calidad con garantia incluida",
                "https://instagram.com"),
            width="100%"
        ),
        width="100%",
        style=styles.accessories_style
    )