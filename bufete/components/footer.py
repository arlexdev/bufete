import reflex as rx
import datetime

from ..styles import styles

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "PRODUCTS", size="4", weight="bold", as_="h3",color="#000"
        ),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce", "/#"),
        footer_item("Content Management", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "RESOURCES", size="4", weight="bold", as_="h3",color="#000"
        ),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify="end",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.center(
            rx.vstack(
                rx.flex(
                    rx.vstack(
                        rx.hstack(
                            rx.image(
                                src="/favicon.ico",
                                width="2.25em",
                                height="auto",
                                border_radius="25%",
                            ),
                            rx.heading(
                                "DocuFácil",
                                size="7",
                                weight="bold",
                                color="#000"
                            ),
                            align_items="center",
                        ),
                        rx.text("Documentos legales, sin complicaciones",color_scheme="gray"),
                        spacing="4",
                        align_items=[
                            "center",
                            "center",
                            "start",
                        ],
                    ),
                    footer_items_1(),
                    footer_items_2(),
                    justify="between",
                    spacing="6",
                    flex_direction=["column", "column", "row"],
                    width="100%",
                ),
                rx.divider(),
                rx.hstack(
                    rx.text(
                        f" © {datetime.date.today().year} Desarrollado con",
                        size="3",
                        white_space="nowrap",
                        color_scheme="gray"
                    ),
                    rx.icon("heart",size=20,color="#000"),
                    rx.text("por arlexdev",color_scheme="gray"),
                    align="center",
                    justify="center",
                    spacing="1",
                    width="100%",
                ),
                padding=rx.breakpoints(
                    initial="1.5em",
                    sm="2.5em",
                    lg="3.5em",
                ),
                style=styles.max_width_style,
                spacing="5",
                width="100%",
            ),
            bg="#fff",
            width="100%",
        ),
        width="100%",
    )
