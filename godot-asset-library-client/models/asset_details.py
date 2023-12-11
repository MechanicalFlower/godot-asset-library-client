import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.asset_summary_download_provider import AssetSummaryDownloadProvider
from ..models.asset_summary_support_level import AssetSummarySupportLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_preview import AssetPreview


T = TypeVar("T", bound="AssetDetails")


@_attrs_define
class AssetDetails:
    """A resource provided by the asset library (add-on, project, ...).<br>
    These properties are only returned when requesting a specific asset,
    not a list of assets.

        Attributes:
            token (Union[Unset, str]): The Token obtained thorugh a login.
            asset_id (Union[Unset, str]): The asset's unique identifier.
            type (Union[Unset, str]): The asset's type, can be "addon" or "project".
            author (Union[Unset, str]): The author's username.
            author_id (Union[Unset, str]): The author's unique identifier.
            category (Union[Unset, str]): The category the asset belongs to.
            category_id (Union[Unset, str]): The unique identifier of the category the asset belongs to.
            download_provider (Union[Unset, AssetSummaryDownloadProvider]): The download provider where the plugin source is
                hosted.
            download_commit (Union[Unset, str]):
            download_hash (Union[Unset, str]): The asset's SHA-256 hash for the latest version. **Note:** This is currently
                always an empty string as asset versions' hashes aren't computed and stored yet.
                 Default: ''.
            cost (Union[Unset, str]): The asset's license as a [SPDX license identifier](https://spdx.org/licenses/). For
                compatibility reasons, this field is called `cost` instead of `license`.
            godot_version (Union[Unset, str]): The Godot version the asset's latest version is intended for (in
                `major.minor` format).<br> This field is present for compatibility reasons with the Godot editor. See also the
                `versions` array.
            icon_url (Union[Unset, str]): The asset's icon URL (should always be a PNG image).
            is_archived (Union[Unset, bool]): If `true`, the asset is marked as archived by its author. When archived, it
                can't receive any further reviews but can still be unarchived at any time by the author.
            issues_url (Union[Unset, str]): The asset's issue reporting URL (typically associated with the Git repository
                specified in `browse_url`).
            modify_date (Union[Unset, datetime.datetime]): The date on which the asset entry was last updated. Note that
                entries can be edited independently of new asset versions being released.
            rating (Union[Unset, str]): The asset's rating (unused). For compatibility reasons, a value of 0 is always
                returned. You most likely want `score` instead.
            support_level (Union[Unset, AssetSummarySupportLevel]): The asset's support level.
            title (Union[Unset, str]): The asset's title (usually less than 50 characters).
            version (Union[Unset, str]): The asset revision string (starting from 1).<br> Every time the asset is edited
                (for anyone and for any reason), this string is incremented by 1.
            version_string (Union[Unset, str]): The version string of the latest version (free-form, but usually
                `major.minor` or `major.minor.patch`).<br> This field is present for compatibility reasons with the Godot
                editor. See also the `versions` array.
            searchable (Union[Unset, str]):
            previews (Union[Unset, List['AssetPreview']]):
            browse_url (Union[Unset, str]): The asset's browsable repository URL.
            description (Union[Unset, str]): The asset's full description.
            download_url (Union[Unset, str]): The download link of the asset's latest version (should always point to a ZIP
                archive).<br> This field is present for compatibility reasons with the Godot editor. See also the `versions`
                array.
    """

    token: Union[Unset, str] = UNSET
    asset_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    author: Union[Unset, str] = UNSET
    author_id: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    category_id: Union[Unset, str] = UNSET
    download_provider: Union[Unset, AssetSummaryDownloadProvider] = UNSET
    download_commit: Union[Unset, str] = UNSET
    download_hash: Union[Unset, str] = ""
    cost: Union[Unset, str] = UNSET
    godot_version: Union[Unset, str] = UNSET
    icon_url: Union[Unset, str] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    issues_url: Union[Unset, str] = UNSET
    modify_date: Union[Unset, datetime.datetime] = UNSET
    rating: Union[Unset, str] = UNSET
    support_level: Union[Unset, AssetSummarySupportLevel] = UNSET
    title: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    version_string: Union[Unset, str] = UNSET
    searchable: Union[Unset, str] = UNSET
    previews: Union[Unset, List["AssetPreview"]] = UNSET
    browse_url: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    download_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        asset_id = self.asset_id
        type = self.type
        author = self.author
        author_id = self.author_id
        category = self.category
        category_id = self.category_id
        download_provider: Union[Unset, str] = UNSET
        if not isinstance(self.download_provider, Unset):
            download_provider = self.download_provider.value

        download_commit = self.download_commit
        download_hash = self.download_hash
        cost = self.cost
        godot_version = self.godot_version
        icon_url = self.icon_url
        is_archived = self.is_archived
        issues_url = self.issues_url
        modify_date: Union[Unset, str] = UNSET
        if not isinstance(self.modify_date, Unset):
            modify_date = self.modify_date.isoformat()

        rating = self.rating
        support_level: Union[Unset, str] = UNSET
        if not isinstance(self.support_level, Unset):
            support_level = self.support_level.value

        title = self.title
        version = self.version
        version_string = self.version_string
        searchable = self.searchable
        previews: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.previews, Unset):
            previews = []
            for previews_item_data in self.previews:
                previews_item = previews_item_data.to_dict()

                previews.append(previews_item)

        browse_url = self.browse_url
        description = self.description
        download_url = self.download_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if type is not UNSET:
            field_dict["type"] = type
        if author is not UNSET:
            field_dict["author"] = author
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if category is not UNSET:
            field_dict["category"] = category
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if download_provider is not UNSET:
            field_dict["download_provider"] = download_provider
        if download_commit is not UNSET:
            field_dict["download_commit"] = download_commit
        if download_hash is not UNSET:
            field_dict["download_hash"] = download_hash
        if cost is not UNSET:
            field_dict["cost"] = cost
        if godot_version is not UNSET:
            field_dict["godot_version"] = godot_version
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if is_archived is not UNSET:
            field_dict["is_archived"] = is_archived
        if issues_url is not UNSET:
            field_dict["issues_url"] = issues_url
        if modify_date is not UNSET:
            field_dict["modify_date"] = modify_date
        if rating is not UNSET:
            field_dict["rating"] = rating
        if support_level is not UNSET:
            field_dict["support_level"] = support_level
        if title is not UNSET:
            field_dict["title"] = title
        if version is not UNSET:
            field_dict["version"] = version
        if version_string is not UNSET:
            field_dict["version_string"] = version_string
        if searchable is not UNSET:
            field_dict["searchable"] = searchable
        if previews is not UNSET:
            field_dict["previews"] = previews
        if browse_url is not UNSET:
            field_dict["browse_url"] = browse_url
        if description is not UNSET:
            field_dict["description"] = description
        if download_url is not UNSET:
            field_dict["download_url"] = download_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_preview import AssetPreview

        d = src_dict.copy()
        token = d.pop("token", UNSET)

        asset_id = d.pop("asset_id", UNSET)

        type = d.pop("type", UNSET)

        author = d.pop("author", UNSET)

        author_id = d.pop("author_id", UNSET)

        category = d.pop("category", UNSET)

        category_id = d.pop("category_id", UNSET)

        _download_provider = d.pop("download_provider", UNSET)
        download_provider: Union[Unset, AssetSummaryDownloadProvider]
        if isinstance(_download_provider, Unset):
            download_provider = UNSET
        else:
            download_provider = AssetSummaryDownloadProvider(_download_provider)

        download_commit = d.pop("download_commit", UNSET)

        download_hash = d.pop("download_hash", UNSET)

        cost = d.pop("cost", UNSET)

        godot_version = d.pop("godot_version", UNSET)

        icon_url = d.pop("icon_url", UNSET)

        is_archived = d.pop("is_archived", UNSET)

        issues_url = d.pop("issues_url", UNSET)

        _modify_date = d.pop("modify_date", UNSET)
        modify_date: Union[Unset, datetime.datetime]
        if isinstance(_modify_date, Unset):
            modify_date = UNSET
        else:
            modify_date = isoparse(_modify_date)

        rating = d.pop("rating", UNSET)

        _support_level = d.pop("support_level", UNSET)
        support_level: Union[Unset, AssetSummarySupportLevel]
        if isinstance(_support_level, Unset):
            support_level = UNSET
        else:
            support_level = AssetSummarySupportLevel(_support_level)

        title = d.pop("title", UNSET)

        version = d.pop("version", UNSET)

        version_string = d.pop("version_string", UNSET)

        searchable = d.pop("searchable", UNSET)

        previews = []
        _previews = d.pop("previews", UNSET)
        for previews_item_data in _previews or []:
            previews_item = AssetPreview.from_dict(previews_item_data)

            previews.append(previews_item)

        browse_url = d.pop("browse_url", UNSET)

        description = d.pop("description", UNSET)

        download_url = d.pop("download_url", UNSET)

        asset_details = cls(
            token=token,
            asset_id=asset_id,
            type=type,
            author=author,
            author_id=author_id,
            category=category,
            category_id=category_id,
            download_provider=download_provider,
            download_commit=download_commit,
            download_hash=download_hash,
            cost=cost,
            godot_version=godot_version,
            icon_url=icon_url,
            is_archived=is_archived,
            issues_url=issues_url,
            modify_date=modify_date,
            rating=rating,
            support_level=support_level,
            title=title,
            version=version,
            version_string=version_string,
            searchable=searchable,
            previews=previews,
            browse_url=browse_url,
            description=description,
            download_url=download_url,
        )

        asset_details.additional_properties = d
        return asset_details

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
