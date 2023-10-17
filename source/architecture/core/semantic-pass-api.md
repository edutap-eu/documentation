# Architecture of the Semantic Pass API

## Overview

Here we provide semantic pass schemas and possible definitions, primarily vendor-neutral.
There is no direct one-to-one mapping from semantic pass definitions to vendor-specific pass models, because of differences between different vendors with their proprietary pass models.

[mapping between existing vendor pass models](https://notificare.com/blog/2023/02/17/how-to-create-digital-passes-for-all/)

[google pass converter](https://github.com/google-wallet/pass-converter)

```{attention}
These semantic pass models are from user-centric view and not technical aspect.
```

We shall provide:

- registry of pass models
- base classes for semantic pass models
- declarative definition of pass models
- transformation engine from semantic model to vendor-specific pass models, where the transformations are defined declaratively
    - transformations concern json data and file data

## Terminology of Semantic Model and Logic:

### Pass Schema
- contains the information which fields have to or can be provided for a concrete pass template
- contains the transformation specification for the different target platforms
- validation information

### Pass Definition
- contains the data definition for a specific pass e.g. LMU Library Pass, but still vendor independent.

### ModelEngine
- based on the fields and their constraints given in the Pass Schema, the ModelEngine validates the Pass Definition.
- based on the transformation definition given in the Pass Schema, the ModelEngine transforms the Pass Definition into a vendor specific pass models.

### Vendor specific:

This is not part of the sematic model, but the vendor specific packages.
Anyway, we need to know the terminology to be able to map the semantic model to the vendor specific models.

```{hint}
Explanation of the [Google Terminology](https://developers.google.com/wallet/generic/resources/terminology)
```

#### Google
- **Pass Class** like a template of a specific pass domain, i.e. the *LMU Library Cards**.
- **Pass Object** the specific pass of a person, like an instance of the Pass Class, referencing it, downloadable to the wallet on the tappers device.

#### Apple

The differentiation into Pass Class and Pass Object as its done as Google is not relevant.
Apple follows a different approach to habdle passes.
Apple contains only passes stored in a `*.pkpass` file which is a .zip file with checksums and a manifest signed by certificates to make it manipulation-safe.

However, to work efficiently with passes, internally at eduTAP we decided to introduce pass templates to distinguish between them and and passes as well.
We have:

- Pass Template: a pass definition that can be used to create a pass object by copy and modify.
- Pass: a pass object that can be used to create a `*.pkpass` file to be downloaded/ sent to the tapper.

## Sematic Model and Transformation Overview

```{figure} SemanticPassModel.svg
:alt: semantic pass model and transformation to vendor specific passes.

Sematic Model and Transformation Overview
```


