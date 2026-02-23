# Summary

Defines a Python class that models an OWL minimum cardinality restriction, requiring individuals to participate in a specific object property relationship at least a defined number of times.

## Description

The implementation represents a semantic constraint within an ontology where an entity must be linked to a minimum number of distinct individuals via a designated object property. It supports both unqualified restrictions, which apply to any related individual, and qualified restrictions, which limit the count to individuals belonging to a specific class expression. Internal state management relies on properties to encapsulate the cardinality value, the property expression, and the optional class filler, ensuring that the constraint can be dynamically inspected or modified. By subclassing the abstract class expression, the logic integrates seamlessly into larger logical constructs, providing a boolean check for qualification status and a formatted string representation for debugging or serialization purposes.
