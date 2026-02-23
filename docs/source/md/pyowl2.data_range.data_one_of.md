# Summary

An implementation of the OWL DataOneOf data range that restricts property values to an explicit, finite enumeration of sorted literals.

## Description

Designed to represent a closed set of specific values within an ontology, this component restricts data membership to a finite, explicitly defined list of literals. By inheriting from the abstract `OWLDataRange` base, it integrates into the broader type system while enforcing that the provided collection of `OWLLiteral` objects is non-empty. A key design choice involves automatically sorting the internal collection of literals upon initialization and modification, which guarantees a canonical representation and simplifies comparison operations. The resulting structure supports string serialization in functional syntax, allowing the enumerated data range to be easily rendered or debugged as a human-readable expression.
