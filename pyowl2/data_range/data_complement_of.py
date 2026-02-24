from pyowl2.abstracts.data_range import OWLDataRange


class OWLDataComplementOf(OWLDataRange):
    """
    This class models a data range expression that defines the set of all values not contained within a specific, nested data range. It is utilized within an ontology to construct complex data type definitions through negation, allowing for the specification of constraints that require values to be excluded from a particular set or type. To use this class, instantiate it with a target `OWLDataRange` object; the resulting instance will semantically represent the complement of that provided range, effectively filtering out any values that belong to it.

    :param data_range: The data range for which this expression represents the complement.
    :type data_range: OWLDataRange
    """

    def __init__(self, data_range: OWLDataRange) -> None:
        """
        Initializes a new instance representing the logical complement of a specific data range within the OWL ontology structure. The constructor accepts a single argument, `data_range`, which must be a valid `OWLDataRange` object defining the set of data values to be negated. It invokes the superclass initialization to establish base properties and stores the provided range internally for use in logical operations and comparisons.

        :param data_range: The OWL data range that this object represents.
        :type data_range: OWLDataRange
        """

        super().__init__()
        self._data_range: OWLDataRange = data_range

    @property
    def data_range(self) -> OWLDataRange:
        """
        Updates the data range operand of this complement expression to the specified value. This method modifies the internal state of the object in place, effectively changing the definition of the complement to apply to the new data range. It accepts an instance of OWLDataRange and assigns it to the underlying private attribute, replacing any previously held value.

        :param value: The data range to assign.
        :type value: OWLDataRange
        """

        return self._data_range

    @data_range.setter
    def data_range(self, value: OWLDataRange) -> None:
        """Setter for data_range."""
        self._data_range = value

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the data complement expression using a functional syntax format. The output string consists of the class name followed by the string representation of the encapsulated data range enclosed in parentheses. This method is primarily intended for debugging and display purposes, providing a clear textual indication of the logical structure being represented.

        :return: A string representation of the object, formatted as 'DataComplementOf({data_range})'.

        :rtype: str
        """

        return f"DataComplementOf({self.data_range})"
