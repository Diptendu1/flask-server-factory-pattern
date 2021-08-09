import requests
import logging
from sqlalchemy.orm import sessionmaker
from app import db
from models.model import User
from models.model import UserRole
from models.model import Role

logger = logging.getLogger("app.access")


def first():
    logger.info("HERE")
    return "first API"


async def get_json(url):
    async with requests.get(url) as response:
        assert response.status == 200
        return await response.json()


def insert_data_ex():
    role = Role(name="role2", description="Role description")
    db.session.add(role)
    db.session.commit()
    return_map = {"message": "added data to roles"}
    return return_map





