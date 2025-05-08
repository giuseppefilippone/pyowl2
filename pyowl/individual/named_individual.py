import typing

from rdflib import URIRef

from pyowl.abstracts.individual import OWLIndividual
from pyowl.base.iri import IRI


class OWLNamedIndividual(OWLIndividual):
    """An individual that is identified by a unique IRI."""

    def __init__(self, iri: typing.Union[URIRef, IRI]) -> None:
        super().__init__()
        self._iri: typing.Union[URIRef, IRI] = iri

    @property
    def iri(self) -> typing.Union[URIRef, IRI]:
        """Getter for iri."""
        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[URIRef, IRI]) -> None:
        """Setter for iri."""
        self._iri = value

    def __str__(self) -> str:
        return f"NamedIndividual({self.iri})"
