import abc

from pyowl2.abstracts.object import OWLObject


class OWLPropertyRange(OWLObject, abc.ABC, metaclass=abc.ABCMeta):

    """
    This class serves as an abstract base class representing the range of an OWL property. In the Web Ontology Language, the range of a property constrains the types of values or individuals that the property can associate with a subject. As a common interface, it unifies the various entities—such as class expressions and data ranges—that can legally serve as the range in property axioms. Because this is an abstract class, it is intended to be subclassed by specific implementations rather than instantiated directly.
    """

    __slots__ = ()
