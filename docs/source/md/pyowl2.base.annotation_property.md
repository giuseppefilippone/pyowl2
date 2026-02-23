# Summary

Implements a representation of an OWL annotation property that facilitates the attachment of metadata to ontology entities without affecting logical semantics.

## Description

The software defines a structure for handling annotation properties within the Web Ontology Language, specifically designed to manage metadata such as labels and comments without influencing the logical reasoning of the ontology. By extending a base entity class, the implementation ensures that these properties are treated as distinct components separate from data and object properties that drive semantic interpretation. Central to the design is the encapsulation of an Internationalized Resource Identifier (IRI), which acts as the unique identifier for the property and is managed through controlled accessors to maintain data integrity. Additionally, a string representation mechanism is included to provide a clear, human-readable format for debugging and logging purposes by explicitly exposing the associated identifier.
