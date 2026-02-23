# Summary

Defines a concrete implementation of an OWL entity that is uniquely identified by an Internationalized Resource Identifier (IRI).

## Description

Extending the abstract concept of an individual within the Web Ontology Language, the implementation provides a mechanism to model concrete instances that possess a persistent, globally resolvable identity. Unlike anonymous nodes, this entity relies on an Internationalized Resource Identifier (IRI) to serve as a unique key, enabling unambiguous reference in axioms and assertions across the ontology. The design encapsulates this identifier within a property interface, allowing for both retrieval and mutation of the identity after instantiation. Furthermore, a string representation is included to facilitate debugging and logging by clearly displaying the associated IRI.
