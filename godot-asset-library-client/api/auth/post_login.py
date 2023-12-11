from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.login_forbidden_result import LoginForbiddenResult
from ...models.login_successful_result import LoginSuccessfulResult
from ...models.username_password import UsernamePassword
from ...types import Response


def _get_kwargs(
    *,
    json_body: UsernamePassword,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/login",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, LoginForbiddenResult, LoginSuccessfulResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LoginSuccessfulResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = LoginForbiddenResult.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, LoginForbiddenResult, LoginSuccessfulResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: UsernamePassword,
) -> Response[Union[Error, LoginForbiddenResult, LoginSuccessfulResult]]:
    """Login as a given user

     Login as a given user. Results in a token which can be used for authenticated requests.

    Args:
        json_body (UsernamePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LoginForbiddenResult, LoginSuccessfulResult]]
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
    json_body: UsernamePassword,
) -> Optional[Union[Error, LoginForbiddenResult, LoginSuccessfulResult]]:
    """Login as a given user

     Login as a given user. Results in a token which can be used for authenticated requests.

    Args:
        json_body (UsernamePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LoginForbiddenResult, LoginSuccessfulResult]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: UsernamePassword,
) -> Response[Union[Error, LoginForbiddenResult, LoginSuccessfulResult]]:
    """Login as a given user

     Login as a given user. Results in a token which can be used for authenticated requests.

    Args:
        json_body (UsernamePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LoginForbiddenResult, LoginSuccessfulResult]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: UsernamePassword,
) -> Optional[Union[Error, LoginForbiddenResult, LoginSuccessfulResult]]:
    """Login as a given user

     Login as a given user. Results in a token which can be used for authenticated requests.

    Args:
        json_body (UsernamePassword):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LoginForbiddenResult, LoginSuccessfulResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
