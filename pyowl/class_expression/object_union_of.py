from pyowl.abstracts.class_expression import OWLClassExpression


class OWLObjectUnionOf(OWLClassExpression):
    """A class expression representing the union of multiple classes, containing individuals that belong to at least one of the given classes."""

    def __init__(self, expressions: list[OWLClassExpression]) -> None:
        super().__init__()
        assert len(expressions) >= 2
        self._classes_expressions: list[OWLClassExpression] = sorted(expressions)

    @property
    def classes_expressions(self) -> list[OWLClassExpression]:
        """Getter for classes_expressions."""
        return self._classes_expressions

    @classes_expressions.setter
    def classes_expressions(self, value: list[OWLClassExpression]) -> None:
        """Setter for classes_expressions."""
        self._classes_expressions = sorted(value)

    def __str__(self) -> str:
        return f"ObjectUnionOf({' '.join(map(str, self.classes_expressions))})"
