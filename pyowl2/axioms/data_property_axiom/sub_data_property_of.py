import typing
from pyowl2.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression


class OWLSubDataPropertyOf(OWLDataPropertyAxiom):
    """An axiom stating that one data property is a subproperty of another data property."""

    def __init__(
        self,
        sub_property: OWLDataPropertyExpression,
        super_property: OWLDataPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
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
        """Getter for sub_data_property_expression."""
        return self._sub_data_property_expression

    @sub_data_property_expression.setter
    def sub_data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expressions."""
        self._sub_data_property_expression = value

    @property
    def super_data_property_expression(self) -> OWLDataPropertyExpression:
        """Getter for super_data_property_expression."""
        return self._super_data_property_expression

    @super_data_property_expression.setter
    def super_data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expressions."""
        self._super_data_property_expression = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"SubDataPropertyOf({self.axiom_annotations} {self.sub_data_property_expression} {self.super_data_property_expression})"
        else:
            return f"SubDataPropertyOf([] {self.sub_data_property_expression} {self.super_data_property_expression})"
