# Summary

Defines a semantic structure representing an OWL Disjoint Union axiom, where a specific class is equivalent to the union of mutually disjoint class expressions.

## Description

The software models the Web Ontology Language (OWL) Disjoint Union axiom, which asserts that a designated named class is equivalent to the logical union of a collection of class expressions that are pairwise disjoint. To ensure consistency and canonical representation, the implementation automatically sorts the provided list of disjoint class expressions upon initialization and modification, regardless of the input order. Validation logic enforces that at least two class expressions are supplied to form a valid partition, preventing semantic errors where a disjoint union cannot be formed. Optional annotations can be associated with the axiom to provide metadata, and the structure includes a string representation method that outputs the axiom in standard functional syntax for debugging or serialization purposes.
