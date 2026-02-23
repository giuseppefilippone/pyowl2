# Summary

Defines an OWL axiom that restricts the domain of an annotation property to a specific class identified by an IRI.

## Description

The implementation models a semantic constraint within an ontology by asserting that the subject of any annotation utilizing a specific property must be an instance of a designated class. It encapsulates the relationship between an annotation property and a domain identifier, which can be represented as either a URI reference or an Internationalized Resource Identifier. By inheriting from a base annotation axiom class, it supports the attachment of optional metadata annotations that describe the axiom itself, separating the logical constraint from descriptive information. The logic includes a string representation mechanism that renders the structure in functional syntax, explicitly handling the presence or absence of these metadata annotations to ensure accurate serialization.
