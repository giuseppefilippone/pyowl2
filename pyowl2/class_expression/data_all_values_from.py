from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.data_range import OWLDataRange


class OWLDataAllValuesFrom(OWLClassExpression):
    """
    This class represents a universal restriction on data properties within an ontology, specifying that for any individual belonging to this class, all values of the associated data properties must fall within a defined data range. It is used to enforce constraints on literal values, ensuring that data such as ages or prices conform to specific types or intervals. To construct an instance, provide a list of data property expressions and the target data range; the implementation automatically sorts the property list to ensure consistent representation.

    :parm data_property_expressions: Sorted data property expressions defining the properties restricted by the data range.
    :type data_property_expressions: list[OWLDataPropertyExpression]
    :parm data_range: The data range that defines the set of permissible values for the associated data properties.
    :type data_range: OWLDataRange
    """

    def __init__(
        self, expressions: list[OWLDataPropertyExpression], data_range: OWLDataRange
    ) -> None:
        """
        Initializes a new instance representing an OWL data restriction where all values of the specified properties must belong to a given data range. The method requires a non-empty list of data property expressions and a target data range. To ensure a canonical internal state, the provided property expressions are sorted before being stored. An assertion error will occur if the list of expressions is empty.

        :param expressions: A non-empty list of OWL data property expressions.
        :type expressions: list[OWLDataPropertyExpression]
        :param data_range: The OWL data range that defines the range of the data property expressions.
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
        Sets the data property expressions for this OWLDataAllValuesFrom restriction by assigning the provided list of OWLDataPropertyExpression objects. The input list is sorted before being stored in the private attribute to maintain a deterministic internal state.

        :param value: The OWL data property expressions to assign. The list will be sorted internally before storage.
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
        Updates the data range filler for this 'all values from' restriction, defining the specific set of data values that the property must take. This method assigns the provided `OWLDataRange` instance to the internal `_data_range` attribute, replacing any previously stored value. The operation performs a direct assignment without performing explicit validation or triggering side effects beyond the state modification.

        :param value: The new data range to assign to the object.
        :type value: OWLDataRange
        """

        return self._data_range

    @data_range.setter
    def data_range(self, value: OWLDataRange) -> None:
        """Setter for data_range."""
        self._data_range = value

    def __str__(self) -> str:
        """
        Returns a string representation of the universal data property restriction, formatted to resemble a logical expression. The method concatenates the string representations of all data property expressions associated with this restriction and appends the string representation of the data range, wrapping them in a "DataAllValuesFrom" prefix. This operation is side-effect free, though the exact output depends on the string representations of the nested property expressions and data range objects.

        :return: A string representation of the object, formatted as a `DataAllValuesFrom` expression containing the data property expressions and data range.

        :rtype: str
        """

        return f"DataAllValuesFrom({' '.join(map(str, self.data_property_expressions))} {self.data_range})"
