# Summary

Defines an abstract base class for named OWL ontology elements where identity, ordering, and hashing are derived strictly from string representations.

## Description

The class serves as a structural ancestor for various components within an OWL ontology, such as classes, object properties, and individuals, ensuring they share a common interface and cannot be instantiated directly. A central design choice dictates that the identity and ordering of these components are determined exclusively by their string representations rather than internal object references or semantic properties. By implementing comparison and hashing operations that delegate to the string form of the object, the implementation ensures that entities with identical textual identifiers are treated as indistinguishable for storage in collections like sets and dictionaries. This approach simplifies the handling of ontology elements by standardizing how they are compared and sorted, relying on lexicographical ordering of their string outputs to drive all relational logic.
