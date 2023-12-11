from enum import Enum


class GetAssetSupport(str, Enum):
    COMMUNITY = "community"
    OFFICIAL = "official"
    TESTING = "testing"

    def __str__(self) -> str:
        return str(self.value)
