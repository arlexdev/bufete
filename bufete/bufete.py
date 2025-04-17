import reflex as rx
from .styles import styles
from bufete.pages.index import index
from .pages.auth.login import login
from .pages.auth.signup import signup
from bufete.pages.templates.compra_venta import compra_venta
from bufete.pages.templates.llenar.compraventa.llenar_compra_venta import llenar_compra_venta


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    theme=rx.theme(
        appearance="light",
        has_background=True,  # Añadir esta línea
        panel_background="solid",
        accent_color="gray",
        gray_color="gray",
        radius="large"
    )
)

title = "Bufete | A & F"
description = "Generador de contratos"
preview = "./preview.png"

app.add_page(
    index,
    title=title,
    description=description,
    image=preview,
    meta=[
        {"char_set": "UTF-8"},
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview}
    ]
)
app.add_page(login)
app.add_page(signup)
app.add_page(compra_venta)
app.add_page(llenar_compra_venta)
