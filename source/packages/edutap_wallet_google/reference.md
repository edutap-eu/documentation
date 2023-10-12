# Reference

## API Documentation

## Overview

Most tasks are done by import and using the sole `api` module:

```python
from edutap.wallet_google import api
```

The `api` module has the functions:

- `api.create`
- `api.read`
- `api.update`
- `api.disable`
- `api.message`
- `api.listing`
- `api.save_link`

To tell the API functions what kind of item to deal with, the first parameter is the registered name of the model (except for `save_link`).

Models can be the different wallet-classes or -objects, but also issuers, permissions and such (see section models below).

## API Functions

```{todo}

Use Sphinx autodoc to document the functions and classes of modules `edutap.wallet_google`.

```

## Models

```{todo}

Create a Sphinx plugin to document the pydantic models of `edutap.wallet_google`.

```

### Top Level Models

### Datatypes and Enums



