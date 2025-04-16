import reflex as rx

from ..views.call_to_action import call_to_action
#from ..views.education import education
#from ..views.technology import technology
#from ..views.clients import clients
from ..views.works import works
from ..views.experience import experience
from ..views.about import about
from ..views.hero import hero
from ..components.footer import footer
from ..components.navbar import navbar


def index() -> rx.Component:
    return rx.box(
            #rx.theme_panel(),
            navbar(),
            rx.vstack(
                hero(),
                about(),
                works(),
                #clients(),
                experience(),
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
