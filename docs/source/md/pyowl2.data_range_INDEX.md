# Summary

Constructs complex data range expressions for OWL ontologies by implementing logical unions, intersections, complements, enumerations, and datatype restrictions.

## Description

It enables the definition of complex data types within semantic web applications by modeling logical set operations and constraints. The architecture supports the creation of composite data ranges through logical unions, intersections, and complements, as well as finite enumerations and specific facet-based restrictions on base datatypes. To ensure consistency across comparisons and hashing, internal collections of operands, literals, or constraints are automatically sorted upon initialization and modification, creating a canonical representation for each expression. Validation rules enforce structural integrity, such as requiring a minimum number of operands for logical operations, while string serialization methods provide human-readable functional syntax for debugging and data exchange.

## Modules

- [`pyowl2.data_range.data_complement_of`] — Implements a data range expression that represents the set of all values not included in a specified nested data range.
- [`pyowl2.data_range.data_intersection_of`] — A logical data range implementation representing the intersection of multiple constituent data ranges within an ontology.
- [`pyowl2.data_range.data_one_of`] — An implementation of the OWL DataOneOf data range that restricts property values to an explicit, finite enumeration of sorted literals.
- [`pyowl2.data_range.data_union_of`] — A logical union of multiple data ranges within an ontology that defines a set of permissible values belonging to at least one constituent range.
- [`pyowl2.data_range.datatype_restriction`] — Implements the logic for creating datatype restrictions in OWL ontologies by applying specific facet constraints to base datatypes.
