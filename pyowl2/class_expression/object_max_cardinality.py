import typing

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectMaxCardinality(OWLClassExpression):
    """An object property restriction specifying the maximum number of individuals to which an individual can be related via a specific object property."""

    def __init__(
        self,
        value: int,
        property: OWLObjectPropertyExpression,
        expression: typing.Optional[OWLClassExpression] = None,
    ) -> None:
        super().__init__()
        assert value >= 0
        self._cardinality: int = value
        self._object_property_expression: OWLObjectPropertyExpression = property
        self._class_expression: typing.Optional[OWLClassExpression] = expression

    @property
    def cardinality(self) -> int:
        """Getter for non_negative_integer."""
        return self._cardinality

    @cardinality.setter
    def cardinality(self, value: int) -> None:
        """Setter for non_negative_integer."""
        self._cardinality = value

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """Getter for object_property_expression."""
        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    @property
    def class_expression(self) -> typing.Optional[OWLClassExpression]:
        """Getter for class_expression."""
        return self._class_expression

    @class_expression.setter
    def class_expression(self, value: typing.Optional[OWLClassExpression]) -> None:
        """Setter for class_expression."""
        self._class_expression = value

    @property
    def is_qualified(self) -> bool:
        return self.class_expression is not None

    def __str__(self) -> str:
        if self.class_expression:
            return f"ObjectMaxCardinality({self.cardinality} {self.object_property_expression} {self.class_expression})"
        else:
            return f"ObjectMaxCardinality({self.cardinality} {self.object_property_expression})"
