import typing

from pyowl.abstracts.assertion import OWLAssertion
from pyowl.abstracts.individual import OWLIndividual
from pyowl.base.annotation import OWLAnnotation


class OWLSameIndividual(OWLAssertion):
    """An axiom stating that two or more named individuals are the same."""

    def __init__(
        self,
        individuals: list[OWLIndividual],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        assert len(individuals) >= 2
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._individuals: list[OWLIndividual] = sorted(individuals)

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def individuals(self) -> list[OWLIndividual]:
        """Getter for Individuals."""
        return self._individuals

    @individuals.setter
    def individuals(self, value: list[OWLIndividual]) -> None:
        """Setter for Individuals."""
        self._individuals = sorted(value)

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"SameIndividual({self.axiom_annotations} {' '.join(map(str, self.individuals))})"
        else:
            return f"SameIndividual([] {' '.join(map(str, self.individuals))})"
