import typing

from pyowl2.abstracts.assertion import OWLAssertion
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLObjectPropertyAssertion(OWLAssertion):
    """
    This axiom represents a specific factual statement within an ontology, declaring that a binary relationship defined by an object property exists between two distinct individuals. It serves to ground abstract properties by connecting a specific source individual to a specific target individual, effectively stating that the source relates to the target via the given property. To construct this assertion, provide the object property expression, the source individual, and the target individual during initialization, optionally including a list of annotations to attach metadata to the axiom itself. Once instantiated, the components of the relationship can be accessed or modified via their corresponding properties.

    :param object_property_expression: The object property expression that relates the source and target individuals.
    :type object_property_expression: OWLObjectPropertyExpression
    :param source_individual: The individual from which the object property relationship originates, representing the subject of the assertion.
    :type source_individual: OWLIndividual
    :param target_individual: The individual to which the object property relationship points, serving as the object of the assertion.
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
        Initializes an OWL object property assertion axiom, which defines a specific relationship between a source individual and a target individual. This constructor accepts the object property expression representing the relation, the individual acting as the subject, and the individual acting as the object. It also supports an optional list of annotations to attach metadata to the axiom, passing them to the parent class for initialization while storing the core assertion components as internal attributes.

        :param expression: The object property expression representing the relationship asserted between the source and target individuals.
        :type expression: OWLObjectPropertyExpression
        :param source: The individual acting as the subject of the object property assertion.
        :type source: OWLIndividual
        :param target: The individual acting as the target of the object property assertion.
        :type target: OWLIndividual
        :param annotations: Optional collection of metadata objects to be attached to the axiom.
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
        Sets the object property expression for this assertion, defining the specific relationship that holds between the involved individuals. The provided value, which must be an instance of OWLObjectPropertyExpression, replaces the existing property expression stored within the object. This method updates the internal state of the assertion in place and returns nothing.

        :param value: The object property expression to assign.
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
        Sets the source individual for this object property assertion, effectively defining the subject of the relationship. This method updates the internal state by assigning the provided `OWLIndividual` instance to the corresponding private attribute, overwriting any previously stored value. It is intended to be used to modify the assertion's subject after the object has been initialized.

        :param value: The OWLIndividual to be set as the source individual.
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
        Sets the target individual (the object) of this OWL object property assertion to the provided value. This method updates the internal state of the assertion, replacing the existing target with the specified `OWLIndividual`. This operation mutates the instance, altering the semantic relationship defined by the assertion.

        :param value: The OWL individual to assign as the target.
        :type value: OWLIndividual
        """

        return self._target_individual

    @target_individual.setter
    def target_individual(self, value: OWLIndividual) -> None:
        """Setter for target_individual."""
        self._target_individual = value

    def __str__(self) -> str:
        """
        Returns a string representation of the object property assertion axiom in a functional syntax style. The output includes the axiom annotations, object property expression, source individual, and target individual. If no annotations are present, an empty list is used in the string representation to preserve the structural format.

        :return: A string representation of the object property assertion in functional syntax, including annotations, the object property expression, and the source and target individuals.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"ObjectPropertyAssertion({self.axiom_annotations} {self.object_property_expression} {self.source_individual} {self.target_individual})"
        else:
            return f"ObjectPropertyAssertion([] {self.object_property_expression} {self.source_individual} {self.target_individual})"
