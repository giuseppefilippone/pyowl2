from __future__ import annotations

import typing

from rdflib import URIRef

from pyowl2.abstracts.entity import OWLEntity

if typing.TYPE_CHECKING:
    from pyowl2.base.iri import IRI


class OWLAnnotationProperty(OWLEntity):
    """A property used to associate metadata (annotations) with IRIs, anonymous individuals, or literals."""

    def __init__(self, iri: typing.Union[URIRef, IRI]) -> None:
        self._iri: typing.Union[URIRef, IRI] = iri

    @property
    def iri(self) -> typing.Union[URIRef, IRI]:
        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[URIRef, IRI]) -> None:
        self._iri = value

    def __str__(self) -> str:
        return f"AnnotationProperty({self._iri})"
