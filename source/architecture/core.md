# Architecture of the eduTAP Core

todo:
- what does the core contain/do?
- which components are in the core
- how do they communicate, where are the boundaries?
- ...

The eduTAP Core is a collection of components to create, issue, and manage passes.

It provides generic components to be used and installed at the :term:`HEIs`, but does not contain parts specific to the software and databases used at the institutions. Latter are part of the eduTAP :term:`MaSAs`.

It contains the following main components:

- Libraries to communicate with the vendor-specific wallet APIs, like with Google, Apple, or :term:`HCE` systems like NXP, Legic and HID. In the future, other wallet providers are planned to be supported.
- An abstract vendor-neutral library to support all libraries above on a simplified level by providing a unified API.
- A scalable event-based system to distribute data emitted by wallet actions.
- a callback handler to proxy events emitted by the wallet provider to the eduTAP system.
  The events are emitted if a pass is saved or deleted in the :term:`holder's wallet`.
- Front ends to manage and issue passes:
  - A "Pass Management Portal" to create/ update pass classes (including a generic "Pass Designer") and manage the lifecycle of pass objects,
  - A white label "Pass User Portal" (web and kiosk modes) to apply for passes and manage their passes.
    It can be configured to define which :term:`pass classes` are to be managed.

```{todo}
UML component diagram
```

## Wallet specific APIs

...

## Abstract Library

## Event system

## Callback handlers

## Front ends

### Pass Management Portal

### Pass User Portal