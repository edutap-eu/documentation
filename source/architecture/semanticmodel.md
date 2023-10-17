# Semantic Pass Models

Here we provide semantic pass models primarily vendor-neutral.
There is no direct one-to-one mapping from semantic pass models to vendor-specific pass models, beecause of differences between different vendors with their proprietary pass models.

[mapping between existing vendor pass models](https://notificare.com/blog/2023/02/17/how-to-create-digital-passes-for-all/)

[google pass converter](https://github.com/google-wallet/pass-converter)

Important: these semantic pass models are from user-centric view and not technical aspect.

We shall provide:

- registry of pass models
- base classes for semantic pass models
- declarative definition of pass models
- transformation engine from semantic model to vendor-specific pass models, where the trafos are defined declaratively
    - trafos concern json data and file data

Terminology: 

[google terminology](https://developers.google.com/wallet/generic/resources/terminology)

- Pass Schema: 
   - contains the information which fields have to or can be provided for a concrete pass template
   - contains the transformation specification for the different target platforms
   - validation information
- Pass Definition: 
   contains the data definition for a specific pass e.g. LMU Library Pass, but still vendor independent.

- ModelEngine(TraraTrara)
   based on the transformation definition given in the Pass Schema, the ModelEngine transforms the Pass Template into a vendor specific pass model and validates.

Vendor specific:

- Google
    - Pass Class
    - Pass Object
- Apple
    - Pass

    the differentiation into Pass Class and Pass Object is not relevant since Apple contains only passes
    stored in a .pkpass file which is a .zip file containing certificates and a manifest to make it manipulation-safe.
    Internally we split it into 
    - Pass Template
        a pass definition that can be used to create a pass object by copy&modify
    - Pass 
        a pass object that can be used to create a .pkpass file and be sent to the user

- 
```{figure} SemanticPassModel.svg
:alt: semantic pass model and transformation to vendor specific passes.

Core Overview.
```


