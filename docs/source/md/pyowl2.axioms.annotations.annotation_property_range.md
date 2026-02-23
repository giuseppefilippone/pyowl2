# Summary

Implements an OWL axiom that constrains the valid range of values for a specific annotation property.

## Description

Defines the semantic constraint that values assigned to a specific annotation property must belong to a certain class or type. By extending the abstract `OWLAnnotationAxiom` base class, the implementation allows the constraint to carry metadata annotations about the axiom itself. The design encapsulates an `OWLAnnotationProperty` and a range identifier, which can be either an IRI or a URI reference, providing property accessors to manage these components. A string representation method facilitates debugging and logging by displaying the property, range, and associated annotations in a standardized format.
