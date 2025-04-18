import reflex as rx
from ..styles import styles

def call_to_action() -> rx.Component:
    return rx.center(
        rx.section(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "Contacto",
                        size=rx.breakpoints(
                            initial="6",
                            sm="7",
                            lg="8"
                        ),
                        weight="bold",
                        as_="h2"
                    ),
                    justify="center",
                    width="100%",
                ),
                rx.box(
                    rx.vstack(
                        rx.icon("mail", size=65,color="#000"),
                        rx.text("Estamos aquí para ayudarte",size="8",align="center",color="#000",weight="bold"),
                        rx.button(
                            rx.text("Contáctame", size="4"),
                            on_click=lambda: rx.redirect("https://mail.google.com/mail/u/0/?fs=1&tf=cm&to=arlexdev@gmail.com", is_external=True),
                            size="4",
                            background_color="#FFFFFF",
                            border="1px solid #c6c6c6",
                            color="#000000",
                            _hover={"background_color": "#f9f9f9"},
                        ),
                        align="center",
                        justify="center",
                        spacing="6",
                        width="100%"
                    ),
                    padding=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="4.5em"
                    ),
                    border="1px solid #e0e0e0",
                    border_radius="12px",
                    width="100%",
                    bg="#f9f9f9"
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
            id="contacto",
        ),
        width="100%"
    )
