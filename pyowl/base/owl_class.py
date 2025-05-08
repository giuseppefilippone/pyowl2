import typing

from rdflib import OWL, Namespace, URIRef

from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.abstracts.entity import OWLEntity
from pyowl.base.iri import IRI


class OWLClass(OWLClassExpression, OWLEntity):
    """A collection of individuals that share common characteristics."""

    def __init__(self, iri: typing.Union[URIRef, IRI]) -> None:
        self._iri: typing.Union[URIRef, IRI] = iri

    @staticmethod
    def thing() -> typing.Self:
        """Returns the OWLThing class."""
        return OWLClass(IRI(Namespace(OWL._NS), OWL.Thing))

    @staticmethod
    def nothing() -> typing.Self:
        """Returns the OWLNothing class."""
        return OWLClass(IRI(Namespace(OWL._NS), OWL.Nothing))

    def is_thing(self) -> bool:
        return self == OWLClass.thing()

    def is_nothing(self) -> bool:
        return self == OWLClass.nothing()

    @property
    def iri(self) -> typing.Union[URIRef, IRI]:
        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[URIRef, IRI]) -> None:
        self._iri = value

    def __str__(self) -> str:
        return f"Class({self.iri})"
