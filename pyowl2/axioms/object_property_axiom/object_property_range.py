import typing

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.abstracts.property_range import OWLPropertyRange
from pyowl2.base.annotation import OWLAnnotation


class OWLObjectPropertyRange(OWLPropertyRange, OWLObjectPropertyAxiom):
    """
    This entity represents an axiom within an ontology that constrains the types of individuals which may serve as values for a specific object property. It asserts that for any pair of individuals related by the given property, the target individual must be an instance of the specified class expression, thereby enforcing type consistency across relationships. To utilize this component, instantiate it with the object property expression to be constrained, the class expression defining the allowable range, and an optional list of annotations for metadata. The class provides properties to access and modify the property expression, the range class expression, and any associated annotations, serving as a fundamental building block for defining type safety in object-oriented relationships.

    :param object_property_expression: The object property expression whose range is defined by this axiom.
    :type object_property_expression: OWLObjectPropertyExpression
    :param class_expression: The class expression defining the range of the object property, specifying the type of individuals that can be its values.
    :type class_expression: OWLClassExpression
    """

    def __init__(
        self,
        property: OWLObjectPropertyExpression,
        expression: OWLClassExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an OWL axiom that defines the range restriction for a specific object property. The constructor accepts an object property expression and a class expression, asserting that individuals connected by the property must belong to the specified class. An optional list of annotations can be supplied to attach metadata to the axiom, which are handled by the superclass initialization. The provided property and class expression are stored as internal attributes for subsequent use.

        :param property: The object property expression that constitutes the subject of the axiom.
        :type property: OWLObjectPropertyExpression
        :param expression: The class expression that serves as the filler for the object property restriction.
        :type expression: OWLClassExpression
        :param annotations: A list of annotations to be attached to the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = (
        #     sorted(annotations) if annotations else annotations
        # )
        self._object_property_expression: OWLObjectPropertyExpression = property
        self._class_expression: OWLClassExpression = expression

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = sorted(value) if value else value

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Assigns the specified object property expression to this instance, replacing any previously held value. The input must be a valid OWLObjectPropertyExpression object. This method directly mutates the internal state of the object to reflect the new association.

        :param value: The object property expression to assign.
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    @property
    def class_expression(self) -> OWLClassExpression:
        """
        Updates the range constraint of the object property by assigning a new `OWLClassExpression`. This setter replaces the existing class expression stored within the `OWLObjectPropertyRange` instance, effectively modifying the axiom's definition to reflect the new restriction. The change is immediate and affects the internal state of the object.

        :param value: The OWL class expression to assign to the object.
        :type value: OWLClassExpression
        """

        return self._class_expression

    @class_expression.setter
    def class_expression(self, value: OWLClassExpression) -> None:
        """Setter for class_expression."""
        self._class_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the OWL object property range axiom, formatted according to a specific functional syntax. The output string encapsulates the axiom's annotations, the object property expression, and the class expression within parentheses. If the axiom contains annotations, they are included in the string; otherwise, an empty list representation is substituted in their place. This method does not modify the object's state and is primarily used for generating human-readable output or logging.

        :return: A string representation of the axiom in the format `ObjectPropertyRange([annotations] property range)`.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"ObjectPropertyRange({self.axiom_annotations} {self.object_property_expression} {self.class_expression})"
        else:
            return f"ObjectPropertyRange([] {self.object_property_expression} {self.class_expression})"
