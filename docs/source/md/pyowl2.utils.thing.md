# Summary

A comprehensive wrapper for OWL class definitions that manages logical axioms, annotations, and hierarchical relationships within an ontology structure.

## Description

The software provides a high-level abstraction for constructing and managing Web Ontology Language (OWL) class definitions by encapsulating an underlying class identity alongside its associated logical axioms and metadata. It serves as a central container that aggregates various types of constraints, including subclass relationships, equivalences, disjointness, and property restrictions, into a single cohesive object. By maintaining an internal registry of these statements, the implementation allows developers to programmatically build complex ontology structures without manually managing individual axiom objects.

Designed with a focus on flexibility and data integrity, the wrapper accepts both raw class expressions and other wrapper instances as inputs, normalizing them internally to ensure consistent handling. It enforces idempotency during state modification by verifying that a specific logical statement does not already exist before adding it to the collection, thereby preventing redundancy. The interface includes specialized properties for querying specific subsets of axioms, such as intersections, unions, or cardinality restrictions, enabling efficient inspection of the class's logical definition.

Static factory methods are provided to instantiate the universal root class `owl:Thing` and the empty class `owl:Nothing`, aligning with standard OWL specifications. The architecture supports the attachment of annotations for metadata and facilitates the definition of complex class expressions through methods that handle set operations like unions and intersections. This approach simplifies the process of defining semantic constraints and hierarchical relationships, making it easier to model domain knowledge within an ontology.
