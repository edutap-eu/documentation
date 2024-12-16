# Getting Started using the Wallet Packages

While Google and Apple handle wallet passes entirely different.
The related low level APIs offer a similar look and feel.

In both cases, pass management is done via the contained `api` module.

## Google

Import the api module.

```python
from edutap.wallet_google import api
```

### Wallet models

There are several ways for creating wallet data models.

Create empty wallet class or object by registered name.
The names are aquivalent to the names used in the google wallet documentation.

```python
model = api.new(name=...)
```

Create wallet class or object by registered name and JSON serializable dictionary.

```python
model = api.new(name=..., data={...})
```

### Create wallet object

#### Case 1

Create wallet object on google server and return save link with reference to it.

Create wallet object model from supported data, no request is made yet.

```python
wallet_object_model = api.new(name="GenericObject", data={...})
```

Sends a request to Google API, a pass gets created on google servers, not in the wallet yet.

```python
api.create(wallet_object_model)
```

Create payload needed for generating a save link for our created pass.

```python
wallet_object_with_class_reference = api.new(
    name="Reference",
    data={
        "id": wallet_object_model.id,
        "model_type": type(wallet_object_model)
    }
)
```

Create URL for adding the pass to a wallet. This link needs to get delivered to the {term}`tapper`.

```python
add_to_wallet_url = api.save_link(
    wallet_object_model,
    wallet_object_with_class_reference,
)
```

#### Case 2

Create URL for adding the pass to a wallet.
No wallet object get created in the first place.
The pass data is contained in the link aka self contained link.

```python
wallet_object_model = api.new(name="GenericObject", data={...})

add_to_wallet_url = api.save_link(
    [
        wallet_object_model
    ]
)
```

### Update wallet object

Create wallet object model.
The pass ID of the wallet object to update must be set.

```python
wallet_object_model = api.new(name="GenericObject", data={
    "id": "existing-wallet-object-id",
    ...
})
```

There are 2 different update strategies. Partial or full update.

Perform a full update. The entire wallet object model gets replaced.

```python
api.update(wallet_object_model)
```

Perform a partial update. Only the contained data get modified.

```python
api.update(wallet_object_model, partial=True)
```

## Apple

Import the api module.

```python
from edutap.wallet_apple import api
```

### Pass models

There are several ways for creating pass data models.

Create empty pass.

```python
model = api.new()
```

Create pass from JSON serializable dictionary.

```python
model = api.new(data={...})
```

Create pass from pkpass file.

```python
with open('...', 'rb') as pkpass_file:
    model = api.new(file=pkpass_file)
```

### Create save link

Apple wallet follows a link where the device downloads the actual pass data.
This link must be created via the `api` and delivered to the tapper in some way.

Create a secure link.

```python
identifier = "some-unique-identifier"
add_to_wallet_url = api.save_link(identifier)
```

### Create pass

Create pass model and set it's data.

```python
pass_model = api.new(data{...})
```

Verify pass model.

```python
api.verify(pass_model)
```

Sign pass model. Now the pass model is immutable.

```python
api.sign(pass_model)
```

Create pkpass file from pass model.

```python
with api.pkpass(pass_model) as pkpass_file:
    ...
```

### Update pass

A pass update is technically the same thing as a create.
If the initially created pkpass file was persisted, it can be reused.

Create pass from pkpass file.

```python
with open('...', 'rb') as pkpass_file:
    pass_model = api.new(file=pkpass_file)

# Update pass model data here.
```

Verify, sign and create pkpass file.

```python
api.verify(pass_model)
api.sign(pass_model)
with api.pkpass(pass_model) as pkpass_file:
    ...
```
