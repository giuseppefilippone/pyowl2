import typing

from pyowl.abstracts.annotation_axiom import OWLAnnotationAxiom
from pyowl.abstracts.annotation_value import OWLAnnotationValue
from pyowl.base.annotation import OWLAnnotation
from pyowl.abstracts.annotation_subject import OWLAnnotationSubject
from pyowl.base.annotation_property import OWLAnnotationProperty


class OWLAnnotationAssertion(OWLAnnotationAxiom):
    """An axiom stating that a specific annotation property has a particular value for a given IRI, anonymous individual, or literal."""

    def __init__(
        self,
        subject: OWLAnnotationSubject,
        property: OWLAnnotationProperty,
        value: OWLAnnotationValue,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._annotation_property: OWLAnnotationProperty = property
        self._annotation_subject: OWLAnnotationSubject = subject
        self._annotation_value: OWLAnnotationValue = value

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
    def annotation_subject(self) -> OWLAnnotationSubject:
        """Getter for annotation_subject."""
        return self._annotation_subject

    @annotation_subject.setter
    def annotation_subject(self, value: OWLAnnotationSubject) -> None:
        """Setter for annotation_subject."""
        self._annotation_subject = value

    @property
    def annotation_value(self) -> OWLAnnotationValue:
        """Getter for annotation_value."""
        return self._annotation_value

    @annotation_value.setter
    def annotation_value(self, value: OWLAnnotationValue) -> None:
        """Setter for annotation_value."""
        self._annotation_value = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"AnnotationAssertion({self.axiom_annotations} {self.annotation_property} {self.annotation_subject} {self.annotation_value})"
        else:
            return f"AnnotationAssertion([] {self.annotation_property} {self.annotation_subject} {self.annotation_value})"
