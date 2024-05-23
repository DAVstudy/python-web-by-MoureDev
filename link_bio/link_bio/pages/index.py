import reflex as rx
import link_bio.utils as utils
import link_bio.styles.styles as styles
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.styles.styles import Size
from link_bio.api.api import live


class IndexState(rx.State):

    is_live: bool

    async def check_live(self):
        self.is_live = await live("devsdav")


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
    on_load=IndexState.check_live
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
               header(live=IndexState.is_live),
               index_links(),
               max_width=styles.MAX_WIDTH,
               width="100%",
               margin_y=Size.BIG.value,
               padding=Size.BIG.value
            )
        ),
        footer()
    )
