from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.abstracts.individual import OWLIndividual
from pyowl.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectHasValue(OWLClassExpression):
    """An object property restriction specifying that an individual must be related to a specific individual via a particular object property."""

    def __init__(
        self, property: OWLObjectPropertyExpression, individual: OWLIndividual
    ) -> None:
        super().__init__()
        self._object_property_expression: OWLObjectPropertyExpression = property
        self._individual: OWLIndividual = individual

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """Getter for object_property_expression."""
        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    @property
    def individual(self) -> OWLIndividual:
        """Getter for individual."""
        return self._individual

    @individual.setter
    def individual(self, value: OWLIndividual) -> None:
        """Setter for individual."""
        self._individual = value

    def __str__(self) -> str:
        return f"ObjectHasValue({self.object_property_expression} {self.individual})"
