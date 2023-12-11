from enum import Enum


class GetAssetSort(str, Enum):
    COST = "cost"
    NAME = "name"
    RATING = "rating"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
