# Summary

Implements a data structure for representing OWL annotations, which associate specific properties with values to attach metadata to ontology entities without affecting logical semantics.

## Description

The implementation models the concept of an annotation within the Web Ontology Language, serving as a container for metadata that enriches ontology elements without altering their logical meaning. It establishes a relationship between an annotation property, which defines the type of metadata, and an annotation value, which holds the actual content such as a literal or IRI. To support complex metadata scenarios, the structure allows for recursive annotations, meaning an annotation can itself be annotated with additional context or provenance information. The design provides mutable access to these core components through properties, enabling dynamic modification of the metadata payload, while also offering string representations for debugging and logging purposes.
