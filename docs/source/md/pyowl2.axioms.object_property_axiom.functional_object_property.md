# Summary

Represents an OWL axiom asserting that a specific object property is functional, meaning it relates an individual to at most one other individual.

## Description

The implementation enforces the semantic constraint that any given subject entity can be associated with a maximum of one distinct object entity through the specified property. By inheriting from the base object property axiom class, it integrates seamlessly into the broader ontology structure while allowing for the attachment of metadata via annotations. The internal state manages the specific property expression, which can be a named property or an inverse property, ensuring that reasoners can infer uniqueness or identity based on these relationships. A string representation method generates the axiom in functional syntax, facilitating debugging or serialization by explicitly listing annotations and the constrained property.
