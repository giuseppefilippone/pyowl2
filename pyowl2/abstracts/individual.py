import abc

from pyowl2.abstracts.entity import OWLEntity


class OWLIndividual(OWLEntity, abc.ABC, metaclass=abc.ABCMeta):
    """
    Represents a specific instance or member of a class within an OWL ontology, acting as the abstract base class for all named individuals. Inheriting from `OWLEntity`, it defines the semantic role of an object that exists in the domain of discourse, distinct from the classes or properties that describe it. This class should not be instantiated directly; rather, it serves as the interface for concrete implementations used to assert the existence of specific entities and their relationships within an ontology model.
    """


    __slots__ = ()
