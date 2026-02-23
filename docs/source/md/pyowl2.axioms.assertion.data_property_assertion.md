# Summary

Defines a class representing an OWL axiom that asserts a specific data property value for an individual.

## Description

The class models a fundamental statement within an ontology where a subject individual is associated with a concrete data value, such as a string or number, through a defined data property expression. References to the property expression, the source individual, and the target literal are stored to ensure the relationship is fully encapsulated within a single object. By extending a base assertion class, the structure supports the attachment of optional annotations, enabling the inclusion of metadata or contextual information alongside the core logical statement. A string representation method generates a functional syntax format of the assertion, which facilitates serialization and debugging by clearly displaying the components and any associated annotations.
