import link_bio.constants as constants


async def repo() -> str:
    return constants.REPO_URL


async def live(user: str) -> bool:
    if user == "devsdav":
        return True
    return False
