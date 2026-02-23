# Summary

A collection of Python classes implements Web Ontology Language (OWL) axioms specifically designed to define and constrain data properties within an ontology.

## Description

These components model various logical relationships, including domain and range restrictions, hierarchical sub-property structures, and constraints regarding property equivalence, disjointness, and functionality. By enforcing rules such as minimum property counts and automatic sorting of property expressions, the software ensures canonical internal representations and logical validity. Furthermore, the architecture supports the attachment of optional metadata annotations and provides string representations in standard OWL functional syntax to facilitate debugging and serialization.

## Modules

- [`pyowl2.axioms.data_property_axiom.data_property_domain`] — Implements a Web Ontology Language (OWL) axiom that restricts the domain of a data property by asserting that individuals associated with the property must belong to a specific class.
- [`pyowl2.axioms.data_property_axiom.data_property_range`] — Defines an OWL axiom that restricts the literal values of a data property to a specific data range.
- [`pyowl2.axioms.data_property_axiom.disjoint_data_properties`] — Models an OWL axiom asserting that a specific set of data properties are mutually disjoint, ensuring no individual shares the same literal value across them.
- [`pyowl2.axioms.data_property_axiom.equivalent_data_properties`] — Implements an OWL axiom structure to declare that a set of data properties share the same extension and are therefore interchangeable.
- [`pyowl2.axioms.data_property_axiom.functional_data_property`] — Defines a class representing an OWL axiom that enforces a functional constraint on data properties, ensuring an individual has at most one value for a specific attribute.
- [`pyowl2.axioms.data_property_axiom.sub_data_property_of`] — Defines a class representing an OWL axiom that asserts one data property is a sub-property of another.
