import abc

from pyowl2.abstracts.axiom import OWLAxiom


class OWLObjectPropertyAxiom(OWLAxiom, abc.ABC, metaclass=abc.ABCMeta):
    """
    This class serves as an abstract base class representing axioms that define the semantics, relationships, or characteristics of object properties within an OWL ontology. As a specialization of the general `OWLAxiom` interface, it provides the foundational structure for specific statements that describe how object properties behave, such as declaring sub-property hierarchies, specifying domains and ranges, or defining property characteristics like transitivity or symmetry. Developers should not instantiate this class directly but rather rely on its concrete subclasses to model specific constraints and rules governing the relationships between individuals in an ontology.
    """


    __slots__ = ()
