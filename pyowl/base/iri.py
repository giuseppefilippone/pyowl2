from __future__ import annotations

import typing

from rdflib import OWL, Namespace, URIRef

from pyowl.abstracts.annotation_subject import OWLAnnotationSubject
from pyowl.abstracts.annotation_value import OWLAnnotationValue


class IRI(OWLAnnotationSubject, OWLAnnotationValue):
    """Internationalized Resource Identifier, a global identifier used to name entities in an ontology."""

    def __init__(
        self,
        namespace: Namespace,
        value: typing.Union[str, URIRef] = "",
    ) -> None:
        self._namespace: Namespace = namespace
        self._value: typing.Union[str, URIRef] = value

    @staticmethod
    def thing_iri() -> typing.Self:
        return IRI(Namespace(OWL._NS), OWL.Thing)

    @staticmethod
    def nothing_iri() -> typing.Self:
        return IRI(Namespace(OWL._NS), OWL.Nothing)

    @property
    def value(self) -> typing.Union[str, URIRef]:
        """Getter for value."""
        return self._value

    @value.setter
    def value(self, value: typing.Union[str, URIRef]) -> None:
        """Setter for full_iri."""
        self._value = value

    @property
    def namespace(self) -> Namespace:
        """Getter for namespace."""
        return self._namespace

    @namespace.setter
    def namespace(self, value: Namespace) -> None:
        self._namespace = value

    def to_uriref(self) -> URIRef:
        assert isinstance(self.namespace, Namespace)
        return (
            self.value if isinstance(self.value, URIRef) else self.namespace[self.value]
        )

    def is_owl_thing(self) -> bool:
        return self.to_uriref() == OWL.Thing

    def is_owl_nothing(self) -> bool:
        return self.to_uriref() == OWL.Nothing

    def __eq__(self, value: object) -> bool:
        return str(self) == str(value)

    def __ne__(self, value: object) -> bool:
        return str(self) != str(value)

    def __lt__(self, value: object) -> bool:
        return str(self) < str(value)

    def __le__(self, value: object) -> bool:
        return str(self) <= str(value)

    def __gt__(self, value: object) -> bool:
        return str(self) > str(value)

    def __ge__(self, value: object) -> bool:
        return str(self) >= str(value)

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.to_uriref())
