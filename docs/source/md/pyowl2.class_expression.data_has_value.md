# Summary

Implements a Web Ontology Language (OWL) class expression that restricts individuals to those possessing a specific data property with a defined literal value.

## Description

The software models a specific type of restriction within the Web Ontology Language known as a data value restriction, which defines a class consisting of individuals that have a particular data property filled with a specific literal. By extending the abstract class expression interface, this implementation encapsulates a data property expression and a literal value to enforce constraints where an individual must possess an exact data attribute match to be considered a member of the class. The design utilizes property getters and setters to manage the internal state, allowing the associated property and literal to be modified dynamically after instantiation. Furthermore, a string representation method is provided to generate a human-readable functional syntax output, which aids in debugging and serialization by displaying the restriction type alongside its constituent property and value.
