import reflex as rx
from link_bio.api.api import live, featured

USER = "devsdav"


class PageState(rx.State):

    is_live: bool
    live_title: str
    featured_info: list

    async def check_live(self):
        live_data = await live(USER)
        self.is_live = live_data["live"]
        self.live_title = live_data["title"]

    async def featured_links(self):
        self.featured_info = await featured()
