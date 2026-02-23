# Summary

Defines a class representing an OWL axiom that asserts a specific object property relates every individual to itself.

## Description

The software implements a representation of the Web Ontology Language (OWL) concept of reflexivity, specifically for object properties. By extending the base axiom class, it allows logical reasoners to infer that for any individual, a relationship exists between that individual and itself via the specified property. The design encapsulates a target object property expression, which can be a named property or an inverse property, along with optional metadata annotations that provide context or human-readable information. Functionality includes managing the internal state of the property expression through property accessors and generating a human-readable string representation that displays the axiom type and its components for debugging or logging purposes.
