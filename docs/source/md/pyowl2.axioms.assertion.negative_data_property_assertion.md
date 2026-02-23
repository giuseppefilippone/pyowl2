# Summary

An implementation of an OWL negative data property assertion that formally declares a specific individual does not possess a particular literal value for a given data property.

## Description

The software models a specific type of axiom used in ontology engineering to represent the absence of a relationship between an individual and a data value. By inheriting from a base assertion class, it encapsulates a source individual, a target literal value, and a data property expression to define the negation, while also supporting optional annotations for metadata. The internal state is managed through properties that allow both retrieval and modification of the core components, ensuring the assertion can be inspected or updated dynamically after instantiation. A string representation method generates a functional syntax format that includes the annotations and the structural elements of the assertion, facilitating serialization or debugging within the broader ontology framework.
