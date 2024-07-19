import reflex as rx
from link_bio.api.api import live, featured
from link_bio.model.Live import Live
from link_bio.model.Featured import Featured

USER = "elxokas"


class PageState(rx.State):

    live_status = Live(live=False, title="")
    featured_info: list[Featured]

    async def check_live(self):
        self.live_status = await live(USER)

    async def featured_links(self):
        self.featured_info = await featured()
