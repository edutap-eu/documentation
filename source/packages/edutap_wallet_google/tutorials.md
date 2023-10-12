# Tutorials

We prepared four tutorials to get you started with the Google Wallet API.

Before starting, follow the [installation and configuration instructions](installation.md).

## Create a pass and load it into the Google Wallet

In this tutorial you will
- create a Wallet Class (a template),
- a Wallet Object (the pass) based on the Wallet Class and
- create a save link to download the pass to the Google Wallet form your mobile device.

We start with a simple example, a generic pass with a title and a header.

At first we create the most simple Wallet Class.

```python
from edutap.wallet_google import api

import os

# if you run the code more than once, you need to change the ID of the class,
# like by incrementing the number part.
class_id = f"{os.environ.get('EDUTAP_WALLET_GOOGLE_ISSUER_ID')}.exampleclass01.edutap_example"

new_class = api.create(
    "GenericClass",
    {
        # ids are always consisting of the issuer id as a prefix followed
        # by a custom postfix, delimited by a dot.
        "id": class_id,
    },
)
```

Now we create a simple Wallet Object based on the freshly created class.

```python

# if you run the code more than once, you need to change the ID of the object,
# like by incrementing the number part.
object_id = f"{os.environ.get('EDUTAP_WALLET_GOOGLE_ISSUER_ID')}.exampleobject01.edutap_example"

new_object = api.create(
    "GenericObject",
    {
        "id": object_id,
        "classId": class_id",
        "cardTitle": {
            "defaultValue": {
                "language": "en",
                "value": "Edutap Example Pass 01"
            },
            "translatedValues": []
        },
        "header": {
            "defaultValue": {
                "language": "en",
                "value": "This is an example pass from the edutap tutorial."
            },
            "translatedValues": []
        },
        "state": "ACTIVE"
    },
)
```

Now the pass is ready for download.
To create a linkt to download the pass, we need to provide the ID of the pass and the origin of the download.

```python
print(
    api.save_link(
        {"genericObjects": [{"id": object_id}]},
        origins=["www.example.com"],
    )
)
```

This prints a link, which can be opened on a mobile device to download the pass to the Google Wallet.
It can be opened in the desktop browser too, given you are logged in with the same Google account as on your mobile device.


## Update a pass

## Send a notification to a pass

## Disable a pass

