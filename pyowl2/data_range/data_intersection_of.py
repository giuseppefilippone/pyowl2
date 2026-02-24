from pyowl2.abstracts.data_range import OWLDataRange


class OWLDataIntersectionOf(OWLDataRange):
    """
    This class represents a logical data range formed by the intersection of multiple constituent data ranges, defining a set of values that must belong to every specified range. It serves to construct highly specific data type constraints within an ontology by combining broader definitions, ensuring that only values satisfying all conditions are considered valid. When instantiating this class, a list of at least two `OWLDataRange` objects must be provided; note that the input list is automatically sorted upon initialization and modification to enforce a canonical ordering.

    :param data_ranges: The sorted list of data range operands that constitute the intersection, guaranteed to contain at least two elements.
    :type data_ranges: list[OWLDataRange]
    """

    def __init__(self, data_ranges: list[OWLDataRange]) -> None:
        """
        Constructs an object representing the intersection of a collection of OWL data ranges. The input list must contain at least two data ranges, as an intersection of fewer elements is considered invalid in this context. To ensure a canonical representation, the provided data ranges are sorted internally before being stored.

        :param data_ranges: A list of OWL data ranges to be included. The list must contain at least two elements.
        :type data_ranges: list[OWLDataRange]
        """

        super().__init__()
        assert len(data_ranges) >= 2
        self._data_ranges: list[OWLDataRange] = sorted(data_ranges)

    @property
    def data_ranges(self) -> list[OWLDataRange]:
        """
        Updates the collection of data ranges that constitute this intersection by assigning the provided list of OWLDataRange objects. The input list is sorted before being stored in the internal state to ensure a canonical ordering of operands. This sorting behavior aids in the consistent comparison and hashing of the object.

        :param value: A list of OWL data ranges to assign. The list will be sorted internally before storage.
        :type value: list[OWLDataRange]
        """

        return self._data_ranges

    @data_ranges.setter
    def data_ranges(self, value: list[OWLDataRange]) -> None:
        """Setter for data_ranges."""
        self._data_ranges = sorted(value)

    def __str__(self) -> str:
        """
        Returns a string representation of the data intersection using a functional syntax format. The resulting string begins with the class name followed by the string representations of the constituent data ranges, which are joined by spaces. This method delegates the string conversion of the individual components to their respective `__str__` implementations.

        :return: A string representation of the object, formatted as 'DataIntersectionOf(...)' containing the string representations of the data ranges.

        :rtype: str
        """

        return f"DataIntersectionOf({' '.join(map(str, self.data_ranges))})"
