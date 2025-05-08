import abc

from pyowl.abstracts.axiom import OWLAxiom


class OWLDataPropertyAxiom(OWLAxiom, abc.ABC, metaclass=abc.ABCMeta):
    """An axiom that defines characteristics or relationships of data properties."""

    __slots__ = ()
