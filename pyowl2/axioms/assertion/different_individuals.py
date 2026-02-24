import typing

from pyowl2.abstracts.assertion import OWLAssertion
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.base.annotation import OWLAnnotation


class OWLDifferentIndividuals(OWLAssertion):
    """
    This axiom asserts that a specific group of individuals within an ontology are mutually distinct, ensuring that no two individuals in the set refer to the same entity. It is utilized to enforce uniqueness constraints across the domain of discourse, preventing logical reasoners from inferring that these individuals are identical. To construct this object, a list of at least two `OWLIndividual` instances must be provided, along with an optional list of annotations for metadata. The implementation automatically sorts the provided individuals to maintain a canonical representation and raises an error if fewer than two individuals are supplied.

    :param individuals: A sorted list of at least two individuals declared to be mutually distinct, maintained in canonical order to ensure consistency.
    :type individuals: list[OWLIndividual]
    """

    def __init__(
        self,
        individuals: list[OWLIndividual],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Constructs an axiom representing the declaration that a set of individuals are pairwise distinct. The method accepts a list of individuals and an optional list of annotations, passing the latter to the parent class constructor. A critical constraint is enforced requiring the list of individuals to contain at least two elements; failing this will trigger an assertion error. As a side effect, the provided individuals are sorted and stored in this canonical order to normalize the axiom's internal state.

        :param individuals: The OWL individuals involved in the axiom. The list must contain at least two elements.
        :type individuals: list[OWLIndividual]
        :param annotations: Optional list of annotations to associate with the axiom.
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
        Replaces the current set of individuals with the provided list of OWLIndividual objects. The input list is sorted prior to assignment to the internal attribute, ensuring a canonical ordering of the individuals within the axiom. This method is part of the OWLDifferentIndividuals class, which represents an axiom asserting that all listed individuals are pairwise distinct.

        :param value: A list of OWLIndividual objects to assign to the collection.
        :type value: list[OWLIndividual]
        """

        return self._individuals

    @individuals.setter
    def individuals(self, value: list[OWLIndividual]) -> None:
        """Setter for individuals."""
        self._individuals = sorted(value)

    def __str__(self) -> str:
        """
        Returns a string representation of the OWL DifferentIndividuals axiom, formatted to display the axiom type, annotations, and associated individuals. The output begins with "DifferentIndividuals(" followed by the axiom annotations if they exist, or an empty list "[]" if they are absent. The string representations of the individuals are then appended, separated by spaces. This method does not modify the object's state.

        :return: A string representation of the axiom, including any annotations and the list of individuals.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"DifferentIndividuals({self.axiom_annotations} {' '.join(map(str, self.individuals))})"
        else:
            return f"DifferentIndividuals([] {' '.join(map(str, self.individuals))})"
