# Summary

Implements a representation of the Web Ontology Language axiom used to declare a specific object property as transitive.

## Description

The software models the logical concept of transitivity within the Web Ontology Language by providing a structure to assert that a specific relationship holds transitively between individuals. By inheriting from a base axiom class, it leverages existing functionality for handling metadata annotations while focusing on storing the specific object property expression that is being characterized. The implementation ensures that if a property relates entity A to B and B to C, the ontology can infer that the property also relates A to C, which is a fundamental requirement for complex reasoning tasks. A string representation method generates output resembling OWL functional syntax, allowing the axiom to be easily serialized or debugged in a human-readable format that explicitly lists annotations and the target property.
