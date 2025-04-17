import reflex as rx
from ..styles.styles import header_style

def nav_icon(icon_name, href, tooltip):
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.link(
                rx.icon(icon_name, size=20, style={
                    "transition": "transform 0.2s",
                    "_hover": {"transform": "rotate(180deg)"}
                }),
                href=href,
                style={"padding": "0.5em"},
            )
        ),
        rx.hover_card.content(
            rx.text(tooltip),
            side="bottom",
        ),
    )

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="3"),
        href=url,
        underline="none",
        color="#gray",
        _hover= {
            "color": "#000"
        }
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.link(
                    rx.image(
                        src="/favicon.ico",
                        width="100%",
                        height="auto",
                        aria_label="logo arlexdev",
                    ),
                    href="/",
                    is_external=False
                ),
                rx.hstack(
                    navbar_link("Inicio", "/#"),
                    navbar_link("Plantillas", "/#plantillas"),
                    navbar_link("Cómo funciona", "/#como-funciona"),
                    navbar_link("Precios", "/#precios"),
                    navbar_link("Sobre nosotros", "/#formación"),
                    #navbar_link("Contacto", "/#contacto"),
                    justify="end",
                    align="center",
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Iniciar sesión",
                        size="3",
                        on_click=lambda: rx.redirect("/login"),
                        background_color="#FFFFFF",
                        border="1px solid #c6c6c6",
                        color="#000000",
                        _hover={"opacity": "0.8"},
                        #_hover={
                        #    "background_color": "#111111",
                        #    "color": "#FFFFFF"
                        #},
                    ),
                    rx.button(
                        rx.text(
                            "Únete gratis",
                            size=rx.breakpoints(
                            initial="3",
                            sm="3",
                            lg="3"
                            ),
                        ),
                        on_click=lambda: rx.redirect("/signup"),
                        size=rx.breakpoints(
                            initial="3",
                            sm="3",
                            lg="3"
                        ),
                        background_color="#000",
                        border="1px solid #c6c6c6",
                        color="#fff",
                        _hover={"opacity": "0.8"},
                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
                width="100%"
            ),
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="/logo_arlexdev.svg",
                            width="100%",
                            height="auto",
                            alt="logo arlexdev",
                        ),
                        href="/",
                        is_external=False
                    ),
                    rx.menu.root(
                        # Trigger del menú
                        rx.menu.trigger(
                            rx.icon(
                                "menu",
                                size=30,
                                aria_label="Menu version tablet y mobile"
                            )
                        ),

                        # Contenido del menú
                        rx.menu.content(
                            # Enlaces de navegación
                            rx.menu.item(
                                navbar_link("Inicio", "/#"),
                                background="transparent"
                            ),
                            rx.menu.item(
                                navbar_link("Sobre mí", "/#sobre-mi"),
                                background="transparent"
                            ),
                            rx.menu.item(
                                navbar_link("Proyectos", "/#proyectos"),
                                background="transparent"
                            ),
                            rx.menu.item(
                                navbar_link("Experiencia", "/#experiencia"),
                                background="transparent"
                            ),
                            rx.menu.item(
                                navbar_link("Formación", "/#formación"),
                                background="transparent"
                            ),

                            # Separador
                            rx.menu.separator(),

                            # Botón de CV
                            rx.menu.item(
                                rx.button(
                                    "Descargar CV",
                                    size="2",
                                    on_click=lambda: rx.redirect(
                                        "https://drive.google.com/file/d/1rUfGukE_9E6QNw5qU6WADHo_Qjk34PQL/view?usp=sharing",
                                        is_external=True
                                    ),
                                    background_color="#FFFFFF",
                                    border="1px solid #2A2A2A",
                                    color="#000000",
                                    _hover={"opacity": "0.8"}
                                )
                            ),

                            # Estilos del contenido
                            size="2",
                            width="100%",
                            left="0",
                            top="2em",
                            background_color="#060606"
                        ),
                        width="100%"
                    ),
                    justify="between",
                    align_items="center",
                    width="100%",
                ),
                width="100%",
            )
        ),
        #background="transparent",
        #background_color="rgba(17, 17, 17, 0.6)",
        padding_x="2em",
        padding_y="1em",
        position="sticky",
        top="0px",
        z_index="5",
        width="100%",
        style=header_style,
    )
