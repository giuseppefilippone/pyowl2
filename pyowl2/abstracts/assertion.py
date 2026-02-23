import abc

from pyowl2.abstracts.axiom import OWLAxiom


class OWLAssertion(OWLAxiom, abc.ABC, metaclass=abc.ABCMeta):
    """
    Represents an abstract base class for axioms that assert specific facts about individuals within an ontology. This class serves as a common interface for statements that declare an individual's membership in a class or its relationships with other individuals via object or data properties. As an abstract type, it is not instantiated directly; rather, it provides the foundational structure for concrete assertion implementations used to build and query ontological knowledge.
    """


    __slots__ = ()
