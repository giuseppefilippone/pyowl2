from pyowl.abstracts.class_expression import OWLClassExpression


class OWLObjectComplementOf(OWLClassExpression):
    """A class expression representing the complement of a given class, containing all individuals not in the specified class."""

    def __init__(self, expression: OWLClassExpression) -> None:
        super().__init__()
        self._expression: OWLClassExpression = expression

    @property
    def expression(self) -> OWLClassExpression:
        """Getter for expression."""
        return self._expression

    @expression.setter
    def expression(self, value: OWLClassExpression) -> None:
        """Setter for value."""
        self._expression = value

    def __str__(self) -> str:
        return f"ObjectComplementOf({self.expression})"
