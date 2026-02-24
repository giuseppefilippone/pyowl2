import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLEquivalentObjectProperties(OWLObjectPropertyAxiom):
    """
    This class models an axiom used to declare that a group of object properties are semantically equivalent, implying that any relationship defined by one property holds true for the others. To utilize this class, instantiate it with a list containing at least two object property expressions; providing fewer than two will raise an assertion error. The input expressions are automatically sorted upon initialization and modification to maintain a consistent internal order, and optional annotations may be attached to provide additional context or metadata about the equivalence statement.

    :param object_property_expressions: Internal storage for the sorted list of object property expressions declared to be equivalent. The list is guaranteed to contain at least two expressions.
    :type object_property_expressions: list[OWLObjectPropertyExpression]
    """

    def __init__(
        self,
        expressions: list[OWLObjectPropertyExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Constructs an axiom declaring that a collection of object properties are equivalent to one another. The initialization requires a list containing at least two object property expressions; providing fewer will trigger an assertion error. It also accepts an optional list of annotations to associate with the axiom. Internally, the provided property expressions are sorted to ensure a canonical representation, regardless of the input order.

        :param expressions: The object property expressions involved in the axiom. The list must contain at least two elements.
        :type expressions: list[OWLObjectPropertyExpression]
        :param annotations: Optional list of annotations to be associated with this axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

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
        """
        Updates the collection of object property expressions that constitute this equivalence axiom. The provided list of expressions is sorted before being assigned to the internal state, ensuring a canonical order is maintained. This method replaces the existing set of properties and creates a new list instance, meaning subsequent modifications to the input list will not affect the object's state.

        :param value: A list of OWL object property expressions to assign. The list will be sorted internally before storage.
        :type value: list[OWLObjectPropertyExpression]
        """

        return self._object_property_expressions

    @object_property_expressions.setter
    def object_property_expressions(
        self, value: list[OWLObjectPropertyExpression]
    ) -> None:
        """Setter for
        object_property_expression."""
        self._object_property_expressions = sorted(value)

    def __str__(self) -> str:
        """
        Returns a string representation of the equivalent object properties axiom, formatted to resemble a functional syntax or constructor call. The representation includes the axiom's annotations, displaying an empty list if no annotations are present, followed by the sequence of object property expressions joined by spaces. This method ensures a consistent textual format for debugging or logging purposes without modifying the underlying object state.

        :return: A string representation of the object, formatted as 'EquivalentObjectProperties(...)' including the annotations and object property expressions.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"EquivalentObjectProperties({self.axiom_annotations} {' '.join(map(str, self.object_property_expressions))})"
        else:
            return f"EquivalentObjectProperties([] {' '.join(map(str, self.object_property_expressions))})"
