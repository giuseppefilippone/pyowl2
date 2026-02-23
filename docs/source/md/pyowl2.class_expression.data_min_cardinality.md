# Summary

Defines an OWL class expression that restricts individuals to possess a minimum number of values for a specific data property, optionally constrained by a data range.

## Description

The implementation models a restriction where an individual must have at least a specific number of data property assertions to be considered a member of the defined class. A non-negative integer cardinality is stored alongside a data property expression to define this constraint, ensuring that the threshold is valid upon initialization. Support for qualified restrictions is provided through an optional data range, which limits the count to only those values that match a specific datatype or set of literals. Properties expose the internal state for modification, and a string representation adhering to OWL functional syntax is generated to describe the restriction structure.
