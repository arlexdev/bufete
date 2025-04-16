import reflex as rx
from ..styles import styles

def technology() -> rx.Component:
    return rx.center(
        rx.section(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "Tecnologías",
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
                        rx.hstack(
                            rx.image(
                                src="/icons/html5.svg",
                                width="26px",
                                height="26px",
                                alt="Logo HTML5"
                            ),
                            rx.text("HTML5"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/css.svg",
                                width="26px",
                                height="26px",
                                alt="Logo CSS"
                            ),
                            rx.text("CSS"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/tailwindcss.svg",
                                width="26px",
                                height="26px",
                                alt="Logo Tailwind CSS"
                            ),
                            rx.text("Tailwind CSS"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/javascript.svg",
                                width="26px",
                                height="26px",
                                alt="Logo JavaScript"
                            ),
                            rx.text("JavaScript"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/react.svg",
                                width="26px",
                                height="26px",
                                alt="Logo React"
                            ),
                            rx.text("React"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/nextjs.svg",
                                width="26px",
                                height="26px",
                                alt="Logo Next.js"
                            ),
                            rx.text("Next.js"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/reflex.svg",
                                width="26px",
                                height="26px",
                                alt="Logo Reflex"
                            ),
                            rx.text("Reflex"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/postgresql.svg",
                                width="26px",
                                height="26px",
                                alt="Logo PostgreSQL"
                            ),
                            rx.text("PostgreSQL"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/mysql.svg",
                                width="26px",
                                height="26px",
                                alt="Logo MySQL"
                            ),
                            rx.text("MySQL"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/fastapi.svg",
                                width="26px",
                                height="26px",
                                alt="Logo FastAPI"
                            ),
                            rx.text("FastAPI"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/python.svg",
                                width="26px",
                                height="26px",
                                alt="Logo Python"
                            ),
                            rx.text("Python"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/git.svg",
                                width="26px",
                                height="26px",
                                alt="Logo Git"
                            ),
                            rx.text("Git"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/github.svg",
                                width="26px",
                                height="26px",
                                alt="Logo Github"
                            ),
                            rx.text("Github"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/dbeaver.svg",
                                width="26px",
                                height="26px",
                                alt="Logo DBeaver"
                            ),
                            rx.text("DBeaver"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.image(
                                src="/icons/figma.svg",
                                width="26px",
                                height="26px",
                                alt="Logo Figma"
                            ),
                            rx.text("Figma"),
                            justify="center",
                            align="center"
                        ),
                        border="1px solid #2A2A2A",
                        border_radius="8px",
                        bg="#060606",
                        padding="20px",
                    ),
                    gap="1rem",
                    grid_template_columns=[
                        #"1fr",
                        "repeat(2, 1fr)",
                        "repeat(2, 1fr)",
                        "repeat(3, 1fr)",
                        "repeat(4, 1fr)",
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
            id="experiencia",
        ),
        width="100%"
    )
