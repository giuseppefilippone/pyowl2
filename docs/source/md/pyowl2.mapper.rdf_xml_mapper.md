# Summary

A utility class that translates high-level OWL ontology constructs into standard RDF triples within an RDFLib graph.

## Description

The software provides a comprehensive mechanism for serializing a wide variety of OWL 2 entities, axioms, and class expressions into their corresponding RDF representations. By accepting an RDFLib graph instance during initialization, the mapper populates it with triples generated from complex structures such as class intersections, unions, restrictions, and property characteristics. A central dispatch method inspects the type of the input object and delegates the transformation to specialized helper methods, ensuring that anonymous classes are represented as blank nodes and collections are handled correctly using RDF lists. Furthermore, the implementation supports both OWL 1 and OWL 2 annotation styles, utilizing reification to attach metadata to axioms when necessary, thereby facilitating the conversion of abstract ontology models into concrete graph data.
