import typing
from pyowl2.abstracts.class_axiom import OWLClassAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLSubClassOf(OWLClassAxiom):
    """An axiom stating that one class is a subclass of another, meaning all instances of the subclass are also instances of the superclass."""

    def __init__(
        self,
        sub_class: OWLClassExpression,
        super_class: OWLClassExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._sub_class_expression: OWLClassExpression = sub_class
        self._super_class_expression: OWLClassExpression = super_class

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def sub_class_expression(self) -> OWLClassExpression:
        """Getter for sub_class_expression."""
        return self._sub_class_expression

    @sub_class_expression.setter
    def sub_class_expression(self, value: OWLClassExpression) -> None:
        """Setter for sub_class_expression."""
        self._sub_class_expression = value

    @property
    def super_class_expression(self) -> OWLClassExpression:
        """Getter for super_class_expression."""
        return self._super_class_expression

    @super_class_expression.setter
    def super_class_expression(self, value: OWLClassExpression) -> None:
        """Setter for super_class_expression."""
        self._super_class_expression = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"SubClassOf({self.axiom_annotations} {self.sub_class_expression} {self.super_class_expression})"
        else:
            return f"SubClassOf([] {self.sub_class_expression} {self.super_class_expression})"
