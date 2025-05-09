import typing

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.data_range import OWLDataRange


class OWLDataMinCardinality(OWLClassExpression):
    """A data property restriction specifying the minimum number of values an individual must have for a particular data property."""

    def __init__(
        self,
        value: int,
        expression: OWLDataPropertyExpression,
        data_range: typing.Optional[OWLDataRange] = None,
    ) -> None:
        super().__init__()
        assert value >= 0
        self._cardinality: int = value
        self._data_property_expression: OWLDataPropertyExpression = expression
        self._data_range: typing.Optional[OWLDataRange] = data_range

    @property
    def cardinality(self) -> int:
        """Getter for non_negative_integer."""
        return self._cardinality

    @cardinality.setter
    def cardinality(self, value: int) -> None:
        """Setter for non_negative_integer."""
        self._cardinality = value

    @property
    def data_property_expression(self) -> OWLDataPropertyExpression:
        """Getter for data_property_expression."""
        return self._data_property_expression

    @data_property_expression.setter
    def data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expression."""
        self._data_property_expression = value

    @property
    def data_range(self) -> typing.Optional[OWLDataRange]:
        """Getter for data_range."""
        return self._data_range

    @data_range.setter
    def data_range(self, value: typing.Optional[OWLDataRange]) -> None:
        """Setter for data_range."""
        self._data_range = value

    @property
    def is_qualified(self) -> bool:
        return self.data_range is not None

    def __str__(self) -> str:
        if self.data_range:
            return f"DataMinCardinality({self.cardinality} {self.data_property_expression} {self.data_range})"
        else:
            return f"DataMinCardinality({self.cardinality} {self.data_property_expression})"
