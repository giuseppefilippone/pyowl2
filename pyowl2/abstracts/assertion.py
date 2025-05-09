import abc

from pyowl2.abstracts.axiom import OWLAxiom


class OWLAssertion(OWLAxiom, abc.ABC, metaclass=abc.ABCMeta):
    """An axiom that asserts facts about individuals, such as class membership or property relationships."""

    __slots__ = ()
