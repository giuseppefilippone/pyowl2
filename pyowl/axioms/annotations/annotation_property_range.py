from __future__ import annotations

import typing

from rdflib import URIRef

from pyowl.abstracts.annotation_axiom import OWLAnnotationAxiom
from pyowl.base.annotation import OWLAnnotation
from pyowl.base.annotation_property import OWLAnnotationProperty

if typing.TYPE_CHECKING:
    from pyowl.base.iri import IRI


class OWLAnnotationPropertyRange(OWLAnnotationAxiom):
    """An axiom specifying that the values of a given annotation property belong to a certain class."""

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
        self._range: typing.Union[URIRef, IRI] = iri

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
    def range(self) -> typing.Union[URIRef, IRI]:
        """Getter for iri."""
        return self._range

    @range.setter
    def range(self, value: typing.Union[URIRef, IRI]) -> None:
        """Setter for iri."""
        self._range = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"AnnotationPropertyRange({self.axiom_annotations} {self.annotation_property} {self.range})"
        else:
            return (
                f"AnnotationPropertyRange([] {self.annotation_property} {self.range})"
            )
