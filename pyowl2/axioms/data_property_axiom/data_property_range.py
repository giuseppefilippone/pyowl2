import typing
from pyowl2.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.abstracts.property_range import OWLPropertyRange
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression


class OWLDataPropertyRange(OWLPropertyRange, OWLDataPropertyAxiom):
    """An axiom specifying the range of values that a data property can have."""

    def __init__(
        self,
        property: OWLDataPropertyExpression,
        data_range: OWLDataRange,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._data_property_expression: OWLDataPropertyExpression = property
        self._data_range: OWLDataRange = data_range

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

    @property
    def data_range(self) -> OWLDataRange:
        """Getter for data_range."""
        return self._data_range

    @data_range.setter
    def data_range(self, value: OWLDataRange) -> None:
        """Setter for data_range."""
        self._data_range = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"DataPropertyRange({self.axiom_annotations} {self.data_property_expression} {self.data_range})"
        else:
            return f"DataPropertyRange([] {self.data_property_expression} {self.data_range})"
