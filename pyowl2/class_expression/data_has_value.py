from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.literal.literal import OWLLiteral


class OWLDataHasValue(OWLClassExpression):
    """
    This class represents a restriction in the Web Ontology Language (OWL) that defines a class of individuals based on the existence of a specific data property value. It asserts that an individual belongs to the defined class if it possesses a particular data property filled with a specific literal value, such as having an age of exactly 30. By encapsulating a data property expression and a target literal, this entity enables the precise formulation of class definitions that depend on concrete data assertions within an ontology.

    :parm data_property_expression: The data property expression that defines the relationship between the subject individual and the specific literal value required by the restriction.
    :type data_property_expression: OWLDataPropertyExpression
    :parm literal: The specific literal value that the data property expression must take for the restriction to be satisfied.
    :type literal: OWLLiteral
    """

    def __init__(
        self, expression: OWLDataPropertyExpression, literal: OWLLiteral
    ) -> None:
        """
        Initializes a new instance representing an OWL data has value restriction, which defines a class of individuals that possess a specific data property with a given literal value. The constructor accepts a data property expression and a literal, storing them internally to define the restriction's criteria. It invokes the superclass initializer to ensure proper inheritance chain setup.

        :param expression: The OWL data property expression associated with this object.
        :type expression: OWLDataPropertyExpression
        :param literal: The OWL literal value associated with the data property expression.
        :type literal: OWLLiteral
        """

        super().__init__()
        self._data_property_expression: OWLDataPropertyExpression = expression
        self._literal: OWLLiteral = literal

    @property
    def data_property_expression(self) -> OWLDataPropertyExpression:
        """
        Assigns the specified data property expression to this `OWLDataHasValue` restriction, updating the internal state of the object. This method replaces any previously associated data property expression with the provided value, which must be an instance of `OWLDataPropertyExpression`. The modification effectively changes which data property is being constrained by this specific class expression.

        :param value: The OWL data property expression to assign to the object.
        :type value: OWLDataPropertyExpression
        """

        return self._data_property_expression

    @data_property_expression.setter
    def data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expression."""
        self._data_property_expression = value

    @property
    def literal(self) -> OWLLiteral:
        """
        Updates the specific literal value associated with this data property restriction. The method accepts an OWLLiteral object and assigns it to the internal state, effectively defining the concrete value that the data property must match. This operation overwrites any previously stored literal and does not return a value.

        :param value: The OWL literal value to set.
        :type value: OWLLiteral
        """

        return self._literal

    @literal.setter
    def literal(self, value: OWLLiteral) -> None:
        """Setter for literal."""
        self._literal = value

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the data property value restriction, formatted in a functional syntax style. The resulting string concatenates the class name with the string representations of the underlying data property expression and the literal value, separated by a space within parentheses. This representation is useful for debugging and logging, and it has no side effects on the object's internal state.

        :return: A string representation of the object, formatted as 'DataHasValue(data_property_expression literal)'.

        :rtype: str
        """

        return f"DataHasValue({self.data_property_expression} {self.literal})"
