# Summary

A collection of high-level wrappers and builders that simplify the programmatic construction and manipulation of Web Ontology Language (OWL) entities, including classes, individuals, properties, and datatypes.

## Description

High-level abstractions encapsulate the identity and logical rules of core Web Ontology Language components, such as classes, individuals, object and data properties, and datatypes. By employing builder patterns and fluent interfaces, the software aggregates logical axioms, domain and range constraints, and property assertions into cohesive objects, thereby simplifying the manipulation of complex ontology structures. The architecture normalizes various input types and enforces data integrity by preventing duplicate entries, allowing developers to incrementally build up semantic definitions involving set operations, restrictions, and hierarchical relationships without manual axiom management. Additionally, a performance profiling utility is included to instrument methods and track execution metrics, providing insights into the efficiency of the underlying operations.

## Modules

- [`pyowl2.utils.data_property`] — A high-level wrapper that centralizes the management of an OWL data property's identity, domain, range, and associated logical axioms.
- [`pyowl2.utils.datatype`] — Provides a structured builder for defining OWL 2 Full data ranges, managing their identity, logical constraints, and associated axioms.
- [`pyowl2.utils.individual`] — Provides a structured representation of an OWL individual that aggregates and manages logical axioms, property assertions, and identity conditions.
- [`pyowl2.utils.object_property`] — Provides a comprehensive interface for defining and manipulating OWL object properties, including their logical characteristics, domain and range constraints, and associated axioms.
- [`pyowl2.utils.thing`] — A comprehensive wrapper for OWL class definitions that manages logical axioms, annotations, and hierarchical relationships within an ontology structure.
- [`pyowl2.utils.utils`] — Provides a class decorator for timing method execution and a utility for displaying the accumulated performance metrics.
