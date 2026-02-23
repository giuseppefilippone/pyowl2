from __future__ import annotations

import typing

from rdflib import URIRef

from pyowl2.abstracts.annotation_axiom import OWLAnnotationAxiom
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.annotation_property import OWLAnnotationProperty

if typing.TYPE_CHECKING:
    from pyowl2.base.iri import IRI


class OWLAnnotationPropertyRange(OWLAnnotationAxiom):
    """
    This axiom represents a constraint that specifies the valid range of values for a given annotation property within an ontology. It asserts that any value associated with the property must be an instance of the class identified by the provided IRI. To use this entity, one must provide the annotation property to be constrained and the IRI representing the range class, along with optional annotations to attach metadata directly to the axiom.

    :parm annotation_property: The annotation property for which the range is being specified.
    :type annotation_property: OWLAnnotationProperty
    :parm range: The IRI or URI reference identifying the class to which the values of the annotation property must belong.
    :type range: typing.Union[URIRef, IRI]
    """

    def __init__(
        self,
        property: OWLAnnotationProperty,
        iri: typing.Union[URIRef, IRI],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL axiom that defines the range of an annotation property. This constructor accepts the specific annotation property, the IRI or URI reference that constitutes the range, and an optional list of annotations to be associated with the axiom itself. It delegates the storage of annotations to the parent class and assigns the property and range values to internal attributes for later access.

        :param property: The annotation property that is the subject of this axiom.
        :type property: OWLAnnotationProperty
        :param iri: The IRI representing the range of the annotation property.
        :type iri: typing.Union[URIRef, IRI]
        :param annotations: A list of annotations associated with this axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

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
        """
        Updates the annotation property associated with this `OWLAnnotationPropertyRange` instance by assigning the provided value to the internal state. This method serves as the setter for the `annotation_property` attribute, replacing any existing reference with the new `OWLAnnotationProperty` object. The operation mutates the instance in place and does not return a value.

        :param value: The OWL annotation property to assign to the object.
        :type value: OWLAnnotationProperty
        """

        return self._annotation_property

    @annotation_property.setter
    def annotation_property(self, value: OWLAnnotationProperty) -> None:
        """Setter for annotation_property."""
        self._annotation_property = value

    @property
    def range(self) -> typing.Union[URIRef, IRI]:
        """
        Sets the range restriction for the OWL annotation property represented by this object. The method accepts a value that must be a URI reference or an IRI, which identifies the specific type or class defining the range. Upon invocation, it updates the internal state of the instance by assigning the provided value to the private `_range` attribute.

        :param value: The URI or IRI to assign as the range.
        :type value: typing.Union[URIRef, IRI]
        """

        return self._range

    @range.setter
    def range(self, value: typing.Union[URIRef, IRI]) -> None:
        """Setter for iri."""
        self._range = value

    def __str__(self) -> str:
        """
        Returns a string representation of the annotation property range axiom, formatted to display the annotations, the annotation property, and the range. The output string follows the pattern "AnnotationPropertyRange([annotations] property range)", where the annotations section reflects the actual `axiom_annotations` if present, or an empty list "[]" if they are absent. This method is intended for debugging or display purposes and does not modify the state of the object.

        :return: A string representation of the annotation property range axiom, formatted as 'AnnotationPropertyRange([annotations] property range)'.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"AnnotationPropertyRange({self.axiom_annotations} {self.annotation_property} {self.range})"
        else:
            return (
                f"AnnotationPropertyRange([] {self.annotation_property} {self.range})"
            )
