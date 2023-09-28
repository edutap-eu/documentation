# Package `edutap.wallet_google`

## Overview

This package provides a Python API to interact with the Google Wallet Restful API

It contains:

- an API to
   - create,
   - read,
   - update,
   - disable,
   - list
  wallet classes and objects
  and
  - issue passes.
- Pydantic models of the classes, objects, and their (nested) primitives.
- An extensible registry for models of classes and objects.
- A session manager for authorized HTTPS communication with the Google Restful API.

## Installation

The package can be installed using `pip install edutap.wallet_google`.

## Configuration

To authenticate with the Google API, you need to provide a credentials file.
It is expected in the filesystem, readable by the program.
Point the environment variable `EDUTAP_WALLET_GOOGLE_CREDENTIALS_FILE` to its location.

Example:

```bash
export EDUTAP_WALLET_GOOGLE_CREDENTIALS_FILE=/home/example/google_credential_file.json
```

```{todo}

Find the page at Google which describes how to get the file.

```

You also need to know the issuer identifer.

## Usage

All one need to do is to import the `api` module:

```python
from edutap.wallet_google import api
```

The `api`` module has the functions:

- `api.create`
- `api.read`
- `api.update`
- `api.disable`
- `api.message`
- `api.listing`
- `api.save_link`

To tell the API functions what kind of item to deal with, the first parameter is the registered name of the model (except for `save_link`).

Models can be the different wallet-classes or -objects, but also issuers, permissions and such (see section models below).

Here a very basic example
- to create a pass template of type `GenericClass`,
- create a pass of type `GenericObject` using the prior created class and then
- create a save link to download it to the phones wallet:

```python
from edutap.wallet_google import api

# ensure the EDUTAP_WALLET_GOOGLE_CREDENTIALS_FILE environment variable is set!

new_class = api.create(
    "GenericClass",
    {
        # ids are always consisting of the issuer id as a prefix followed
        # by a postfix, delimited by a dot.
        "id": "1234567890123456789.exampleclass01.edutap",
    },
)

new_object = api.create(
    "GenericObject",
    {
        "id": "1234567890123456789.exampleobject01.edutap"
        "classId": "1234567890123456789.exampleclass01.edutap",
        "cardTitle": {
            "defaultValue": {
                "language": "en",
                "value": "Example Pass 01"
            },
            "translatedValues": []
        },
        "header": {
            "defaultValue": {
                "language": "en",
                "value": "This is an example pass."
            },
            "translatedValues": []
        },
        "state": "ACTIVE"
    },
)

new_link = api.save_link(
    {"id": "1234567890123456789.exampleobject01.edutap"},
    origins=["https://example.com"],
)
```

## Models

### Top Level Models

### Datatypes and Enums

```{todo}

Create a Sphinx plugin to document the pydantic models of `edutap.wallet_google`.

```

## API Documentation

```{todo}

Use Sphinx autodoc to document the functions and classes of modules `edutap.wallet_google`.

```

