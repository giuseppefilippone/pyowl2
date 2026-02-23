# Summary

A collection of Python classes modeling Web Ontology Language axioms that define the characteristics, constraints, and hierarchical relationships of object properties.

## Description

These structures enable the precise definition of semantic rules governing how entities relate to one another, covering concepts such as transitivity, symmetry, functionality, and domain or range restrictions. By inheriting from a common base class, the implementations share a unified mechanism for handling metadata annotations and generating string representations in standard functional syntax, which facilitates debugging and interoperability. To ensure consistency and simplify logical comparisons, specific components automatically sort property expressions into a canonical form during initialization, particularly when dealing with sets of equivalent or disjoint properties. This architecture allows reasoners to infer complex relationships and validate data integrity by enforcing strict logical constraints on the types of connections allowed between individuals within an ontology.

## Modules

- [`pyowl2.axioms.object_property_axiom.asymmetric_object_property`] — Implements a data structure for representing the Web Ontology Language axiom that declares an object property to be asymmetric.
- [`pyowl2.axioms.object_property_axiom.disjoint_object_properties`] — Defines a class representing an OWL axiom that asserts a collection of object properties are mutually exclusive and cannot relate the same pair of individuals.
- [`pyowl2.axioms.object_property_axiom.equivalent_object_properties`] — Models an OWL axiom declaring that a collection of object properties are semantically equivalent to one another.
- [`pyowl2.axioms.object_property_axiom.functional_object_property`] — Represents an OWL axiom asserting that a specific object property is functional, meaning it relates an individual to at most one other individual.
- [`pyowl2.axioms.object_property_axiom.inverse_functional_object_property`] — Defines an OWL axiom that enforces a uniqueness constraint on an object property by ensuring that no two distinct individuals can relate to the same target individual via that property.
- [`pyowl2.axioms.object_property_axiom.inverse_object_properties`] — Implements a data structure representing an OWL axiom that declares two object properties to be inverses of one another.
- [`pyowl2.axioms.object_property_axiom.irreflexive_object_property`] — Models an OWL axiom that declares a specific object property to be irreflexive, meaning no individual can be related to itself through that property.
- [`pyowl2.axioms.object_property_axiom.object_property_chain`] — Represents a sorted sequence of object property expressions used to define property chain axioms within an ontology.
- [`pyowl2.axioms.object_property_axiom.object_property_domain`] — Implements a representation for the Web Ontology Language axiom that restricts the domain of an object property to a specific class expression.
- [`pyowl2.axioms.object_property_axiom.object_property_range`] — A Python class representing an OWL axiom that constrains the range of an object property to a specific class expression.
- [`pyowl2.axioms.object_property_axiom.reflexive_object_property`] — Defines a class representing an OWL axiom that asserts a specific object property relates every individual to itself.
- [`pyowl2.axioms.object_property_axiom.sub_object_property_of`] — Defines a class representing the OWL SubObjectPropertyOf axiom to establish hierarchical relationships between object properties.
- [`pyowl2.axioms.object_property_axiom.symmetric_object_property`] — Implements a data structure representing the Web Ontology Language axiom that declares an object property to be symmetric.
- [`pyowl2.axioms.object_property_axiom.transitive_object_property`] — Implements a representation of the Web Ontology Language axiom used to declare a specific object property as transitive.
