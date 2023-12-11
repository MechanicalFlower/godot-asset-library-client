from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category import Category
from ...models.get_configure_type import GetConfigureType
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type: Union[Unset, None, GetConfigureType] = GetConfigureType.ANY,
    session: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["session"] = session

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/configure",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Category, ValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Category.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Category, ValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, GetConfigureType] = GetConfigureType.ANY,
    session: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Category, ValidationError]]:
    """Fetch categories

     Returns category names and IDs (used for editor integration).

    Args:
        type (Union[Unset, None, GetConfigureType]):  Default: GetConfigureType.ANY.
        session (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Category, ValidationError]]
    """

    kwargs = _get_kwargs(
        type=type,
        session=session,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, GetConfigureType] = GetConfigureType.ANY,
    session: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Category, ValidationError]]:
    """Fetch categories

     Returns category names and IDs (used for editor integration).

    Args:
        type (Union[Unset, None, GetConfigureType]):  Default: GetConfigureType.ANY.
        session (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Category, ValidationError]
    """

    return sync_detailed(
        client=client,
        type=type,
        session=session,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, GetConfigureType] = GetConfigureType.ANY,
    session: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Category, ValidationError]]:
    """Fetch categories

     Returns category names and IDs (used for editor integration).

    Args:
        type (Union[Unset, None, GetConfigureType]):  Default: GetConfigureType.ANY.
        session (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Category, ValidationError]]
    """

    kwargs = _get_kwargs(
        type=type,
        session=session,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, GetConfigureType] = GetConfigureType.ANY,
    session: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Category, ValidationError]]:
    """Fetch categories

     Returns category names and IDs (used for editor integration).

    Args:
        type (Union[Unset, None, GetConfigureType]):  Default: GetConfigureType.ANY.
        session (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Category, ValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            type=type,
            session=session,
        )
    ).parsed
