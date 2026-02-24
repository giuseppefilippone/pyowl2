from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.literal.literal import OWLLiteral


class OWLDataOneOf(OWLDataRange):
    """
    This class models a data range defined by an explicit enumeration of specific literal values, effectively restricting data membership to a finite, closed set. It is utilized within ontologies to define properties that can only take on one of the pre-defined values, such as a specific set of integers or strings. Upon instantiation, the class requires a non-empty list of `OWLLiteral` objects and automatically maintains these literals in a sorted order to ensure consistency.

    :param literals: The sorted list of literal values explicitly enumerated in this data range, guaranteed to be non-empty.
    :type literals: list[OWLLiteral]
    """

    def __init__(self, literals: list[OWLLiteral]) -> None:
        """
        Initializes an instance representing an OWL DataOneOf expression, which defines a data range restricted to a specific set of literal values. The method accepts a list of OWLLiteral objects, which must contain at least one element; providing an empty list will trigger an assertion error. Upon initialization, the input literals are sorted and stored internally to maintain a canonical order, and the parent class constructor is invoked.

        :param literals: The values to be included in the collection. Must contain at least one element.
        :type literals: list[OWLLiteral]
        """

        super().__init__()
        assert len(literals) >= 1
        self._literals: list[OWLLiteral] = sorted(literals)

    @property
    def literals(self) -> list[OWLLiteral]:
        """
        Updates the collection of literal values that define this data range by assigning the provided list of OWLLiteral objects. The method enforces a specific ordering by sorting the input list before storing it internally, which ensures a canonical representation but may alter the original sequence of the provided arguments. This operation overwrites the existing internal state and requires that all elements in the input list be comparable to avoid raising a TypeError during the sorting process.

        :param value: A list of OWL literals to be assigned to the object.
        :type value: list[OWLLiteral]
        """

        return self._literals

    @literals.setter
    def literals(self, value: list[OWLLiteral]) -> None:
        """Setter for literals."""
        self._literals = sorted(value)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the data one-of expression using a functional syntax format. The output string begins with "DataOneOf" followed by the string representations of the literals contained within the object, joined by spaces and enclosed in parentheses. This method is typically invoked implicitly when the object is passed to the print function or converted to a string.

        :return: A string representation of the object, formatted as 'DataOneOf(...)' containing the space-separated string values of the internal literals.

        :rtype: str
        """

        return f"DataOneOf({' '.join(map(str, self.literals))})"
