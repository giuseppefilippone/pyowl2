import typing

from rdflib import OWL, Namespace, URIRef

from pyowl2.abstracts.entity import OWLEntity
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.iri import IRI


class OWLObjectProperty(OWLEntity, OWLObjectPropertyExpression):
    """A property that links individuals to other individuals."""

    def __init__(self, iri: typing.Union[URIRef, IRI]) -> None:
        self._iri: typing.Union[URIRef, IRI] = iri

    @staticmethod
    def top() -> typing.Self:
        return OWLObjectProperty(IRI(Namespace(OWL._NS), OWL.topObjectProperty))

    @staticmethod
    def bottom() -> typing.Self:
        return OWLObjectProperty(IRI(Namespace(OWL._NS), OWL.bottomObjectProperty))

    @property
    def iri(self) -> typing.Union[URIRef, IRI]:
        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[URIRef, IRI]) -> None:
        self._iri = value

    def is_top_object_property(self) -> bool:
        return self == OWLObjectProperty.top()

    def is_bottom_object_property(self) -> bool:
        return self == OWLObjectProperty.bottom()

    def __str__(self) -> str:
        return f"ObjectProperty({self._iri})"
