# Summary

Establishes a hierarchical framework of abstract base classes for modeling Web Ontology Language components, including entities, axioms, and expressions.

## Description

The architecture relies on a deep inheritance hierarchy rooted in a generic base object, which enforces strict contracts for concrete implementations representing classes, individuals, and properties. A central design pattern involves basing object identity, equality, and total ordering exclusively on string serialization, ensuring that distinct instances are treated as equivalent if their textual representations match. This approach decouples logical comparison from internal structural analysis while facilitating consistent storage in hash-based collections and sorted lists. Furthermore, the structure separates metadata annotations from core logical assertions, allowing reasoners to process semantic rules without interference from descriptive information. Memory efficiency is prioritized through the use of empty slots, preventing dynamic attribute creation and maintaining a rigid schema for ontological data representation.

## Modules

- [`pyowl2.abstracts.annotation_axiom`] — Defines a specialized axiom class used to attach metadata and descriptive information to logical assertions within an ontology without affecting their semantic meaning.
- [`pyowl2.abstracts.annotation_subject`] — Defines an abstract base class for Web Ontology Language annotation subjects where equality and ordering are determined by string representation.
- [`pyowl2.abstracts.annotation_value`] — An abstract base class representing values assigned to annotation properties in the Web Ontology Language, enforcing string-based comparison and hashing.
- [`pyowl2.abstracts.assertion`] — Defines an abstract base class for axioms that assert specific facts about individuals within an ontology.
- [`pyowl2.abstracts.axiom`] — An abstract base class representing fundamental assertions within an ontology that manages optional metadata annotations and defines equality and ordering based on string serialization.
- [`pyowl2.abstracts.class_axiom`] — Defines an abstract base class representing logical assertions specifically related to the definition and interrelation of ontology classes.
- [`pyowl2.abstracts.class_expression`] — An abstract base class representing Web Ontology Language (OWL) class expressions that standardizes equality, ordering, and hashing operations based on string serialization.
- [`pyowl2.abstracts.data_property_axiom`] — Defines an abstract base class for axioms that govern data properties within the Web Ontology Language (OWL) framework.
- [`pyowl2.abstracts.data_property_expression`] — Defines an abstract base class representing expressions involving OWL data properties that link individuals to literal values.
- [`pyowl2.abstracts.data_range`] — An abstract base class representing sets of literal values within an ontology that enforces comparison and hashing based on string representations.
- [`pyowl2.abstracts.entity`] — Defines an abstract base class for named OWL ontology elements where identity, ordering, and hashing are derived strictly from string representations.
- [`pyowl2.abstracts.individual`] — Establishes the abstract interface for named individuals in an OWL ontology.
- [`pyowl2.abstracts.object`] — An abstract base class that serves as the foundational root for all Web Ontology Language (OWL) entities.
- [`pyowl2.abstracts.object_property_axiom`] — Defines an abstract base class representing axioms that govern the semantics and characteristics of object properties in OWL ontologies.
- [`pyowl2.abstracts.object_property_expression`] — An abstract base class defining the interface for object property expressions in an OWL ontology, encompassing both named properties and complex constructs like inverse properties.
- [`pyowl2.abstracts.property_range`] — Defines an abstract base class representing the range of an OWL property.
