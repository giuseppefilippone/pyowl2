# Summary

Implements a Web Ontology Language (OWL) axiom that restricts the domain of a data property by asserting that individuals associated with the property must belong to a specific class.

## Description

The software models a specific type of logical constraint within the Web Ontology Language by linking a data property expression to a class expression that defines its valid subjects. By storing references to both the property and the domain class, the implementation ensures that any individual utilizing the data property logically belongs to the specified class, thereby enforcing consistency within an ontology. Design choices include support for optional annotations, allowing users to attach metadata to the axiom, and the use of property getters and setters to manage the internal state of the property and class expressions. Furthermore, the logic includes a string representation method that outputs the axiom in a functional syntax style, explicitly handling the presence or absence of annotations to maintain a consistent structural format.
