import reflex as rx
from Web_Compras.styles.styles import Image_Size
from Web_Compras.components.navbar_link import navbar_link
from Web_Compras.styles.colors import Color, Color_Text

def navbar() -> rx.Component:
    return rx.box(
        # Diseño para dispositivos de escritorio
        rx.desktop_only(
            rx.hstack(
                # Logo y enlaces agrupados
                rx.hstack(
                    # Logo de la navbar
                    rx.image(
                        src="todo-motos.png",
                        width=Image_Size.NAVBAR.value,
                        height="auto",
                        border_radius="25%",
                    ),
                    # Espacio entre el logo y los enlaces
                    rx.hstack(
                        navbar_link("Home", "/#"),
                        navbar_link("About", "/#"),
                        navbar_link("Pricing", "/#"),
                        navbar_link("Contact", "/#"),
                        spacing="5",  # Espacio entre los enlaces
                    ),
                    spacing="40px",  # Espacio entre logo y enlaces
                    align_items="center",
                    justify="start",  # Alinea los elementos al inicio
                ),
                # Botones "Sign Up" y "Log In"
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button(
                        "Log In",
                        size="3"
                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",  # Distribuye el espacio entre los elementos
                align_items="center",
                width="100%",  # Asegura que el hstack ocupe todo el ancho
            ),
        ),
        # Diseño para dispositivos móviles y tabletas
        rx.mobile_and_tablet(
            rx.hstack(
                # Logo y título para móvil
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex",
                        size="6",
                        weight="bold"
                    ),
                    align_items="center",
                ),
                # Menú desplegable para móvil
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
                width="100%",
            ),
        ),
        # Estilos generales para la navbar
        bg=Color.NAVBAR.value,
        padding="1em",
        # position="fixed",  # Comentado por si necesitas fijar la posición
        # top="0px",         # Comentado por si necesitas ajustar la posición
        # z_index="5",       # Comentado por si necesitas ajustar la capa
        width="100%",
    )
