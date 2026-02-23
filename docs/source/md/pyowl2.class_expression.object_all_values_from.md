# Summary

Defines a Python class representing the OWL universal restriction ObjectAllValuesFrom, which constrains the range of an object property to a specific class expression.

## Description

The implementation models the Web Ontology Language (OWL) universal restriction, a logical construct asserting that every individual connected via a specific object property must belong to a designated class. By inheriting from a base class expression, it integrates into a broader ontology framework, storing an object property expression that defines the relationship and a class expression that serves as the constraint or filler. Access to these internal components is managed through property getters and setters, allowing the logical definition of the restriction to be queried or modified dynamically during runtime. A string representation method is provided to generate a human-readable format of the restriction, which aids in debugging and logging by displaying the property and the associated class expression.
