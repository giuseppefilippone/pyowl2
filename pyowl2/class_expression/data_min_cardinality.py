import typing

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.data_range import OWLDataRange


class OWLDataMinCardinality(OWLClassExpression):
    """
    This class represents a restriction within an ontology that defines a minimum threshold for the number of data values an individual must possess for a specific data property. It functions by combining a non-negative integer cardinality with a data property expression to specify that a valid individual must have at least that many associated values. Users can optionally provide a data range to create a qualified restriction, which constrains the count to only those values that match a specific datatype or set of literals, thereby enabling precise definitions of class characteristics.

    :param cardinality: The minimum number of values an individual must possess for the specified data property, represented as a non-negative integer.
    :type cardinality: int
    :param data_property_expression: Defines the relationship between the subject individual and the data values subject to the minimum cardinality restriction.
    :type data_property_expression: OWLDataPropertyExpression
    :param data_range: An optional data range that restricts the specific values counted towards the minimum cardinality. If provided, the restriction is qualified, requiring the minimum number of values to belong to this range; otherwise, it applies to any values of the data property.
    :type data_range: typing.Optional[OWLDataRange]
    """

    def __init__(
        self,
        value: int,
        expression: OWLDataPropertyExpression,
        data_range: typing.Optional[OWLDataRange] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL data minimum cardinality restriction, which defines that a specific data property must have at least a certain number of values. The constructor accepts a non-negative integer for the cardinality, a data property expression to be restricted, and an optional data range to constrain the type of the values. It asserts that the cardinality value is not negative, raising an error if this condition is violated, and stores the provided arguments as internal attributes.

        :param value: The non-negative integer value representing the cardinality.
        :type value: int
        :param expression: The OWL data property expression upon which the restriction is applied.
        :type expression: OWLDataPropertyExpression
        :param data_range: The optional data range restricting the values of the data property expression.
        :type data_range: typing.Optional[OWLDataRange]
        """

        super().__init__()
        assert value >= 0
        self._cardinality: int = value
        self._data_property_expression: OWLDataPropertyExpression = expression
        self._data_range: typing.Optional[OWLDataRange] = data_range

    @property
    def cardinality(self) -> int:
        """
        Assigns the provided integer value to the internal `_cardinality` attribute, thereby updating the minimum cardinality constraint for this OWL data restriction. This operation modifies the object's state in place. Although the method accepts any integer, standard OWL semantics imply that the value should be non-negative, though this specific implementation does not enforce validation.

        :param value: The new value for the cardinality.
        :type value: int
        """

        return self._cardinality

    @cardinality.setter
    def cardinality(self, value: int) -> None:
        """Setter for cardinality."""
        self._cardinality = value

    @property
    def data_property_expression(self) -> OWLDataPropertyExpression:
        """
        Updates the specific data property expression to which this minimum cardinality restriction applies. This setter assigns the provided `OWLDataPropertyExpression` instance to the internal state, overwriting any existing value. As a side effect, the object's state is mutated to reflect the new property definition.

        :param value: The OWL data property expression to assign to the object.
        :type value: OWLDataPropertyExpression
        """

        return self._data_property_expression

    @data_property_expression.setter
    def data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expression."""
        self._data_property_expression = value

    @property
    def data_range(self) -> typing.Optional[OWLDataRange]:
        """
        Sets the data range for this OWL minimum cardinality restriction. This method updates the internal state by assigning the provided `OWLDataRange` instance (or None) to the underlying private attribute, effectively replacing the existing data type constraint that property values must satisfy.

        :param value: The OWL data range to assign, or None to clear the value.
        :type value: typing.Optional[OWLDataRange]
        """

        return self._data_range

    @data_range.setter
    def data_range(self, value: typing.Optional[OWLDataRange]) -> None:
        """Setter for data_range."""
        self._data_range = value

    @property
    def is_qualified(self) -> bool:
        """
        Indicates whether this minimum cardinality restriction is qualified by a specific data range. In the context of OWL, a restriction is considered qualified if it limits the count of values to those belonging to a particular data type, rather than applying to all values of the associated data property. This property returns True if a data range is explicitly defined for the restriction, and False otherwise.

        :return: True if the data range is not None, indicating the instance is qualified.

        :rtype: bool
        """

        return self.data_range is not None

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the OWL data minimum cardinality restriction, formatted using a functional syntax. The output includes the cardinality value and the associated data property expression, enclosed within parentheses and prefixed by 'DataMinCardinality'. If a specific data range is defined for the restriction, it is appended to the string; otherwise, the representation consists solely of the cardinality and the property expression.

        :return: A string representation of the data minimum cardinality restriction, comprising the cardinality, data property expression, and optionally the data range.

        :rtype: str
        """

        if self.data_range:
            return f"DataMinCardinality({self.cardinality} {self.data_property_expression} {self.data_range})"
        else:
            return f"DataMinCardinality({self.cardinality} {self.data_property_expression})"
