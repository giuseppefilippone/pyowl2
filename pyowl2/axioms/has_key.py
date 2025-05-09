import typing

from pyowl2.abstracts.class_axiom import OWLClassAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLHasKey(OWLClassAxiom):
    """An axiom specifying a set of properties that uniquely identify instances of a particular class."""

    def __init__(
        self,
        expression: OWLClassExpression,
        object_properties: list[OWLObjectPropertyExpression],
        data_properties: list[OWLDataPropertyExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = sorted(annotations) if annotations else annotations
        self._class_expression: OWLClassExpression = expression
        self._object_property_expressions: list[OWLObjectPropertyExpression] = sorted(
            object_properties
        )
        self._data_property_expressions: list[OWLDataPropertyExpression] = sorted(
            data_properties
        )

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = sorted(value) if value else value

    @property
    def class_expression(self) -> OWLClassExpression:
        """Getter for class_expression."""
        return self._class_expression

    @class_expression.setter
    def class_expression(self, value: OWLClassExpression) -> None:
        """Setter for class_expression."""
        self._class_expression = value

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
            return f"HasKey({self.axiom_annotations} {self.class_expression}({' '.join(map(str, self.object_property_expressions))})({' '.join(map(str, self.data_property_expressions))}))"
        else:
            return f"HasKey([] {self.class_expression}({' '.join(map(str, self.object_property_expressions))})({' '.join(map(str, self.data_property_expressions))}))"
