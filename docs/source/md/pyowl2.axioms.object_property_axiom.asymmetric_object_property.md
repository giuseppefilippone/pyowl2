# Summary

Implements a data structure for representing the Web Ontology Language axiom that declares an object property to be asymmetric.

## Description

The logic encapsulated here enforces a semantic constraint where if an individual A is related to individual B via a specific property, B cannot be related back to A using that same property. This structure stores the target object property expression and optionally accepts a list of annotations to attach metadata or context to the logical statement. By inheriting from a base object property axiom class, the implementation integrates seamlessly into the ontology structure while delegating the management of annotations to the parent initialization. A string representation method generates a functional syntax format, which is useful for debugging, logging, or serializing the axiom in a human-readable form that explicitly lists annotations and the property expression.
