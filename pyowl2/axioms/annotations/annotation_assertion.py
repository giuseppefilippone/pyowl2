import typing

from pyowl2.abstracts.annotation_axiom import OWLAnnotationAxiom
from pyowl2.abstracts.annotation_subject import OWLAnnotationSubject
from pyowl2.abstracts.annotation_value import OWLAnnotationValue
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.annotation_property import OWLAnnotationProperty


class OWLAnnotationAssertion(OWLAnnotationAxiom):
    """
    This class represents an axiom used to attach metadata to entities within an OWL ontology by asserting that a specific annotation property holds a particular value for a given subject. It functions as a triple connecting a subject—which can be an IRI, anonymous individual, or literal—to a property and a corresponding value, effectively labeling or describing the subject. Users can instantiate this object to define relationships such as labels, comments, or custom metadata, and optionally include a list of annotations on the axiom itself to capture provenance or other contextual information.

    :param annotation_property: The annotation property being asserted to have a specific value for the subject.
    :type annotation_property: OWLAnnotationProperty
    :param annotation_subject: The entity being annotated, which can be an IRI, an anonymous individual, or a literal.
    :type annotation_subject: OWLAnnotationSubject
    :param annotation_value: The specific value being asserted for the annotation property and subject, which can be an IRI, an anonymous individual, or a literal.
    :type annotation_value: OWLAnnotationValue
    """

    def __init__(
        self,
        subject: OWLAnnotationSubject,
        property: OWLAnnotationProperty,
        value: OWLAnnotationValue,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL annotation assertion axiom, which links a specific subject to an annotation property and a corresponding value. The constructor requires the subject, the property, and the value as arguments, storing them internally to define the core assertion. It also accepts an optional list of annotations that apply to the axiom itself, delegating their storage to the parent class initialization.

        :param subject: The entity or node to which the annotation is attached.
        :type subject: OWLAnnotationSubject
        :param property: The annotation property that links the subject to the value.
        :type property: OWLAnnotationProperty
        :param value: The value of the annotation, representing the object of the annotation triple.
        :type value: OWLAnnotationValue
        :param annotations: Optional list of annotations associated with this axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

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
        """
        Assigns the specified OWLAnnotationProperty to this assertion, replacing any existing value. This method directly modifies the internal state of the object to reflect the new annotation property. While the type hint indicates an OWLAnnotationProperty is expected, the implementation performs no runtime validation, so passing incompatible types may lead to errors elsewhere in the module.

        :param value: The OWL annotation property to assign to the object.
        :type value: OWLAnnotationProperty
        """

        return self._annotation_property

    @annotation_property.setter
    def annotation_property(self, value: OWLAnnotationProperty) -> None:
        """Setter for annotation_property."""
        self._annotation_property = value

    @property
    def annotation_subject(self) -> OWLAnnotationSubject:
        """
        Updates the subject of the annotation assertion to the specified value, replacing any previously assigned subject. The provided value must be an instance of OWLAnnotationSubject, representing the entity (such as an IRI or anonymous individual) to which the annotation is attached. This method directly mutates the internal state of the object.

        :param value: The IRI or anonymous individual that serves as the subject of the annotation.
        :type value: OWLAnnotationSubject
        """

        return self._annotation_subject

    @annotation_subject.setter
    def annotation_subject(self, value: OWLAnnotationSubject) -> None:
        """Setter for annotation_subject."""
        self._annotation_subject = value

    @property
    def annotation_value(self) -> OWLAnnotationValue:
        """
        Updates the value associated with this annotation assertion. It replaces the currently stored annotation value with the specified OWLAnnotationValue, effectively mutating the object's state.

        :param value: The annotation value to assign.
        :type value: OWLAnnotationValue
        """

        return self._annotation_value

    @annotation_value.setter
    def annotation_value(self, value: OWLAnnotationValue) -> None:
        """Setter for annotation_value."""
        self._annotation_value = value

    def __str__(self) -> str:
        """
        Returns a string representation of the annotation assertion formatted in a functional-style syntax. The output string includes the list of annotations associated with the axiom itself, followed by the annotation property, the subject, and the value. If the axiom has no associated annotations, the representation explicitly displays an empty list in the corresponding position.

        :return: A string representation of the annotation assertion, formatted as "AnnotationAssertion(annotations property subject value)".

        :rtype: str
        """

        if self.axiom_annotations:
            return f"AnnotationAssertion({self.axiom_annotations} {self.annotation_property} {self.annotation_subject} {self.annotation_value})"
        else:
            return f"AnnotationAssertion([] {self.annotation_property} {self.annotation_subject} {self.annotation_value})"
