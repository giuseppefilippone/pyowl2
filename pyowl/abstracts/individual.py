import abc

from pyowl.abstracts.entity import OWLEntity


class OWLIndividual(OWLEntity, abc.ABC, metaclass=abc.ABCMeta):
    """An instance or member of a class within an ontology."""

    __slots__ = ()
