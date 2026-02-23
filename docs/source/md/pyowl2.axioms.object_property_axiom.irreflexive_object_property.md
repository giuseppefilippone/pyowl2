# Summary

Models an OWL axiom that declares a specific object property to be irreflexive, meaning no individual can be related to itself through that property.

## Description

The implementation extends the base object property axiom class to encapsulate the logic required for irreflexivity constraints within an ontology. By storing a specific object property expression, the software ensures that the relationship defined by that expression cannot hold between an entity and itself, which is crucial for modeling distinct entities such as parent-child relationships. Optional annotations are supported to allow users to attach metadata or human-readable descriptions directly to the axiom, inheriting this capability from the parent class structure. A string representation method generates the functional syntax output, dynamically including any associated annotations to facilitate serialization or debugging of the ontology structure.
