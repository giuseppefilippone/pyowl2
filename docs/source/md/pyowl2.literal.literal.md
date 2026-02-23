# Summary

A set of Python classes that model and manipulate OWL literals, including typed values and language-tagged strings, for ontology processing.

## Description

The software provides a structured object-oriented approach to handling data values within an OWL ontology, distinguishing between typed data, plain strings, and language-tagged text. It utilizes a polymorphic design where a central wrapper class encapsulates various underlying representations, allowing for unified access to values while preserving specific semantic details like datatypes or language codes. Specific subclasses handle distinct literal categories, such as integers or booleans with explicit type definitions versus textual content associated with natural languages, ensuring that ontology assertions maintain precise semantic meaning. To facilitate interoperability with semantic web standards, the implementation includes mechanisms to convert these high-level objects into standard RDFLib formats, alongside utility methods that enable runtime type checking against XML Schema and OWL datatypes.
