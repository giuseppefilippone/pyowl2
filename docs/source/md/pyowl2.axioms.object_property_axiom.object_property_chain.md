# Summary

Represents a sorted sequence of object property expressions used to define property chain axioms within an ontology.

## Description

The implementation automatically sorts the provided expressions upon initialization to establish a canonical form, meaning the original input order is not preserved. Comparisons and hashing operations rely on this sorted structure and the resulting string representation, ensuring that two chains containing the same properties are considered equal regardless of the order in which they were provided. Requiring at least two property expressions enforces the structural constraints necessary for valid property chain axioms while providing a standardized string output for debugging and serialization.
