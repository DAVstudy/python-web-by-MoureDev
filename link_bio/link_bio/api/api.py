import link_bio.constants as constants
from .TwitchAPI import TwitchAPI

TWITCH_API = TwitchAPI()


async def repo() -> str:
    return constants.REPO_URL


async def live(user: str) -> dict:
    return TWITCH_API.live(user)
