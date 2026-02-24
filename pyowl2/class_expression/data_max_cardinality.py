import typing

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.data_range import OWLDataRange


class OWLDataMaxCardinality(OWLClassExpression):
    """
    This class represents a restriction in an ontology that defines the maximum number of data values an individual may have for a specific data property. It is constructed using a non-negative integer cardinality and a data property expression, which identifies the attribute being restricted. An optional data range can be included to create a qualified restriction, specifying that the cardinality limit applies only to values within that particular range, whereas its absence applies the limit to all values of the property.

    :param cardinality: The non-negative integer defining the upper limit of values an individual may possess for the associated data property.
    :type cardinality: int
    :param data_property_expression: The data property expression defining the relationship between the subject individual and the data values subject to the maximum cardinality restriction.
    :type data_property_expression: OWLDataPropertyExpression
    :param data_range: Optional data range that restricts the values counted towards the maximum cardinality. If specified, the restriction is qualified, applying only to values within this range; otherwise, it applies to all values of the data property.
    :type data_range: typing.Optional[OWLDataRange]
    """

    def __init__(
        self,
        value: int,
        expression: OWLDataPropertyExpression,
        data_range: typing.Optional[OWLDataRange] = None,
    ) -> None:
        """
        Initializes a new instance representing a maximum data cardinality restriction within an OWL ontology, defining that a specific data property can have at most a certain number of values for a given individual. The constructor accepts a non-negative integer representing the maximum cardinality, the data property expression to be restricted, and an optional data range to further qualify the values. It performs an assertion to ensure the provided cardinality value is not negative, raising an error if this condition is violated, and proceeds to initialize the internal attributes with the provided arguments.

        :param value: The non-negative integer value representing the cardinality.
        :type value: int
        :param expression: The data property expression to which the restriction applies.
        :type expression: OWLDataPropertyExpression
        :param data_range: The data range that the values of the data property expression must belong to. If None, the restriction is unqualified.
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
        Updates the maximum cardinality value for this OWL data restriction to the specified integer. This method directly modifies the internal state of the object by assigning the new value to the underlying `_cardinality` attribute. While the implementation performs no explicit validation, the value is expected to be a non-negative integer consistent with OWL semantics, and changing it will affect any subsequent logic or comparisons that depend on this constraint.

        :param value: The new cardinality value to assign.
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
        Sets the data property expression that this maximum cardinality restriction applies to. This method accepts an instance of OWLDataPropertyExpression and updates the internal state of the object, effectively reconfiguring the restriction to constrain the specified property. Any subsequent operations or evaluations involving this OWLDataMaxCardinality instance will reflect the newly assigned data property.

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
        Assigns a new data range to this maximum cardinality restriction, defining the specific type of data values allowed. The method accepts an optional OWLDataRange instance; if provided, it replaces the existing data range, effectively altering the semantic constraints of the ontology element. This operation updates the object's internal state immediately.

        :param value: The OWL data range to assign, or None to clear the current value.
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
        Indicates whether this data maximum cardinality restriction is qualified by checking for the presence of a specific data range. A restriction is considered qualified if it limits the count to values belonging to a particular data range, rather than applying to the general range of the data property. This property returns True if the data range attribute is explicitly set, and False otherwise.

        :return: True if a data range is defined, False otherwise.

        :rtype: bool
        """

        return self.data_range is not None

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the data maximum cardinality restriction, formatted to display the class name followed by the cardinality value and the associated data property expression. The method conditionally appends the data range to the output string only if it is defined; otherwise, the representation omits the range. This ensures a concise and accurate textual summary of the object's state without causing errors when the data range attribute is unset.

        :return: A string representation of the `DataMaxCardinality` object, displaying the cardinality, data property expression, and data range (if defined).

        :rtype: str
        """

        if self.data_range:
            return f"DataMaxCardinality({self.cardinality} {self.data_property_expression} {self.data_range})"
        else:
            return f"DataMaxCardinality({self.cardinality} {self.data_property_expression})"
