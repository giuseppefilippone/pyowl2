# Summary

Implements a class representing an OWL data exact cardinality restriction that constrains individuals to possess exactly a specific number of values for a given data property.

## Description

The software models the Web Ontology Language (OWL) concept of exact cardinality restrictions for data properties, ensuring that an individual possesses exactly a defined number of data values. It supports both qualified and unqualified restrictions by allowing an optional data range parameter, which, when provided, limits the count to values falling within a specific datatype. Internal state management is handled through properties that expose the cardinality, the associated data property expression, and the optional data range, enabling validation and modification of these constraints. A boolean helper indicates whether the restriction is qualified, and a string representation method generates a functional syntax output to facilitate debugging or serialization.
