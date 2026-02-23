# Summary

A structured object-oriented framework for modeling and manipulating OWL literals, including typed values and language-tagged strings, within ontology processing workflows.

## Description

The software employs a polymorphic design to handle data values within an OWL ontology, distinguishing between typed data, plain strings, and language-tagged text through a central wrapper class. Specific subclasses manage distinct literal categories, such as integers or booleans with explicit type definitions versus textual content associated with natural languages, ensuring that ontology assertions maintain precise semantic meaning. To facilitate interoperability with semantic web standards, the implementation converts these high-level objects into standard RDFLib formats while providing utility methods for runtime type checking against XML Schema and OWL datatypes.

## Modules

- [`pyowl2.literal.literal`] — A set of Python classes that model and manipulate OWL literals, including typed values and language-tagged strings, for ontology processing.
