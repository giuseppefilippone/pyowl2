# Summary

Implements a representation for the Web Ontology Language axiom that restricts the domain of an object property to a specific class expression.

## Description

The software models a specific type of Web Ontology Language (OWL) axiom used to define the domain of an object property, ensuring that any individual acting as the subject of a relationship belongs to a specified class. By inheriting from a base axiom class, it integrates standard annotation handling capabilities while introducing specific attributes to hold the object property expression and the class expression that defines the domain constraint. The design allows for the dynamic assignment and retrieval of both the property and the class expression, enabling the construction of complex ontological rules where the validity of property assertions depends on the type of the source individual. Furthermore, the implementation includes a string conversion mechanism that outputs the axiom in a functional syntax format, which is useful for serialization, debugging, or interoperability with other OWL tools.
