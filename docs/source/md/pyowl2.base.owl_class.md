# Summary

Implements a representation of named OWL ontology classes identified by an Internationalized Resource Identifier (IRI).

## Description

The core component serves as a concrete implementation for named classes within the Web Ontology Language, bridging abstract entity definitions with specific resource identifiers. By inheriting from both `OWLClassExpression` and `OWLEntity`, it functions as a fundamental building block for constructing complex logical descriptions and defining relationships. Instances are uniquely identified by an Internationalized Resource Identifier (IRI), which acts as the definitive reference for the class in axioms and assertions, ensuring that concepts like "Person" or "Vehicle" are distinct and addressable. The design includes static accessors for the universal class and the empty class, representing the top and bottom elements of the class hierarchy respectively, while instance methods allow for easy verification of these special states. Additionally, the internal IRI is managed through properties to maintain encapsulation while allowing for updates to the unique identifier.
