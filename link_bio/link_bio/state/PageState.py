import reflex as rx
from link_bio.api.api import live

USER = "devsdav"


class PageState(rx.State):

    is_live: bool
    live_title: str

    async def check_live(self):
        live_data = await live(USER)
        self.is_live = live_data["live"]
        self.live_title = live_data["title"]
