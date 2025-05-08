import typing

from pyowl.abstracts.annotation_value import OWLAnnotationValue
from pyowl.abstracts.object import OWLObject
from pyowl.base.annotation_property import OWLAnnotationProperty


class OWLAnnotation(OWLObject):
    """A construct that provides metadata about an ontology, axiom, or individual without affecting the ontology's logical meaning."""

    def __init__(
        self,
        property: OWLAnnotationProperty,
        value: OWLAnnotationValue,
        annotations: list[typing.Self] = None,
    ) -> None:
        self._annotation_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._annotation_property: OWLAnnotationProperty = property
        self._annotation_value: OWLAnnotationValue = value

    @property
    def annotation_annotations(self) -> list[typing.Self]:
        """Getter for annotation_annotations."""
        return self._annotation_annotations

    @annotation_annotations.setter
    def annotation_annotations(self, value: list[typing.Self]) -> None:
        """Setter for annotation_annotations."""
        self._annotation_annotations = value

    @property
    def annotation_property(self) -> OWLAnnotationProperty:
        """Getter for annotation_property."""
        return self._annotation_property

    @annotation_property.setter
    def annotation_property(self, value: OWLAnnotationProperty) -> None:
        """Setter for annotation_property."""
        self._annotation_property = value

    @property
    def annotation_value(self) -> OWLAnnotationValue:
        """Getter for annotation_value."""
        return self._annotation_value

    @annotation_value.setter
    def annotation_value(self, value: OWLAnnotationValue) -> None:
        """Setter for annotation_value."""
        self._annotation_value = value

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.annotation_annotations:
            return f"Annotation({self.annotation_annotations} {self.annotation_property} {self.annotation_value})"
        else:
            return f"Annotation([] {self.annotation_property} {self.annotation_value})"
