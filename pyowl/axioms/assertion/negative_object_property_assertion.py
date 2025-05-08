import typing

from pyowl.abstracts.assertion import OWLAssertion
from pyowl.abstracts.individual import OWLIndividual
from pyowl.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl.base.annotation import OWLAnnotation


class OWLNegativeObjectPropertyAssertion(OWLAssertion):
    """An axiom stating that a specific object property does not relate a pair of individuals."""

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        source: OWLIndividual,
        target: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._object_property_expression: OWLObjectPropertyExpression = expression
        self._source_individual: OWLIndividual = source
        self._target_individual: OWLIndividual = target

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """Getter for object_property_expression."""
        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    @property
    def source_individual(self) -> OWLIndividual:
        """Getter for source_individual."""
        return self._source_individual

    @source_individual.setter
    def source_individual(self, value: OWLIndividual) -> None:
        """Setter for source_individual."""
        self._source_individual = value

    @property
    def target_individual(self) -> OWLIndividual:
        """Getter for target_individual."""
        return self._target_individual

    @target_individual.setter
    def target_individual(self, value: OWLIndividual) -> None:
        """Setter for target_individual."""
        self._target_individual = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"NegativeObjectPropertyAssertion({self.axiom_annotations} {self.object_property_expression} {self.source_individual} {self.target_individual})"
        else:
            return f"NegativeObjectPropertyAssertion([] {self.object_property_expression} {self.source_individual} {self.target_individual})"
