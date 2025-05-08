import typing

from rdflib import OWL, Namespace, URIRef

from pyowl.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl.abstracts.entity import OWLEntity
from pyowl.base.iri import IRI


class OWLDataProperty(OWLEntity, OWLDataPropertyExpression):
    """A property that links individuals to data values."""

    def __init__(self, iri: typing.Union[URIRef, IRI]) -> None:
        self._iri: typing.Union[URIRef, IRI] = iri

    @staticmethod
    def top() -> typing.Self:
        return OWLDataProperty(IRI(Namespace(OWL._NS), OWL.topDataProperty))

    @staticmethod
    def bottom() -> typing.Self:
        return OWLDataProperty(IRI(Namespace(OWL._NS), OWL.bottomDataProperty))

    @property
    def iri(self) -> typing.Union[URIRef, IRI]:
        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[URIRef, IRI]) -> None:
        self._iri = value

    def is_top_data_property(self) -> bool:
        return self == OWLDataProperty.top()

    def is_bottom_data_property(self) -> bool:
        return self == OWLDataProperty.bottom()

    def __str__(self) -> str:
        return f"DataProperty({self._iri})"
