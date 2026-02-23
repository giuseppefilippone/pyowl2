# Summary

Defines an abstract base class for axioms that govern data properties within the Web Ontology Language (OWL) framework.

## Description

Building upon the general axiom structure, this interface specifically targets properties that associate individuals with literal values like strings or integers, distinguishing them from object properties that link individuals to other individuals. By utilizing the Abstract Base Class metaclass, it ensures that concrete subclasses must implement specific logic to represent semantic rules such as declaring a property functional or defining its domain. The design enforces a strict separation of concerns where the component serves solely as a type definition and contract, preventing direct instantiation and guiding developers toward using specialized implementations for precise ontological modeling. This abstraction facilitates the extension of the ontology system by providing a stable root for all data-related property constraints, ensuring consistency across the library's logical framework.
