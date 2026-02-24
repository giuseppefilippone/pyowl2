import typing

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.data_range import OWLDataRange


class OWLDataExactCardinality(OWLClassExpression):
    """
    This class represents a restriction used in ontology modeling to define that an individual must have exactly a specific number of values for a given data property. It functions as a class expression that can be used to construct complex class definitions, ensuring that instances satisfy a precise count of data property assertions. To use this class, instantiate it with a non-negative integer representing the required cardinality, a data property expression identifying the relationship, and an optional data range to constrain the type of values counted. If the data range is provided, the restriction becomes qualified, meaning the exact count applies only to values that fall within that specific range; otherwise, the count applies to all values associated with the property.

    :param cardinality: Stores the non-negative integer defining the exact number of data property values required for an individual to satisfy this restriction.
    :type cardinality: int
    :param data_property_expression: The data property expression that defines the relationship between the subject individual and the data values.
    :type data_property_expression: OWLDataPropertyExpression
    :param data_range: Optional data range that restricts the specific values the data property must take. If provided, the restriction is qualified, requiring the exact number of values to fall within this range; otherwise, the restriction applies to any data value.
    :type data_range: typing.Optional[OWLDataRange]
    """

    def __init__(
        self,
        value: int,
        expression: OWLDataPropertyExpression,
        data_range: typing.Optional[OWLDataRange] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL data exact cardinality restriction, which constrains individuals to have exactly a specific number of values for a given data property. The constructor accepts a non-negative integer for the cardinality, a data property expression to be restricted, and an optional data range that the values must satisfy. It performs an assertion to ensure the cardinality value is not negative and stores the provided arguments as internal attributes for subsequent access.

        :param value: Non-negative integer representing the cardinality of the restriction.
        :type value: int
        :param expression: The data property expression that the restriction applies to.
        :type expression: OWLDataPropertyExpression
        :param data_range: The data range that restricts the values of the data property expression, or None if the restriction is unqualified.
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
        Updates the exact number of values required for the data property restriction represented by this instance. This setter assigns the provided integer value to the internal `_cardinality` attribute, effectively modifying the constraint definition. It allows the specific cardinality of the `OWLDataExactCardinality` object to be changed after it has been created.

        :param value: The new count or size to assign.
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
        Assigns the specified data property expression to this exact cardinality restriction, replacing any previously held value. This method directly modifies the internal state of the object by updating the private attribute storing the property expression. While the type hint expects an instance of `OWLDataPropertyExpression`, the implementation performs no runtime validation, so passing an incompatible type may lead to errors in subsequent operations.

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
        Assigns a new data range to this exact cardinality restriction, replacing any previously defined range. The method accepts an optional `OWLDataRange` instance; setting the value to `None` effectively removes the data range constraint. This operation directly modifies the internal state of the object by updating the underlying `_data_range` attribute.

        :param value: The OWL data range to assign, or None to clear the property.
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
        Determines whether this exact cardinality restriction is qualified by a specific data range. In the context of OWL, a qualified restriction limits the count to values that belong to a particular datatype, whereas an unqualified restriction applies to all values of the property. This property returns `True` if the `data_range` attribute is defined, and `False` if it is `None`.

        :return: True if a data range is defined, False otherwise.

        :rtype: bool
        """

        return self.data_range is not None

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the data exact cardinality restriction, formatted in a functional syntax style. The output includes the specific cardinality value and the associated data property expression. If the restriction defines a specific data range, this range is appended to the string; otherwise, the representation consists solely of the cardinality and the property. This method does not modify the state of the object.

        :return: A string representation of the object, formatted to include the cardinality, data property expression, and optionally the data range.

        :rtype: str
        """

        if self.data_range:
            return f"DataExactCardinality({self.cardinality} {self.data_property_expression} {self.data_range})"
        else:
            return f"DataExactCardinality({self.cardinality} {self.data_property_expression})"
