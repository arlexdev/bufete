import reflex as rx

def stroke() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/stroke_arlexdev.svg",
            width="100%",
            height="auto",
            alt="logo arlexdev stroke",
            loading="lazy",
        ),
        width="100%",
    )
