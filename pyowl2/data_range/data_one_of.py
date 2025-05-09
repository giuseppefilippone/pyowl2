from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.literal.literal import OWLLiteral


class OWLDataOneOf(OWLDataRange):
    """A data range consisting of an explicit enumeration of literal values."""

    def __init__(self, literals: list[OWLLiteral]) -> None:
        super().__init__()
        assert len(literals) >= 1
        self._literals: list[OWLLiteral] = sorted(literals)

    @property
    def literals(self) -> list[OWLLiteral]:
        """Getter for literals."""
        return self._literals

    @literals.setter
    def literals(self, value: list[OWLLiteral]) -> None:
        """Setter for literals."""
        self._literals = sorted(value)

    def __str__(self) -> str:
        return f"DataOneOf({' '.join(map(str, self.literals))})"
