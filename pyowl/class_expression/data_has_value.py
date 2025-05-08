from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl.literal.literal import OWLLiteral


class OWLDataHasValue(OWLClassExpression):
    """A data property restriction specifying that a particular data property must have at least one specific value."""

    def __init__(
        self, expression: OWLDataPropertyExpression, literal: OWLLiteral
    ) -> None:
        super().__init__()
        self._data_property_expression: OWLDataPropertyExpression = expression
        self._literal: OWLLiteral = literal

    @property
    def data_property_expression(self) -> OWLDataPropertyExpression:
        """Getter for data_property_expression."""
        return self._data_property_expression

    @data_property_expression.setter
    def data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expression."""
        self._data_property_expression = value

    @property
    def literal(self) -> OWLLiteral:
        """Getter for literal."""
        return self._literal

    @literal.setter
    def literal(self, value: OWLLiteral) -> None:
        """Setter for literal."""
        self._literal = value

    def __str__(self) -> str:
        return f"DataHasValue({self.data_property_expression} {self.literal})"
