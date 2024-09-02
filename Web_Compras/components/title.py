import reflex as rx
from Web_Compras.styles import styles
from Web_Compras.styles.fonts import Font, FontWeight
from Web_Compras.styles.colors import Color, Color_Text
from Web_Compras.styles.styles import Size

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="2xl",  # Tamaño más grande para mayor impacto
        width="100%",
        font_family=Font.TITLE.value,  # Asegúrate de que esta fuente sea clara y moderna
        font_weight=FontWeight.MEDIUM.value,  # Peso aumentado para un aspecto más imponente
        padding_top=Size.DEFAULT.value,
        color=Color_Text.PRIMARY.value,
        letter_spacing="1px",  # Opcional: Ajustar el espaciado para mayor claridad visual
    )
