import typing

from pyowl2.abstracts.assertion import OWLAssertion
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.base.annotation import OWLAnnotation


class OWLClassAssertion(OWLAssertion):
    """An axiom stating that a specific individual is an instance of a particular class."""

    def __init__(
        self,
        expression: OWLClassExpression,
        individual: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._class_expression: OWLClassExpression = expression
        self._individual: OWLIndividual = individual

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def class_expression(self) -> OWLClassExpression:
        """Getter for class_expression."""
        return self._class_expression

    @class_expression.setter
    def class_expression(self, value: OWLClassExpression) -> None:
        """Setter for class_expression."""
        self._class_expression = value

    @property
    def individual(self) -> OWLIndividual:
        """Getter for individual."""
        return self._individual

    @individual.setter
    def individual(self, value: OWLIndividual) -> None:
        """Setter for individual."""
        self._individual = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"ClassAssertion({self.axiom_annotations} {self.class_expression} {self.individual})"
        else:
            return f"ClassAssertion([] {self.class_expression} {self.individual})"
