from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_details import AssetDetails
from ...models.post_asset_edit_id_response_200 import (
    PostAssetEditIdResponse200,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    json_body: AssetDetails,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/asset/edit/{id}".format(
            id=id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostAssetEditIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostAssetEditIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostAssetEditIdResponse200]:
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
    json_body: AssetDetails,
) -> Response[PostAssetEditIdResponse200]:
    """Update information about an asset

     Update information about a single asset.

    Args:
        id (str):
        json_body (AssetDetails): A resource provided by the asset library (add-on, project,
            ...).<br>
            These properties are only returned when requesting a specific asset,
            not a list of assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAssetEditIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AssetDetails,
) -> Optional[PostAssetEditIdResponse200]:
    """Update information about an asset

     Update information about a single asset.

    Args:
        id (str):
        json_body (AssetDetails): A resource provided by the asset library (add-on, project,
            ...).<br>
            These properties are only returned when requesting a specific asset,
            not a list of assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAssetEditIdResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AssetDetails,
) -> Response[PostAssetEditIdResponse200]:
    """Update information about an asset

     Update information about a single asset.

    Args:
        id (str):
        json_body (AssetDetails): A resource provided by the asset library (add-on, project,
            ...).<br>
            These properties are only returned when requesting a specific asset,
            not a list of assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAssetEditIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AssetDetails,
) -> Optional[PostAssetEditIdResponse200]:
    """Update information about an asset

     Update information about a single asset.

    Args:
        id (str):
        json_body (AssetDetails): A resource provided by the asset library (add-on, project,
            ...).<br>
            These properties are only returned when requesting a specific asset,
            not a list of assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAssetEditIdResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
