import reflex as rx
from ..styles import styles

def education() -> rx.Component:
    return rx.center(
        rx.section(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "Formación",
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
                        rx.hstack(
                            rx.text("One Next Education - Oracle + Alura",size="4", color_scheme="gray"),
                            rx.image(
                                src="/icons/alura.svg",
                                width="40px",
                                height="auto",
                                border_radius="50%",
                                aria_label="logo Alura Latam",
                            ),
                            justify="between",
                            align="center",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text("Full Stack Developer",size="5",weight="bold"),
                            rx.cond(
                                "jul. 2022 - may. 2023" != "",
                                rx.badge(
                                    "jul. 2022 - may. 2023",
                                    color_scheme="gray",
                                    size="3"
                                ),
                            ),
                            rx.text(
                                "Formación como Full Stack Developer en diversas áreas de programación y tecnología.",
                                color_scheme="gray"
                            ),
                            width="100%"
                        ),
                        spacing="4",
                        width="100%"
                    ),
                    padding=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="3.5em"
                    ),
                    border="1px solid #2A2A2A",
                    border_radius="12px",
                    width="100%",
                    bg="#060606"
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text("Universidad Tecnológica Boliviana",size="4", color_scheme="gray"),
                            rx.image(
                                src="/icons/utb.svg",
                                width="40px",
                                height="auto",
                                border_radius="50%",
                                aria_label="logo Universidad Tecnológica Boliviana",
                            ),
                            justify="between",
                            align="center",
                            width="100%"
                        ),
                        rx.vstack(
                            rx.text("Ingeniería de Sistemas",size="5",weight="bold"),
                            rx.cond(
                                "ago. 2019 - jun. 2023" != "",
                                rx.badge(
                                    "ago. 2019 - jun. 2023",
                                    color_scheme="gray",
                                    size="3"
                                ),
                            ),
                            rx.text(
                                "Egresado con una sólida base en programación, sistemas y tecnologías emergentes.",
                                color_scheme="gray"
                            ),
                            width="100%"
                        ),
                        #flex_direction=["column-reverse", "row"],
                        spacing="4",
                        width="100%"
                    ),
                    padding=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="3.5em"
                    ),
                    border="1px solid #2A2A2A",
                    border_radius="12px",
                    width="100%",
                    bg="#060606"
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text("Universidad Tecnológica Boliviana",size="4",color_scheme="gray"),
                            rx.image(
                                src="/icons/utb.svg",
                                width="40px",
                                height="auto",
                                border_radius="50%",
                                aria_label="logo Universidad Tecnológica Boliviana",
                            ),
                            justify="between",
                            align="center",
                            width="100%"
                        ),
                        rx.vstack(
                            rx.text("Experto en Hacking Ético y Ciberinteligencia Empresarial",size="5",weight="bold"),
                            rx.cond(
                                "jun. 2022 - dic. 2022" != "",
                                rx.badge(
                                    "jun. 2022 - dic. 2022",
                                    color_scheme="gray",
                                    size="3"
                                ),
                            ),
                            rx.text(
                                "Especialización en seguridad informática y ciberinteligencia.",
                                color_scheme="gray"
                            ),
                            width="100%"
                        ),
                        #flex_direction=["column-reverse", "row"],
                        spacing="4",
                        width="100%"
                    ),
                    padding=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="3.5em"
                    ),
                    border="1px solid #2A2A2A",
                    border_radius="12px",
                    width="100%",
                    bg="#060606"
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
            id="formación",
        ),
        width="100%"
    )
