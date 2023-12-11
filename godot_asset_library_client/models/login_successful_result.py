from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginSuccessfulResult")


@_attrs_define
class LoginSuccessfulResult:
    """
    Attributes:
        authenticated (Union[Unset, bool]):
        username (Union[Unset, str]):
        token (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    authenticated: Union[Unset, bool] = UNSET
    username: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authenticated = self.authenticated
        username = self.username
        token = self.token
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authenticated is not UNSET:
            field_dict["authenticated"] = authenticated
        if username is not UNSET:
            field_dict["username"] = username
        if token is not UNSET:
            field_dict["token"] = token
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authenticated = d.pop("authenticated", UNSET)

        username = d.pop("username", UNSET)

        token = d.pop("token", UNSET)

        url = d.pop("url", UNSET)

        login_successful_result = cls(
            authenticated=authenticated,
            username=username,
            token=token,
            url=url,
        )

        login_successful_result.additional_properties = d
        return login_successful_result

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
