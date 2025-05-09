from __future__ import annotations

import typing

from rdflib import URIRef

from pyowl2.abstracts.annotation_axiom import OWLAnnotationAxiom
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.annotation_property import OWLAnnotationProperty

if typing.TYPE_CHECKING:
    from pyowl2.base.iri import IRI


class OWLAnnotationPropertyDomain(OWLAnnotationAxiom):
    """An axiom specifying that a given annotation property applies to subjects of a certain class."""

    def __init__(
        self,
        property: OWLAnnotationProperty,
        iri: typing.Union[URIRef, IRI],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._annotation_property: OWLAnnotationProperty = property
        self._domain: typing.Union[URIRef, IRI] = iri

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def annotation_property(self) -> OWLAnnotationProperty:
        """Getter for annotation_property."""
        return self._annotation_property

    @annotation_property.setter
    def annotation_property(self, value: OWLAnnotationProperty) -> None:
        """Setter for annotation_property."""
        self._annotation_property = value

    @property
    def domain(self) -> typing.Union[URIRef, IRI]:
        """Getter for iri."""
        return self._domain

    @domain.setter
    def domain(self, value: typing.Union[URIRef, IRI]) -> None:
        """Setter for iri."""
        self._domain = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"AnnotationPropertyDomain({self.axiom_annotations} {self.annotation_property} {self.domain})"
        else:
            return (
                f"AnnotationPropertyDomain([] {self.annotation_property} {self.domain})"
            )
