import typing

from pyowl2.abstracts.assertion import OWLAssertion
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.literal.literal import OWLLiteral


class OWLDataPropertyAssertion(OWLAssertion):
    """
    This class represents a fundamental axiom used to define facts about an individual within an OWL ontology by associating it with a specific data value via a data property. It serves as a structured container linking a subject individual to a target literal—such as a number or string—through a specific property expression, enabling the representation of statements like "Alice hasAge 30". To utilize this component, one must provide the data property expression, the source individual, and the target literal during instantiation, with the option to attach annotations for further context or metadata.

    :parm data_property_expression: The data property expression that relates the source individual to the target value.
    :type data_property_expression: OWLDataPropertyExpression
    :parm source_individual: The individual that is the subject of the assertion, possessing the specific data value for the data property.
    :type source_individual: OWLIndividual
    :parm target_value: The data value to which the relationship points, such as "30" in the assertion "Alice hasAge 30".
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
        Constructs an axiom asserting that a specific individual is associated with a literal value via a data property. The method initializes the instance by storing the provided data property expression, the source individual, and the target literal value. It also accepts an optional list of annotations, delegating their storage to the superclass initialization to ensure they are correctly associated with the axiom.

        :param expression: The data property expression representing the relationship between the source individual and the literal value.
        :type expression: OWLDataPropertyExpression
        :param source: The individual that is the subject of the data property assertion.
        :type source: OWLIndividual
        :param value: The OWL literal value that is the target of this data property assertion.
        :type value: OWLLiteral
        :param annotations: Optional list of annotations to be associated with this axiom.
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
        Updates the specific data property expression used in this assertion by assigning the provided value to the internal state. This setter replaces the existing `_data_property_expression` attribute with the new `OWLDataPropertyExpression` instance. The method expects the input to be a valid data property expression object, ensuring the assertion maintains a valid OWL structure.

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
        Assigns the provided individual as the source (or subject) of this data property assertion. This operation directly updates the internal state of the assertion, overwriting any existing source individual. The method expects an instance of OWLIndividual, though no runtime validation is explicitly performed to ensure the type matches the hint.

        :param value: The OWL individual to set as the source individual.
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
        Updates the literal value associated with this data property assertion by assigning the provided `OWLLiteral` instance to the internal `_target_value` attribute. This setter overwrites any previously stored value, effectively modifying the assertion to reference the new data value.

        :param value: The literal to assign as the target value.
        :type value: OWLLiteral
        """

        return self._target_value

    @target_value.setter
    def target_value(self, value: OWLLiteral) -> None:
        """Setter for target_value."""
        self._target_value = value

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the data property assertion axiom, formatted according to a functional syntax style. The representation includes the axiom's annotations, data property expression, source individual, and target value, enclosed within parentheses. If the axiom has no associated annotations, an empty list is displayed in their place to preserve the structural format. This method does not modify the object's state.

        :return: A string representation of the data property assertion in functional syntax format.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"DataPropertyAssertion({self.axiom_annotations} {self.data_property_expression} {self.source_individual} {self.target_value})"
        else:
            return f"DataPropertyAssertion([] {self.data_property_expression} {self.source_individual} {self.target_value})"
