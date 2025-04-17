import reflex as rx
from bufete.components.footer import footer
from bufete.components.navbar import navbar
from bufete.styles import styles

@rx.page(route="/templates/compra-venta", title="Plantilla Compra y Venta")
def compra_venta():
    return rx.box(
        navbar(),
        rx.center(
            rx.section(
                rx.vstack(
                    #rx.hstack(
                    #    rx.heading(
                    #        "Catálogo de plantillas",
                    #        size=rx.breakpoints(
                    #            initial="6",
                    #            sm="7",
                    #            lg="8"
                                #        ),
                    #        color="#000",
                    #        weight="bold",
                    #        as_="h2"
                            #    ),
                    #    justify="center",
                    #    width="100%",
                    #),
                    rx.hstack(
                        rx.vstack(
                            rx.hstack(
                                rx.badge(
                                    "$50",
                                    size="3",
                                    bg="#fff",
                                    border="1px dashed #000",
                                    #border_radius="16px",
                                ),
                                rx.badge("Productividad",size="3"),
                            ),
                            rx.heading("Plantilla Compra y Venta", size="8"),
                            rx.text("Aquí van los detalles completos de la plantilla de compra y venta."),
                            rx.hstack(
                                rx.button(
                                    rx.text(
                                        "Iniciar personalización",
                                        size=rx.breakpoints(
                                        initial="3",
                                        sm="4",
                                        lg="4"
                                        ),
                                    ),
                                    on_click=lambda: rx.redirect("/templates/llenar/llenar-compra-venta"),
                                    size=rx.breakpoints(
                                        initial="3",
                                        sm="4",
                                        lg="4"
                                    ),
                                    background_color="#000",
                                    border="1px solid #c6c6c6",
                                    color="#fff",
                                    _hover={"opacity": "0.8"},
                                ),
                                rx.button(
                                    rx.text(
                                        "Consigue el paquete completo",
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
                                    _hover={"opacity": "0.8"},
                                ),
                                width="100%",
                                justify="center",
                                align="center",
                                role="group",
                                aria_label="Enlaces a redes sociales"
                            ),
                        ),
                        rx.box(
                            rx.vstack(
                                rx.image(
                                    src="/favicon.ico",
                                    width="150px",
                                    height="auto",
                                    alt="Foto de perfil Arlexdev",
                                ),
                                justify="center",
                                align_items="center",
                                spacing="6",
                                #width="100%"
                            ),
                            padding=rx.breakpoints(
                                initial="1.5em",
                                sm="2em",
                                lg="2em"
                            ),
                            border="1px solid #e0e0e0",
                            border_radius="16px",
                            #width="100%",
                        ),
                        justify="between",
                        width="100%"
                    ),
                    rx.vstack(
                        rx.text("Descripción general",size="7",weight="bold"),
                        rx.text("El Contrato de Compra y venta es un documento legal que establece los términos acordados entre un comprador y un vendedor para la transferencia de un bien a cambio de un pago. Perfecto para vehículos, propiedades, equipos o cualquier transacción comercial."),
                        padding_top="6em"
                    ),
                    margin=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="3.5em"
                    ),
                    padding_top="6rem",
                    spacing="8"
                ),
                style=styles.max_width_style,
                width="100%",
                size="2",
                id="sobre-mi",
            ),

            width="100%"
        ),
        footer(),
    ),
