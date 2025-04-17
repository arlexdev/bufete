import reflex as rx
from ..styles import styles

# Datos de las plantillas
TEMPLATES = [
    {
        "badge": "Los más vendidos",
        "title": "Compra y venta",
        "desc": "Formaliza acuerdos de compraventa con cláusulas claras y legales.",
        "button_href": "/templates/compra-venta",
        "image_src": "/favicon.ico",
    },
    {
        "badge": "Los más vendidos",
        "title": "Compra y venta",
        "desc": "An all-in-one Notion template designed for professionals, creators, and teams.",
        "button_href": "#proyectos",
        "image_src": "/favicon.ico",
    },
    {
        "badge": "Los más vendidos",
        "title": "Contrato de Arrendamiento",
        "desc": "Crea un contrato seguro para alquilar tu propiedad, adaptado a las leyes locales.",
        "button_href": "#proyectos",
        "image_src": "/favicon.ico",
    },
]

def template_card(data):
    return rx.box(
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.image(
                        src=data["image_src"],
                        width="150px",
                        height="auto",
                        alt="Foto de perfil Arlexdev",
                    ),
                    justify="center",
                    align_items="center",
                    spacing="6",
                    width="100%"
                ),
                padding=rx.breakpoints(
                    initial="1.5em",
                    sm="2em",
                    lg="2em"
                ),
                border="1px solid #e0e0e0",
                border_radius="16px",
                width="100%",
            ),
            rx.vstack(
                rx.badge(data["badge"], size="3"),
                rx.text(data["title"], size="6", weight="bold", color="#000"),
                rx.text(data["desc"], color_scheme="gray", weight="light"),
                rx.button(
                    rx.text(
                        "Ver Plantilla",
                        size=rx.breakpoints(
                            initial="3",
                            sm="4",
                            lg="4"
                        ),
                    ),
                    size=rx.breakpoints(
                        initial="3",
                        sm="4",
                        lg="4"
                    ),
                    on_click=lambda: rx.redirect(data["button_href"]),
                    color="#000",
                    background_color="#fff",
                    border="1px solid #c6c6c6",
                    _hover={
                        #"opacity": "0.8",
                        "background_color": "#f5f5f5"
                    },
                    width="100%"
                ),
                width="100%"
            ),
            spacing="6",
            width="100%"
        ),
        padding=rx.breakpoints(
            initial="1.5em",
            sm="2em",
            lg="20px"
        ),
        border="1px solid #e0e0e0",
        border_radius="24px",
        background=rx.color("gray", 2),
        width="100%",
    )

def catalog() -> rx.Component:
    return rx.center(
        rx.section(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "Catálogo de plantillas",
                        size=rx.breakpoints(
                            initial="6",
                            sm="7",
                            lg="8"
                        ),
                        color="#000",
                        weight="bold",
                        as_="h2"
                    ),
                    justify="center",
                    width="100%",
                ),
                rx.grid(
                    rx.foreach(TEMPLATES, template_card),
                    gap="1rem",
                    grid_template_columns=[
                        "1fr",
                        "repeat(2, 1fr)",
                        "repeat(2, 1fr)",
                        "repeat(3, 1fr)",
                    ],
                    width="100%",
                ),
                rx.box(
                    rx.hstack(
                        rx.hstack(
                            rx.icon(tag="pin", size=40, color="#000"),
                            rx.vstack(
                                rx.text("Más plantillas", size="5", weight="bold", color="#000"),
                                rx.text(
                                    "Transforma por completo tu forma de trabajar y vivir con las plantillas premium. Estas plantillas son sistemas completos con múltiples páginas.",
                                    color_scheme="gray",
                                    weight="light",
                                    width="600px"
                                ),
                            ),
                            align="center",
                            spacing="6",
                        ),
                        rx.button(
                            rx.text(
                                "Ver Plantilla",
                                size=rx.breakpoints(
                                    initial="3",
                                    sm="4",
                                    lg="4"
                                ),
                            ),
                            size=rx.breakpoints(
                                initial="3",
                                sm="4",
                                lg="4"
                            ),
                            on_click=lambda: rx.redirect("#proyectos"),
                            color="#000",
                            background_color="#fff",
                            border="1px solid #c6c6c6",
                            _hover={"background_color": "#f9f9f9"},
                        ),
                        justify="between",
                        align_items="center",
                        width="100%"
                    ),
                    padding=rx.breakpoints(
                        initial="1.5em",
                        sm="2em",
                        lg="20px"
                    ),
                    border="1px dashed #000",
                    border_radius="24px",
                    width="100%",
                ),
                margin=rx.breakpoints(
                    initial="1.5em",
                    sm="2.5em",
                    lg="3.5em"
                ),
                spacing="8"
            ),
            style=styles.max_width_style,
            width="100%",
            size="2",
            id="plantillas",
        ),
        width="100%"
    )
