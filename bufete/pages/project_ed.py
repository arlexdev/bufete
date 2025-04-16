import reflex as rx
from ..components.footer import footer
from ..components.navbar import navbar
from ..styles import styles

def imagen_con_descripcion(imagen_src: str, titulo: str, descripcion: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(
                src=imagen_src,
                width="100%",
                height="auto",
                border_radius="15px",
                loading="lazy",
            ),
            rx.heading(titulo, size="5",weight="bold"),
            rx.text(descripcion,color_scheme="gray"),
            spacing="4",
            align="start",
        ),
        padding=rx.breakpoints(
            initial="1.5em",
            sm="2.5em",
            lg="3.5em"
        ),
        border="1px solid #2A2A2A",
        border_radius="12px",
        width="100%",
        bg="#060606",
    )

def galeria_imagenes() -> rx.Component:
    return rx.vstack(
        rx.desktop_only(
            rx.hstack(
                rx.heading(
                    "Galería del Sistema",
                    size=rx.breakpoints(
                        initial="6",
                        sm="7",
                        lg="8"
                    ),
                    weight="bold"
                ),
                #padding_top="40px",
                align="center",
                width="100%",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.heading(
                    "Galería del Sistema",
                    size=rx.breakpoints(
                        initial="6",
                        sm="7",
                        lg="8"
                    ),
                    weight="bold"
                ),
                #padding_top="40px",
                align="center",
                width="100%",
            ),
        ),
        rx.grid(
            rx.foreach(
                [
                    {
                        "src": "/project_ed/dashboard.webp",
                        "titulo": "Panel Principal",
                        "descripcion": "Vista general del sistema con estadísticas y accesos rápidos."
                    },
                    {
                        "src": "/project_ed/mapa.webp",
                        "titulo": "Mapa Interactivo",
                        "descripcion": "Visualización geográfica de miembros con marcadores personalizados."
                    },
                    {
                        "src": "/project_ed/busqueda.webp",
                        "titulo": "Sistema de Búsqueda",
                        "descripcion": "Interfaz de búsqueda avanzada con filtros y resultados en tiempo real."
                    },
                    {
                        "src": "/project_ed/registro.webp",
                        "titulo": "Registro de Miembros",
                        "descripcion": "Formulario completo para el registro y actualización de miembros."
                    }
                ],
                lambda item: imagen_con_descripcion(
                    item["src"],
                    item["titulo"],
                    item["descripcion"]
                )
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
        spacing="8",
    )


def caracteristica_detallada(titulo: str, descripcion: str, detalles: list) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(titulo, size="4",weight="bold"),
            rx.separator(),
            rx.text(descripcion),
            rx.list.unordered(
                *[rx.list.item(f"{detalle}") for detalle in detalles],
                color=rx.color("gray",11)
            ),
            spacing="4",
            align="start",
        ),
        padding=rx.breakpoints(
            initial="1.5em",
            sm="2.5em",
            lg="3.5em"
        ),
        border="1px solid #2A2A2A",
        border_radius="12px",
        width="100%",
        bg="#060606",
    )


