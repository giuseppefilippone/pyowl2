from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.individual import OWLIndividual


class OWLObjectOneOf(OWLClassExpression):
    """
    This class represents an enumeration class expression, which defines a specific class by explicitly listing a finite set of individuals as its members. It is used to assert that the class extension consists exactly of the provided instances, allowing for the precise definition of classes based on specific entities rather than general properties. When initializing this expression, a non-empty list of `OWLIndividual` objects must be provided; the class automatically sorts these individuals internally to ensure a canonical representation. As a subclass of `OWLClassExpression`, it can be utilized in complex logical constructs where a specific set of instances needs to be referenced as a class.

    :param individuals: The sorted list of individuals explicitly enumerated as members of the class expression.
    :type individuals: list[OWLIndividual]
    """

    def __init__(self, individuals: list[OWLIndividual]) -> None:
        """
        Initializes an OWL class expression that defines a class by enumerating a specific set of individuals. The constructor accepts a list of `OWLIndividual` objects, which must contain at least one element; otherwise, an assertion error is raised. To ensure a consistent internal representation, the provided individuals are sorted before being stored.

        :param individuals: A non-empty collection of OWL individuals to be included. The input will be sorted internally.
        :type individuals: list[OWLIndividual]
        """

        super().__init__()
        assert len(individuals) >= 1
        self._individuals: list[OWLIndividual] = sorted(individuals)

    @property
    def individuals(self) -> list[OWLIndividual]:
        """
        Replaces the current set of individuals defining this OWL enumeration with the provided list. The method sorts the input list of OWLIndividual objects before assigning them to the internal attribute, thereby enforcing a canonical order for the stored individuals.

        :param value: A list of OWL individuals to be stored. The list is sorted before assignment.
        :type value: list[OWLIndividual]
        """

        return self._individuals

    @individuals.setter
    def individuals(self, value: list[OWLIndividual]) -> None:
        """Setter for individuals."""
        self._individuals = sorted(value)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the object enumeration, formatted using the standard functional syntax. The method concatenates the string representations of all contained individuals, separated by spaces, and encloses them within 'ObjectOneOf(...)'. If the collection of individuals is empty, the method returns 'ObjectOneOf()'.

        :return: A string representation of the object, formatted as "ObjectOneOf(...)" containing the space-separated string representations of the individuals.

        :rtype: str
        """

        return f"ObjectOneOf({' '.join(map(str, self.individuals))})"
