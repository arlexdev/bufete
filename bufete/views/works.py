import reflex as rx
from ..styles import styles

def works() -> rx.Component:
    return rx.center(
        rx.section(
            rx.vstack(
                rx.hstack(
                    #rx.icon(
                    #    "folder-open-dot",
                    #    size=30
                    #),
                    rx.heading(
                        "¿Cómo funciona DocuFácil?",
                        size=rx.breakpoints(
                            initial="6",
                            sm="7",
                            lg="8"
                        ),
                        color="#000",
                        weight="bold",
                        as_="h2"
                    ),
                    width="100%",
                    justify="center"
                ),
                rx.box(
                    rx.hstack(
                        rx.vstack(
                            rx.icon(tag="square-check",size=40,color="#000"),
                            rx.vstack(
                                rx.text("Elige tu plantilla",size="5", weight="bold",color="#000"),
                                rx.text("Selecciona el documento que necesitas de nuestro catálogo.",color_scheme="gray",weight="light",width="600px"),
                                padding_top="9em"
                            ),
                        ),
                        rx.image(
                            src="/favicon.ico",
                            width="150px",
                            height="auto",
                            alt="Logo "
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
                    border="1px solid #e0e0e0",
                    border_radius="24px",
                    width="100%",
                    #bg="#060606"
                ),
                rx.grid(
                    rx.box(
                        rx.hstack(
                            rx.vstack(
                                rx.icon(tag="book-open-text",size=40,color="#000"),
                                rx.vstack(
                                    rx.text("Responde preguntas",size="5", weight="bold",color="#000"),
                                    rx.text("Completa un formulario sencillo para personalizar tu documento.",color_scheme="gray",weight="light",width="400px"),

                                    padding_top="9em"
                                ),
                            ),
                            rx.image(
                                src="/favicon.ico",
                                width="150px",
                                height="auto",
                                alt="Logo "
                            ),
                            justify="between",
                            align_items="center",
                            #width="100%"
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
                        rx.hstack(
                            rx.vstack(
                                rx.icon(tag="download",size=40,color="#000"),
                                rx.vstack(
                                    rx.text("Descarga al instante",size="5", weight="bold",color="#000"),
                                    rx.text("Obtén tu documento en PDF o Word, listo para usar.",color_scheme="gray",weight="light",width="400px"),
                                    padding_top="9em"
                                ),
                            ),
                            rx.image(
                                src="/favicon.ico",
                                width="150px",
                                height="auto",
                                alt="Logo "
                            ),
                            justify="between",
                            align_items="center",
                            #width="100%"
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
                spacing="8",
            ),
            style=styles.max_width_style,
            id="proyectos",
            size="2",
        ),
        width="100%"
    )
