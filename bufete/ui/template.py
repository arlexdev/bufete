from typing import Callable

import reflex as rx

from bufete.components.footer import footer
from bufete.components.navbar import navbar


def template(
    page: Callable[[], rx.Component]
) -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            page(),
        ),
        footer(),
        width="100%",
    )
