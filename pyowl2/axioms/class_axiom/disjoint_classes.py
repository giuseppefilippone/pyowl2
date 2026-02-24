import typing

from pyowl2.abstracts.class_axiom import OWLClassAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLDisjointClasses(OWLClassAxiom):
    """
    This axiom defines a mutual exclusion relationship between two or more class expressions within an ontology, asserting that no individual can be an instance of more than one of the specified classes simultaneously. To utilize this entity, instantiate it with a list of `OWLClassExpression` objects, ensuring the list contains at least two elements; the implementation automatically sorts these expressions to maintain a consistent internal order. Optional annotations can be attached to provide metadata about the axiom itself, such as provenance or confidence scores.

    :param class_expressions: The sorted list of class expressions involved in the disjointness axiom.
    :type class_expressions: list[OWLClassExpression]
    """

    def __init__(
        self,
        expressions: list[OWLClassExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing a disjoint classes axiom within an OWL ontology. The constructor accepts a list of class expressions that are asserted to be mutually disjoint, along with an optional list of annotations. It enforces the constraint that at least two class expressions must be provided, raising an assertion error if this condition is not met. The provided expressions are sorted internally to maintain a consistent order, and any annotations are delegated to the superclass for management.

        :param expressions: A list of OWL class expressions involved in the axiom. The list must contain at least two elements.
        :type expressions: list[OWLClassExpression]
        :param annotations: A list of annotations to be associated with this axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        assert len(expressions) >= 2
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._class_expressions: list[OWLClassExpression] = sorted(expressions)

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def class_expressions(self) -> list[OWLClassExpression]:
        """
        Replaces the current collection of class expressions with the provided list of OWLClassExpression objects. This setter normalizes the input by sorting the elements before storing them in the private attribute, ensuring a deterministic internal order regardless of the input sequence. The operation modifies the object in place and returns None.

        :param value: A list of OWL class expressions to assign. The list will be sorted before being stored.
        :type value: list[OWLClassExpression]
        """

        return self._class_expressions

    @class_expressions.setter
    def class_expressions(self, value: list[OWLClassExpression]) -> None:
        """Setter for class_expressions."""
        self._class_expressions = sorted(value)

    def __str__(self) -> str:
        """
        Returns a string representation of the disjoint classes axiom formatted in a functional syntax style. The output begins with the keyword 'DisjointClasses' followed by the list of axiom annotations; if no annotations are present, an empty list is explicitly included. The string concludes with the space-separated string representations of all class expressions involved in the disjointness relationship.

        :return: A string representation of the DisjointClasses axiom in functional syntax, including the axiom annotations and the list of class expressions.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"DisjointClasses({self.axiom_annotations} {' '.join(map(str, self.class_expressions))})"
        else:
            return f"DisjointClasses([] {' '.join(map(str, self.class_expressions))})"
