# Summary

Represents an OWL axiom that defines a new datatype by equating it to a specific data range.

## Description

The implementation extends the base *OWLAxiom* class to model the logical construct of defining a custom datatype within an ontology. By associating a specific *OWLDatatype* instance with a defining *OWLDataRange*, the software enables the creation of complex data types that restrict values based on existing ranges or literal constraints. Optional annotations can be attached to the definition to provide metadata, which are handled through inheritance from the parent axiom class. State management is facilitated through properties that allow the retrieval and modification of both the target datatype and the defining data range, while a custom string representation ensures the axiom can be displayed in a human-readable format consistent with OWL syntax.
