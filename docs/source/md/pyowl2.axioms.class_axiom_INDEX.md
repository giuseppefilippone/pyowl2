# Summary

A software component that implements core Web Ontology Language (OWL) class axioms to define logical relationships and constraints between ontology classes.

## Description

The software models fundamental semantic constructs, including hierarchical subclass relationships, mutual exclusion constraints, and logical equivalences or disjoint unions. By inheriting from a shared base class, these implementations enforce strict validation rules—such as requiring a minimum number of class expressions—and automatically sort inputs to ensure canonical, deterministic representations for comparison and serialization. Optional metadata can be attached to these logical statements through annotations, while string representation methods provide outputs in standard OWL functional syntax to aid in debugging and data exchange.

## Modules

- [`pyowl2.axioms.class_axiom.disjoint_classes`] — Implements the OWL DisjointClasses axiom to enforce mutual exclusion among a set of class expressions within an ontology.
- [`pyowl2.axioms.class_axiom.disjoint_union`] — Defines a semantic structure representing an OWL Disjoint Union axiom, where a specific class is equivalent to the union of mutually disjoint class expressions.
- [`pyowl2.axioms.class_axiom.equivalent_classes`] — Defines a logical axiom asserting that two or more OWL class expressions share the exact same set of instances.
- [`pyowl2.axioms.class_axiom.sub_class_of`] — Implements the OWL SubClassOf axiom to model hierarchical relationships between ontology classes by asserting that all instances of a subclass are also instances of a superclass.
