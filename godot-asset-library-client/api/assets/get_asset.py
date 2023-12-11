from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_asset_sort import GetAssetSort
from ...models.get_asset_support import GetAssetSupport
from ...models.get_asset_type import GetAssetType
from ...models.paginated_asset_list import PaginatedAssetList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type: Union[Unset, None, GetAssetType] = GetAssetType.ANY,
    category: Union[Unset, None, str] = UNSET,
    support: Union[Unset, None, GetAssetSupport] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
    godot_version: Union[Unset, None, str] = UNSET,
    max_results: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, GetAssetSort] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["category"] = category

    json_support: Union[Unset, None, str] = UNSET
    if not isinstance(support, Unset):
        json_support = support.value if support else None

    params["support"] = json_support

    params["filter"] = filter_

    params["user"] = user

    params["godot_version"] = godot_version

    params["max_results"] = max_results

    params["page"] = page

    params["offset"] = offset

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params["reverse"] = reverse

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/asset",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedAssetList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedAssetList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedAssetList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, GetAssetType] = GetAssetType.ANY,
    category: Union[Unset, None, str] = UNSET,
    support: Union[Unset, None, GetAssetSupport] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
    godot_version: Union[Unset, None, str] = UNSET,
    max_results: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, GetAssetSort] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
) -> Response[PaginatedAssetList]:
    """List assets

     Return a paginated list of assets.

    Args:
        type (Union[Unset, None, GetAssetType]):  Default: GetAssetType.ANY.
        category (Union[Unset, None, str]):
        support (Union[Unset, None, GetAssetSupport]):
        filter_ (Union[Unset, None, str]):
        user (Union[Unset, None, str]):
        godot_version (Union[Unset, None, str]):
        max_results (Union[Unset, None, str]):
        page (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        sort (Union[Unset, None, GetAssetSort]):
        reverse (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAssetList]
    """

    kwargs = _get_kwargs(
        type=type,
        category=category,
        support=support,
        filter_=filter_,
        user=user,
        godot_version=godot_version,
        max_results=max_results,
        page=page,
        offset=offset,
        sort=sort,
        reverse=reverse,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, GetAssetType] = GetAssetType.ANY,
    category: Union[Unset, None, str] = UNSET,
    support: Union[Unset, None, GetAssetSupport] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
    godot_version: Union[Unset, None, str] = UNSET,
    max_results: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, GetAssetSort] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
) -> Optional[PaginatedAssetList]:
    """List assets

     Return a paginated list of assets.

    Args:
        type (Union[Unset, None, GetAssetType]):  Default: GetAssetType.ANY.
        category (Union[Unset, None, str]):
        support (Union[Unset, None, GetAssetSupport]):
        filter_ (Union[Unset, None, str]):
        user (Union[Unset, None, str]):
        godot_version (Union[Unset, None, str]):
        max_results (Union[Unset, None, str]):
        page (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        sort (Union[Unset, None, GetAssetSort]):
        reverse (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAssetList
    """

    return sync_detailed(
        client=client,
        type=type,
        category=category,
        support=support,
        filter_=filter_,
        user=user,
        godot_version=godot_version,
        max_results=max_results,
        page=page,
        offset=offset,
        sort=sort,
        reverse=reverse,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, GetAssetType] = GetAssetType.ANY,
    category: Union[Unset, None, str] = UNSET,
    support: Union[Unset, None, GetAssetSupport] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
    godot_version: Union[Unset, None, str] = UNSET,
    max_results: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, GetAssetSort] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
) -> Response[PaginatedAssetList]:
    """List assets

     Return a paginated list of assets.

    Args:
        type (Union[Unset, None, GetAssetType]):  Default: GetAssetType.ANY.
        category (Union[Unset, None, str]):
        support (Union[Unset, None, GetAssetSupport]):
        filter_ (Union[Unset, None, str]):
        user (Union[Unset, None, str]):
        godot_version (Union[Unset, None, str]):
        max_results (Union[Unset, None, str]):
        page (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        sort (Union[Unset, None, GetAssetSort]):
        reverse (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAssetList]
    """

    kwargs = _get_kwargs(
        type=type,
        category=category,
        support=support,
        filter_=filter_,
        user=user,
        godot_version=godot_version,
        max_results=max_results,
        page=page,
        offset=offset,
        sort=sort,
        reverse=reverse,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, GetAssetType] = GetAssetType.ANY,
    category: Union[Unset, None, str] = UNSET,
    support: Union[Unset, None, GetAssetSupport] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
    godot_version: Union[Unset, None, str] = UNSET,
    max_results: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, GetAssetSort] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
) -> Optional[PaginatedAssetList]:
    """List assets

     Return a paginated list of assets.

    Args:
        type (Union[Unset, None, GetAssetType]):  Default: GetAssetType.ANY.
        category (Union[Unset, None, str]):
        support (Union[Unset, None, GetAssetSupport]):
        filter_ (Union[Unset, None, str]):
        user (Union[Unset, None, str]):
        godot_version (Union[Unset, None, str]):
        max_results (Union[Unset, None, str]):
        page (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        sort (Union[Unset, None, GetAssetSort]):
        reverse (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAssetList
    """

    return (
        await asyncio_detailed(
            client=client,
            type=type,
            category=category,
            support=support,
            filter_=filter_,
            user=user,
            godot_version=godot_version,
            max_results=max_results,
            page=page,
            offset=offset,
            sort=sort,
            reverse=reverse,
        )
    ).parsed
