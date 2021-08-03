import requests
import logging

logger = logging.getLogger("app.access")

def first():
    logger.info("HERE")
    return "first API"


async def get_json(url):
    async with requests.get(url) as response:
        assert response.status == 200
        return await response.json()
