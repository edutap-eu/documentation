# Architecture of the eduTAP Core


```{toctree}
---
maxdepth: 2
caption: Contents
---

wallet-specific-api-libraries-and-support-services.md
semantic-pass-api.md
pass-management.md
event-system.md

```

The eduTAP Core is a collection of components to create, issue, and manage passes.

It provides generic components to be used and installed at the {term}`HEIs<HEI>`, but does not contain parts specific to the software and databases used at the institutions. Latter are part of the eduTAP {term}`MaSAs<MaSA>`.

It contains the following main components:

- Libraries to communicate with the vendor-specific wallet APIs, like with Google, Apple, or {term}`HCE` systems like NXP, Legic, and HID. In the future, other wallet providers are planned to be supported.
- An abstract vendor-neutral library to support all libraries above on a simplified level by providing a unified API.
- A scalable event-based system to distribute data emitted by wallet actions.
- a callback handler to proxy events emitted by the Google wallet provider to the eduTAP system.
  The events are emitted if a pass is saved or deleted in the holder's Google {term}`wallet`.
- an Restful API service to store and retrieve Apple passes and templates. It emits events similar to the Google callback handler.
- Front ends to manage and issue passes:
  - A "Pass Backoffice" to create/ update pass classes (including a generic "Pass Designer") and manage the lifecycle of pass objects,
  - A white label "Tapper Portal" (web and kiosk modes) to apply for passes and manage their passes.
    It can be configured to define which {term}`pass classes <pass class>` are to be managed.


```{figure} ../uml/core.svg
:alt: Component diagram showing architectural overview.

Core Overview.
```