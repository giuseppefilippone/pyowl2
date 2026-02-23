# Summary

Implements the OWL DisjointClasses axiom to enforce mutual exclusion among a set of class expressions within an ontology.

## Description

The software models the semantic constraint that no individual can simultaneously belong to more than one class in a specified collection, a fundamental concept in ontology engineering known as the DisjointClasses axiom. By inheriting from a base class axiom, it integrates seamlessly into the broader ontology structure while enforcing strict validation rules, such as requiring a minimum of two class expressions to define a meaningful disjointness relationship. Internally, the implementation automatically sorts the provided class expressions to maintain a deterministic order, which aids in comparison and serialization processes. Optional metadata can be attached to the axiom through annotations, and the logic includes a string representation method that outputs the structure in standard OWL functional syntax.
