from pyowl2.abstracts.class_expression import OWLClassExpression


class OWLObjectIntersectionOf(OWLClassExpression):
    """
    This class expression models the logical intersection of multiple class expressions, defining a set of individuals that belong to all specified operands. It is constructed using a list of `OWLClassExpression` instances, which must contain at least two elements to form a valid intersection. Upon initialization or modification, the constituent expressions are automatically sorted to ensure a canonical representation, meaning the order of input does not affect the internal state or equality.

    :param classes_expressions: A sorted list of class expressions representing the operands of the intersection, guaranteed to contain at least two elements.
    :type classes_expressions: list[OWLClassExpression]
    """

    def __init__(self, expressions: list[OWLClassExpression]) -> None:
        """
        Constructs an object representing the logical intersection of a list of OWL class expressions. The input list must contain at least two elements, as an assertion is raised for smaller lists. To maintain a consistent internal state and facilitate comparison, the provided expressions are sorted before being assigned to the internal storage attribute.

        :param expressions: A list of OWL class expressions to be combined. The list must contain at least two elements.
        :type expressions: list[OWLClassExpression]
        """

        super().__init__()
        assert len(expressions) >= 2
        self._classes_expressions: list[OWLClassExpression] = sorted(expressions)

    @property
    def classes_expressions(self) -> list[OWLClassExpression]:
        """
        Sets the list of class expressions that define this intersection. The provided list is sorted before being assigned to the internal state to ensure a canonical representation, meaning the original order of the input list is not preserved. This operation modifies the object in place and requires that the elements in the list support comparison operations to be sorted successfully.

        :param value: The list of OWL class expressions to assign. The list will be sorted before being stored.
        :type value: list[OWLClassExpression]
        """

        return self._classes_expressions

    @classes_expressions.setter
    def classes_expressions(self, value: list[OWLClassExpression]) -> None:
        """Setter for classes_expressions."""
        self._classes_expressions = sorted(value)

    def __str__(self) -> str:
        """
        Returns a string representation of the object intersection using a functional syntax format. The method converts each constituent class expression to a string, joins them with spaces, and wraps the result in 'ObjectIntersectionOf(...)'. This provides a readable textual representation suitable for debugging or display purposes.

        :return: A string representation of the object intersection, formatted as 'ObjectIntersectionOf(...)' with the constituent class expressions joined by spaces.

        :rtype: str
        """

        return f"ObjectIntersectionOf({' '.join(map(str, self.classes_expressions))})"
