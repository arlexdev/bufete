import reflex as rx

from bufete.components.footer import footer
from bufete.components.navbar import navbar

@rx.page(route="/login", title="Inicio de sesión")
def login() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
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
                            "Sign in to your account",
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
                            rx.link("Regístrate", href="#/signup", size="3"),
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
                            "Email address",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            placeholder="user@reflex.dev",
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
                                "Password",
                                size="3",
                                weight="medium",
                            ),
                            rx.link(
                                "Forgot password?",
                                href="#",
                                size="3",
                            ),
                            justify="between",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            placeholder="Enter your password",
                            type="password",
                            size="3",
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.button(
                        "Sign in",
                        size="3",
                        width="100%",
                        on_click=rx.redirect("/contratos"),
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
                    width="100%",
                ),
                max_width="28em",
                size="4",
                width="100%",
            ),
            align="center",
            justify="center",
            height="100vh",
            width="100%"
        ),
        footer(),
    )
