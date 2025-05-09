import typing

from pyowl2.abstracts.class_axiom import OWLClassAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.owl_class import OWLClass


class OWLDisjointUnion(OWLClassAxiom):
    """An axiom stating that a class is equivalent to the union of several disjoint classes."""

    def __init__(
        self,
        expression: OWLClass,
        expressions: list[OWLClassExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        assert len(expressions) >= 2
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._union_class: OWLClass = expression
        self._disjoint_class_expressions: list[OWLClassExpression] = sorted(expressions)

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def union_class(self) -> OWLClass:
        """Getter for union_class."""
        return self._union_class

    @union_class.setter
    def union_class(self, value: OWLClass) -> None:
        """Setter for union_class."""
        self._union_class = value

    @property
    def disjoint_class_expressions(self) -> list[OWLClassExpression]:
        """Getter for disjointc_class_expressions."""
        return self._disjoint_class_expressions

    @disjoint_class_expressions.setter
    def disjoint_class_expressions(self, value: list[OWLClassExpression]) -> None:
        """Setter for disjointc_class_expressions."""
        self._disjoint_class_expressions = sorted(value)

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"DisjointUnion({self.axiom_annotations} {self.union_class} {' '.join(map(str, self.disjoint_class_expressions))})"
        else:
            return f"DisjointUnion([] {self.union_class} {' '.join(map(str, self.disjoint_class_expressions))})"
