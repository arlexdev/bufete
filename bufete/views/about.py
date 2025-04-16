import reflex as rx
from ..styles import styles

def about() -> rx.Component:
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
                    rx.box(
                        rx.vstack(
                            rx.box(
                                rx.vstack(
                                    rx.image(
                                        src="/favicon.ico",
                                        width="150px",
                                        height="auto",
                                        alt="Foto de perfil Arlexdev",
                                        #mask_image="linear-gradient(to bottom, #111111 80%, transparent)"
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
                                #bg="#060606"
                            ),
                            rx.vstack(
                                rx.badge("Los más vendidos",size="3"),
                                rx.text("Compra y venta",size="4", weight="bold",color="#000"),
                                rx.text("An all-in-one Notion template designed for professionals, creators, and teams.",color_scheme="gray",weight="light"),
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
                                    _hover={"opacity": "0.8"},
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
                        width="100%",
                        #bg="#060606"
                    ),
                    rx.box(
                        rx.vstack(
                            rx.box(
                                rx.vstack(
                                    rx.image(
                                        src="/favicon.ico",
                                        width="150px",
                                        height="auto",
                                        alt="Foto de perfil Arlexdev",
                                        #mask_image="linear-gradient(to bottom, #111111 80%, transparent)"
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
                                #bg="#060606"
                            ),
                            rx.vstack(
                                rx.badge("Los más vendidos",size="3"),
                                rx.text("Compra y venta",size="4", weight="bold",color="#000"),
                                rx.text("An all-in-one Notion template designed for professionals, creators, and teams.",color_scheme="gray",weight="light"),
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
                                    _hover={"opacity": "0.8"},
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
                        width="100%",
                        #bg="#060606"
                    ),
                    rx.box(
                        rx.vstack(
                            rx.box(
                                rx.vstack(
                                    rx.image(
                                        src="/favicon.ico",
                                        width="150px",
                                        height="auto",
                                        alt="Foto de perfil Arlexdev",
                                        #mask_image="linear-gradient(to bottom, #111111 80%, transparent)"
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
                                #bg="#060606"
                            ),
                            rx.vstack(
                                rx.badge("Los más vendidos",size="3"),
                                rx.text("Contrato de Arrendamiento",size="4", weight="bold",color="#000"),
                                rx.text("An all-in-one Notion template designed for professionals, creators, and teams.",color_scheme="gray",weight="light"),
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
                                    _hover={"opacity": "0.8"},
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
                        width="100%",
                        #bg="#060606"
                    ),
                    gap="1rem",
                    grid_template_columns=[
                        "1fr",
                        "repeat(2, 1fr)",
                        "repeat(2, 1fr)",
                        "repeat(3, 1fr)",
                        #"repeat(4, 1fr)",
                    ],
                    width="100%",
                ),
                rx.box(
                    rx.hstack(
                        rx.hstack(
                            rx.icon(tag="pin",size=40,color="#000"),
                            rx.vstack(
                                rx.text("Más plantillas",size="5", weight="bold",color="#000"),
                                rx.text("Transforma por completo tu forma de trabajar y vivir con las plantillas premium. Estas plantillas son sistemas completos con múltiples páginas.",color_scheme="gray",weight="light",width="600px"),
                            ),
                            align="center",

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
                            _hover={"opacity": "0.8"},
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
                    #bg="#060606"
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
            id="sobre-mi",
        ),
        width="100%"
    )
