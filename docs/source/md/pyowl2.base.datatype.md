# Summary

A Python implementation of an OWL datatype that represents data value categories identified by IRIs and includes utilities for checking against standard XML Schema and OWL types.

## Description

The software defines a class that models data types within the Web Ontology Language (OWL), serving as a bridge between abstract ontology concepts and concrete RDF representations. By inheriting from both entity and data range abstractions, the class establishes a dual identity that allows it to function as a named resource and a range of permissible values. The core design relies on an Internationalized Resource Identifier (IRI) to uniquely define the data type, enabling the representation of both standard XML Schema definitions—such as integers, strings, and dates—and custom user-defined types. To facilitate semantic processing, the implementation includes logic to compare the stored IRI against canonical namespaces, allowing applications to easily determine if a specific instance corresponds to common numeric, boolean, or temporal categories without manual string parsing. This abstraction simplifies the manipulation of typed literals in semantic web applications by providing a consistent interface for type identification and conversion to standard RDF URI references.
