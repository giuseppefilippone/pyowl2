# Summary

Defines a class representing an OWL axiom that asserts a collection of object properties are mutually exclusive and cannot relate the same pair of individuals.

## Description

It models the semantic constraint where specific relationship types within an ontology cannot overlap, ensuring that if one property links two individuals, no other property in the defined set can link the same pair. The implementation enforces a canonical internal representation by automatically sorting the provided list of property expressions, which simplifies comparison and structural consistency regardless of the input order. Validation logic ensures that at least two property expressions are supplied during initialization, as disjointness is a relationship that requires multiple entities to be meaningful. Inheritance from the base object property axiom class allows for the attachment of optional annotations, providing a mechanism to add metadata or contextual information to the logical constraint.
