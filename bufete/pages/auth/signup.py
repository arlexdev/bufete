import reflex as rx

from bufete.components.footer import footer
from bufete.components.navbar import navbar

@rx.page(route="/signup", title="Registro")
def signup() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.section(
                rx.card(
                    rx.vstack(
                        rx.center(
                            rx.image(
                                src="/favicon.ico",
                                width="2.5em",
                                height="auto",
                                border_radius="25%",
                            ),
                            rx.heading(
                                "Crear una nueva cuenta",
                                size="6",
                                as_="h2",
                                text_align="center",
                                width="100%",
                            ),
                            direction="column",
                            spacing="5",
                            width="100%",
                        ),
                        rx.hstack(
                            rx.vstack(
                                rx.text(
                                    "Nombre",
                                    size="3",
                                    weight="medium",
                                    text_align="left",
                                    width="100%",
                                ),
                                rx.input(
                                    rx.input.slot(rx.icon("user")),
                                    placeholder="Nombre",
                                    type="email",
                                    size="3",
                                    width="100%",
                                ),
                                justify="start",
                                spacing="2",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text(
                                    "Apellido",
                                    size="3",
                                    weight="medium",
                                    text_align="left",
                                    width="100%",
                                ),
                                rx.input(
                                    rx.input.slot(rx.icon("user")),
                                    placeholder="Apellido",
                                    type="email",
                                    size="3",
                                    width="100%",
                                ),
                                justify="start",
                                spacing="2",
                                width="100%",
                            ),
                            width="100%"
                        ),
                        rx.vstack(
                            rx.text(
                                "Correo electrónico",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("user")),
                                placeholder="Ingrese su correo electrónico",
                                type="email",
                                size="3",
                                width="100%",
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Contraseña",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("lock")),
                                    placeholder="Ingrese su contraseña",
                                type="password",
                                size="3",
                                width="100%",
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),
                        rx.box(
                            rx.checkbox(
                                " He leído y acepto la Términos del servicio y Política de Privacidad del Cliente.",
                                default_checked=True,
                                spacing="2",
                            ),
                            width="100%",
                        ),
                        rx.button(
                            rx.text(
                                "Registrarse",
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
                            width="100%"
                        ),
                        rx.center(
                            rx.text("Ya estas registrado?", size="3"),
                                rx.link("Iniciar sesión", href="/login", size="3"),
                            opacity="0.8",
                            spacing="2",
                            direction="row",
                            width="100%",
                        ),
                        spacing="6",
                        width="100%",
                    ),
                    max_width="28em",
                    size="4",
                    width="100%",
                ),
                width="100%",
                justify_items="center",
                size="3",
            ),
            width="100%",
            justify="center",
            align="center",
        ),
        footer(),
    )
