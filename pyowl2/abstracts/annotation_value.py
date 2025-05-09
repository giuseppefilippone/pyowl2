import abc

from pyowl2.abstracts.object import OWLObject


class OWLAnnotationValue(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """The value associated with an annotation property for a given subject. It can be an anonymous individual, an IRI or a Literal."""

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
