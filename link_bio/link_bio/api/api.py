import link_bio.constants as constants
from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI


TWITCH_API = TwitchAPI()
SUPABASE_API = SupabaseAPI()


async def repo() -> str:
    return constants.REPO_URL


async def live(user: str) -> dict:
    return TWITCH_API.live(user)


async def featured() -> list:
    return SUPABASE_API.featured()
