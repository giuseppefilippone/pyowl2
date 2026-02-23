# Summary

Models an OWL axiom declaring that a collection of object properties are semantically equivalent to one another.

## Description

The implementation ensures that any relationship defined by one property in the group holds true for all others, which is a fundamental concept in ontology engineering for defining synonyms or interchangeable relations. To maintain data integrity, the logic requires at least two object property expressions upon initialization, preventing the creation of trivial or malformed axioms. A key design choice involves automatically sorting the internal list of expressions whenever the object is created or modified, which guarantees a canonical representation and simplifies comparison operations. Optional annotations can be attached to the axiom to provide metadata, and the string representation is formatted to resemble standard functional syntax for easier debugging and logging.
