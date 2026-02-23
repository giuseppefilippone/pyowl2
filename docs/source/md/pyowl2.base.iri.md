# Summary

Defines a class representing an Internationalized Resource Identifier (IRI) that acts as a global identifier for entities within an OWL ontology by combining a namespace prefix with a specific local value.

## Description

The software provides a robust mechanism for creating and managing Internationalized Resource Identifiers (IRIs) which function as unique global identifiers for ontology elements such as classes, properties, and individuals. By inheriting from abstract annotation interfaces, the implementation ensures compatibility with broader OWL data structures while leveraging the `rdflib` library to handle the underlying namespace logic and URI resolution. It encapsulates a namespace and a local value, allowing the conversion of these components into a standard `URIRef` object for seamless integration with RDF data stores. Furthermore, the design includes utility logic to recognize fundamental OWL concepts like `owl:Thing` and `owl:Nothing`, and it implements standard comparison and hashing protocols based on the string representation of the identifier to support use in collections and sorting operations.
