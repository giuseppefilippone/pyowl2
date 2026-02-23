# Summary

Defines a class representing an OWL restriction that limits the maximum number of data values an individual may possess for a specific data property.

## Description

The implementation models a specific type of class expression used in ontologies to enforce upper bounds on the number of data values associated with an individual via a particular property. By combining a non-negative integer cardinality with a data property expression, the logic ensures that instances do not exceed the specified limit for the defined attribute. An optional data range parameter allows for the creation of qualified restrictions, where the cardinality constraint applies exclusively to values belonging to that specific range rather than all possible values of the property. The design includes internal validation to guarantee that the cardinality remains non-negative and exposes properties to determine whether the restriction is qualified based on the presence of the data range. String representation logic dynamically adjusts to include the data range only when it is defined, providing a clear textual summary of the constraint.
