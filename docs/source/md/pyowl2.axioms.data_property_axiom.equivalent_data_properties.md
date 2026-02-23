# Summary

Implements an OWL axiom structure to declare that a set of data properties share the same extension and are therefore interchangeable.

## Description

The software models a specific type of Web Ontology Language (OWL) axiom used to define that multiple data properties are semantically equivalent, meaning they refer to the same set of data assertions. By requiring a minimum of two property expressions upon initialization, the implementation ensures logical validity, while automatically sorting these expressions to maintain a canonical internal state regardless of the input order. This design allows for the attachment of optional metadata annotations, facilitating the enrichment of the axiom with additional context or information. The internal logic normalizes the representation of equivalent properties, which aids in comparison operations and ensures consistent structural output when the object is converted to a string.
