# Summary

OWLObjectHasSelf models a Web Ontology Language (OWL) class expression that restricts individuals to those related to themselves via a specific object property.

## Description

It represents a specific type of existential restriction where an individual must satisfy a relationship with itself using a designated object property. The implementation encapsulates an object property expression, which can range from a simple property to more complex constructs like inverse properties, serving as the criteria for the self-relation. By providing getter and setter mechanisms, the design allows the underlying property expression to be modified dynamically after instantiation, altering the semantic definition of the restriction. A string representation method is included to generate a human-readable format, typically used for debugging or displaying the structure of the ontology concept.
