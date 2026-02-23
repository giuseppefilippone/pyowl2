from pyowl2.abstracts.class_expression import OWLClassExpression


class OWLObjectComplementOf(OWLClassExpression):
    """
    This class represents a logical negation within an ontology, defining the set of all individuals that do not belong to a specified class expression. It serves as a wrapper around another class expression, which may be a simple named class or a complex logical construct, effectively inverting its membership criteria to represent concepts such as "non-human" or "not a parent." To utilize this functionality, an instance is created by passing the target class expression to the constructor, and the internal expression can be accessed or modified via the corresponding property, enabling the dynamic definition of exclusionary constraints in knowledge representation.

    :parm expression: The class expression acting as the operand for the complement operation, representing the specific class being negated.
    :type expression: OWLClassExpression
    """

    def __init__(self, expression: OWLClassExpression) -> None:
        """
        Constructs an instance representing the logical complement (negation) of a specific OWL class expression. This initializer accepts a single argument, `expression`, which defines the operand to be negated and is stored internally for subsequent access. The method also ensures that the initialization logic defined by the parent class is executed to establish the correct object state.

        :param expression: The OWL class expression to be represented by this instance.
        :type expression: OWLClassExpression
        """

        super().__init__()
        self._expression: OWLClassExpression = expression

    @property
    def expression(self) -> OWLClassExpression:
        """
        Updates the class expression that serves as the operand for this object complement. The method accepts a single argument, `value`, which should be an instance of `OWLClassExpression`. Assigning this value modifies the internal state of the object, specifically replacing the stored expression with the new one provided.

        :param value:
        :type value: OWLClassExpression
        """

        return self._expression

    @expression.setter
    def expression(self, value: OWLClassExpression) -> None:
        """Setter for expression."""
        self._expression = value

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the object complement using a functional syntax style. The output is constructed by concatenating the class name with the string representation of the internal expression, enclosed in parentheses. This method is primarily used for debugging and logging, and it relies on the nested expression having a valid string conversion method, though it does not modify the object's state.

        :return: A string representation of the object, formatted as "ObjectComplementOf(expression)".

        :rtype: str
        """

        return f"ObjectComplementOf({self.expression})"
