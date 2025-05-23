from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectAllValuesFrom(OWLClassExpression):
    """An object property restriction specifying that all values for a particular object property must be instances of a specified class."""

    def __init__(
        self, property: OWLObjectPropertyExpression, expression: OWLClassExpression
    ) -> None:
        super().__init__()
        self._object_property_expression: OWLObjectPropertyExpression = property
        self._class_expression: OWLClassExpression = expression

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """Getter for object_property_expression."""
        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    @property
    def class_expression(self) -> OWLClassExpression:
        """Getter for class_expression."""
        return self._class_expression

    @class_expression.setter
    def class_expression(self, value: OWLClassExpression) -> None:
        """Setter for class_expression."""
        self._class_expression = value

    def __str__(self) -> str:
        return f"ObjectAllValuesFrom({self.object_property_expression} {self.class_expression})"
