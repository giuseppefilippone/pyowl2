import typing

from pyowl2.abstracts.assertion import OWLAssertion
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.literal.literal import OWLLiteral


class OWLNegativeDataPropertyAssertion(OWLAssertion):
    """
    This entity models a negative assertion within an ontology, formally declaring that a specific individual is not associated with a particular literal value through a given data property. It is constructed by defining a source individual, a target data value, and the data property expression that connects them, effectively stating that the relationship does not exist. Users can optionally attach a list of annotations to the axiom to provide context or metadata. The internal components—the property, the individual, and the target value—are accessible and mutable, allowing for the assertion to be inspected or modified after creation.

    :param data_property_expression: The data property expression that is asserted not to relate the source individual to the target value.
    :type data_property_expression: OWLDataPropertyExpression
    :param source_individual: The individual that serves as the subject of the negative assertion, representing the entity that is asserted not to possess the specified data property value.
    :type source_individual: OWLIndividual
    :param target_value: The concrete data value that the source individual is asserted not to possess for the given data property.
    :type target_value: OWLLiteral
    """

    def __init__(
        self,
        expression: OWLDataPropertyExpression,
        source: OWLIndividual,
        value: OWLLiteral,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL negative data property assertion, which declares that a specific individual does not have a particular data property relationship with a given literal value. The constructor accepts the data property expression, the source individual, the target literal value, and an optional list of annotations to be associated with the axiom. It invokes the superclass constructor to handle the annotations and stores the core components of the assertion as private instance attributes.

        :param expression: The data property expression used to associate the source individual with the literal value.
        :type expression: OWLDataPropertyExpression
        :param source: The individual that is the subject of the data property assertion.
        :type source: OWLIndividual
        :param value: The literal value serving as the target of the data property assertion.
        :type value: OWLLiteral
        :param annotations: A list of annotations to be attached to this axiom, or None if no annotations are provided.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._data_property_expression: OWLDataPropertyExpression = expression
        self._source_individual: OWLIndividual = source
        self._target_value: OWLLiteral = value

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def data_property_expression(self) -> OWLDataPropertyExpression:
        """
        Assigns a new data property expression to this negative data property assertion, replacing any previously held value. The method accepts an instance of OWLDataPropertyExpression, defining the specific data property that is being negated for the subject individual. This setter directly mutates the internal state of the object.

        :param value: The OWL data property expression to assign to the object.
        :type value: OWLDataPropertyExpression
        """

        return self._data_property_expression

    @data_property_expression.setter
    def data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expression."""
        self._data_property_expression = value

    @property
    def source_individual(self) -> OWLIndividual:
        """
        Updates the subject individual associated with the negative data property assertion. This method assigns the provided OWLIndividual object to the internal state, overwriting any previously stored source individual.

        :param value: The OWL individual to assign as the source.
        :type value: OWLIndividual
        """

        return self._source_individual

    @source_individual.setter
    def source_individual(self, value: OWLIndividual) -> None:
        """Setter for source_individual."""
        self._source_individual = value

    @property
    def target_value(self) -> OWLLiteral:
        """
        Assigns the specific literal value that is being negated by this assertion. The method accepts an OWLLiteral object representing the data value and updates the internal state to reflect this new target. This operation modifies the object in place, changing the semantic meaning of the assertion to deny that the subject individual has this specific property value.

        :param value: The OWLLiteral to assign as the target value.
        :type value: OWLLiteral
        """

        return self._target_value

    @target_value.setter
    def target_value(self, value: OWLLiteral) -> None:
        """Setter for target_value."""
        self._target_value = value

    def __str__(self) -> str:
        """
        Returns a string representation of the negative data property assertion using a functional syntax format. The output string includes the axiom annotations, the data property expression, the source individual, and the target value. If the object has no associated annotations, the representation explicitly displays an empty list in the annotation position.

        :return: A string representation of the negative data property assertion in a functional syntax, including the annotations, data property expression, source individual, and target value.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"NegativeDataPropertyAssertion({self.axiom_annotations} {self.data_property_expression} {self.source_individual} {self.target_value})"
        else:
            return f"NegativeDataPropertyAssertion([] {self.data_property_expression} {self.source_individual} {self.target_value})"
