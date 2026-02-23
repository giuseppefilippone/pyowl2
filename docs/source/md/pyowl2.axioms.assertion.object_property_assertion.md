# Summary

Defines a class representing an OWL axiom that asserts a specific binary relationship between two individuals.

## Description

The software models a specific type of Web Ontology Language (OWL) axiom that declares a binary relationship exists between two distinct individuals. By inheriting from a base assertion class, it manages the core components of the relationship, including the property expression defining the link, the source individual acting as the subject, and the target individual acting as the object. Optional metadata annotations can be attached to the assertion to provide additional context or information, which are handled through the parent class initialization. Access to the internal state is provided via properties that allow both retrieval and modification of the property expression and the involved individuals, ensuring the encapsulated data remains consistent with the ontology's structure. A string representation method generates the axiom in a functional syntax format, facilitating debugging or serialization by displaying the relationship and its components clearly.
