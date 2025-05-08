from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectHasSelf(OWLClassExpression):
    """An object property restriction stating that an individual must be related to itself via a specific object property."""

    def __init__(self, expression: OWLObjectPropertyExpression) -> None:
        super().__init__()
        self._object_property_expression: OWLObjectPropertyExpression = expression

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """Getter for object_property_expression."""
        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    def __str__(self) -> str:
        return f"ObjectHasSelf({self.object_property_expression})"
