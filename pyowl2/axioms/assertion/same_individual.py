import typing

from pyowl2.abstracts.assertion import OWLAssertion
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.base.annotation import OWLAnnotation


class OWLSameIndividual(OWLAssertion):
    """
    This class models an OWL axiom asserting that a collection of named individuals are identical within the domain of discourse. By declaring individuals as the same, any properties or assertions applicable to one individual can be inferred for the others. To use this class, instantiate it with a list containing at least two `OWLIndividual` objects; providing fewer than two will raise an assertion error. The class automatically sorts the provided list of individuals to maintain a canonical order, and it optionally accepts a list of annotations to attach metadata to the axiom.

    :parm individuals: Sorted list of named individuals asserted to be identical.
    :type individuals: list[OWLIndividual]
    """

    def __init__(
        self,
        individuals: list[OWLIndividual],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL SameIndividual axiom, which asserts that a collection of individuals are identical. The constructor requires a list containing at least two OWLIndividual objects, as an assertion error will be raised if fewer are provided. The provided individuals are sorted internally to maintain a canonical order, and optional annotations are passed to the parent axiom class for initialization.

        :param individuals: A list of OWL individuals involved in the axiom. The list must contain at least two elements.
        :type individuals: list[OWLIndividual]
        :param annotations: Optional list of annotations to be attached to the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

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
        """
        Sets the list of individuals associated with this OWL SameIndividual axiom. The method accepts a list of `OWLIndividual` objects and assigns them to the internal storage. Notably, the input list is sorted before assignment, ensuring that the individuals are maintained in a deterministic order regardless of the sequence provided.

        :param value: The new list of OWLIndividual objects to store. The list is sorted before assignment.
        :type value: list[OWLIndividual]
        """

        return self._individuals

    @individuals.setter
    def individuals(self, value: list[OWLIndividual]) -> None:
        """Setter for individuals."""
        self._individuals = sorted(value)

    def __str__(self) -> str:
        """
        Returns a string representation of the axiom formatted in a functional syntax style. The representation begins with the keyword 'SameIndividual' followed by the axiom annotations. If the axiom contains no annotations, an empty list indicator '[]' is used in their place. The string concludes with the space-separated string representations of the individuals declared to be identical.

        :return: A string representation of the axiom in the format 'SameIndividual([annotations] individuals)'.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"SameIndividual({self.axiom_annotations} {' '.join(map(str, self.individuals))})"
        else:
            return f"SameIndividual([] {' '.join(map(str, self.individuals))})"
