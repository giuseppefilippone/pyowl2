# Summary

Represents the logical intersection of multiple OWL class expressions, ensuring a canonical representation through sorting.

## Description

Designed to model the set of individuals that belong to every specified operand, this implementation enforces a strict requirement that the input list contains at least two class expressions. To guarantee that the order of input does not affect the internal state or logical equality, the constituent expressions are automatically sorted during initialization and modification. This canonical sorting mechanism ensures that two intersections defined with the same operands in different orders are treated identically. The resulting structure provides a string representation in functional syntax, wrapping the sorted operands within a standard `ObjectIntersectionOf` format for readability and debugging.
