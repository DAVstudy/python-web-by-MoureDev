import reflex as rx
from link_bio.api.api import live

USER = "juansguarnizo"


class PageState(rx.State):

    is_live: bool

    async def check_live(self):
        self.is_live = await live(USER)
