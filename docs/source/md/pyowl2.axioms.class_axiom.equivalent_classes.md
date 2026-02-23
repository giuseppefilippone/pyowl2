# Summary

Defines a logical axiom asserting that two or more OWL class expressions share the exact same set of instances.

## Description

The implementation models the semantic identity between distinct concepts, enabling reasoners to infer that any individual belonging to one class must also belong to all others declared equivalent. To ensure consistency and logical validity, the construction process mandates that a minimum of two class expressions are provided, preventing the creation of trivial or incomplete equivalences. A key design choice involves the automatic sorting of these expressions upon initialization and modification, which guarantees a canonical representation where the order of input does not affect the identity of the axiom. Optional metadata can be attached via annotations, and the structure supports a functional-style string representation that explicitly renders the annotation state alongside the equivalent class expressions.
