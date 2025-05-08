import typing
from pyowl.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl.base.annotation import OWLAnnotation
from pyowl.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLSymmetricObjectProperty(OWLObjectPropertyAxiom):
    """An axiom stating that if an object property relates A to B, then it must also relate B to A."""

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = (
        #     sorted(annotations) if annotations else annotations
        # )
        self._object_property_expression: OWLObjectPropertyExpression = expression

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = sorted(value) if value else value

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
            return f"SymmetricObjectProperty({self.axiom_annotations} {self.object_property_expression})"
        else:
            return f"SymmetricObjectProperty([] {self.object_property_expression})"
