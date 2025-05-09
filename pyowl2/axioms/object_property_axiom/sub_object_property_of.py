import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.axioms.object_property_axiom.object_property_chain import (
    OWLObjectPropertyChain,
)
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLSubObjectPropertyOf(OWLObjectPropertyAxiom):
    """An axiom stating that one object property is a subproperty of another object property."""

    def __init__(
        self,
        sub_property: typing.Union[OWLObjectPropertyChain, OWLObjectPropertyExpression],
        super_property: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
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
        """Getter for sub_object_property_expression."""
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
        """Getter for super_object_property_expression."""
        return self._super_object_property_expression

    @super_object_property_expression.setter
    def super_object_property_expression(
        self, value: OWLObjectPropertyExpression
    ) -> None:
        """Setter for super_object_property_expression."""
        self._super_object_property_expression = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"SubObjectPropertyOf({self.axiom_annotations} {self.sub_object_property_expression} {self.super_object_property_expression})"
        else:
            return f"SubObjectPropertyOf([] {self.sub_object_property_expression} {self.super_object_property_expression})"
