# Summary

A high-level wrapper that centralizes the management of an OWL data property's identity, domain, range, and associated logical axioms.

## Description

The software provides a structured abstraction for an OWL data property, encapsulating its core identity defined by an Internationalized Resource Identifier (IRI) alongside optional domain and range constraints. It maintains an internal registry of axioms that define the property's logical characteristics, such as functionality, hierarchical relationships with other properties, and equivalence or disjointness constraints. Through its interface, users can assert specific data property values for individuals, including both positive and negative assertions, and apply complex restrictions like existential, universal, and cardinality constraints. The design simplifies ontology manipulation by offering dedicated methods to add, filter, and manage these logical statements and annotations, ensuring that the property's definition remains consistent and semantically valid within the broader ontology structure.
