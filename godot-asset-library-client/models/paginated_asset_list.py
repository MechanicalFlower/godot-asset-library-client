from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_summary import AssetSummary


T = TypeVar("T", bound="PaginatedAssetList")


@_attrs_define
class PaginatedAssetList:
    """A paginated list of assets.

    Attributes:
        page (Union[Unset, int]): The requested page string.
        page_length (Union[Unset, int]): The requested page length.<br> **Note:** This can be higher than the total
            amount of items returned.
        pages (Union[Unset, int]): The total string of pages available.<br> **Note:** If requesting a page higher than
            this value, a successful response will be returned (status code 200) but no items will be listed.
        total_items (Union[Unset, int]): The total string of items available.
        result (Union[Unset, List['AssetSummary']]):
    """

    page: Union[Unset, int] = UNSET
    page_length: Union[Unset, int] = UNSET
    pages: Union[Unset, int] = UNSET
    total_items: Union[Unset, int] = UNSET
    result: Union[Unset, List["AssetSummary"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page = self.page
        page_length = self.page_length
        pages = self.pages
        total_items = self.total_items
        result: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.result, Unset):
            result = []
            for result_item_data in self.result:
                result_item = result_item_data.to_dict()

                result.append(result_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if page_length is not UNSET:
            field_dict["page_length"] = page_length
        if pages is not UNSET:
            field_dict["pages"] = pages
        if total_items is not UNSET:
            field_dict["total_items"] = total_items
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_summary import AssetSummary

        d = src_dict.copy()
        page = d.pop("page", UNSET)

        page_length = d.pop("page_length", UNSET)

        pages = d.pop("pages", UNSET)

        total_items = d.pop("total_items", UNSET)

        result = []
        _result = d.pop("result", UNSET)
        for result_item_data in _result or []:
            result_item = AssetSummary.from_dict(result_item_data)

            result.append(result_item)

        paginated_asset_list = cls(
            page=page,
            page_length=page_length,
            pages=pages,
            total_items=total_items,
            result=result,
        )

        paginated_asset_list.additional_properties = d
        return paginated_asset_list

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
