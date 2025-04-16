"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from bufete.pages.index import index
#from bufete.pages.project_ed import project_ed

from .styles import styles


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
#app.add_page(project_ed, route="/project_ed")
