import link_bio.constants as constants
from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI
from .ConfigCat import ConfigCatAPI
from link_bio.model.Live import Live
from link_bio.model.Featured import Featured


TWITCH_API = TwitchAPI()
SUPABASE_API = SupabaseAPI()
CONFIGCAT_API = ConfigCatAPI() 


async def repo() -> str:
    return constants.REPO_URL


async def live(user: str) -> Live:
    return TWITCH_API.live(user)


async def featured() -> list[Featured]:
    return SUPABASE_API.featured()


async def schedule() -> dict:
    return CONFIGCAT_API.schedule()
