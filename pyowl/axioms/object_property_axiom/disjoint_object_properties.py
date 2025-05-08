import typing
from pyowl.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl.base.annotation import OWLAnnotation
from pyowl.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLDisjointObjectProperties(OWLObjectPropertyAxiom):
    """An axiom stating that two or more object properties cannot relate the same pair of individuals."""

    def __init__(
        self,
        expressions: list[OWLObjectPropertyExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        assert len(expressions) >= 2
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._object_property_expressions: list[OWLObjectPropertyExpression] = sorted(
            expressions
        )

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def object_property_expressions(self) -> list[OWLObjectPropertyExpression]:
        """Getter for object_property_expressions."""
        return self._object_property_expressions

    @object_property_expressions.setter
    def object_property_expressions(
        self, value: list[OWLObjectPropertyExpression]
    ) -> None:
        """Setter for object_property_expressions."""
        self._object_property_expressions = sorted(value)

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"DisjointObjectProperties({self.axiom_annotations} {' '.join(map(str, self.object_property_expressions))})"
        else:
            return f"DisjointObjectProperties([] {' '.join(map(str, self.object_property_expressions))})"
