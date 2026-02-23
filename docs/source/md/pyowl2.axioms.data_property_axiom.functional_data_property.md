# Summary

Defines a class representing an OWL axiom that enforces a functional constraint on data properties, ensuring an individual has at most one value for a specific attribute.

## Description

The implementation models a specific type of Web Ontology Language (OWL) axiom used to declare that a data property is functional, meaning any given individual can be associated with at most one distinct data value through that property. By extending the base axiom class, it integrates into the broader ontology structure while enforcing a uniqueness constraint where multiple values assigned to the same individual are inferred to be identical. The design allows for the attachment of optional metadata annotations and stores the target data property expression, providing mechanisms to access and modify this core component. Additionally, the logic includes a string representation method that outputs the axiom in standard functional syntax, facilitating debugging, logging, or serialization tasks.
