# Summary

Models an OWL Object Property as a binary relation connecting two individuals within an ontology, including support for universal top and bottom property vocabularies.

## Description

The software defines a concrete implementation of an OWL Object Property, which functions as a binary relation connecting two individuals within an ontology. By inheriting from abstract base classes for entities and property expressions, it integrates into a larger framework for representing semantic web data structures. Instances are uniquely identified by an Internationalized Resource Identifier (IRI), which can be set or retrieved to manage the property's identity. The implementation also provides access to the universal top and bottom properties defined in the OWL vocabulary, allowing users to represent the most general and most specific relations respectively. Additionally, logic is included to determine whether a specific instance corresponds to these universal vocabulary elements, facilitating semantic reasoning and validation.
