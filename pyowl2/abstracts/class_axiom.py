import abc

from pyowl2.abstracts.axiom import OWLAxiom


class OWLClassAxiom(OWLAxiom, abc.ABC, metaclass=abc.ABCMeta):
    """
    Represents a fundamental logical assertion within an ontology that specifically pertains to the definition or interrelation of classes. This abstract base class categorizes axioms that describe class-level semantics, such as declaring one class to be a subclass of another, establishing equivalence between classes, or defining disjointness. It serves as a common type for all class-specific constraints, allowing users to filter or process axioms that deal strictly with conceptual structures rather than individual instances or property characteristics.
    """


    __slots__ = ()
