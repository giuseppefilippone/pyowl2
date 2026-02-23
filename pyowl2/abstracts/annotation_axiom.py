from pyowl2.abstracts.axiom import OWLAxiom


class OWLAnnotationAxiom(OWLAxiom):
    """
    Represents a logical statement within an ontology that serves as a vehicle for attaching metadata to other axioms. It allows for the association of descriptive information, such as comments, labels, or provenance details, with specific logical assertions without altering the underlying semantics. This mechanism is essential for documenting the ontology and providing context for human users, as these annotations are typically ignored by automated reasoners.
    """

    __slots__ = ()
