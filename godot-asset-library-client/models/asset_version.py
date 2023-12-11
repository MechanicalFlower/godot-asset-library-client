import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetVersion")


@_attrs_define
class AssetVersion:
    """An asset version.

    Attributes:
        created_at (Union[Unset, datetime.datetime]): The version's release date.
        download_url (Union[Unset, str]): The version's custom download URL (if any). Will be an empty string if not
            set.
        godot_version (Union[Unset, str]): The minor Godot version the asset version was declared to be compatible with
            (in `major.minor` format).
        version_string (Union[Unset, str]): The version identifier.
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    download_url: Union[Unset, str] = UNSET
    godot_version: Union[Unset, str] = UNSET
    version_string: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        download_url = self.download_url
        godot_version = self.godot_version
        version_string = self.version_string

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if godot_version is not UNSET:
            field_dict["godot_version"] = godot_version
        if version_string is not UNSET:
            field_dict["version_string"] = version_string

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        download_url = d.pop("download_url", UNSET)

        godot_version = d.pop("godot_version", UNSET)

        version_string = d.pop("version_string", UNSET)

        asset_version = cls(
            created_at=created_at,
            download_url=download_url,
            godot_version=godot_version,
            version_string=version_string,
        )

        asset_version.additional_properties = d
        return asset_version

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
