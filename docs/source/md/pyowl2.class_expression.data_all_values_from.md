# Summary

A Python class implementation representing the OWL DataAllValuesFrom restriction, which enforces that all values of specific data properties must belong to a defined data range.

## Description

The software models a universal restriction within the Web Ontology Language (OWL), specifically focusing on data properties where every associated value must fall within a specified data range. By inheriting from the base class expression, it integrates into a broader ontology framework, allowing developers to define complex constraints such as ensuring all ages are integers or all prices are positive numbers. A key design aspect involves the automatic sorting of the provided data property expressions upon initialization and modification, which guarantees a canonical internal state and facilitates consistent comparisons or hashing operations. The implementation exposes these components through managed properties and provides a human-readable string representation that mirrors standard logical notation, making it easier to debug and inspect the structure of the restriction.
