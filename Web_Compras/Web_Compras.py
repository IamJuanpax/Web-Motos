import reflex as rx
from Web_Compras.components.navbar import navbar
from Web_Compras.components.footer import footer
from Web_Compras.views.body.accessories import accessories
from Web_Compras.views.header.header import header
from Web_Compras.views.body.stock import stock
from Web_Compras.views.sponsors.sponsors import sponsors
from Web_Compras.styles import styles

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                stock(),
                accessories(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.DEFAULT.value,
                padding=styles.Size.BIG.value,
                spacing="25px"
            )
        ),
        footer()
    )


app = rx.App(
    stylesheets=styles.STYLESHEETSS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title= "Todo Motos",
    description= "Compra lo que puedas",
    )