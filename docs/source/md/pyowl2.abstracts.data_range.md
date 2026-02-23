# Summary

An abstract base class representing sets of literal values within an ontology that enforces comparison and hashing based on string representations.

## Description

Serving as a foundational component for defining value spaces in an ontology, this class establishes a contract for representing specific datatypes or logical combinations of literal values. It enforces a strict behavioral model where object identity, ordering, and hash values are derived exclusively from the string serialization of the instance rather than internal state or memory location. By delegating rich comparison operators and hashing mechanisms to the string representation, the implementation ensures that two distinct instances are treated as identical if their textual forms match. This design allows concrete subclasses to focus solely on defining the specific structure of the data range while inheriting a consistent and predictable mechanism for storage in collections and logical evaluation.
