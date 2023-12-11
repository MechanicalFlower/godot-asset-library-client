from enum import Enum


class AssetSummaryDownloadProvider(str, Enum):
    BITBUCKET = "BitBucket"
    CGIT = "cgit"
    CUSTOM = "Custom"
    GITHUB = "GitHub"
    GITLAB = "GitLab"
    GOGSGITEA = "Gogs/Gitea"

    def __str__(self) -> str:
        return str(self.value)
