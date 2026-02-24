import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLAsymmetricObjectProperty(OWLObjectPropertyAxiom):
    """
    This class represents an axiom in the Web Ontology Language (OWL) that declares a specific object property to be asymmetric. Semantically, this constraint ensures that if an individual A is related to an individual B through the specified property, then B cannot be related to A through the same property, effectively defining a one-way relationship. It is commonly used to model concepts such as parenthood or temporal precedence where reciprocity is logically impossible. To use this class, instantiate it with the target `OWLObjectPropertyExpression` and, optionally, a list of `OWLAnnotation` objects to attach metadata or context to the axiom.

    :param object_property_expression: The object property expression that is declared to be asymmetric.
    :type object_property_expression: OWLObjectPropertyExpression
    """

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Constructs an axiom asserting that a specific object property is asymmetric within the ontology. The method requires an `OWLObjectPropertyExpression` representing the property to which the asymmetry constraint applies. Optionally, a list of `OWLAnnotation` objects can be provided to attach metadata to the axiom; these are managed by the parent class initialization.

        :param expression: The object property expression (which may be a named property or an inverse property) to be used in this axiom.
        :type expression: OWLObjectPropertyExpression
        :param annotations: A list of annotations to be attached to the axiom, or None if no annotations are provided.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._object_property_expression: OWLObjectPropertyExpression = expression

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
        Sets the object property expression for this asymmetric object property axiom, identifying the specific property that is subject to the asymmetry constraint. This operation overwrites the existing property expression stored in the instance with the provided value.

        :param value: The object property expression to assign.
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the asymmetric object property axiom, formatted to resemble a functional syntax declaration. The output string includes the axiom annotations followed by the object property expression. If the axiom contains annotations, they are listed explicitly; otherwise, an empty list is displayed in their place. This method is primarily used for debugging or logging purposes to provide a readable snapshot of the object's state.

        :return: A string representation of the asymmetric object property axiom, including its annotations and object property expression.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"AsymmetricObjectProperty({self.axiom_annotations} {self.object_property_expression})"
        else:
            return f"AsymmetricObjectProperty([] {self.object_property_expression})"
