# Summary

Defines a class representing the inverse of an OWL object property to model reciprocal relationships between individuals.

## Description

The implementation provides a mechanism to express the inverse of a specific object property within an ontology, effectively reversing the direction of the relationship between two individuals. By wrapping an existing property, the logic allows systems to infer reciprocal connections, such as deriving a parent relationship from a child relationship, without requiring explicit assertions for both directions. The design includes methods to verify whether the underlying property corresponds to the universal top or bottom properties, ensuring consistency with OWL semantics. Additionally, the structure supports standard functional syntax output, enabling clear serialization and debugging of the logical constructs.
