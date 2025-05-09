from pyowl2.abstracts.data_range import OWLDataRange


class OWLDataIntersectionOf(OWLDataRange):
    """A data range that represents the intersection of multiple data ranges."""

    def __init__(self, data_ranges: list[OWLDataRange]) -> None:
        super().__init__()
        assert len(data_ranges) >= 2
        self._data_ranges: list[OWLDataRange] = sorted(data_ranges)

    @property
    def data_ranges(self) -> list[OWLDataRange]:
        """Getter for data_ranges."""
        return self._data_ranges

    @data_ranges.setter
    def data_ranges(self, value: list[OWLDataRange]) -> None:
        """Setter for data_ranges."""
        self._data_ranges = sorted(value)

    def __str__(self) -> str:
        return f"DataIntersectionOf({' '.join(map(str, self.data_ranges))})"
