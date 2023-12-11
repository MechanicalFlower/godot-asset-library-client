from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_asset_id_support_level_json_body import PostAssetIdSupportLevelJsonBody
from ...models.successful_asset_operation import SuccessfulAssetOperation
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    json_body: PostAssetIdSupportLevelJsonBody,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/asset/{id}/support_level".format(
            id=id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SuccessfulAssetOperation]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessfulAssetOperation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SuccessfulAssetOperation]:
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
    json_body: PostAssetIdSupportLevelJsonBody,
) -> Response[SuccessfulAssetOperation]:
    """Change the support level of an asset

     API used by moderators to change the support level of an asset.

    Args:
        id (str):
        json_body (PostAssetIdSupportLevelJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessfulAssetOperation]
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
    json_body: PostAssetIdSupportLevelJsonBody,
) -> Optional[SuccessfulAssetOperation]:
    """Change the support level of an asset

     API used by moderators to change the support level of an asset.

    Args:
        id (str):
        json_body (PostAssetIdSupportLevelJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessfulAssetOperation
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
    json_body: PostAssetIdSupportLevelJsonBody,
) -> Response[SuccessfulAssetOperation]:
    """Change the support level of an asset

     API used by moderators to change the support level of an asset.

    Args:
        id (str):
        json_body (PostAssetIdSupportLevelJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessfulAssetOperation]
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
    json_body: PostAssetIdSupportLevelJsonBody,
) -> Optional[SuccessfulAssetOperation]:
    """Change the support level of an asset

     API used by moderators to change the support level of an asset.

    Args:
        id (str):
        json_body (PostAssetIdSupportLevelJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessfulAssetOperation
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
