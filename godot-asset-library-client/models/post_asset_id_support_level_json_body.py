from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostAssetIdSupportLevelJsonBody")


@_attrs_define
class PostAssetIdSupportLevelJsonBody:
    """
    Attributes:
        token (str):
        support_level (Union[Unset, str]):
    """

    token: str
    support_level: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        support_level = self.support_level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if support_level is not UNSET:
            field_dict["support_level"] = support_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        support_level = d.pop("support_level", UNSET)

        post_asset_id_support_level_json_body = cls(
            token=token,
            support_level=support_level,
        )

        post_asset_id_support_level_json_body.additional_properties = d
        return post_asset_id_support_level_json_body

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
