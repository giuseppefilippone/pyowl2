import typing

from pyowl2.abstracts.annotation_value import OWLAnnotationValue
from pyowl2.abstracts.object import OWLObject
from pyowl2.base.annotation_property import OWLAnnotationProperty


class OWLAnnotation(OWLObject):
    """
    This construct represents a piece of metadata attached to an ontology, axiom, or entity that does not alter the logical semantics of the underlying model. It is defined by a specific property that characterizes the type of metadata, such as a label or comment, and a corresponding value, which may be a literal, an IRI, or an anonymous individual. Users can instantiate this class to enrich ontology elements with human-readable descriptions or provenance data, and it supports recursive annotation to provide context about the annotation itself. By separating non-logical information from the axiomatic structure, it allows for the documentation of entities without impacting automated reasoning tasks.

    :parm annotation_annotations: A list of annotations associated with this annotation, providing additional metadata or context about the annotation itself.
    :type annotation_annotations: typing.Optional[list[OWLAnnotation]]
    :parm annotation_property: The property that defines the relationship between the subject and the value, characterizing the specific type of metadata being asserted.
    :type annotation_property: OWLAnnotationProperty
    :parm annotation_value: The specific data or content of the annotation, which can be a literal, an IRI, or an anonymous individual, serving as the value associated with the annotation property.
    :type annotation_value: OWLAnnotationValue
    """

    def __init__(
        self,
        property: OWLAnnotationProperty,
        value: OWLAnnotationValue,
        annotations: list[typing.Self] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL annotation, which associates a specific property with a value to attach metadata to ontology entities. The constructor accepts an optional list of sub-annotations, enabling the annotation itself to be annotated (e.g., to provide provenance information for a label). If no sub-annotations are provided, the internal storage for them is set to None. This method performs direct assignment of the inputs to internal attributes, establishing the object's state without invoking external side effects or deep copying operations.

        :param property: The annotation property that serves as the predicate for this annotation.
        :type property: OWLAnnotationProperty
        :param value: The value associated with the annotation property.
        :type value: OWLAnnotationValue
        :param annotations: A list of annotations to be applied to this annotation instance.
        :type annotations: list[typing.Self]
        """

        self._annotation_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._annotation_property: OWLAnnotationProperty = property
        self._annotation_value: OWLAnnotationValue = value

    @property
    def annotation_annotations(self) -> list[typing.Self]:
        """
        Replaces the current list of annotations associated with this annotation instance with the provided list. The input value must be a list of instances of the same class, representing nested annotations. This method performs a direct assignment, meaning subsequent modifications to the input list will affect the internal state of the object.

        :param value: A list of annotation instances of the same type to assign.
        :type value: list[typing.Self]
        """

        return self._annotation_annotations

    @annotation_annotations.setter
    def annotation_annotations(self, value: list[typing.Self]) -> None:
        """Setter for annotation_annotations."""
        self._annotation_annotations = value

    @property
    def annotation_property(self) -> OWLAnnotationProperty:
        """
        Sets the annotation property for this OWLAnnotation instance to the specified value. This method accepts an object of type OWLAnnotationProperty and updates the internal state of the annotation, overwriting any previously assigned property. As a setter, it modifies the object in place and does not return a value.

        :param value: The OWL annotation property instance to assign.
        :type value: OWLAnnotationProperty
        """

        return self._annotation_property

    @annotation_property.setter
    def annotation_property(self, value: OWLAnnotationProperty) -> None:
        """Setter for annotation_property."""
        self._annotation_property = value

    @property
    def annotation_value(self) -> OWLAnnotationValue:
        """
        Assigns a new value to the annotation, replacing the current content. The method accepts an instance of OWLAnnotationValue and updates the internal state of the object accordingly. This operation effectively changes the semantic payload of the annotation without altering its property.

        :param value: The OWL annotation value to set, which can be a literal, IRI, or anonymous individual.
        :type value: OWLAnnotationValue
        """

        return self._annotation_value

    @annotation_value.setter
    def annotation_value(self, value: OWLAnnotationValue) -> None:
        """Setter for annotation_value."""
        self._annotation_value = value

    def __repr__(self) -> str:
        """
        Returns a string representation of the OWLAnnotation instance, primarily intended for debugging and interactive use. This implementation delegates directly to the `__str__` method, ensuring that the output format is consistent with the standard string conversion of the object. Consequently, the representation is human-readable and mirrors the result of calling `str()` on the instance.

        :return: Returns a string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns a string representation of the annotation formatted in a functional style. The output includes the list of meta-annotations, the annotation property, and the annotation value. If no meta-annotations are present, the representation explicitly displays an empty list in their place. This method is useful for debugging or logging to provide a concise summary of the annotation's structure.

        :return: A string representation of the annotation, displaying its annotations, property, and value.

        :rtype: str
        """

        if self.annotation_annotations:
            return f"Annotation({self.annotation_annotations} {self.annotation_property} {self.annotation_value})"
        else:
            return f"Annotation([] {self.annotation_property} {self.annotation_value})"
