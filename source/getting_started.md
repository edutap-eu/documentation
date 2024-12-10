# Using the wallet packages

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

```python
# Create empty wallet class or object by registered name.
# The names are aquivalent to the names used in the google wallet documentation.
model = api.new(name=...)
```

```python
# Create wallet class or object by registered name and JSON serializable dictionary.
model = api.new(name=..., data={...})
```

### Create wallet object

#### Case 1

Create wallet object on google server and return save link with reference to it.

```python
# Create wallet object model from supported data, no request is made yet.
wallet_object_model = api.new(name="GenericObject", data={...})

# Sends a request to Google API, a pass gets created on google servers,
# not in the wallet yet.
api.create(wallet_object_model)

# Create payload needed for generating a save link for our created pass.
wallet_object_with_class_reference = api.new(
    name="GoogleWalletObjectWithClassReference",
    data={
        "classReference": wallet_object_model.id
    }
)

# Create URL for adding the pass to a wallet. This link needs to get delivered
# to the tapper.
add_to_wallet_url = api.save_link({
    "genericObjects": [
        wallet_object_with_class_reference
    ]
})
```

#### Case 2

Create URL for adding the pass to a wallet.
No wallet object get created in the first place.
The pass data is contained in the link aka self contained link.

```python
wallet_object_model = api.new(name="GenericObject", data={...})

add_to_wallet_url = api.save_link({
    "genericObjects": [
        wallet_object_model
    ]
})
```

### Update wallet object

```python
# Create wallet object model.
# The pass ID of the wallet object to update must be set.
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

```python
# Create empty pass.
model = api.new()
```

```python
# Create pass from JSON serializable dictionary.
model = api.new(data={...})
```

```python
# Create pass from pkpass file.
with open('...', 'rb') as pkpass_file:
    model = api.new(file=pkpass_file)
```

### Create save link

Apple wallet follows a link where the device downloads the actual pass data.
This link must be created via the `api` and delivered to the tapper in some way.

```python
# Create a secure link
identifier = "some-unique-identifier"
add_to_wallet_url = api.save_link(identifier)
```

### Create pass

```python
# Create pass model and set it's data.
pass_model = api.new(data{...})

# Verify pass model.
api.verify(pass_model)

# Sign pass model. Now the pass model is immutable.
api.sign(pass_model)

# Create pkpass file from pass model.
with api.pkpass(pass_model) as pkpass_file:
    ...
```

### Update pass

A pass update is technically the same thing as a create.
If the initially created pkpass file was persisted, it can be reused.

```python
# Create pass from pkpass file.
with open('...', 'rb') as pkpass_file:
    pass_model = api.new(file=pkpass_file)

# Update pass model data here.

# Verify, sign and create pkpass file.
api.verify(pass_model)
api.sign(pass_model)
with api.pkpass(pass_model) as pkpass_file:
    ...
```
