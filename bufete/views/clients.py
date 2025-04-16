import reflex as rx
from ..styles import styles

def clients() -> rx.Component:
    return rx.center(
        rx.section(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "He colaborado con",
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
                rx.grid(
                    rx.box(
                        rx.vstack(
                            rx.hover_card.root(
                                rx.hover_card.trigger(
                                    rx.image(
                                        src="/icons/logo_iglesia.svg",
                                        width="auto",
                                        height="150px",
                                        border_radius="50%",
                                        alt="logo Iglesia Nacional Evangélica Los Amigos",
                                    ),
                                ),
                                rx.hover_card.content(
                                    rx.text("Iglesia Nacional Evangélica Los Amigos"),
                                    align="center"
                                ),
                            ),
                            justify="center",
                            align="center",
                            spacing="6",
                            width="100%"
                        ),
                        padding=rx.breakpoints(
                            initial="1.5em",
                            sm="2.5em",
                            lg="4.5em"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="12px",
                        width="100%",
                        bg="#060606"
                    ),
                    rx.box(
                        rx.vstack(
                            rx.hover_card.root(
                                rx.hover_card.trigger(
                                    rx.link(
                                        rx.image(
                                            src="/icons/logo_mi_teleferico.svg",
                                            width="auto",
                                            height="150px",
                                            border_radius="50%",
                                            alt="logo Mi Teleferico",
                                        ),
                                        href="https://www.miteleferico.bo/",
                                        is_external=True
                                    ),
                                ),
                                rx.hover_card.content(
                                    rx.text("Mi Teleférico"),
                                    align="center"
                                ),
                            ),
                            justify="center",
                            align="center",
                            spacing="6",
                            width="100%"
                        ),
                        padding=rx.breakpoints(
                            initial="1.5em",
                            sm="2.5em",
                            lg="4.5em"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="12px",
                        width="100%",
                        bg="#060606"
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
                    align="center"
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
