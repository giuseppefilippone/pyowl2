# Summary

Implements the logic for creating datatype restrictions in OWL ontologies by applying specific facet constraints to base datatypes.

## Description

The software provides a mechanism to narrow the value space of standard datatypes by applying specific constraints, such as minimum or maximum values, which are essential for defining precise data characteristics in semantic web applications. It introduces an enumeration for standard facet types and a class to represent individual constraints, ensuring that only valid XML Schema Definition (XSD) restrictions are utilized during instantiation. The central component combines a base datatype with a collection of these constraints, automatically sorting them to maintain a canonical order and enforcing that at least one restriction is present. By implementing comparison and hashing methods based on string representations, the software ensures that these constraints can be reliably used within sets and sorted collections, facilitating the construction of complex data ranges.
