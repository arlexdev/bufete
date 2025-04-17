import reflex as rx
from ..views.call_to_action import call_to_action
from ..views.how_it_works import how_it_works
from ..views.plans import plans
from ..views.catalog import catalog
from ..views.hero import hero
from ..components.footer import footer
from ..components.navbar import navbar


def index() -> rx.Component:
    return rx.box(
            #rx.theme_panel(),
            navbar(),
            rx.vstack(
                hero(),
                catalog(),
                how_it_works(),
                #clients(),
                plans(),
                #education(),
                #technology(),
                call_to_action(),
                #services(),
                footer(),
                width="100%"
            ),
            color="white",
            bg="#FFFFFF",
        )
