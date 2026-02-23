# Summary

Provides the fundamental data structures required to model Web Ontology Language (OWL) entities, including global identifiers, named classes, data types, and annotation mechanisms.

## Description

Establishes the core components necessary for constructing and manipulating OWL ontologies by modeling essential elements such as named classes, data types, and annotation properties. Central to the architecture is the use of Internationalized Resource Identifiers (IRIs) as unique global identifiers, which serve as the definitive reference for all entities and facilitate integration with RDF data stores through `rdflib`. The design strictly separates logical semantic constructs, like class hierarchies and data value categories, from non-logical metadata, allowing for the attachment of rich contextual information without affecting reasoning processes. By implementing specific abstractions for entities and expressions, the software supports complex logical descriptions and recursive metadata scenarios while providing utilities for type checking against standard XML Schema definitions.

## Modules

- [`pyowl2.base.annotation`] — Implements a data structure for representing OWL annotations, which associate specific properties with values to attach metadata to ontology entities without affecting logical semantics.
- [`pyowl2.base.annotation_property`] — Implements a representation of an OWL annotation property that facilitates the attachment of metadata to ontology entities without affecting logical semantics.
- [`pyowl2.base.datatype`] — A Python implementation of an OWL datatype that represents data value categories identified by IRIs and includes utilities for checking against standard XML Schema and OWL types.
- [`pyowl2.base.iri`] — Defines a class representing an Internationalized Resource Identifier (IRI) that acts as a global identifier for entities within an OWL ontology by combining a namespace prefix with a specific local value.
- [`pyowl2.base.owl_class`] — Implements a representation of named OWL ontology classes identified by an Internationalized Resource Identifier (IRI).
