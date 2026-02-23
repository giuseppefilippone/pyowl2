# Summary

Implements a data structure representing an OWL axiom that declares two object properties to be inverses of one another.

## Description

The software models a specific type of Web Ontology Language (OWL) axiom used to define reciprocal relationships between two object properties. By storing references to two distinct object property expressions, it establishes a logical constraint where the existence of a relationship defined by the first property implies the existence of a relationship defined by the second property in the opposite direction. This structure allows reasoning systems to infer bidirectional connections between entities, such as linking a "hasParent" property with an "isChildOf" property. In addition to holding the core property expressions, the implementation supports the attachment of metadata annotations and provides a string representation formatted according to OWL functional syntax for serialization or debugging purposes.
