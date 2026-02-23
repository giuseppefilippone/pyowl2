import abc

from pyowl2.abstracts.axiom import OWLAxiom


class OWLDataPropertyAxiom(OWLAxiom, abc.ABC, metaclass=abc.ABCMeta):
    """
    This abstract base class serves as the foundational interface for axioms that define the characteristics, constraints, and relationships of data properties within an OWL ontology. It distinguishes itself from object property axioms by focusing on properties that link individuals to literal data values, such as strings or integers, rather than to other individuals. As a specialization of the general axiom type, it provides a common contract for concrete implementations that model specific logical statements, such as declaring a property as functional, defining its domain, or establishing a sub-property hierarchy. Users should not instantiate this class directly but should instead utilize its specific subclasses to represent precise semantic rules in their ontological models.
    """


    __slots__ = ()
