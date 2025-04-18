import reflex as rx
from ..styles import styles

def hero() -> rx.Component:
    return rx.box(
        # Fondo decorativo

        #rx.box(
        #        position="absolute",
        #        top="0",
        #        left="0",
        #        right="0",
        #        bottom="0",
        #    background="linear-gradient(to right, #2A2A2A 1px, transparent 1px), linear-gradient(to bottom, #2A2A2A 1px, transparent 1px)",
        #    background_size="40px 40px",
        #    z_index="0"
        #),
        #rx.box(
        #    position="absolute",
        #    top="0",
        #    left="0",
        #    right="0",
        #    bottom="0",
        #    background_color="black",
        #    mask_image="radial-gradient(ellipse at center, transparent 20%, black)",
        #    webkit_mask_image="radial-gradient(ellipse at center, transparent 20%, black)",
        #    z_index="0"
        #),
        rx.center(
            rx.section(
                rx.vstack(
                    # Badge de disponibilidad
                    rx.link(
                        rx.badge(
                            rx.hstack(
                                rx.icon(
                                    tag="flame",
                                    color="red"
                                ),
                                #rx.box(
                                #    background_color="var(--green-9)",
                                #    border_radius="50%",
                                #    width="10px",
                                #    height="10px",
                                #    aria_label="Indicador de disponibilidad"
                                #),
                                rx.text("En todas las plantillas"),
                                spacing="2",
                                align="center"
                            ),
                            color_scheme="gray",
                            variant="surface",
                            radius="full",
                            size=rx.breakpoints(
                            initial="2",
                            sm="3",
                            lg="3"
                            ),
                        ),
                        href="",
                        is_external=True,
                        aria_label="Ver perfil de LinkedIn"
                    ),
                    rx.vstack(
                        # Encabezado principal
                        rx.heading(
                            "Crea documentos legales en minutos",
                            size=rx.breakpoints(
                                initial="7",
                                sm="8",
                                lg="9"
                            ),
                            #background_image="linear-gradient(to bottom, #000, #ffffffaf)",
                            #background_clip="text",
                            #color="transparent",
                            color="#000",
                            align="center",
                            weight="bold",
                            as_="h1",
                            width="700px"
                        ),
                        # Descripción
                        rx.heading(
                            "Personaliza contratos, avisos legales y más con nuestras plantillas fáciles de usar. ¡Empieza gratis hoy!",
                            width=rx.breakpoints(
                                initial="300px",
                                sm="400px",
                                md="500px",
                                lg="600px"
                            ),
                            size="5",
                            color_scheme="gray",
                            role="presentation",
                            as_="h2",
                            weight="light",
                            align="center"
                        ),
                        # Botones de redes sociales

                        rx.hstack(
                            rx.button(
                                rx.text(
                                    "Explorar plantillas",
                                    size=rx.breakpoints(
                                    initial="3",
                                    sm="4",
                                    lg="4"
                                    ),
                                ),
                                on_click=lambda: rx.redirect("#plantillas"),
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
                                on_click=lambda: rx.redirect("#precios"),
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
                        align="center",
                        justify="center",
                        spacing="6"
                    ),
                    margin=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="3.5em"
                    ),
                    spacing="5",
                    justify="center",
                    align="center"
                ),
                padding_top="4rem",
                style=styles.max_width_style,
                width="100%",
                size="2"
            ),
            width="100%",
            position="relative"
        ),
        position="relative",
        width="100%",
        height="100%"
    )
