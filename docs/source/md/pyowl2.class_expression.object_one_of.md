# Summary

An implementation of the OWL ObjectOneOf class expression that defines a class by explicitly enumerating a finite set of individuals.

## Description

The software models a specific type of class expression found in the Web Ontology Language (OWL) where a class is defined strictly by the explicit listing of its member instances. By requiring a non-empty collection of individuals during initialization, the logic enforces that an enumeration must contain at least one element, preventing the creation of empty class definitions through this mechanism. To maintain a canonical and predictable internal state, the implementation automatically sorts the provided individuals whenever the collection is set or modified, ensuring that the order of input does not affect the identity of the logical construct. This design facilitates consistent comparisons and storage, while the string representation adheres to standard functional syntax, making the output suitable for parsing or display in ontology engineering tools.
