# Summary

Models an OWL axiom asserting that a collection of named individuals are identical within the domain of discourse.

## Description

The software implements a specific type of Web Ontology Language (OWL) assertion used to declare that multiple distinct entities refer to the same individual within a knowledge base. By extending the base assertion class, it integrates seamlessly into the broader ontology structure while enforcing strict validation rules to ensure logical consistency. Specifically, the implementation requires a minimum of two individuals to form a valid identity assertion and automatically sorts these entities to maintain a canonical representation regardless of input order. Additionally, the logic supports the attachment of optional metadata annotations and generates a standardized string output that adheres to functional syntax conventions for interoperability.
