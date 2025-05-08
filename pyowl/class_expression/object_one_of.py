from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.abstracts.individual import OWLIndividual


class OWLObjectOneOf(OWLClassExpression):
    """A class expression that explicitly lists a finite set of individuals as its members."""

    def __init__(self, individuals: list[OWLIndividual]) -> None:
        super().__init__()
        assert len(individuals) >= 1
        self._individuals: list[OWLIndividual] = sorted(individuals)

    @property
    def individuals(self) -> list[OWLIndividual]:
        """Getter for individuals."""
        return self._individuals

    @individuals.setter
    def individuals(self, value: list[OWLIndividual]) -> None:
        """Setter for individuals."""
        self._individuals = sorted(value)

    def __str__(self) -> str:
        return f"ObjectOneOf({' '.join(map(str, self.individuals))})"
