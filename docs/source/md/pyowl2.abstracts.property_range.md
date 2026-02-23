# Summary

Defines an abstract base class representing the range of an OWL property.

## Description

In the context of the Web Ontology Language, the range of a property acts as a constraint that defines the specific types of values or individuals a property can associate with a given subject. By serving as a common interface, this abstraction unifies diverse entities such as class expressions and data ranges that are legally permissible to serve as a range within property axioms. It inherits from the base object class and utilizes the Abstract Base Class module to enforce a contract that ensures all concrete implementations adhere to the expected structural requirements. Consequently, specific implementations must subclass this definition to provide the necessary logic for handling property ranges, as direct instantiation is not supported.
