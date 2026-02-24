import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLInverseObjectProperties(OWLObjectPropertyAxiom):
    """
    This class represents an axiom within an ontology that declares two object properties to be inverses of one another. It establishes a logical rule where if the first property relates an individual A to an individual B, the second property must necessarily relate B to A. To use this class, instantiate it with the two property expressions that form the inverse pair, optionally providing a list of annotations to attach metadata to the axiom. This structure is essential for defining reciprocal relationships, such as linking "hasParent" with "isChildOf", thereby allowing reasoning systems to infer bidirectional connections between entities.

    :param object_property_expression: The object property expression declared to be the inverse of the second property expression.
    :type object_property_expression: OWLObjectPropertyExpression
    :param inverse_object_property_expression: The object property expression that is declared to be the inverse of the first property expression.
    :type inverse_object_property_expression: OWLObjectPropertyExpression
    """

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        inverse_expression: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Constructs an axiom representing the assertion that two object properties are inverses of one another within an OWL ontology. This initializer requires two `OWLObjectPropertyExpression` arguments: the primary property and the property designated as its inverse. It also accepts an optional list of `OWLAnnotation` objects, which are passed to the parent class to provide metadata about the axiom itself.

        :param expression: The object property expression that forms the first part of the inverse relationship.
        :type expression: OWLObjectPropertyExpression
        :param inverse_expression: The object property expression that is the inverse of the primary property expression.
        :type inverse_expression: OWLObjectPropertyExpression
        :param annotations: Optional list of annotations to be associated with the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._object_property_expression: OWLObjectPropertyExpression = expression
        self._inverse_object_property_expression: OWLObjectPropertyExpression = (
            inverse_expression
        )

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Assigns the specified object property expression to this instance, effectively updating one side of the inverse relationship defined by the axiom. The provided value, which must be an instance of `OWLObjectPropertyExpression`, replaces the existing property expression stored internally. This method modifies the object's state in place and does not return a value.

        :param value: The OWL object property expression to assign to the instance.
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    @property
    def inverse_object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Sets the object property expression that constitutes the inverse relationship within this axiom. This method updates the internal attribute to the provided `OWLObjectPropertyExpression`, overwriting any previous value.

        :param value: The OWL object property expression to assign.
        :type value: OWLObjectPropertyExpression
        """

        return self._inverse_object_property_expression

    @inverse_object_property_expression.setter
    def inverse_object_property_expression(
        self, value: OWLObjectPropertyExpression
    ) -> None:
        """Setter for inverse_object_property_expression."""
        self._inverse_object_property_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the inverse object properties axiom, formatted to display the annotations and the two related object property expressions. The output string starts with the identifier "InverseObjectProperties" and includes the list of annotations, the primary object property expression, and the inverse object property expression. If the axiom has associated annotations, they are rendered within the string; otherwise, an empty list is explicitly included to preserve the structural format.

        :return: Returns a string representation of the inverse object properties axiom in functional syntax.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"InverseObjectProperties({self.axiom_annotations} {self.object_property_expression} {self.inverse_object_property_expression})"
        else:
            return f"InverseObjectProperties([] {self.object_property_expression} {self.inverse_object_property_expression})"
