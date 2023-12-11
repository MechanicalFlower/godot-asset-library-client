from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_details import EditDetails
from ...types import Response


def _get_kwargs(
    id: str,
) -> Dict[str, Any]:
    return {
        "method": "get",
        "url": "/asset/edit/{id}".format(
            id=id,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[EditDetails]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EditDetails.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[EditDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[EditDetails]:
    """Returns a previously-submitted asset edit

     Returns a previously-submitted asset edit. All fields with null are unchanged, and will stay the
    same as in the original. The previews array is merged from the new and original previews.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditDetails]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[EditDetails]:
    """Returns a previously-submitted asset edit

     Returns a previously-submitted asset edit. All fields with null are unchanged, and will stay the
    same as in the original. The previews array is merged from the new and original previews.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditDetails
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[EditDetails]:
    """Returns a previously-submitted asset edit

     Returns a previously-submitted asset edit. All fields with null are unchanged, and will stay the
    same as in the original. The previews array is merged from the new and original previews.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditDetails]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[EditDetails]:
    """Returns a previously-submitted asset edit

     Returns a previously-submitted asset edit. All fields with null are unchanged, and will stay the
    same as in the original. The previews array is merged from the new and original previews.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditDetails
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
