import typing

from pyowl.abstracts.class_axiom import OWLClassAxiom
from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.base.annotation import OWLAnnotation


class OWLDisjointClasses(OWLClassAxiom):
    """An axiom stating that two or more classes have no individuals in common."""

    def __init__(
        self,
        expressions: list[OWLClassExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        assert len(expressions) >= 2
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._class_expressions: list[OWLClassExpression] = sorted(expressions)

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def class_expressions(self) -> list[OWLClassExpression]:
        """Getter for class_expressions."""
        return self._class_expressions

    @class_expressions.setter
    def class_expressions(self, value: list[OWLClassExpression]) -> None:
        """Setter for class_expressions."""
        self._class_expressions = sorted(value)

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"DisjointClasses({self.axiom_annotations} {' '.join(map(str, self.class_expressions))})"
        else:
            return f"DisjointClasses([] {' '.join(map(str, self.class_expressions))})"
