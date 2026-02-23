# Summary

Defines an abstract base class representing expressions involving OWL data properties that link individuals to literal values.

## Description

Acting as a root interface within the ontology model, the class distinguishes data properties—which associate individuals with literals like strings or integers—from object properties that link individuals to other individuals. It utilizes Python's abstract base class framework to mandate that subclasses implement logic for identifying specific semantic states, such as whether the expression represents the universal top data property or the empty bottom data property. These checks are critical for reasoning tasks and ontology normalization, as they allow the system to treat the top property as an identity element and the bottom property as a contradiction. By enforcing this contract, the implementation ensures consistent behavior across different types of data property expressions used throughout the broader software architecture.
