# Summary

Provides a comprehensive interface for defining and manipulating OWL object properties, including their logical characteristics, domain and range constraints, and associated axioms.

## Description

A high-level abstraction wraps a core property entity identified by an Internationalized Resource Identifier (IRI), aggregating its definition and logical rules into a single manageable object. It maintains an internal collection of axioms, enabling users to dynamically configure property characteristics such as symmetry, transitivity, and functionality through boolean flags that automatically update the underlying ontology structure. The design supports the creation of complex hierarchical relationships, such as sub-property and inverse property definitions, alongside class expression restrictions involving cardinality and value constraints. Furthermore, the software allows for the assertion of specific relationships between individuals, serving as a central hub for constructing and managing the complete logical profile of a relationship type.
