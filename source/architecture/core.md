# Architecture of the eduTAP Core

The eduTAP Core is a collection of components to create, issue, and manage passes.

It provides generic components to be used and installed at the {term}`HEIs<HEI>`, but does not contain parts specific to the software and databases used at the institutions. Latter are part of the eduTAP {term}`MaSAs<MaSA>`.

It contains the following main components:

- Libraries to communicate with the vendor-specific wallet APIs, like with Google, Apple, or {term}`HCE` systems like NXP, Legic and HID. In the future, other wallet providers are planned to be supported.
- An abstract vendor-neutral library to support all libraries above on a simplified level by providing a unified API.
- A scalable event-based system to distribute data emitted by wallet actions.
- a callback handler to proxy events emitted by the wallet provider to the eduTAP system.
  The events are emitted if a pass is saved or deleted in the holder's {term}`wallet`.
- Front ends to manage and issue passes:
  - A "Pass Management Portal" to create/ update pass classes (including a generic "Pass Designer") and manage the lifecycle of pass objects,
  - A white label "Pass User Portal" (web and kiosk modes) to apply for passes and manage their passes.
    It can be configured to define which {term}`pass classes <pass class>` are to be managed.

```{todo}
UML component diagram
```

## Wallet specific API Libraries

A set of libraries to be used by developers writing management software for passes to interact with the specific vendors REST APIs.

In eduTAP the APIs are meant to be used by the Pass Management Portal and the Pass User Portal.

It is planned to support the following vendors

- Apple
- Google
- HCE vendors (NXP, Legic, HID)
- EUDI Wallet
- Open Wallet Foundation

```{todo}
Add Links to the vendors wallet pages
```

```{todo}
Distinguish between the Wallet Apps, the Wallet Pass APIs and the HCE/ OEM passes. Refine the section above. We may need an own section explaining the universe we are addressing here.
```

At first, we will implement APIs for Google and Apple. The next part focuses on this.

For both, pass objects and pass classes the API provides the following functionality:
- create,
- read,
- update,
- notify (messaging)
- manage the state (lifecycle),
- list (with basic filters).

There are predefined, vendor-specific stereotypes of pass classes (access, payment, transit, health, ...)

```{todo}
Define term stereotype - but not as glossary term only, better at own or at a concept page!
What is the difference to a pass type?
```

## Abstract Wallet Library



## Event system

## Callback handlers

## Front ends

### Pass Management Portal

### Pass User Portal