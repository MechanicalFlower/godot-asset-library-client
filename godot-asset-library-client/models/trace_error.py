from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceError")


@_attrs_define
class TraceError:
    """
    Attributes:
        file (Union[Unset, str]):
        line (Union[Unset, str]):
        function (Union[Unset, str]):
        class_ (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    file: Union[Unset, str] = UNSET
    line: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file = self.file
        line = self.line
        function = self.function
        class_ = self.class_
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if line is not UNSET:
            field_dict["line"] = line
        if function is not UNSET:
            field_dict["function"] = function
        if class_ is not UNSET:
            field_dict["class"] = class_
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = d.pop("file", UNSET)

        line = d.pop("line", UNSET)

        function = d.pop("function", UNSET)

        class_ = d.pop("class", UNSET)

        type = d.pop("type", UNSET)

        trace_error = cls(
            file=file,
            line=line,
            function=function,
            class_=class_,
            type=type,
        )

        trace_error.additional_properties = d
        return trace_error

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
