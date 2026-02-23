from pyowl2.abstracts.data_range import OWLDataRange


class OWLDataUnionOf(OWLDataRange):
    """
    This class represents a logical union of multiple data ranges within an ontology, defining a set of permissible values that belong to at least one of the constituent ranges. It extends the base data range type and is initialized with a list of `OWLDataRange` objects, requiring a minimum of two ranges to form a valid union. Upon initialization and modification, the class automatically sorts the internal list of data ranges to maintain a canonical representation, ensuring consistent behavior for comparisons and storage.

    :parm data_ranges: The sorted list of data ranges forming the union.
    :type data_ranges: list[OWLDataRange]
    """

    def __init__(self, data_ranges: list[OWLDataRange]) -> None:
        """
        Constructs a data union expression from a collection of OWL data ranges. This initializer enforces the semantic constraint that a union must consist of at least two distinct operands, raising an assertion error if the input list is shorter. To maintain a normalized internal state, the provided data ranges are sorted before being assigned to the instance's internal storage.

        :param data_ranges: A collection of OWL data ranges. Must contain at least two elements.
        :type data_ranges: list[OWLDataRange]
        """

        super().__init__()
        assert len(data_ranges) >= 2
        self._data_ranges: list[OWLDataRange] = sorted(data_ranges)

    @property
    def data_ranges(self) -> list[OWLDataRange]:
        """
        Sets the list of data ranges that constitute the union. The provided list of OWLDataRange objects is sorted before being assigned to the internal state, ensuring a consistent and deterministic ordering. This operation overwrites any previously stored data ranges.

        :param value: A list of OWLDataRange objects to assign. The list will be sorted internally before storage.
        :type value: list[OWLDataRange]
        """

        return self._data_ranges

    @data_ranges.setter
    def data_ranges(self, value: list[OWLDataRange]) -> None:
        """Setter for data_ranges."""
        self._data_ranges = sorted(value)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the data union, formatted as "DataUnionOf(...)" where the constituent data ranges are separated by spaces. This method constructs the string by converting each element in the internal collection of data ranges to its string representation and joining them. It does not modify the state of the object and relies on the string conversion logic of the contained data ranges; if the union is empty, it returns "DataUnionOf()".

        :return: A string representation of the object, formatted as 'DataUnionOf(...)' with the data ranges joined by spaces.

        :rtype: str
        """

        return f"DataUnionOf({' '.join(map(str, self.data_ranges))})"
