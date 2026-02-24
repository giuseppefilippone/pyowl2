import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.axioms.object_property_axiom.object_property_chain import (
    OWLObjectPropertyChain,
)
from pyowl2.base.annotation import OWLAnnotation


class OWLSubObjectPropertyOf(OWLObjectPropertyAxiom):
    """
    This class represents an axiom in the Web Ontology Language (OWL) that asserts a hierarchical relationship between two object properties, indicating that the first is a subproperty of the second. It is used to define that any relationship defined by the sub-property expression necessarily implies a relationship defined by the super-property expression. The implementation supports both simple property hierarchies and complex property chains, allowing for the expression of intricate logical rules where a sequence of properties implies a more general property. To use this entity, instantiate it with the specific sub-property expression, the general super-property expression, and an optional list of annotations for metadata.

    :param sub_object_property_expression: The object property expression or property chain that serves as the subproperty in the relationship.
    :type sub_object_property_expression: typing.Union[OWLObjectPropertyChain, OWLObjectPropertyExpression]
    :param super_object_property_expression: The object property expression declared to be the superproperty, serving as the more general property in the subproperty relationship.
    :type super_object_property_expression: OWLObjectPropertyExpression
    """

    def __init__(
        self,
        sub_property: typing.Union[OWLObjectPropertyChain, OWLObjectPropertyExpression],
        super_property: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an OWL axiom representing a sub-property relationship between two object property expressions. This constructor accepts a sub-property, which may be a simple object property expression or a complex property chain, and a super-property expression. It also supports an optional list of annotations, which are passed to the parent class for initialization, thereby associating metadata with the axiom.

        :param sub_property: The object property expression or property chain acting as the sub-property in the axiom.
        :type sub_property: typing.Union[OWLObjectPropertyChain, OWLObjectPropertyExpression]
        :param super_property: The object property expression that serves as the parent or more general property in the sub-property axiom.
        :type super_property: OWLObjectPropertyExpression
        :param annotations: Optional list of annotations to be associated with the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = (
        #     sorted(annotations) if annotations else annotations
        # )
        self._sub_object_property_expression: typing.Union[
            OWLObjectPropertyChain, OWLObjectPropertyExpression
        ] = sub_property
        self._super_object_property_expression: OWLObjectPropertyExpression = (
            super_property
        )

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = sorted(value) if value else value

    @property
    def sub_object_property_expression(
        self,
    ) -> typing.Union[OWLObjectPropertyChain, OWLObjectPropertyExpression]:
        """
        Sets the sub-property expression for this OWL sub-object property axiom to the provided value. The value can be either a single object property expression or a chain of object properties, accommodating both simple and complex sub-property relationships. This method updates the internal state of the axiom instance to reflect the new sub-property definition.

        :param value: The object property expression or property chain to set as the sub-property.
        :type value: typing.Union[OWLObjectPropertyChain, OWLObjectPropertyExpression]
        """

        return self._sub_object_property_expression

    @sub_object_property_expression.setter
    def sub_object_property_expression(
        self,
        value: typing.Union[OWLObjectPropertyChain, OWLObjectPropertyExpression],
    ) -> None:
        """Setter for sub_object_property_expression."""
        self._sub_object_property_expression = value

    @property
    def super_object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Sets the super object property expression for this `SubObjectPropertyOf` axiom to the provided value. This operation updates the internal state of the object, effectively defining the parent property in the sub-property relationship by assigning the given `OWLObjectPropertyExpression` to the underlying private attribute.

        :param value: The object property expression to set as the super property.
        :type value: OWLObjectPropertyExpression
        """

        return self._super_object_property_expression

    @super_object_property_expression.setter
    def super_object_property_expression(
        self, value: OWLObjectPropertyExpression
    ) -> None:
        """Setter for super_object_property_expression."""
        self._super_object_property_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the sub-object property axiom formatted according to a specific functional syntax. The output string includes the axiom annotations, or an empty list if none are present, followed by the sub-property and super-property expressions. This method ensures that the annotation field is always represented, providing a consistent textual format for the axiom regardless of whether it is annotated.

        :return: A string representation of the axiom in functional syntax format, including the sub-property, super-property, and any annotations.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"SubObjectPropertyOf({self.axiom_annotations} {self.sub_object_property_expression} {self.super_object_property_expression})"
        else:
            return f"SubObjectPropertyOf([] {self.sub_object_property_expression} {self.super_object_property_expression})"
