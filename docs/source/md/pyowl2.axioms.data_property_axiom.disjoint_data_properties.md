# Summary

Models an OWL axiom asserting that a specific set of data properties are mutually disjoint, ensuring no individual shares the same literal value across them.

## Description

The implementation enforces a strict requirement that at least two property expressions must be provided during initialization, and it automatically sorts these expressions to guarantee a canonical internal representation regardless of input order. By inheriting from the base axiom class, the logic supports the inclusion of optional annotations, enabling the attachment of metadata to the logical constraint. Additionally, a string representation is provided in functional syntax style, which explicitly formats the output to display annotations and the sorted list of properties for readability and serialization purposes.
