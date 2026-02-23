# Summary

Defines a class representing an OWL object property restriction that constrains an individual to have exactly a specific number of relationships.

## Description

It models the semantic concept of exact cardinality within an ontology, ensuring that an individual is linked to a precise count of other individuals via a defined object property. The implementation supports both qualified and unqualified restrictions by allowing an optional class expression filler, which specifies the type of the related individuals or defaults to any type if omitted. Internal state management relies on properties to encapsulate the cardinality value, the property expression, and the optional class expression, with the constructor enforcing a precondition that the cardinality must be a non-negative integer. A string representation method generates human-readable output in functional syntax, dynamically adjusting the format based on whether the restriction is qualified. By inheriting from a base class expression, this component integrates into a broader framework for constructing and manipulating complex ontology structures.
