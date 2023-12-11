from enum import Enum


class GetConfigureType(str, Enum):
    ADDON = "addon"
    ANY = "any"
    PROJECT = "project"

    def __str__(self) -> str:
        return str(self.value)