def project_ed() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.section(
                rx.vstack(
                    rx.vstack(
                        rx.hstack(
                            rx.heading(
                                "Sistema de Gestión Integral de Membresías",
                                size="8",
                                color=rx.color_mode_cond(light="black", dark="white"),
                                weight="bold"
                            ),
                            rx.button(
                                rx.text(
                                    "Atrás",
                                    size=rx.breakpoints(
                                    initial="3",
                                    sm="4",
                                    lg="4"
                                    ),
                                ),
                                on_click=lambda: rx.redirect("/#proyectos", is_external=False),
                                size=rx.breakpoints(
                                    initial="3",
                                    sm="4",
                                    lg="4"
                                ),
                                background_color="#FFFFFF",
                                border="1px solid #2A2A2A",
                                color="#000000",
                                _hover={"opacity": "0.8"},
                            ),
                            justify="between",
                            width="100%"
                        ),
                        rx.text(
                            "Plataforma web moderna desarrollada para optimizar la administración y seguimiento de miembros de la iglesia, integrando tecnologías de geolocalización y gestión de datos.",
                            size="4",
                            color_scheme="gray"
                        ),
                        rx.image(
                            src="/project_1.webp",
                            width="100%",
                            height="auto",
                            border_radius="15px",
                            loading="lazy",
                        ),
                        spacing="6",
                        padding_y="8",
                    ),

                    # Sección de Características Detalladas
                    rx.vstack(
                        rx.desktop_only(
                            rx.hstack(
                                rx.heading(
                                    "Características Principales",
                                    size=rx.breakpoints(
                                        initial="6",
                                        sm="7",
                                        lg="8"
                                    ),
                                    weight="bold"
                                ),
                                #padding_top="40px",
                                align="center",
                                width="100%",
                            ),
                        ),
                        rx.mobile_and_tablet(
                            rx.hstack(
                                rx.heading(
                                    "Características Principales",
                                    size=rx.breakpoints(
                                        initial="6",
                                        sm="7",
                                        lg="8"
                                    ),
                                    weight="bold"
                                ),
                                #padding_top="40px",
                                align="center",
                                width="100%",
                            ),
                        ),
                        rx.grid(
                            caracteristica_detallada(
                                "Gestión de Membresías",
                                "Sistema integral para la administración de miembros.",
                                [
                                    "Categorización en Nuevos, Provisionales y Plenos",
                                    "Registro detallado de información personal",
                                    "Sistema de numeración por carnet",
                                    "Historial de cambios de estado",
                                    "Gestión de documentación"
                                ]
                            ),
                            caracteristica_detallada(
                                "Sistema de Búsqueda Avanzada",
                                "Búsqueda potente y flexible con múltiples criterios.",
                                [
                                    "Búsqueda por nombre, apellido y número de carnet",
                                    "Filtros por tipo de membresía",
                                    "Resultados en tiempo real",
                                    "Historial de búsquedas"
                                ]
                            ),
                            caracteristica_detallada(
                                "Visualización Geográfica",
                                "Mapa interactivo con funcionalidades avanzadas.",
                                [
                                    "Marcadores diferenciados por tipo de membresía",
                                    "Información detallada en ventanas emergentes",
                                    "Filtros de visualización",
                                    "Agrupación de marcadores",
                                    "Integración con Google Maps"
                                ]
                            ),
                            caracteristica_detallada(
                                "Gestión de Estados",
                                "Control completo del ciclo de vida de membresías.",
                                [
                                    "Registro de fechas de ingreso y baja",
                                    "Seguimiento de cambios de estado",
                                    "Notificaciones automáticas",
                                    "Reportes de estado",
                                    "Estadísticas de membresía"
                                ]
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
                        spacing="8",
                    ),

                    # Galería de Imágenes
                    galeria_imagenes(),

                    # Sección de Tecnologías
                    rx.vstack(
                        rx.heading("Tecnologías Utilizadas", size="6",weight="bold"),
                        rx.box(
                            rx.grid(
                                rx.vstack(
                                    rx.text("Frontend", font_weight="bold"),
                                    rx.badge(
                                        rx.text("Reflex"),
                                        variant="soft",
                                        color_scheme="violet",
                                        size="2"
                                    ),
                                    align="center"
                                ),
                                rx.vstack(
                                    rx.text("Backend", font_weight="bold"),
                                    rx.badge(
                                        rx.text("Python"),
                                        color_scheme="yellow",
                                        variant="soft",
                                        size="2"
                                    ),
                                    align="center"
                                ),
                                rx.vstack(
                                    rx.text("Base de Datos", font_weight="bold"),
                                    rx.badge(
                                        rx.text("SQLite + SQLModel"),
                                        variant="soft",
                                        color_scheme="purple",
                                        size="2"
                                    ),
                                    align="center"
                                ),
                                rx.vstack(
                                    rx.text("Mapa", font_weight="bold"),
                                    rx.badge(
                                        rx.text("Folium"),
                                        variant="soft",
                                        color_scheme="green",
                                        size="2"
                                    ),
                                    align="center"
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
                            ),
                            padding=rx.breakpoints(
                                initial="1.5em",
                                sm="2.5em",
                                lg="3.5em"
                            ),
                            border="1px solid #2A2A2A",
                            border_radius="12px",
                            width="100%",
                            bg="#060606",
                        ),
                        rx.container(
                            rx.text("Este sistema representa una solución moderna y eficiente para la gestión integral de miembros de la iglesia, combinando funcionalidad con facilidad de uso.",size="4",align="center",
                                color_scheme="gray"),
                        ),
                        align="center",
                        spacing="6",
                        width="100%",
                    ),
                    margin=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="3.5em"
                    ),
                    spacing="9"
                ),
                style=styles.max_width_style,
                width="100%",
                size="2",
                id="experiencia",
            ),
            width="100%"
        ),
        footer(),
        bg="#000000",
    )
