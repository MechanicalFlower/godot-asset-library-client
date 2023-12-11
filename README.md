<div align="center">

# `🐦 godot-asset-library-client`

![Python Version](https://img.shields.io/badge/python-3.90%20|%203.10%20|%203.110%20|%203.12-0a7bbc?logo=python&logoColor=white)
![license](https://img.shields.io/badge/license-MIT-green?logo=open-source-initiative&logoColor=white)
[![standard-readme compliant](https://img.shields.io/badge/readme-standard-brightgreen.svg?logo=readme&logoColor=white)](https://github.com/RichardLitt/standard-readme)

<!-- ![PyPI - Package Version](https://img.shields.io/pypi/v/godot-asset-library-client?logo=pypi&logoColor=white) -->

[![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json)](https://github.com/charliermarsh/ruff)
[![format - black](https://img.shields.io/badge/format-black-000000.svg)](https://github.com/psf/black)
[![types - mypy](https://img.shields.io/badge/types-mypy-blue.svg)](https://github.com/python/mypy)

A client library for accessing Godot Asset Library.

</div>

## Usage

First, create a client:

```python
from godot_asset_library_client import Client

client = Client(base_url="https://api.example.com")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from godot_asset_library_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from godot_asset_library_client.models import MyDataModel
from godot_asset_library_client.api.my_tag import get_my_data_model
from godot_asset_library_client.types import Response

with client as client:
    my_data: MyDataModel = get_my_data_model.sync(client=client)
    # or if you need more info (e.g. status_code)
    response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from godot_asset_library_client.models import MyDataModel
from godot_asset_library_client.api.my_tag import get_my_data_model
from godot_asset_library_client.types import Response

async with client as client:
    my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
    response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl=False
)
```

## Contributing

![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)

We welcome community contributions to this project.

Please read our [Contributor Guide](CONTRIBUTING.md) for more information on how to get started.
