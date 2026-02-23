# Summary

A Python class representing an OWL axiom that constrains the range of an object property to a specific class expression.

## Description

The implementation models a semantic constraint within an ontology by asserting that any individual serving as a value for a specific object property must belong to a defined class type. By inheriting from both `OWLPropertyRange` and `OWLObjectPropertyAxiom`, the class integrates range restriction logic directly into the axiom structure, allowing for the enforcement of type safety across relationships. It encapsulates an object property expression and a class expression, storing them as internal attributes while supporting optional annotations for metadata enrichment. The design includes property accessors for modifying the constraint components and a string representation method that outputs the axiom in standard functional syntax for debugging or serialization.
