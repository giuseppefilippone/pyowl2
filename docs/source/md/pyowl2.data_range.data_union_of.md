# Summary

A logical union of multiple data ranges within an ontology that defines a set of permissible values belonging to at least one constituent range.

## Description

Extending the base data range type, this implementation models the OWL union construct by combining a collection of data range objects into a single composite entity. It enforces a semantic constraint requiring at least two operands to form a valid union, ensuring the logical integrity of the expression during initialization. To maintain a canonical representation and facilitate consistent comparisons, the internal list of constituent ranges is automatically sorted upon assignment and modification. The logic also includes a string conversion method that outputs a human-readable format, listing the sorted components within a specific notation style.
