import typing

from pyowl2.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLDisjointDataProperties(OWLDataPropertyAxiom):
    """
    This class models an axiom within an OWL ontology that declares a set of data properties to be mutually disjoint. Semantically, this implies that no single individual can possess the same literal value for any two properties included in the set. To utilize this class, instantiate it with a list containing at least two `OWLDataPropertyExpression` objects; an optional list of annotations may be provided to attach metadata to the axiom. Note that the class enforces a minimum of two properties and automatically sorts the provided expressions to ensure consistent representation.

    :param data_property_expressions: The sorted list of two or more data properties involved in the axiom, representing properties that are mutually exclusive in their values for any individual.
    :type data_property_expressions: list[OWLDataPropertyExpression]
    """

    def __init__(
        self,
        expressions: list[OWLDataPropertyExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an axiom asserting that a specific set of data properties are pairwise disjoint. This method accepts a list of data property expressions and an optional list of annotations, delegating annotation handling to the superclass. A precondition is enforced requiring the input list to contain at least two expressions; failing this will trigger an assertion error. To maintain a canonical internal state, the provided property expressions are sorted before being assigned to the instance.

        :param expressions: A list of OWL data property expressions. The list must contain at least two elements.
        :type expressions: list[OWLDataPropertyExpression]
        :param annotations: Optional list of annotations to be associated with the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        assert len(expressions) >= 2
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._data_property_expressions: list[OWLDataPropertyExpression] = sorted(
            expressions
        )

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def data_property_expressions(self) -> list[OWLDataPropertyExpression]:
        """
        Assigns a new collection of data property expressions to this disjointness axiom. The provided list is sorted before being stored to ensure a consistent internal representation, effectively discarding the original order of the input elements.

        :param value: The OWL data property expressions to assign. The provided list will be sorted before storage.
        :type value: list[OWLDataPropertyExpression]
        """

        return self._data_property_expressions

    @data_property_expressions.setter
    def data_property_expressions(self, value: list[OWLDataPropertyExpression]) -> None:
        """Setter for data_property_expressions."""
        self._data_property_expressions = sorted(value)

    def __str__(self) -> str:
        """
        Returns a string representation of the axiom formatted in a functional syntax style. The output always includes a list structure for annotations, displaying the actual annotations if present or an empty list otherwise. Following the annotations, the method appends the string representations of all associated data property expressions, joined by spaces.

        :return: A string representation of the object, formatted as a constructor-like call including any annotations and the list of data property expressions.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"DisjointDataProperties({self.axiom_annotations} {' '.join(map(str, self.data_property_expressions))})"
        else:
            return f"DisjointDataProperties([] {' '.join(map(str, self.data_property_expressions))})"
