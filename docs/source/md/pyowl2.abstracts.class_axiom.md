# Summary

Defines an abstract base class representing logical assertions specifically related to the definition and interrelation of ontology classes.

## Description

Extending the general concept of an ontology axiom, this component focuses on class-level semantics to categorize logical statements that describe how concepts relate to one another. It serves as a foundational type for concrete implementations dealing with subclass hierarchies, equivalences, or disjointness, thereby distinguishing conceptual constraints from those concerning individual instances or properties. By enforcing an abstract interface, the design ensures that all derived class-specific axioms adhere to a common structural contract while allowing the broader system to filter and process these logical rules efficiently. The implementation utilizes empty `__slots__` to prevent dynamic attribute creation, promoting memory efficiency and enforcing a strict, predictable schema for all subclasses.
