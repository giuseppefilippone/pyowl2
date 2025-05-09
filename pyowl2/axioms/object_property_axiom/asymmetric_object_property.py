import typing
from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLAsymmetricObjectProperty(OWLObjectPropertyAxiom):
    """An axiom stating that if a property relates one individual to another, the inverse relation does not hold."""

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._object_property_expression: OWLObjectPropertyExpression = expression

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

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"AsymmetricObjectProperty({self.axiom_annotations} {self.object_property_expression})"
        else:
            return f"AsymmetricObjectProperty([] {self.object_property_expression})"
