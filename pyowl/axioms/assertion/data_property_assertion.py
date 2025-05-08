import typing

from pyowl.abstracts.assertion import OWLAssertion
from pyowl.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl.abstracts.individual import OWLIndividual
from pyowl.base.annotation import OWLAnnotation
from pyowl.literal.literal import OWLLiteral


class OWLDataPropertyAssertion(OWLAssertion):
    """An axiom stating that a specific individual has a particular data value for a given data property."""

    def __init__(
        self,
        expression: OWLDataPropertyExpression,
        source: OWLIndividual,
        value: OWLLiteral,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._data_property_expression: OWLDataPropertyExpression = expression
        self._source_individual: OWLIndividual = source
        self._target_value: OWLLiteral = value

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def data_property_expression(self) -> OWLDataPropertyExpression:
        """Getter for data_property_expression."""
        return self._data_property_expression

    @data_property_expression.setter
    def data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expression."""
        self._data_property_expression = value

    @property
    def source_individual(self) -> OWLIndividual:
        """Getter for source_individual."""
        return self._source_individual

    @source_individual.setter
    def source_individual(self, value: OWLIndividual) -> None:
        """Setter for source_individual."""
        self._source_individual = value

    @property
    def target_value(self) -> OWLLiteral:
        """Getter for target_value."""
        return self._target_value

    @target_value.setter
    def target_value(self, value: OWLLiteral) -> None:
        """Setter for target_value."""
        self._target_value = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"DataPropertyAssertion({self.axiom_annotations} {self.data_property_expression} {self.source_individual} {self.target_value})"
        else:
            return f"DataPropertyAssertion([] {self.data_property_expression} {self.source_individual} {self.target_value})"
