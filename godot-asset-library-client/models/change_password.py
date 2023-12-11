from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangePassword")


@_attrs_define
class ChangePassword:
    """
    Attributes:
        token (Union[Unset, str]):
        old_password (Union[Unset, str]):
        new_password (Union[Unset, str]):
    """

    token: Union[Unset, str] = UNSET
    old_password: Union[Unset, str] = UNSET
    new_password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        old_password = self.old_password
        new_password = self.new_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if old_password is not UNSET:
            field_dict["old_password"] = old_password
        if new_password is not UNSET:
            field_dict["new_password"] = new_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        old_password = d.pop("old_password", UNSET)

        new_password = d.pop("new_password", UNSET)

        change_password = cls(
            token=token,
            old_password=old_password,
            new_password=new_password,
        )

        change_password.additional_properties = d
        return change_password

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
