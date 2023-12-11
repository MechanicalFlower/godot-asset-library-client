from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditSummary")


@_attrs_define
class EditSummary:
    """
    Attributes:
        edit_id (Union[Unset, str]):
        status (Union[Unset, str]):
        reason (Union[Unset, str]):
        warning (Union[Unset, str]):
    """

    edit_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    warning: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edit_id = self.edit_id
        status = self.status
        reason = self.reason
        warning = self.warning

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edit_id is not UNSET:
            field_dict["edit_id"] = edit_id
        if status is not UNSET:
            field_dict["status"] = status
        if reason is not UNSET:
            field_dict["reason"] = reason
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        edit_id = d.pop("edit_id", UNSET)

        status = d.pop("status", UNSET)

        reason = d.pop("reason", UNSET)

        warning = d.pop("warning", UNSET)

        edit_summary = cls(
            edit_id=edit_id,
            status=status,
            reason=reason,
            warning=warning,
        )

        edit_summary.additional_properties = d
        return edit_summary

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
