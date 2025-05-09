from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression


class OWLDataAllValuesFrom(OWLClassExpression):
    """A data property restriction specifying that all values for a particular data property must come from a specified data range."""

    def __init__(
        self, expressions: list[OWLDataPropertyExpression], data_range: OWLDataRange
    ) -> None:
        super().__init__()
        assert len(expressions) >= 1
        self._data_property_expressions: list[OWLDataPropertyExpression] = sorted(
            expressions
        )
        self._data_range: OWLDataRange = data_range

    @property
    def data_property_expressions(self) -> list[OWLDataPropertyExpression]:
        """Getter for data_property_expressions."""
        return self._data_property_expressions

    @data_property_expressions.setter
    def data_property_expressions(self, value: list[OWLDataPropertyExpression]) -> None:
        """Setter for data_property_expressions."""
        self._data_property_expressions = sorted(value)

    @property
    def data_range(self) -> OWLDataRange:
        """Getter for data_range."""
        return self._data_range

    @data_range.setter
    def data_range(self, value: OWLDataRange) -> None:
        """Setter for data_range."""
        self._data_range = value

    def __str__(self) -> str:
        return f"DataAllValuesFrom({' '.join(map(str, self.data_property_expressions))} {self.data_range})"
