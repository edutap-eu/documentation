# Architecture of eduTAP Pass Management

Pass management is the task, of creating and designing passes and then offering those passes to potential users, here called tappers.

There are different types of organizations intended to be using this service:
- HEIs
- Specific service providers like
  - Student unions (cantinas, cafes, vending machines, housing/dorms, ...)
  - Libraries
  - Inter-institutional service providers, like educational sporting facilities

Use cases in the domain of pass management are:

- An admin creates (designs) new and manages existing pass classes.
- A tapper applies for a pass, then
  - manage the application cycle and reject or issue the pass (like for a common ID pass),
  - immediate issuing of a pass (like for a service pass).
- A tapper downloads their passes to their device.
- A tapper manages their passes.
- A manager manages the tappers' passes.
- A manager sends notifications to whole pass classes or a single pass.

```{figure} pass-management.png
:alt: Use case diagram showing the pass management roles and actions.

Pass management use-case.

```
- A *Tapper* is a person who uses the offers of the providers with their smartphone and the passports stored in it using the reader terminal.
- A *Manager* - is a person who has the role of supporting the tapper with applications and passes.
- An *Administrator* is a person who manages pass classes.

The application is divided into two main, but interconnected areas:

1. a back office for administrators and managers.
1. a tapper portal for the holders of passes.

Technically it consists of two web-application backends, each a RESTful API offering the functionality for the task.
The reason is better scalability.
While the back office is used only by a small group of staffers, the tapper portal is accessed by up to several 10 thousand tappers at one organization.
Thus the tapper portal needs the ability to scale horizontally on a different level than the back office.

Each, the back office and the tapper portal, has a management front-end provided as a JS application.

Both are offered as white-label applications with the ability to change the logo or CSS by the organization installing the apps.

Some organizations may decide to integrate the tapper portal part only into their existing portals.
In this case, the RESTFul API alone can be used to fulfill the task.

Both, the back office and tapper portal need a kiosk mode.
A kiosk has an NFC device and offers direct interaction with the tapper's device to also write passes to the phone.
