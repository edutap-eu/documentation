# Architecture of the Service Directory

The Service Directory is a central (one for all organizations), web-based system to announce services (like a library, canteen, and lab access) on {term}`HEIs<HEI>` or related organizations to a central directory and provide {term}`tappers<tapper>` a UI to find services they are interested in.

## Parts

It consists of

1. a central management system for organizations to announce a tapper {term}`service`,
1. a central search portal to find services and information on how to get digital passes to access these services.
   It provides a REST API to include the directory entries in the local portals of the organizations if needed.
   Alternatively, it provides the possibility to configure micro search portals for organizations without resources to integrate with their portal, with some customization features (simple style and logo overrides).

# Considerations

We need a central management system with fine-grained access control in the style of a modern CMS. It stores the data in a classical database.

Additional collected data is then provided to a modern, scalable search index (like ElastichSearch, Typesense, ...).

The search portal is a separate, modern web application. It uses the index data to provide the information to the tapper.

While the central management system does not need to scale much, the tapper search portal and the index servers do need to be able to scale massively.

# Use case


```{figure} uml/service-dir.png
:alt: Use case diagram for service directory.

Service Directory.

```