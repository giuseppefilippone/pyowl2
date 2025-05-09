from pyowl2.abstracts.data_range import OWLDataRange


class OWLDataComplementOf(OWLDataRange):
    """A data range that represents the complement of another data range."""

    def __init__(self, data_range: OWLDataRange) -> None:
        super().__init__()
        self._data_range: OWLDataRange = data_range

    @property
    def data_range(self) -> OWLDataRange:
        """Getter for data_range."""
        return self._data_range

    @data_range.setter
    def data_range(self, value: OWLDataRange) -> None:
        """Setter for data_range."""
        self._data_range = value

    def __str__(self) -> str:
        return f"DataComplementOf({self.data_range})"
