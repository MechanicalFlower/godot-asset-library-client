from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetPreview")


@_attrs_define
class AssetPreview:
    """ABCD.

    Attributes:
        preview_id (Union[Unset, str]):
        type (Union[Unset, str]):
        link (Union[Unset, str]):
        thumbnail (Union[Unset, str]):
    """

    preview_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    thumbnail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        preview_id = self.preview_id
        type = self.type
        link = self.link
        thumbnail = self.thumbnail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preview_id is not UNSET:
            field_dict["preview_id"] = preview_id
        if type is not UNSET:
            field_dict["type"] = type
        if link is not UNSET:
            field_dict["link"] = link
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        preview_id = d.pop("preview_id", UNSET)

        type = d.pop("type", UNSET)

        link = d.pop("link", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        asset_preview = cls(
            preview_id=preview_id,
            type=type,
            link=link,
            thumbnail=thumbnail,
        )

        asset_preview.additional_properties = d
        return asset_preview

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
