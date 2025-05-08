import abc

from pyowl.abstracts.property_range import OWLPropertyRange


class OWLClassExpression(OWLPropertyRange, abc.ABC, metaclass=abc.ABCMeta):
    """An expression that defines a class in terms of other classes and properties."""

    __slots__ = ()

    def __eq__(self, value: object) -> bool:
        return str(self) == str(value)

    def __ne__(self, value: object) -> bool:
        return str(self) != str(value)

    def __lt__(self, value: object) -> bool:
        return str(self) < str(value)

    def __le__(self, value: object) -> bool:
        return str(self) <= str(value)

    def __gt__(self, value: object) -> bool:
        return str(self) > str(value)

    def __ge__(self, value: object) -> bool:
        return str(self) >= str(value)

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)
