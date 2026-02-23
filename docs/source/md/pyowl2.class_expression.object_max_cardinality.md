# Summary

Defines a Python class representing an OWL object maximum cardinality restriction, which limits the number of relationships an individual can have via a specific object property.

## Description

This software component models a specific type of restriction within the Web Ontology Language (OWL) by enforcing an upper bound on the number of distinct individuals an entity can be related to through a given object property. The design accommodates both unqualified constraints, which apply to any related individual, and qualified constraints that require the related individuals to also belong to a specific class expression. By encapsulating the cardinality value, the property being restricted, and an optional filler class, the implementation allows for the dynamic definition and modification of these semantic rules. Additional logic determines whether the restriction is qualified and provides a string representation in functional syntax format to support ontology serialization and debugging.
