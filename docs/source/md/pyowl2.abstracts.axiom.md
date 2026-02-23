# Summary

An abstract base class representing fundamental assertions within an ontology that manages optional metadata annotations and defines equality and ordering based on string serialization.

## Description

Designed to serve as the foundational component for defining the logical structure of a knowledge base, the class provides a blueprint for creating specific types of assertions within an ontology. It supports the attachment of optional metadata through annotations, which are automatically sorted upon assignment to maintain a consistent internal state regardless of the input order. A key design characteristic is the reliance on string serialization for determining object identity, where equality, hash values, and total ordering are all derived from the textual representation of the assertion rather than direct attribute comparison. This approach ensures that instances can be reliably used in hash-based collections and sorted lists, provided the string formatting remains deterministic and consistent with the logical equivalence of the axioms.
