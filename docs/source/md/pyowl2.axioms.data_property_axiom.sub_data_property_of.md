# Summary

Defines a class representing an OWL axiom that asserts one data property is a sub-property of another.

## Description

The class `OWLSubDataPropertyOf` models a specific type of axiom within the Web Ontology Language (OWL) used to define a hierarchical relationship where one data property is a specialization of another. By storing references to both the sub-property and super-property expressions, the implementation ensures that any logical inference or validation involving the sub-property automatically applies to the super-property as well. Construction of the object requires these two property expressions, and it optionally accepts a list of annotations to attach metadata or contextual information, which are managed through inheritance from the base axiom class. To facilitate debugging or serialization, the logic includes a string representation method that outputs the relationship in standard OWL functional syntax, explicitly handling the presence or absence of annotations in the output format.
