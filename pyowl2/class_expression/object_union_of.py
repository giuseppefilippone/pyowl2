from pyowl2.abstracts.class_expression import OWLClassExpression


class OWLObjectUnionOf(OWLClassExpression):
    """
    This class models a logical union (disjunction) of class expressions, defining a group of individuals that belong to at least one of the constituent classes. It is used to construct complex, inclusive definitions within an ontology by combining multiple class criteria. When initializing or modifying this object, a list of at least two `OWLClassExpression` instances must be provided; the list is automatically sorted to ensure a consistent internal representation.

    :parm classes_expressions: Sorted list of class expressions comprising the union, containing at least two elements.
    :type classes_expressions: list[OWLClassExpression]
    """

    def __init__(self, expressions: list[OWLClassExpression]) -> None:
        """
        Constructs an object representing the logical union (disjunction) of the provided OWL class expressions. This initializer requires that the input list contains at least two class expressions, as a union of fewer elements is not supported by this specific implementation. The expressions are sorted internally before being stored, which normalizes the representation for comparison and hashing purposes, effectively disregarding the original input order.

        :param expressions: A list of OWL class expressions to be combined. The list must contain at least two elements.
        :type expressions: list[OWLClassExpression]
        """

        super().__init__()
        assert len(expressions) >= 2
        self._classes_expressions: list[OWLClassExpression] = sorted(expressions)

    @property
    def classes_expressions(self) -> list[OWLClassExpression]:
        """
        Assigns a new list of class expressions to serve as the operands for this union. The input list is sorted before being stored internally to maintain a consistent, canonical order, regardless of the order provided by the caller. This method replaces the existing collection of expressions rather than modifying it in place.

        :param value: A list of OWL class expressions to assign. The list will be sorted before storage.
        :type value: list[OWLClassExpression]
        """

        return self._classes_expressions

    @classes_expressions.setter
    def classes_expressions(self, value: list[OWLClassExpression]) -> None:
        """Setter for classes_expressions."""
        self._classes_expressions = sorted(value)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the object union expression. The output is formatted by concatenating the literal "ObjectUnionOf(" with the string representations of the constituent class expressions, which are joined by single spaces, and terminating with a closing parenthesis. This method provides a standard functional syntax view of the logical structure without modifying the object's state.

        :return: A string representation of the object union, formatted as "ObjectUnionOf(...)" containing the string representations of the constituent class expressions.

        :rtype: str
        """

        return f"ObjectUnionOf({' '.join(map(str, self.classes_expressions))})"
