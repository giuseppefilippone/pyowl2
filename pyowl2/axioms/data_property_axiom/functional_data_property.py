import typing
from pyowl2.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression


class OWLFunctionalDataProperty(OWLDataPropertyAxiom):
    """An axiom stating that a data property can have at most one value for each individual."""

    def __init__(
        self,
        property: OWLDataPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._data_property_expression: OWLDataPropertyExpression = property

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def data_property_expression(self) -> OWLDataPropertyExpression:
        """Getter for data_property_expression."""
        return self._data_property_expression

    @data_property_expression.setter
    def data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expression."""
        self._data_property_expression = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"FunctionalDataProperty({self.axiom_annotations} {self.data_property_expression})"
        else:
            return f"FunctionalDataProperty([] {self.data_property_expression})"
