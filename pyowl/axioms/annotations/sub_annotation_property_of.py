import typing

from pyowl.abstracts.annotation_axiom import OWLAnnotationAxiom
from pyowl.base.annotation import OWLAnnotation
from pyowl.base.annotation_property import OWLAnnotationProperty


class OWLSubAnnotationPropertyOf(OWLAnnotationAxiom):
    """An axiom stating that one annotation property is a subproperty of another annotation property."""

    def __init__(
        self,
        sub_property: OWLAnnotationProperty,
        super_property: OWLAnnotationProperty,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._sub_annotation_property: OWLAnnotationProperty = sub_property
        self._super_annotation_property: OWLAnnotationProperty = super_property

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def sub_annotation_property(self) -> OWLAnnotationProperty:
        """Getter for sub_annotation_property."""
        return self._sub_annotation_property

    @sub_annotation_property.setter
    def sub_annotation_property(self, value: OWLAnnotationProperty) -> None:
        """Setter for sub_annotation_property."""
        self._sub_annotation_property = value

    @property
    def super_annotation_property(self) -> OWLAnnotationProperty:
        """Getter for super_annotation_property."""
        return self._super_annotation_property

    @super_annotation_property.setter
    def super_annotation_property(self, value: OWLAnnotationProperty) -> None:
        """Setter for super_annotation_property."""
        self._super_annotation_property = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"SubAnnotationPropertyOf({self.axiom_annotations} {self.sub_annotation_property} {self.super_annotation_property})"
        else:
            return f"SubAnnotationPropertyOf([] {self.sub_annotation_property} {self.super_annotation_property})"
