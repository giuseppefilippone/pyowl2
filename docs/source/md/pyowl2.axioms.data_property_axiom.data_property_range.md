# Summary

Defines an OWL axiom that restricts the literal values of a data property to a specific data range.

## Description

An implementation that establishes a constraint within an ontology by linking a specific data property expression to a defined data range, ensuring that any literal values assigned to the property adhere to the specified type. Inheriting from both `OWLPropertyRange` and `OWLDataPropertyAxiom` allows the component to integrate seamlessly into the broader ontology structure while supporting optional metadata annotations for additional context. Internal state is managed through private attributes for the property and range, which are exposed via properties that allow for both mutation and retrieval of these core components. A string representation method generates the axiom in functional syntax, facilitating debugging or serialization by explicitly listing annotations, the subject property, and the target range.
