import reflex as rx
from ..styles import styles

def feature_item(feature: str) -> rx.Component:
    return rx.hstack(
        rx.icon(
            "check", color="#000", size=21
        ),
        rx.text(feature, size="4", weight="regular",color="#000"),
    )


def standard_features() -> rx.Component:
    return rx.vstack(
        feature_item("Sin acceso a plantillas avanzadas"),
        feature_item("Sin descarga en Word."),
        feature_item("Sin revisión legal opcional."),
        feature_item("Sin soporte prioritario."),
        spacing="3",
        width="100%",
        align_items="start",
    )


def popular_features() -> rx.Component:
    return rx.vstack(
        feature_item("Descarga en PDF y Word."),
        feature_item("Personalización completa."),
        feature_item("Revisión legal opcional."),
        feature_item("Soporte prioritario por email o chat"),
        feature_item("Guardado ilimitado de contratos en la cuenta del usuario."),
        spacing="3",
        width="100%",
        align_items="start",
    )


def pricing_card_standard() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="circle", color="#000", size=50),
            rx.badge(
                "$0",
                color_scheme="gray",
                size="3",
            ),
            justify="between",
            width="100%"
        ),
        rx.vstack(
            rx.text("Acceso a plantillas básicas",size="5", weight="bold",color="#000"),
            rx.text("Obtén plantillas gratis",color_scheme="gray",weight="light",width="400px"),
            width="100%"
        ),
        rx.divider(),
        rx.text(
            "Gratis",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
            color="#000"
        ),
        standard_features(),
        rx.spacer(),
        rx.button(
            rx.text(
                "Obtenga el paquete gratis",
                size=rx.breakpoints(
                initial="3",
                sm="4",
                lg="4"
                ),
            ),
            on_click=lambda: rx.redirect("", is_external=True),
            size=rx.breakpoints(
                initial="3",
                sm="4",
                lg="4"
            ),
            background_color="#000",
            border="1px solid #c6c6c6",
            color="#fff",
            _hover={"opacity": "0.8"},
            width="100%"
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        bg="fff",
        #background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        border_radius="24px",
    )


def pricing_card_popular() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="square-square", color="#000", size=50),
            rx.badge(
                "$19",
                color_scheme="gray",
                size="3",
            ),
            justify="between",
            width="100%"
        ),
        rx.vstack(
            rx.text("Acceso a plantillas básicas",size="5", weight="bold",color="#000"),
            rx.text("Obtén plantillas gratis",color_scheme="gray",weight="light",width="400px"),
            width="100%"
        ),
        rx.divider(),
        rx.text(
            "Premium",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
            color="#000",
        ),
        popular_features(),
        rx.spacer(),
        rx.button(
            rx.text(
                "Desbloquear paquete completo",
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
            width="100%"
        ),
        spacing="6",
        border="1px solid #e0e0e0",
        background=rx.color("gray", 2),
        padding="28px",
        width="100%",
        border_radius="24px",
    )

def plans() -> rx.Component:
    return rx.center(
        rx.section(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "Planes para todos",
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
                    pricing_card_standard(),
                    pricing_card_popular(),
                    gap="1rem",
                    grid_template_columns=[
                        "1fr",
                        "repeat(2, 1fr)",
                        "repeat(2, 1fr)",
                        #"repeat(3, 1fr)",
                        #"repeat(4, 1fr)",
                    ],
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
            id="precios",
        ),
        width="100%"
    )
