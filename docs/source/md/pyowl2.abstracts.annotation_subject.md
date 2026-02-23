# Summary

Defines an abstract base class for Web Ontology Language annotation subjects where equality and ordering are determined by string representation.

## Description

Acts as a polymorphic abstraction for entities within the Web Ontology Language framework that can be the target of an annotation, such as Internationalized Resource Identifiers or anonymous individuals. The implementation enforces a specific comparison strategy where equality and ordering are determined exclusively by the string representation of the subject's underlying value rather than object identity or type. By delegating all rich comparison methods and hashing operations to this string conversion, the design ensures that instances can be consistently sorted, compared, and used within hash-based collections like sets and dictionaries. Subclasses are expected to define a specific `value` attribute, which acts as the source of truth for generating the textual representation used throughout these operations.
