import reflex as rx
from Web_Compras.components.link_article import link_article
from Web_Compras.components.title import title 
from Web_Compras.styles.styles import Size, Image_Size
from Web_Compras.styles import styles

def stock() -> rx.Component:
    return rx.vstack(
        #title("Motos Disponibles"),  # Título principal
        rx.image(
            src="motos-disponibles.png",
            height=Image_Size.BODY.value,
            width="auto"
        ),
        # Envolver las filas de artículos en un vstack con spacing
        rx.vstack(
            # Primera fila de artículos
            rx.hstack(
                link_article("moto1.jpg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
                link_article("moto2.jpeg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
                link_article("moto3.jpeg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
                link_article("moto4.jpg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
                width="100%"
            ),
            # Segunda fila de artículos
            rx.hstack(
                link_article("moto5.jpg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
                link_article("moto6.jpeg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
                link_article("moto3.jpeg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
                link_article("moto1.jpg", "bicicleta", "Bicicleta nueva de alta calidad", "https://instagram.com"),
                width="100%",
            ),
            #spacing="20px"  # Espacio entre las filas
        ),
        width="100%",
        style=styles.stock_style
    )

