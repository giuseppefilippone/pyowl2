# Summary

Provides a structured builder for defining OWL 2 Full data ranges, managing their identity, logical constraints, and associated axioms.

## Description

The software implements a builder pattern for constructing and managing OWL 2 Full data ranges, encapsulating a datatype identity defined by an Internationalized Resource Identifier (IRI) alongside a collection of logical axioms. It enables the programmatic definition of complex data structures—such as intersections, unions, complements, and facet-based restrictions—by automatically generating and storing the necessary OWL axioms while preventing duplicate entries. The design normalizes various input types, seamlessly handling both base data range objects and wrapper instances to establish equivalence relationships and datatype definitions. This separation of identity from logical constraints facilitates the creation of rich ontology definitions, allowing developers to incrementally build up the rules governing valid data values.
