# Summary

A comprehensive Python framework for constructing, manipulating, and serializing OWL 2 ontologies through a high-level object-oriented abstraction over the Owlready2 library.

## Description

The architecture abstracts the underlying `Owlready2` library to manage the lifecycle of knowledge bases, handling everything from initialization and loading to final serialization. It relies on a deep hierarchy of abstract base classes that enforce strict contracts, where object identity and equality are determined exclusively by string serialization to ensure consistency across hash-based collections. Logical components such as entities, axioms, and class expressions are modeled as distinct, mutable objects that automatically sort their internal state to maintain canonical forms, effectively separating semantic logic from non-logical metadata annotations. To bridge the gap between high-level Python objects and the semantic web graph, the system utilizes specialized utilities for sanitizing and parsing RDF/XML into structured models, as well as mapping components that serialize these objects back into standard RDF triples. Finally, a suite of builder wrappers simplifies the programmatic construction of complex ontological structures by aggregating axioms and constraints through fluent interfaces.

## Modules

- [`pyowl2.ontology`] — A comprehensive interface for creating, loading, and manipulating OWL ontologies by wrapping the Owlready2 library to manage entities, axioms, and annotations.

## Sub-packages

- [`pyowl2.abstracts`] — Establishes a hierarchical framework of abstract base classes for modeling Web Ontology Language components, including entities, axioms, and expressions.
- [`pyowl2.axioms`] — An object-oriented implementation of Web Ontology Language (OWL) axioms that models logical assertions, property constraints, and entity declarations.
- [`pyowl2.base`] — Provides the fundamental data structures required to model Web Ontology Language (OWL) entities, including global identifiers, named classes, data types, and annotation mechanisms.
- [`pyowl2.class_expression`] — A comprehensive implementation of Web Ontology Language (OWL) class expressions that models logical restrictions, set operations, and cardinality constraints for data and object properties.
- [`pyowl2.data_range`] — Constructs complex data range expressions for OWL ontologies by implementing logical unions, intersections, complements, enumerations, and datatype restrictions.
- [`pyowl2.expressions`] — Provides a framework for representing and manipulating Web Ontology Language (OWL) property expressions, including data, object, and inverse object properties.
- [`pyowl2.getter`] — An ontology processing utility that sanitizes RDF/XML graphs and transforms them into a structured OWL 2 object model.
- [`pyowl2.individual`] — Provides concrete representations for both named and anonymous individuals within Web Ontology Language structures.
- [`pyowl2.literal`] — A structured object-oriented framework for modeling and manipulating OWL literals, including typed values and language-tagged strings, within ontology processing workflows.
- [`pyowl2.mapper`] — A utility class that translates high-level OWL ontology constructs into standard RDF triples within an RDFLib graph.
- [`pyowl2.utils`] — A collection of high-level wrappers and builders that simplify the programmatic construction and manipulation of Web Ontology Language (OWL) entities, including classes, individuals, properties, and datatypes.
