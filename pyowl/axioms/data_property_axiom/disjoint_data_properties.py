import typing
from pyowl.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl.base.annotation import OWLAnnotation
from pyowl.abstracts.data_property_expression import OWLDataPropertyExpression


class OWLDisjointDataProperties(OWLDataPropertyAxiom):
    """An axiom stating that two or more data properties cannot have the same values for the same individual."""

    def __init__(
        self,
        expressions: list[OWLDataPropertyExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        assert len(expressions) >= 2
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._data_property_expressions: list[OWLDataPropertyExpression] = sorted(expressions)

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def data_property_expressions(self) -> list[OWLDataPropertyExpression]:
        """Getter for data_property_expressions."""
        return self._data_property_expressions

    @data_property_expressions.setter
    def data_property_expressions(self, value: list[OWLDataPropertyExpression]) -> None:
        """Setter for data_property_expressions."""
        self._data_property_expressions = sorted(value)

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"DisjointDataProperties({self.axiom_annotations} {' '.join(map(str, self.data_property_expressions))})"
        else:
            return f"DisjointDataProperties([] {' '.join(map(str, self.data_property_expressions))})"
