import reflex as rx
from Web_Compras.components.link_article import link_article
from Web_Compras.components.title import title 
from Web_Compras.styles.styles import Size, Image_Size
from Web_Compras.styles import styles

def stock() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="motos-disponibles.png",
            height=Image_Size.BODY.value,
            width="auto"
        ),
        # Envolver las filas de artículos en un vstack con spacing
        rx.vstack(
            # Primera fila de artículos
            rx.hstack(
                link_article(
                    "stock/moto1.jpg",
                    "Honda Marshal",
                    "Nuevo modelo mejorado para mas confort y estilo, y para amantes de la velocidad, 50 caballos extra",
                    "https://instagram.com"
                    ),
                link_article(
                    "stock/moto2.jpeg",
                    "Suzuki Transal",
                    "Nuevo modelo mejorado para mas confort y estilo, y para amantes de la velocidad, 50 caballos extra",
                    "https://instagram.com"
                    ),
                link_article(
                    "stock/moto3.jpeg",
                    "Honda Velma",
                    "Nuevo modelo mejorado para mas confort y estilo, y para amantes de la velocidad, 50 caballos extra",
                    "https://instagram.com"
                    ),
                link_article(
                    "stock/moto4.jpg",
                    "Dukati Imperio",
                    "Nuevo modelo mejorado para mas confort y estilo, y para amantes de la velocidad, 50 caballos extra",
                    "https://instagram.com"
                    ),
                width="100%"
            ),
            # Segunda fila de artículos
            rx.hstack(
                link_article(
                    "stock/moto5.jpg",
                    "Zanella 110",
                    "Ultima tecnologia en motociclismo, de la mano de una de las mejores marcas en el rubro",
                    "https://instagram.com"
                    ),
                link_article(
                    "stock/moto6.jpeg",
                    "Tornado T",
                    "Ultima tecnologia en motociclismo, de la mano de una de las mejores marcas en el rubro",
                    "https://instagram.com"
                    ),
                link_article(
                    "stock/moto3.jpeg",
                    "C90",
                    "Ultima tecnologia en motociclismo, de la mano de una de las mejores marcas en el rubro",
                    "https://instagram.com"
                    ),
                link_article(
                    "stock/moto1.jpg",
                    "Honda Titan",
                    "Ultima tecnologia en motociclismo, de la mano de una de las mejores marcas en el rubro",
                    "https://instagram.com"
                    ),
                width="100%",
            ),
            #spacing="20px"  # Espacio entre las filas
        ),
        width="100%",
        style=styles.stock_style
    )

