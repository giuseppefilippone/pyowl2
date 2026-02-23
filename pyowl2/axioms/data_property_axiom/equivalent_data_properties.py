import typing

from pyowl2.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLEquivalentDataProperties(OWLDataPropertyAxiom):
    """
    This class represents an OWL axiom asserting that two or more data properties share the same property extension, effectively treating them as synonyms for the purpose of data assertions. To utilize this class, instantiate it with a list of `OWLDataPropertyExpression` objects containing at least two members, optionally accompanied by a list of `OWLAnnotation` objects for metadata. It is important to note that the class enforces a minimum of two properties and automatically sorts the provided expressions upon initialization and assignment to maintain a consistent internal state.

    :parm data_property_expressions: Internal list of data property expressions declared to be equivalent, maintained in sorted order.
    :type data_property_expressions: list[OWLDataPropertyExpression]
    """

    def __init__(
        self,
        expressions: list[OWLDataPropertyExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an OWL axiom representing the equivalence between a set of data properties. The constructor accepts a list of data property expressions and an optional list of annotations, passing the annotations to the parent class. It enforces a constraint that the list of expressions must contain at least two elements. The property expressions are stored in a sorted list to normalize the internal state, ensuring that the order of input does not affect the axiom's identity or representation.

        :param expressions: The data property expressions involved in the axiom. The list must contain at least two elements.
        :type expressions: list[OWLDataPropertyExpression]
        :param annotations: A list of annotations to be attached to the axiom.
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
        Updates the set of data property expressions that constitute this equivalence axiom. The provided list is sorted before being assigned to the internal attribute, ensuring a consistent canonical order. This operation overwrites the previously stored collection of expressions.

        :param value: A list of OWL data property expressions to assign to the object.
        :type value: list[OWLDataPropertyExpression]
        """

        return self._data_property_expressions

    @data_property_expressions.setter
    def data_property_expressions(self, value: list[OWLDataPropertyExpression]) -> None:
        """Setter for data_property_expressions."""
        self._data_property_expressions = sorted(value)

    def __str__(self) -> str:
        """
        Generates a human-readable string representation of the OWL equivalent data properties axiom. The output formats the axiom as a pseudo-function call containing the list of annotations, displaying an empty list if none are present, followed by the space-separated string representations of the data property expressions. This method is primarily used for debugging or logging purposes to visualize the structure of the axiom.

        :return: A string representation of the object, displaying the axiom annotations and the list of data property expressions.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"EquivalentDataProperties({self.axiom_annotations} {' '.join(map(str, self.data_property_expressions))})"
        else:
            return f"EquivalentDataProperties([] {' '.join(map(str, self.data_property_expressions))})"
