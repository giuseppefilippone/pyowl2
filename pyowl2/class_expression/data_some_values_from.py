from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.data_range import OWLDataRange


class OWLDataSomeValuesFrom(OWLClassExpression):
    """
    This class represents an existential restriction on data properties, asserting that an individual must have at least one value for a specified property that falls within a particular data range. It serves to define a class of individuals based on the existence of data values satisfying specific criteria, such as having an age within a certain integer interval. When constructing an instance, users provide a list of data property expressions and the corresponding data range; internally, the list of properties is automatically sorted to maintain a consistent order regardless of the input sequence.

    :parm data_property_expressions: Sorted list of data property expressions defining the properties restricted by this class. The restriction requires that an individual has at least one value for any of these properties within the specified data range.
    :type data_property_expressions: list[OWLDataPropertyExpression]
    :parm data_range: The data range or datatype that at least one value of the associated data properties must fall within.
    :type data_range: OWLDataRange
    """

    def __init__(
        self,
        expressions: list[OWLDataPropertyExpression],
        data_range: OWLDataRange = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL data property existential restriction, defining a class of individuals connected to a specific data range via a given property. The constructor requires a non-empty list of data property expressions and accepts an optional data range. Internally, the provided property expressions are sorted to ensure a canonical representation, and the data range is stored as an instance attribute.

        :param expressions: A non-empty collection of OWL data property expressions.
        :type expressions: list[OWLDataPropertyExpression]
        :param data_range: The data range associated with the data property expressions.
        :type data_range: OWLDataRange
        """

        super().__init__()
        assert len(expressions) >= 1
        self._data_property_expressions: list[OWLDataPropertyExpression] = sorted(
            expressions
        )
        self._data_range: OWLDataRange = data_range

    @property
    def data_property_expressions(self) -> list[OWLDataPropertyExpression]:
        """
        Assigns a new collection of data property expressions to this restriction, replacing the existing set. The provided list of OWLDataPropertyExpression objects is sorted prior to storage to maintain a canonical internal order. This normalization ensures that the sequence of properties does not affect the object's state or equality comparisons.

        :param value: The OWL data property expressions to assign. The provided list will be sorted before storage.
        :type value: list[OWLDataPropertyExpression]
        """

        return self._data_property_expressions

    @data_property_expressions.setter
    def data_property_expressions(self, value: list[OWLDataPropertyExpression]) -> None:
        """Setter for data_property_expressions."""
        self._data_property_expressions = sorted(value)

    @property
    def data_range(self) -> OWLDataRange:
        """
        Updates the data range component of this OWL data restriction to the provided value. This method replaces the existing internal data range with the new instance, effectively altering the set of literal values that the property restriction targets. The operation mutates the object's state and requires the input to be a valid OWLDataRange object.

        :param value: The OWL data range to assign.
        :type value: OWLDataRange
        """

        return self._data_range

    @data_range.setter
    def data_range(self, value: OWLDataRange) -> None:
        """Setter for data_range."""
        self._data_range = value

    def __str__(self) -> str:
        """
        Generates a human-readable string representation of the OWL data some values from restriction, formatted to display the class identifier along with its constituent components. The resulting string concatenates the keyword 'DataSomeValuesFrom' with the string representations of the associated data property expressions and the specific data range, separated by spaces. This method is intended for logging or debugging purposes and does not modify the state of the object.

        :return: A human-readable string representation of the object, formatted as a DataSomeValuesFrom expression containing the data property expressions and data range.

        :rtype: str
        """

        return f"DataSomeValuesFrom({' '.join(map(str, self.data_property_expressions))} {self.data_range})"
