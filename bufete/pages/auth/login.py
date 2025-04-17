import reflex as rx

from bufete.components.footer import footer
from bufete.components.navbar import navbar

@rx.page(route="/login", title="Inicio de sesión")
def login() -> rx.Component:
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
                                "¡Te damos la Bienvenida!",
                                size="6",
                                as_="h2",
                                text_align="center",
                                width="100%",
                            ),
                            rx.hstack(
                                rx.text(
                                    "Nuevo aquí?",
                                    size="3",
                                    text_align="left",
                                ),
                                rx.link("Regístrate", href="/signup", size="3",underline="none"),
                                spacing="2",
                                opacity="0.8",
                                width="100%",
                            ),
                            direction="column",
                            spacing="5",
                            width="100%",
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
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.text(
                                    "Contraseña",
                                    size="3",
                                    weight="medium",
                                ),
                                rx.link(
                                    "Forgot password?",
                                    href="#",
                                    size="3",
                                    underline="none"
                                ),
                                justify="between",
                                width="100%",
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("lock")),
                                placeholder="Ingrese su contraseña",
                                type="password",
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.button(
                            rx.text(
                                "Iniciar Sesión",
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
                        rx.hstack(
                            rx.divider(margin="0"),
                            rx.text(
                                "Or continue with",
                                white_space="nowrap",
                                weight="medium",
                            ),
                            rx.divider(margin="0"),
                            align="center",
                            width="100%",
                        ),
                        rx.button(
                            rx.image(
                                src="/icons/google.svg",
                                width="20px",
                                height="20px",
                                alt="Google Logo",
                            ),
                            "Iniciar sesión con Google",
                            variant="outline",
                            size="3",
                            width="100%",
                        ),
                        spacing="6",
                        justify_items="center",
                        width="100%",
                    ),
                    max_width="28em",
                    size="4",
                    width="100%",
                ),
                size="3",
                width="100%",
                justify_items="center",
            ),
            align="center",
            justify_items="center",
            width="100%"
        ),
        footer(),
    )
