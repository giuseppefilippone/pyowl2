# Summary

Defines a class representing the OWL SubObjectPropertyOf axiom to establish hierarchical relationships between object properties.

## Description

The implementation models the logical assertion that a specific object property or a chain of properties is a sub-property of a more general object property. By accepting either a simple property expression or a complex property chain as the sub-property, the design accommodates both straightforward hierarchies and intricate logical rules where a sequence of relationships implies a broader connection. Optional annotations can be attached to the axiom to provide metadata, which are managed through inheritance from the base axiom class. A string representation method generates the axiom in functional syntax, ensuring consistent textual output that includes the sub-property, super-property, and any associated annotations.
