# Summary

Defines a Python class representing an OWL existential restriction that requires individuals to possess specific data property values within a defined range.

## Description

The software models the Web Ontology Language (OWL) existential restriction known as "DataSomeValuesFrom," which defines a class of individuals based on the requirement that they possess at least one value for a specific data property falling within a designated data range. By inheriting from a base class expression, it integrates into a broader ontology framework, allowing for the construction of complex logical statements involving data properties and types. A key design choice involves the automatic sorting of the provided data property expressions upon initialization and modification, ensuring a canonical internal representation that supports consistent comparison and hashing regardless of the input order. Access to the underlying data properties and the associated data range is managed through properties that enforce this sorting logic, while a string representation method provides a human-readable format useful for debugging and logging.
