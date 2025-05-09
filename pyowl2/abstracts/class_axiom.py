import abc

from pyowl2.abstracts.axiom import OWLAxiom


class OWLClassAxiom(OWLAxiom, abc.ABC, metaclass=abc.ABCMeta):
    """An axiom that defines relationships between classes, such as subclass relationships or class equivalence."""

    __slots__ = ()
