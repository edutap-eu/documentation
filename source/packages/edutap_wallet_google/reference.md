# Reference

## API Functions

Most tasks are done by import and using the sole `api` module:

```python
from edutap.wallet_google import api
```

To tell the API functions what kind of item to deal with, the first parameter is the registered name of the model (except for `save_link`).
Models can be the different top-level wallet-classes or -objects, but also issuers, permissions and such (see section models below).

```{eval-rst}
.. currentmodule:: edutap.wallet_google.api


.. autosummary::
   :toctree: _autosummary

   create
   read
   update
   disable
   message
   listing
   save_link
```

## Models

### Top Level Models

```{eval-rst}

.. rubric:: Generic

`edutap.wallet_google.models.generic`

.. currentmodule:: edutap.wallet_google.models.generic

.. autosummary::
   :toctree: _autosummary

   GenericClass
   GenericObject


.. rubric:: Retail

`edutap.wallet_google.models.retail`

.. currentmodule:: edutap.wallet_google.models.retail

.. autosummary::
   :toctree: _autosummary

   GiftCardClass
   GiftCardObject
   LoyaltyClass
   LoyaltyObject
   OfferClass
   OfferObject

.. rubric:: Ticket and Transit

`edutap.wallet_google.models.tickets_and_transit`

.. currentmodule:: edutap.wallet_google.models.tickets_and_transit

.. autosummary::
   :toctree: _autosummary

   EventTicketClass
   EventTicketObject


.. rubric:: Issuer

`edutap.wallet_google.models.issuer`

.. currentmodule:: edutap.wallet_google.models.issuer

.. autosummary::
   :toctree: _autosummary

   Issuer
   Permissions
   SmartTap

.. rubric:: JWT

`edutap.wallet_google.models.jwt`

.. currentmodule:: edutap.wallet_google.models.jwt

.. autosummary::
   :toctree: _autosummary

   JwtResource
   JwtResponse
   Resources

```

### Data-Types

```{eval-rst}

.. currentmodule:: edutap.wallet_google.models.retail

.. rubric:: Retail

`edutap.wallet_google.models.retail`

.. autosummary::
   :toctree: _autosummary

   LoyaltyPointsBalance
   LoyaltyPoints

.. rubric:: Ticket and Transit

`edutap.wallet_google.models.tickets_and_transit`

.. currentmodule:: edutap.wallet_google.models.tickets_and_transit

.. autosummary::
   :toctree: _autosummary

   EventSeat
   EventReservationInfo

.. rubric:: Primitives: Enumerations

`edutap.wallet_google.models.primitives.enums`

.. currentmodule:: edutap.wallet_google.models.primitives.enums

.. autosummary::
   :toctree: _autosummary

   Action
   AnimationType
   BarcodeRenderEncoding
   BarcodeType
   ConfirmationCodeLabel
   DateFormat
   DoorsOpenLabel
   GateLabel
   GenericType
   MessageType
   MultipleDevicesAndHoldersAllowedStatus
   NfcConstraint
   PredefinedItem
   RedemptionChannel
   ReviewStatus
   Role
   RowLabel
   ScreenshotEligibility
   SeatLabel
   SectionLabel
   SharedDataType
   State
   RetailState
   TotpAlgorithm
   TransitOption
   ViewUnlockRequirement

.. rubric:: Primitives: Barcode

`edutap.wallet_google.models.primitives.barcode`

.. currentmodule:: edutap.wallet_google.models.primitives.barcode

.. autosummary::
   :toctree: _autosummary

   Barcode
   TotpParameters
   TotpDetails
   RotatingBarcode

.. rubric:: Primitives: Class Template Info

`edutap.wallet_google.models.primitives.class_template_info`

.. currentmodule:: edutap.wallet_google.models.primitives.class_template_info

.. autosummary::
   :toctree: _autosummary

   FieldReference
   FieldSelector
   TemplateItem
   BarcodeSectionDetail
   CardBarcodeSectionDetails
   CardRowOneItem
   CardRowTwoItems
   CardRowThreeItems
   CardRowTemplateInfo
   CardTemplateOverride
   DetailsItemInfo
   DetailsTemplateOverride
   FirstRowOption
   ListTemplateOverride
   ClassTemplateInfo


.. rubric:: Primitives: Data

`edutap.wallet_google.models.primitives.data`

.. currentmodule:: edutap.wallet_google.models.primitives.data

.. autosummary::
   :toctree: _autosummary

   TextModuleData
   LabelValue
   LabelValueRow
   LinksModuleData
   ImageModuleData
   InfoModuleData
   AppTarget
   AppLinkInfo
   AppLinkData

.. rubric:: Primitives: Datetime

`edutap.wallet_google.models.primitives.datetime`

.. currentmodule:: edutap.wallet_google.models.primitives.datetime

.. autosummary::
   :toctree: _autosummary

   DateTime
   EventDateTime
   TimeInterval

.. rubric:: Primitives: Localized String

`edutap.wallet_google.models.primitives.localized_string`

.. currentmodule:: edutap.wallet_google.models.primitives.localized_string

.. autosummary::
   :toctree: _autosummary

   TranslatedString
   LocalizedString

.. rubric:: Primitives: Location

`edutap.wallet_google.models.primitives.location`

.. currentmodule:: edutap.wallet_google.models.primitives.location

.. autosummary::
   :toctree: _autosummary

   LatLongPoint
   EventVenue

.. rubric:: Primitives: Money

`edutap.wallet_google.models.primitives.money`

.. currentmodule:: edutap.wallet_google.models.primitives.money

.. autosummary::
   :toctree: _autosummary

   Money

.. rubric:: Primitives: Notification

`edutap.wallet_google.models.primitives.notification`

.. currentmodule:: edutap.wallet_google.models.primitives.notification

.. autosummary::
   :toctree: _autosummary

   ExpiryNotification
   UpcomingNotification
   Notifications
   Message
   AddMessageRequest

.. rubric:: Primitives: Retail

`edutap.wallet_google.models.primitives.retail`

.. currentmodule:: edutap.wallet_google.models.primitives.retail

.. autosummary::
   :toctree: _autosummary

   DiscoverableProgramMerchantSignupInfo
   DiscoverableProgramMerchantSigninInfo
   DiscoverableProgram

.. rubric:: Primitives: Reviews

`edutap.wallet_google.models.primitives.review`

.. currentmodule:: edutap.wallet_google.models.primitives.review

.. autosummary::
   :toctree: _autosummary

   Review

.. rubric:: Primitives: Smarttap

`edutap.wallet_google.models.primitives.smarttap`

.. currentmodule:: edutap.wallet_google.models.primitives.smarttap

.. autosummary::
   :toctree: _autosummary

   Permission
   AuthenticationKey
   SignUpInfo
   IssuerToUserInfo
   IssuerContactInfo
   SmartTapMerchantData

```