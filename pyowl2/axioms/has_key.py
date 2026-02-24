import typing

from pyowl2.abstracts.class_axiom import OWLClassAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLHasKey(OWLClassAxiom):
    """
    This entity represents an OWL axiom used to declare that a specific class possesses a set of properties—comprising both object and data properties—that function as a unique key for its instances. By defining this key, the ontology asserts that no two distinct individuals of the specified class can share identical values for all the listed properties, thereby facilitating efficient retrieval and reasoning. To construct this axiom, provide the class expression to which the key applies, along with lists of the object and data property expressions that form the key; optional annotations may also be supplied to attach metadata. The implementation automatically sorts the provided property lists to maintain a canonical order.

    :param class_expression: The class expression specifying the type of individuals for which the associated properties act as a unique key.
    :type class_expression: OWLClassExpression
    :param object_property_expressions: A sorted list of object property expressions that form part of the key, used to uniquely identify instances by their relationships to other individuals.
    :type object_property_expressions: list[OWLObjectPropertyExpression]
    :param data_property_expressions: A list of data property expressions that form part of the key, relating individuals to data values to uniquely identify instances of the class.
    :type data_property_expressions: list[OWLDataPropertyExpression]
    """

    def __init__(
        self,
        expression: OWLClassExpression,
        object_properties: list[OWLObjectPropertyExpression],
        data_properties: list[OWLDataPropertyExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an OWL axiom asserting that a specific class expression is uniquely identified by a combination of object and data properties. The constructor accepts the target class expression, lists of object and data property expressions that constitute the key, and an optional list of annotations. It invokes the superclass constructor to handle the annotations. As a side effect, the provided lists of object and data properties are sorted internally before being assigned to instance attributes, ensuring a deterministic internal state.

        :param expression: The OWL class expression that constitutes the subject of the axiom.
        :type expression: OWLClassExpression
        :param object_properties: A collection of object property expressions involved in the axiom. The list is sorted internally upon initialization.
        :type object_properties: list[OWLObjectPropertyExpression]
        :param data_properties: A list of data property expressions involved in the axiom.
        :type data_properties: list[OWLDataPropertyExpression]
        :param annotations: Optional list of annotations to be attached to the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = sorted(annotations) if annotations else annotations
        self._class_expression: OWLClassExpression = expression
        self._object_property_expressions: list[OWLObjectPropertyExpression] = sorted(
            object_properties
        )
        self._data_property_expressions: list[OWLDataPropertyExpression] = sorted(
            data_properties
        )

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = sorted(value) if value else value

    @property
    def class_expression(self) -> OWLClassExpression:
        """
        Updates the OWL class expression associated with this HasKey axiom. This method assigns the provided `OWLClassExpression` instance to the internal attribute, thereby modifying the state of the object to reflect the new class context for the key constraint.

        :param value: The OWL class expression to assign to the property.
        :type value: OWLClassExpression
        """

        return self._class_expression

    @class_expression.setter
    def class_expression(self, value: OWLClassExpression) -> None:
        """Setter for class_expression."""
        self._class_expression = value

    @property
    def object_property_expressions(self) -> list[OWLObjectPropertyExpression]:
        """
        Updates the collection of object property expressions that constitute the key constraint for this axiom. It accepts a list of OWLObjectPropertyExpression instances and assigns them to the internal state. Notably, the provided list is sorted before storage, ensuring that the properties are maintained in a deterministic order regardless of the input sequence.

        :param value: A list of OWL object property expressions to assign.
        :type value: list[OWLObjectPropertyExpression]
        """

        return self._object_property_expressions

    @object_property_expressions.setter
    def object_property_expressions(
        self, value: list[OWLObjectPropertyExpression]
    ) -> None:
        """Setter for object_property_expressions."""
        self._object_property_expressions = sorted(value)

    @property
    def data_property_expressions(self) -> list[OWLDataPropertyExpression]:
        """
        Updates the collection of data property expressions that define the key constraint by assigning a new list of `OWLDataPropertyExpression` objects. The input list is sorted prior to storage to ensure a consistent, canonical order, which means the order of elements in the provided argument does not affect the final internal state. This method modifies the object's internal state directly and returns nothing.

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
        Returns a string representation of the HasKey axiom, formatted according to a functional-style syntax. The output string concatenates the axiom's annotations, the target class expression, and the sequences of object and data property expressions that define the key. If the axiom contains annotations, they are included in the string; otherwise, an empty list placeholder is used. This method relies on the string conversion of the internal components and does not modify the object's state.

        :return: Returns a functional-style string representation of the HasKey axiom, including the class expression, property expressions, and any annotations.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"HasKey({self.axiom_annotations} {self.class_expression}({' '.join(map(str, self.object_property_expressions))})({' '.join(map(str, self.data_property_expressions))}))"
        else:
            return f"HasKey([] {self.class_expression}({' '.join(map(str, self.object_property_expressions))})({' '.join(map(str, self.data_property_expressions))}))"
