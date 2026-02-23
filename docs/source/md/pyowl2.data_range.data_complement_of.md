# Summary

Implements a data range expression that represents the set of all values not included in a specified nested data range.

## Description

Designed for use within ontology structures, the software provides a mechanism to define complex data types through logical negation. By wrapping an existing data range, it creates a new semantic entity that encompasses every possible value except those found within the wrapped range. This functionality allows developers to construct constraints that require values to be excluded from specific sets, thereby enhancing the expressiveness of type definitions. The implementation includes property management to access or modify the nested range and a string representation method to facilitate debugging and display of the logical structure.
