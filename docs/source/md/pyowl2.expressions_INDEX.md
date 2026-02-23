# Summary

Provides a framework for representing and manipulating Web Ontology Language (OWL) property expressions, including data, object, and inverse object properties.

## Description

Software components model the structural relationships defined by the Web Ontology Language, specifically focusing on how individuals connect to data values or other individuals. Central to the architecture is the use of Internationalized Resource Identifiers (IRIs) to uniquely identify each property, ensuring precise referencing within semantic graphs. Concrete implementations for data properties, binary object properties, and inverse relationships inherit from abstract base classes to maintain a consistent interface for entity manipulation and querying. Logic is included to handle universal top and bottom vocabulary terms, enabling semantic reasoning tasks and validation of the ontology's logical consistency. By supporting standard functional syntax output and encapsulating complex relationship logic, the code facilitates the serialization and debugging of semantic web data structures.

## Modules

- [`pyowl2.expressions.data_property`] — A Python implementation of an OWL data property that associates ontology individuals with literal data values using a unique Internationalized Resource Identifier.
- [`pyowl2.expressions.inverse_object_property`] — Defines a class representing the inverse of an OWL object property to model reciprocal relationships between individuals.
- [`pyowl2.expressions.object_property`] — Models an OWL Object Property as a binary relation connecting two individuals within an ontology, including support for universal top and bottom property vocabularies.
