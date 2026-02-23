# Summary

An implementation of the OWL object union construct that represents the logical disjunction of multiple class expressions.

## Description

OWLObjectUnionOf models the logical disjunction of multiple class expressions within an ontology, representing individuals that belong to at least one of the constituent classes. The implementation enforces a canonical internal representation by automatically sorting the provided list of expressions during initialization and modification, which ensures consistency for comparisons and hashing regardless of the input order. It requires a minimum of two class expressions to construct a valid union, preventing the creation of degenerate logical structures. Furthermore, the logic provides a string representation that adheres to standard functional syntax, outputting the union operator followed by the sorted components.
