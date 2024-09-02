import reflex as rx
from Web_Compras.styles.styles import Size, Image_Size
from Web_Compras.styles.colors import Color, Color_Text

def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Primera columna con enlaces de navegación
            rx.vstack(
                rx.text("Acerca de Nosotros", font_weight="bold"),
                rx.link("Quiénes somos", href="#"),
                rx.link("Términos y condiciones", href="#"),
                rx.link("Política de privacidad", href="#"),
                spacing="2",
            ),
            # Segunda columna con ayuda
            rx.vstack(
                rx.text("Ayuda", font_weight="bold"),
                rx.link("Cómo comprar", href="#"),
                rx.link("Medios de pago", href="#"),
                rx.link("Devoluciones", href="#"),
                spacing="2",
            ),
            # Tercera columna con contacto
            rx.vstack(
                rx.text("Contacto", font_weight="bold"),
                rx.link("Numero", href="#"),
                rx.link("Instagram", href="#"),
                rx.link("Gmail", href="#"),
                spacing="2",
            ),
            # Cuarta columna, Ubicacion
            rx.vstack(
                rx.text("Ubicación"),
                rx.link(
                    rx.image(
                        src="mapa.jpg",
                        height=Image_Size.FOOTER.value,
                        width="150px",
                        border_radius="8px",
                    ),
                    href="https://instagram.com",  # Reemplaza con el enlace deseado
                    is_external=True,
                ),
                spacing="2",
            ),
            width="80%",  # Ajusta el ancho del contenido
            align_items="flex-start",
            justify_content="space-around",  # Ajusta el contenido más cerca del centro
            padding="20px",
            margin="auto"  # Centra el hstack en el contenedor padre
        ),
        bg=Color.FOOTER.value,  #Color de fondo
        width="100%",
    )
