import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLDisjointObjectProperties(OWLObjectPropertyAxiom):
    """
    This class models a semantic axiom asserting that a collection of object properties are mutually exclusive, meaning no single pair of individuals can be related by more than one of these properties simultaneously. It is typically used to define strict separation between relationship types within an ontology, such as ensuring that a "parent of" relationship cannot also be a "sibling of" relationship for the same entities. When constructing an instance, users must provide a list of at least two object property expressions; the class automatically sorts this list to ensure a canonical internal representation. Additionally, optional annotations may be supplied to attach metadata or contextual information to the axiom.

    :param object_property_expressions: The sorted list of object property expressions declared to be disjoint, indicating that they cannot relate the same pair of individuals.
    :type object_property_expressions: list[OWLObjectPropertyExpression]
    """

    def __init__(
        self,
        expressions: list[OWLObjectPropertyExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an axiom asserting that a collection of object properties are mutually disjoint. The method requires a list of at least two object property expressions, as disjointness cannot be defined for a single property. It also accepts an optional list of annotations, which are handled by the parent class. Internally, the list of property expressions is sorted to maintain a consistent, canonical order, regardless of the input sequence.

        :param expressions: A list of object property expressions to be used in the axiom. The list must contain at least two elements.
        :type expressions: list[OWLObjectPropertyExpression]
        :param annotations: Optional list of annotations to be attached to the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        assert len(expressions) >= 2
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._object_property_expressions: list[OWLObjectPropertyExpression] = sorted(
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
    def object_property_expressions(self) -> list[OWLObjectPropertyExpression]:
        """
        Replaces the current collection of object property expressions involved in this disjointness axiom with the provided list. The input list is sorted before being stored internally to ensure a canonical ordering, which means the sequence of properties in the input does not affect the internal representation. This method directly modifies the internal state of the object.

        :param value: A list of object property expressions to assign. The list will be sorted before storage.
        :type value: list[OWLObjectPropertyExpression]
        """

        return self._object_property_expressions

    @object_property_expressions.setter
    def object_property_expressions(
        self, value: list[OWLObjectPropertyExpression]
    ) -> None:
        """Setter for object_property_expressions."""
        self._object_property_expressions = sorted(value)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the disjoint object properties axiom, formatted to resemble a functional syntax constructor. The string includes the axiom annotations, defaulting to an empty list representation if none are present, followed by the string representations of the object property expressions involved in the disjointness relationship. This method has no side effects and does not alter the state of the object.

        :return: A string representation of the disjoint object properties axiom, including any annotations and the list of object property expressions.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"DisjointObjectProperties({self.axiom_annotations} {' '.join(map(str, self.object_property_expressions))})"
        else:
            return f"DisjointObjectProperties([] {' '.join(map(str, self.object_property_expressions))})"
