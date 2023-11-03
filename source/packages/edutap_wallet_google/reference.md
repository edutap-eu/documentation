# Reference

## API Documentation

## Overview

Most tasks are done by import and using the sole `api` module:

```python
from edutap.wallet_google import api
```

The `api` module has the functions:

- [`api.create`](#edutap.wallet_google.api.create)
- [`api.read`](#edutap.wallet_google.api.read)
- [`api.update`](#edutap.wallet_google.api.update)
- [`api.disable`](#edutap.wallet_google.api.disable)
- [`api.message`](#edutap.wallet_google.api.message)
- [`api.listing`](#edutap.wallet_google.api.listing)
- [`api.save_link`](#edutap.wallet_google.api.save_link)

To tell the API functions what kind of item to deal with, the first parameter is the registered name of the model (except for `save_link`).

Models can be the different wallet-classes or -objects, but also issuers, permissions and such (see section models below).


## API Functions

```{eval-rst}
.. autofunction:: edutap.wallet_google.api.create
```

```{eval-rst}
.. autofunction:: edutap.wallet_google.api.read
```

```{eval-rst}
.. autofunction:: edutap.wallet_google.api.update
```

```{eval-rst}
.. autofunction:: edutap.wallet_google.api.disable
```

```{eval-rst}
.. autofunction:: edutap.wallet_google.api.message
```

```{eval-rst}
.. autofunction:: edutap.wallet_google.api.listing
```

```{eval-rst}
.. autofunction:: edutap.wallet_google.api.save_link
```

## Models

```{todo}

Create a Sphinx plugin to document the pydantic models of `edutap.wallet_google`.

```

### Top Level Models

### Datatypes and Enums



