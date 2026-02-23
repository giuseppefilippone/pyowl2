# Summary

Implements a data structure representing the OWL SubAnnotationPropertyOf axiom, which establishes a hierarchical relationship where one annotation property is a sub-property of another.

## Description

By storing references to both the specific sub-property and the broader super-property, the logic enables semantic inference, ensuring that annotations applied using the sub-property are implicitly understood to apply to the super-property as well. The design leverages inheritance to manage optional metadata about the axiom itself, allowing users to attach additional context or source information. Access to the core properties is provided through mutable attributes, and the structure includes a string representation method that outputs the relationship in standard functional syntax for interoperability.
