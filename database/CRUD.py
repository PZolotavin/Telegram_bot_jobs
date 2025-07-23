from typing import Dict, List, TypeVar
from . import models


T = TypeVar('T')


def _store_date(database: models.db, model: T, *data: List | Dict) -> None:
    with database.atomic():
        model.replace_many(*data).execute()


class CRUDInterface:
    @staticmethod
    def create():
        return _store_date