import typing

from pyowl2.abstracts.annotation_axiom import OWLAnnotationAxiom
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.annotation_property import OWLAnnotationProperty


class OWLSubAnnotationPropertyOf(OWLAnnotationAxiom):
    """
    This class represents an axiom within the Web Ontology Language (OWL) that defines a hierarchical relationship between two annotation properties, asserting that one is a subproperty of the other. By establishing this relationship, it enables semantic inference where any annotation applied using the subproperty is implicitly understood to also apply to the superproperty. To use this class, instantiate it with the specific sub-property and super-property instances, optionally including a list of annotations to provide metadata about the axiom itself, such as its source or context. The properties of the axiom can be accessed and modified directly via the provided attributes, allowing for dynamic updates to the ontology structure.

    :param sub_annotation_property: The annotation property asserted to be a subproperty of the super annotation property.
    :type sub_annotation_property: OWLAnnotationProperty
    :param super_annotation_property: The annotation property asserted to be the superproperty in the subproperty relationship, representing the parent property that the sub-property implies.
    :type super_annotation_property: OWLAnnotationProperty
    """

    def __init__(
        self,
        sub_property: OWLAnnotationProperty,
        super_property: OWLAnnotationProperty,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an axiom asserting that one annotation property is a sub-property of another within an OWL ontology. This constructor requires the specific sub-property and super-property to be defined, while allowing for an optional list of annotations to be attached to the axiom itself. It invokes the superclass initialization to handle the annotations and stores the property references internally for subsequent access and reasoning.

        :param sub_property: The annotation property acting as the sub-property in the relationship.
        :type sub_property: OWLAnnotationProperty
        :param super_property: The parent annotation property that the sub-property is a specialization of.
        :type super_property: OWLAnnotationProperty
        :param annotations: A list of annotations to be associated with this axiom. If None, the axiom is created without annotations.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

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
        """
        Sets the specific annotation property that serves as the sub-property within this `OWLSubAnnotationPropertyOf` axiom. This method accepts an `OWLAnnotationProperty` instance and updates the internal state, replacing any previously stored value for this property.

        :param value: The OWL annotation property to be set as the sub-annotation property.
        :type value: OWLAnnotationProperty
        """

        return self._sub_annotation_property

    @sub_annotation_property.setter
    def sub_annotation_property(self, value: OWLAnnotationProperty) -> None:
        """Setter for sub_annotation_property."""
        self._sub_annotation_property = value

    @property
    def super_annotation_property(self) -> OWLAnnotationProperty:
        """
        Sets the super annotation property that defines the parent of the relationship represented by this `OWLSubAnnotationPropertyOf` axiom. It accepts an `OWLAnnotationProperty` instance and assigns it to the internal `_super_annotation_property` attribute, overwriting any existing value. This operation directly modifies the object's state to reflect the new hierarchy.

        :param value: The annotation property to set as the super property.
        :type value: OWLAnnotationProperty
        """

        return self._super_annotation_property

    @super_annotation_property.setter
    def super_annotation_property(self, value: OWLAnnotationProperty) -> None:
        """Setter for super_annotation_property."""
        self._super_annotation_property = value

    def __str__(self) -> str:
        """
        Returns a string representation of the sub-annotation property axiom in a functional syntax format. The string begins with "SubAnnotationPropertyOf" followed by the axiom annotations; if no annotations are present, an empty list is explicitly displayed. The representation concludes with the sub-annotation property and the super-annotation property identifiers.

        :return: A string representation of the axiom, formatted as `SubAnnotationPropertyOf([annotations] sub_property super_property)`.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"SubAnnotationPropertyOf({self.axiom_annotations} {self.sub_annotation_property} {self.super_annotation_property})"
        else:
            return f"SubAnnotationPropertyOf([] {self.sub_annotation_property} {self.super_annotation_property})"
