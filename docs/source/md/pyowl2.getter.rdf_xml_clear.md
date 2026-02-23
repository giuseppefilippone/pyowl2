# Summary

A utility class that sanitizes an ontology by removing specific RDF/XML type declarations and normalizing property definitions within the underlying graph.

## Description

The software provides a mechanism to sanitize an ontology by stripping away specific RDF/XML structural definitions while preserving the underlying data. It operates by interacting directly with the triple store of an Owlready2 ontology, systematically removing type assertions for classes, properties, and lists to simplify the graph structure. Beyond mere deletion, the logic performs normalization tasks, such as replacing specific property types like *owl:OntologyProperty* with *owl:AnnotationProperty* and ensuring that inverse functional or transitive properties are correctly typed as object properties. Helper functions facilitate the translation between RDF Internationalized Resource Identifiers and the internal integer abbreviations used by the ontology engine, ensuring efficient lookups and modifications. The overall process mutates the ontology in place, effectively cleaning the semantic metadata to prepare the data model for further processing or export without the overhead of complex structural definitions.
