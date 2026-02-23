# Summary

Defines an OWL axiom that enforces a uniqueness constraint on an object property by ensuring that no two distinct individuals can relate to the same target individual via that property.

## Description

The implementation models the Web Ontology Language concept of an inverse-functional object property, which imposes a semantic constraint ensuring that a specific property maps a target individual back to a unique source individual. By asserting this axiom, a reasoner can infer that if two distinct entities are found to be related to the same individual via the defined property, those entities must actually be identical. This behavior is essential for representing unique identifiers, such as social security numbers or email addresses, where a single value should correspond to exactly one entity within the domain.

Structurally, the class inherits from a base object property axiom to leverage common functionality for handling metadata and annotations. It encapsulates the specific property expression being constrained and allows for the attachment of optional annotations to provide further context or documentation. Furthermore, the logic includes a string representation method that outputs the axiom in a format resembling OWL functional syntax, facilitating easier debugging and interoperability with other semantic web tools.
