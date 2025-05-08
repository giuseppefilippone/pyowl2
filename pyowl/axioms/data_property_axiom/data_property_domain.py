import typing
from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl.base.annotation import OWLAnnotation
from pyowl.abstracts.data_property_expression import OWLDataPropertyExpression


class OWLDataPropertyDomain(OWLDataPropertyAxiom):
    """An axiom specifying the class of individuals to which a data property applies."""

    def __init__(
        self,
        property: OWLDataPropertyExpression,
        expression: OWLClassExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._data_property_expression: OWLDataPropertyExpression = property
        self._class_expression: OWLClassExpression = expression

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
    def class_expression(self) -> OWLClassExpression:
        """Getter for class_expression."""
        return self._class_expression

    @class_expression.setter
    def class_expression(self, value: OWLClassExpression) -> None:
        """Setter for class_expression."""
        self._class_expression = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"DataPropertyDomain({self.axiom_annotations} {self.data_property_expression} {self.class_expression})"
        else:
            return f"DataPropertyDomain([] {self.data_property_expression} {self.class_expression})"
