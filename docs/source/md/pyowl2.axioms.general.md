# Summary

Models a logical assertion within an ontology that links a subject class expression to an object class expression via a specific property.

## Description

The implementation extends the base axiom structure to represent complex constraints by associating a subject class expression with a target class expression through an intermediate property identified by an Internationalized Resource Identifier (IRI). Designed for flexibility, the internal state is fully mutable, allowing the modification of the subject, property, and target components after instantiation to accommodate evolving ontology models. Optional metadata can be attached to the logical assertion through a list of annotations, which are managed by the parent class to support rich semantic descriptions. A string representation is provided to visualize the logical structure, explicitly displaying the components in a readable format that highlights the relationship between the defined entities.
