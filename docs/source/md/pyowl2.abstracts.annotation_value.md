# Summary

An abstract base class representing values assigned to annotation properties in the Web Ontology Language, enforcing string-based comparison and hashing.

## Description

Acting as a foundational component for handling annotation data within the ontology framework, the class provides a unified type for diverse value representations such as anonymous individuals, IRIs, and literals. A central design aspect involves overriding standard Python comparison and hashing dunder methods to base all logical equivalence and ordering operations on the string representation of the object. By delegating equality checks and hash generation to the string output, the implementation ensures that two distinct objects are considered identical if their textual forms match, regardless of their specific concrete types. This approach facilitates consistent sorting and storage in hash-based collections while abstracting away the complexities of the underlying semantic structures.
