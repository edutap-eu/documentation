# Architecture of the Mandant Specific Applications (MaSAs)

Large parts of eduTAP are meant to be installed at {term}`HEIs<HEI>` or related organizations, the mandants.
The core of eduTAP follows an overall generic approach with pluggability in mind, together with scalability.
Instead of modifications in the core itself, we encourage making use of the different strategies to connect with a variety of existing applications.

We call those short MaSAs (**Ma**ndant **S**pecific **A**pplications).

The main areas to plug in are:

1. providing relevant user data from a directory service ({term}`LDAP`, {term}`AD`, {term}`eDirectory`, ...) to the Pass Management Systems,
1. writing data to the directory service or related storage layers, consumed from the event system,
1. (optional) interacting with the RestAPI of the Pass Management System to integrate the pass management in existing user service portals.

The above tasks need some degree of mandant-specific implementation in code and configuration.
To ease these tasks we plan to offer helpers, like

- libraries bundling common tasks,
- sample applications,
- example interactions with storage layers (like LDAP),
