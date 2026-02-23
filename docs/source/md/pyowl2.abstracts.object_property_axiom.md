# Summary

Defines an abstract base class representing axioms that govern the semantics and characteristics of object properties in OWL ontologies.

## Description

Acting as a specialized extension of the general `OWLAxiom` interface, this class establishes a structural foundation for statements that define how object properties behave and relate to one another. It encompasses a wide range of semantic constraints, including sub-property hierarchies, domain and range specifications, and logical characteristics such as transitivity or symmetry. By utilizing the Abstract Base Class module, the design ensures that this component serves solely as a contract, forcing developers to implement concrete subclasses for modeling specific relationships between individuals rather than instantiating this generic definition directly.
