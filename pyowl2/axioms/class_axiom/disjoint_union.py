import typing

from pyowl2.abstracts.class_axiom import OWLClassAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.owl_class import OWLClass


class OWLDisjointUnion(OWLClassAxiom):
    """
    This class represents a semantic axiom within an ontology that defines a specific class as the union of a set of mutually disjoint class expressions. It asserts that the designated union class is equivalent to the logical disjunction of the provided expressions, while simultaneously enforcing that those expressions share no common instances. Users must provide a primary class and a list of at least two class expressions to define the partition; the implementation automatically sorts these expressions to maintain a canonical internal state. Additionally, optional annotations can be attached to the axiom to provide context or metadata.

    :param union_class: The named class declared to be equivalent to the union of the disjoint class expressions.
    :type union_class: OWLClass
    :param disjoint_class_expressions: The list of class expressions that are declared to be disjoint, maintained in sorted order.
    :type disjoint_class_expressions: list[OWLClassExpression]
    """

    def __init__(
        self,
        expression: OWLClass,
        expressions: list[OWLClassExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an OWL Disjoint Union axiom, which asserts that a specific class is equivalent to the union of a set of class expressions and that those expressions are pairwise disjoint. The constructor requires the list of class expressions to contain at least two elements; otherwise, an assertion error is raised. As a side effect, the provided list of class expressions is sorted internally before storage, ensuring that the order of input does not affect the resulting object's state. Optional annotations may be provided to attach metadata to the axiom.

        :param expression: The class defined as the disjoint union of the provided expressions.
        :type expression: OWLClass
        :param expressions: A list of class expressions that are mutually disjoint. Must contain at least two elements.
        :type expressions: list[OWLClassExpression]
        :param annotations: Optional list of annotations to be associated with the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        assert len(expressions) >= 2
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._union_class: OWLClass = expression
        self._disjoint_class_expressions: list[OWLClassExpression] = sorted(expressions)

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def union_class(self) -> OWLClass:
        """
        Assigns the specified `OWLClass` instance to the internal attribute representing the class defined by the disjoint union axiom. This method serves as the setter for the `union_class` property, effectively updating the subject of the axiom. It modifies the object's state in place, replacing any existing value without performing validation on the input type.

        :param value: The OWL class to assign as the union class.
        :type value: OWLClass
        """

        return self._union_class

    @union_class.setter
    def union_class(self, value: OWLClass) -> None:
        """Setter for union_class."""
        self._union_class = value

    @property
    def disjoint_class_expressions(self) -> list[OWLClassExpression]:
        """
        Assigns a new list of class expressions to the disjoint union definition. The input list is sorted internally before storage to ensure a canonical ordering, regardless of the sequence provided. This operation overwrites the existing set of expressions stored in the object.

        :param value: The OWL class expressions to set as disjoint.
        :type value: list[OWLClassExpression]
        """

        return self._disjoint_class_expressions

    @disjoint_class_expressions.setter
    def disjoint_class_expressions(self, value: list[OWLClassExpression]) -> None:
        """Setter for disjoint_class_expressions."""
        self._disjoint_class_expressions = sorted(value)

    def __str__(self) -> str:
        """
        Generates a human-readable string representation of the disjoint union axiom in a functional syntax format. The output string includes the axiom annotations, defaulting to an empty list '[]' if none are present, followed by the union class and the space-separated list of disjoint class expressions. This ensures a consistent textual format regardless of whether the axiom contains annotations.

        :return: A string representation of the disjoint union in functional syntax, including annotations, the union class, and the disjoint class expressions.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"DisjointUnion({self.axiom_annotations} {self.union_class} {' '.join(map(str, self.disjoint_class_expressions))})"
        else:
            return f"DisjointUnion([] {self.union_class} {' '.join(map(str, self.disjoint_class_expressions))})"
