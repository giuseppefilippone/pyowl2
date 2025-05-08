import typing
from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl.base.annotation import OWLAnnotation
from pyowl.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectPropertyDomain(OWLObjectPropertyAxiom):
    """An axiom specifying the class of individuals to which an object property applies."""

    def __init__(
        self,
        property: OWLObjectPropertyExpression,
        expression: OWLClassExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = (
        #     sorted(annotations) if annotations else annotations
        # )
        self._object_property_expression: OWLObjectPropertyExpression = property
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
        if self.axiom_annotations:
            return f"ObjectPropertyDomain({self.axiom_annotations} {self.object_property_expression} {self.class_expression})"
        else:
            return f"ObjectPropertyDomain([] {self.object_property_expression} {self.class_expression})"
