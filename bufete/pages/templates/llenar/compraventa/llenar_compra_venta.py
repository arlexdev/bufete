# bufete/pages/templates/llenar_compra_venta.py
import reflex as rx
from bufete.components.footer import footer
from bufete.components.navbar import navbar
from bufete.styles import styles

class CompraVentaState(rx.State):
    step: int = 1
    datos: dict = {}

    @rx.event
    def siguiente(self, form_data: dict):
        self.datos = {**self.datos, **form_data}
        if self.step < 3:
            self.step += 1

    @rx.event
    def anterior(self):
        if self.step > 1:
            self.step -= 1

def barra_progreso():
    valor = rx.cond(
        CompraVentaState.step == 1, 33,
        rx.cond(CompraVentaState.step == 2, 66, 100)
    )
    return rx.progress(
        value=valor,
        width="100%",
        height="8px",
        color_scheme="green"
    )

def preview_contrato():
    return rx.card(
        rx.vstack(
            rx.text("Datos recopilados:"),
            #rx.text(CompraVentaState.datos.to_string()),
        ),
        width="100%",
        height="200px"
    )

def form_step_1():
    return rx.box(
        rx.form(
            rx.vstack(
                rx.heading("Paso 1: Datos Básicos"),
                rx.divider(),
                rx.input(placeholder="Nombre completo", name="nombre", required=True, width="100%"),
                rx.input(placeholder="Carnet de Identidad", name="ci", required=True, width="100%"),
                rx.select(
                    ["Comercial", "Vivienda"],
                    placeholder="Tipo de Uso",
                    name="uso",
                    required=True,
                ),
                rx.button("Siguiente", type="submit"),
            ),
            on_submit=CompraVentaState.siguiente,
            reset_on_submit=True,
        ),
        padding=rx.breakpoints(
            initial="1.5em",
            sm="2em",
            lg="2em"
        ),
        border="1px solid #e0e0e0",
        border_radius="16px",
        width="100%",
    ),


def form_step_2():
    return rx.form(
        rx.vstack(
            rx.heading("Paso 2: Datos del Inmueble"),
            rx.input(placeholder="Partida en Derechos Reales", name="partida", required=True),
            rx.input(placeholder="Número de Oficina", name="nro_oficina"),
            rx.input(placeholder="Piso", name="piso"),
            rx.hstack(
                rx.button("Anterior", on_click=CompraVentaState.anterior),
                rx.button("Siguiente", type="submit"),
                spacing="4"
            ),
        ),
        on_submit=CompraVentaState.siguiente,
        reset_on_submit=True,
    )

def form_step_3():
    return rx.form(
        rx.vstack(
            rx.heading("Paso 3: Ubicación y Parqueo"),
            rx.input(placeholder="Partida Parqueo", name="partida_parqueo"),
            rx.input(placeholder="Edificio", name="edificio", required=True),
            rx.input(placeholder="Calle", name="calle", required=True),
            rx.input(placeholder="Zona", name="zona", required=True),
            rx.input(placeholder="Ciudad", name="ciudad", required=True),
            rx.hstack(
                rx.button("Anterior", on_click=CompraVentaState.anterior),
                rx.button("Finalizar", type="submit"),
                spacing="4"
            ),
        ),
        on_submit=CompraVentaState.siguiente,  # Aquí puedes cambiar la lógica para finalizar
        reset_on_submit=True,
    )

@rx.page(route="/templates/llenar/llenar-compra-venta", title="Llenar Contrato de Compra y Venta")
def llenar_compra_venta():
    return rx.box(
        navbar(),
        rx.center(
            rx.section(
                rx.vstack(
                    rx.hstack(
                        rx.vstack(
                            rx.hstack(
                                rx.badge(
                                    "$50",
                                    size="3",
                                    bg="#fff",
                                    border="1px dashed #000",
                                    #border_radius="16px",
                                ),
                                rx.badge("Productividad",size="3"),
                            ),
                            rx.heading("Contrato de Compra y Venta", size="8"),
                            form_step_1(),
                            rx.hstack(
                                rx.button(
                                    rx.text(
                                        "Anterior",
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
                                ),
                                rx.button(
                                    rx.text(
                                        "Siguiente",
                                        size=rx.breakpoints(
                                        initial="3",
                                        sm="4",
                                        lg="4"
                                        ),
                                    ),
                                    size=rx.breakpoints(
                                        initial="3",
                                        sm="4",
                                        lg="4"
                                    ),
                                    on_click=lambda: rx.redirect("#proyectos"),
                                    color="#000",
                                    background_color="#fff",
                                    border="1px solid #c6c6c6",
                                    _hover={"opacity": "0.8"},
                                    disabled=True
                                ),
                                rx.button(
                                    rx.text(
                                        "Pagar y Descargar",
                                        size=rx.breakpoints(
                                        initial="3",
                                        sm="4",
                                        lg="4"
                                        ),
                                    ),
                                    size=rx.breakpoints(
                                        initial="3",
                                        sm="4",
                                        lg="4"
                                    ),
                                    on_click=lambda: rx.redirect("#proyectos"),
                                    color_scheme="green",
                                    #color="#000",
                                    #background_color="#fff",
                                    border="1px solid green",
                                    _hover={"opacity": "0.8"},
                                    disabled=True
                                ),
                                width="100%",
                                #justify="center",
                                align="center",
                            ),
                            spacing="6",
                            width="80%"
                        ),
                        rx.box(
                            rx.vstack(
                                rx.heading("Hello World!"),
                                rx.scroll_area(
                                    rx.flex(
                                        rx.text(
                                            """Three fundamental aspects of typography are legibility, readability, and
                                        aesthetics. Although in a non-technical sense “legible” and “readable”
                                        are often used synonymously, typographically they are separate but
                                        related concepts.""",
                                        ),
                                        rx.text(
                                            """Legibility describes how easily individual characters can be
                                        distinguished from one another. It is described by Walter Tracy as “the
                                        quality of being decipherable and recognisable”. For instance, if a “b”
                                        and an “h”, or a “3” and an “8”, are difficult to distinguish at small
                                        sizes, this is a problem of legibility.""",
                                        ),
                                        rx.text(
                                            """Typographers are concerned with legibility insofar as it is their job to
                                        select the correct font to use. Brush Script is an example of a font
                                        containing many characters that might be difficult to distinguish. The
                                        selection of cases influences the legibility of typography because using
                                        only uppercase letters (all-caps) reduces legibility.""",
                                        ),
                                        direction="column",
                                        spacing="4",
                                    ),
                                    type="always",
                                    scrollbars="vertical",
                                    width="100%",
                                    style={"height": 180},
                                )
                            ),
                            padding=rx.breakpoints(
                                initial="1.5em",
                                sm="2em",
                                lg="2em"
                            ),
                            border="1px solid #e0e0e0",
                            border_radius="16px",
                            width="100%",
                        ),
                        spacing="6",
                        justify="between",
                        width="100%"
                    ),
                    margin=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="3.5em"
                    ),
                    padding_top="6rem",
                    spacing="8"
                ),
                style=styles.max_width_style,
                width="100%",
                size="2",
                id="sobre-mi",
            ),
            width="100%"
        ),
        footer(),
    ),
