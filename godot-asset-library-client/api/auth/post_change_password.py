from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_password import ChangePassword
from ...models.change_pwd_successful_result import ChangePwdSuccessfulResult
from ...types import Response


def _get_kwargs(
    *,
    json_body: ChangePassword,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/change_password",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ChangePwdSuccessfulResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ChangePwdSuccessfulResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ChangePwdSuccessfulResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ChangePassword,
) -> Response[ChangePwdSuccessfulResult]:
    """Change a user's password

     Change a user's password. The token is invalidated in the process.

    Args:
        json_body (ChangePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangePwdSuccessfulResult]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ChangePassword,
) -> Optional[ChangePwdSuccessfulResult]:
    """Change a user's password

     Change a user's password. The token is invalidated in the process.

    Args:
        json_body (ChangePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangePwdSuccessfulResult
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ChangePassword,
) -> Response[ChangePwdSuccessfulResult]:
    """Change a user's password

     Change a user's password. The token is invalidated in the process.

    Args:
        json_body (ChangePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangePwdSuccessfulResult]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ChangePassword,
) -> Optional[ChangePwdSuccessfulResult]:
    """Change a user's password

     Change a user's password. The token is invalidated in the process.

    Args:
        json_body (ChangePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangePwdSuccessfulResult
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
