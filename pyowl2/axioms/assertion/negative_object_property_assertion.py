import typing

from pyowl2.abstracts.assertion import OWLAssertion
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLNegativeObjectPropertyAssertion(OWLAssertion):
    """
    This class represents an axiom in the Web Ontology Language (OWL) that explicitly negates a relationship between two specific individuals. It is used to assert that a given object property expression does not link a source individual to a target individual, allowing for the precise definition of what is false within an ontology. Users can instantiate this class by providing the property to be negated, the subject and object individuals, and an optional list of annotations to attach metadata to the assertion.

    :param object_property_expression: The object property expression that is asserted not to hold between the source and target individuals.
    :type object_property_expression: OWLObjectPropertyExpression
    :param source_individual: The individual from which the relationship is asserted not to originate.
    :type source_individual: OWLIndividual
    :param target_individual: The individual to which the relationship is asserted not to point.
    :type target_individual: OWLIndividual
    """

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        source: OWLIndividual,
        target: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL negative object property assertion axiom, which formally states that a specific object property relationship does not hold between a source individual and a target individual. The constructor requires the property expression, the source individual, and the target individual as mandatory arguments to define the core assertion. It also accepts an optional list of annotations, which are passed to the parent class to handle axiom-level metadata.

        :param expression: The object property expression representing the relationship between the source and target individuals.
        :type expression: OWLObjectPropertyExpression
        :param source: The individual acting as the subject of the object property assertion.
        :type source: OWLIndividual
        :param target: The individual that serves as the target of the object property assertion.
        :type target: OWLIndividual
        :param annotations: Optional list of annotations to be associated with this axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._object_property_expression: OWLObjectPropertyExpression = expression
        self._source_individual: OWLIndividual = source
        self._target_individual: OWLIndividual = target

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Assigns the specified object property expression to this negative object property assertion, replacing any existing value. This method updates the internal state of the instance to reflect the new relationship that is being negated. The provided value must be an instance of OWLObjectPropertyExpression to maintain semantic validity within the OWL structure.

        :param value: The OWL object property expression to assign.
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    @property
    def source_individual(self) -> OWLIndividual:
        """
        Updates the subject of the negative object property assertion to the provided OWLIndividual. This setter modifies the internal state by overwriting the current source individual with the new value.

        :param value:
        :type value: OWLIndividual
        """

        return self._source_individual

    @source_individual.setter
    def source_individual(self, value: OWLIndividual) -> None:
        """Setter for source_individual."""
        self._source_individual = value

    @property
    def target_individual(self) -> OWLIndividual:
        """
        Updates the target individual associated with this negative object property assertion. This method assigns the provided OWLIndividual instance to the internal state, overwriting any previously stored value. It defines the specific individual that is asserted not to participate in the object property relationship with the source individual.

        :param value: The OWLIndividual to be set as the target individual.
        :type value: OWLIndividual
        """

        return self._target_individual

    @target_individual.setter
    def target_individual(self, value: OWLIndividual) -> None:
        """Setter for target_individual."""
        self._target_individual = value

    def __str__(self) -> str:
        """
        Returns a string representation of the negative object property assertion using a functional syntax format. The output includes the axiom type, the list of annotations (represented as an empty list if none are present), the object property expression, the source individual, and the target individual. This ensures a consistent textual format that explicitly indicates the presence or absence of annotations.

        :return: A string representation of the negative object property assertion in functional syntax, displaying the annotations, object property expression, source individual, and target individual.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"NegativeObjectPropertyAssertion({self.axiom_annotations} {self.object_property_expression} {self.source_individual} {self.target_individual})"
        else:
            return f"NegativeObjectPropertyAssertion([] {self.object_property_expression} {self.source_individual} {self.target_individual})"
