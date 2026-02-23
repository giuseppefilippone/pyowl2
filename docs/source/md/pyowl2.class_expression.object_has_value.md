# Summary

Implements a class representing an OWL object property restriction that constrains individuals to be related to a specific named individual via a particular property.

## Description

The implementation models the OWL "ObjectHasValue" restriction, which is used to define a class of individuals that must be associated with a specific, named individual through a defined object property. By accepting an object property expression and a target individual during initialization, the logic allows for the creation of complex class expressions that assert exact value constraints within an ontology. State management is handled through property accessors that permit the retrieval and modification of both the relationship property and the specific individual value, ensuring the restriction can be dynamically updated. A string representation method is provided to generate a human-readable format of the restriction, which is useful for debugging and logging the logical structure of the ontology components.
