import abc
import typing

from pyowl2.abstracts.object import OWLObject
from pyowl2.base.annotation import OWLAnnotation


class OWLAxiom(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """A fundamental statement or assertion within an ontology that contributes to its logical structure."""

    # __slots__ = ()
    def __init__(self, annotations: typing.Optional[list[OWLAnnotation]] = None):
        self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = (
            sorted(annotations) if annotations else annotations
        )

    @property
    def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        """Getter for axiom_annotations."""
        return self._axiom_annotations

    @axiom_annotations.setter
    def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
        """Setter for axiom_annotations."""
        self._axiom_annotations = sorted(value) if value else value

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
