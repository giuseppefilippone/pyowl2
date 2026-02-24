import typing

from pyowl2.abstracts.class_axiom import OWLClassAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLEquivalentClasses(OWLClassAxiom):
    """
    This axiom defines a logical equivalence between two or more class expressions, asserting that they share the exact same set of instances within an ontology. It is utilized to model scenarios where distinct concepts are semantically identical, allowing reasoners to infer that any individual belonging to one class must also belong to all others declared equivalent. To construct this object, a user must provide a list containing at least two `OWLClassExpression` instances, along with an optional list of annotations for metadata. The implementation automatically sorts the provided expressions to maintain a canonical representation, ensuring that the order of input does not affect the identity of the axiom.

    :param class_expressions: A sorted list of class expressions declared to be equivalent, containing at least two elements.
    :type class_expressions: list[OWLClassExpression]
    """

    def __init__(
        self,
        expressions: list[OWLClassExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an axiom asserting that a collection of class expressions are equivalent to one another. The constructor requires a list containing at least two `OWLClassExpression` instances; providing fewer will raise an assertion error. Optional annotations can be attached to the axiom. Internally, the provided class expressions are sorted to ensure a canonical representation, regardless of the input order.

        :param expressions: A list of OWL class expressions to be combined. The list must contain at least two elements.
        :type expressions: list[OWLClassExpression]
        :param annotations: Optional list of annotations to be attached to the axiom.
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
        Sets the list of class expressions that are declared equivalent within this axiom. The provided list of OWLClassExpression objects is sorted prior to storage to maintain a consistent internal order. This method replaces any existing class expressions currently held by the object.

        :param value: The OWL class expressions to assign. The list will be sorted before being stored.
        :type value: list[OWLClassExpression]
        """

        return self._class_expressions

    @class_expressions.setter
    def class_expressions(self, value: list[OWLClassExpression]) -> None:
        """Setter for class_expressions."""
        self._class_expressions = sorted(value)

    def __str__(self) -> str:
        """
        Returns a string representation of the OWL equivalent classes axiom using a functional-style syntax. The output string begins with 'EquivalentClasses' and includes the axiom annotations; if no annotations are present, an empty list '[]' is explicitly rendered. The class expressions defining the equivalence are converted to strings and concatenated with spaces to complete the representation.

        :return: A string representation of the equivalent classes axiom, including its annotations and class expressions.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"EquivalentClasses({self.axiom_annotations} {' '.join(map(str, self.class_expressions))})"
        else:
            return f"EquivalentClasses([] {' '.join(map(str, self.class_expressions))})"
