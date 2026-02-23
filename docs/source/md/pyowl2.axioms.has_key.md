# Summary

Implements the OWL HasKey axiom to define unique identifiers for class instances using a combination of object and data properties.

## Description

The software defines a structure for representing the OWL HasKey axiom, which asserts that a specific class expression is uniquely identified by a set of property expressions. By combining object and data properties, the axiom enforces a constraint that no two distinct individuals of the class can share identical values for all specified properties, thereby supporting efficient data retrieval and reasoning. The design ensures internal consistency by automatically sorting the provided property lists upon initialization and modification, maintaining a canonical order regardless of input sequence. Additionally, the implementation supports optional annotations for metadata and provides a string representation following a functional-style syntax to facilitate debugging and serialization.
