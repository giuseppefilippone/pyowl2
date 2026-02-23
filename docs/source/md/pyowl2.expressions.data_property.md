# Summary

A Python implementation of an OWL data property that associates ontology individuals with literal data values using a unique Internationalized Resource Identifier.

## Description

It defines a structure for representing data properties within the Web Ontology Language, specifically those that connect individual entities to concrete data values like integers or strings rather than other objects. Central to this design is the use of an Internationalized Resource Identifier (IRI) as the primary means of identification, ensuring that each property can be uniquely referenced and distinguished within a semantic graph. The implementation provides access to standard OWL vocabulary terms, specifically the universal top data property and the empty bottom data property, through static factory methods that encapsulate the creation of these specific system entities. Utility logic is included to verify whether a given instance corresponds to these special system properties, facilitating logical reasoning and validation tasks within the broader ontology framework. By inheriting from base entity and expression classes, the component integrates seamlessly into a larger library designed for manipulating and querying semantic web data structures.
