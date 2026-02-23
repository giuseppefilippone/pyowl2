import typing

from pyowl2.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLSubDataPropertyOf(OWLDataPropertyAxiom):
    """
    This axiom defines a hierarchical relationship between two data properties within an OWL ontology, asserting that the first property is a subproperty of the second. By establishing this relationship, it implies that any individual associated with a specific value via the subproperty is also implicitly associated with that same value via the superproperty. To construct this axiom, provide the specific subproperty expression and the general superproperty expression, optionally including a list of annotations to attach metadata or contextual information to the statement.

    :parm sub_data_property_expression: The data property expression declared as the subproperty, representing the more specific property in the relationship.
    :type sub_data_property_expression: OWLDataPropertyExpression
    :parm super_data_property_expression: The data property expression that serves as the superproperty (the more general property) in the subproperty relationship.
    :type super_data_property_expression: OWLDataPropertyExpression
    """

    def __init__(
        self,
        sub_property: OWLDataPropertyExpression,
        super_property: OWLDataPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an axiom asserting that a specific data property is a sub-property of another data property. This constructor requires the sub-property and super-property as data property expressions, establishing a hierarchical relationship where the sub-property implies the super-property. It also accepts an optional list of annotations to provide metadata about the axiom itself, delegating the initialization of these annotations to the parent class.

        :param sub_property: The data property expression acting as the sub-property (child) in the axiom.
        :type sub_property: OWLDataPropertyExpression
        :param super_property: The data property expression acting as the super-property (parent) in the sub-property relationship.
        :type super_property: OWLDataPropertyExpression
        :param annotations: A list of annotations to be associated with the axiom. If None, the axiom is created without annotations.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._sub_data_property_expression: OWLDataPropertyExpression = sub_property
        self._super_data_property_expression: OWLDataPropertyExpression = super_property

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def sub_data_property_expression(self) -> OWLDataPropertyExpression:
        """
        Sets the sub-data property expression for this OWL sub-data property axiom. This method accepts an `OWLDataPropertyExpression` object and assigns it to the internal state, overwriting any existing value stored for the sub-property. As a setter, it directly modifies the object's internal representation to reflect the new hierarchical relationship between data properties.

        :param value: The OWL data property expression to assign as the sub-data-property expression.
        :type value: OWLDataPropertyExpression
        """

        return self._sub_data_property_expression

    @sub_data_property_expression.setter
    def sub_data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expressions."""
        self._sub_data_property_expression = value

    @property
    def super_data_property_expression(self) -> OWLDataPropertyExpression:
        """
        Sets the super data property expression for this `OWLSubDataPropertyOf` axiom, defining the parent property in the sub-property relationship. This method accepts an instance of `OWLDataPropertyExpression` and updates the internal state by overwriting the existing value stored in the private attribute. It serves as the setter for the corresponding property, ensuring that the axiom reflects the specified hierarchical relationship between data properties.

        :param value: The data property expression to assign as the super property.
        :type value: OWLDataPropertyExpression
        """

        return self._super_data_property_expression

    @super_data_property_expression.setter
    def super_data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expressions."""
        self._super_data_property_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the OWL sub-data-property axiom in a functional syntax format. The representation includes the axiom annotations, the sub-data property expression, and the super-data property expression. If no annotations are present, an empty list is explicitly rendered in the output string.

        :return: Returns a string representation of the axiom in functional syntax, including the sub-property, super-property, and any associated annotations.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"SubDataPropertyOf({self.axiom_annotations} {self.sub_data_property_expression} {self.super_data_property_expression})"
        else:
            return f"SubDataPropertyOf([] {self.sub_data_property_expression} {self.super_data_property_expression})"
