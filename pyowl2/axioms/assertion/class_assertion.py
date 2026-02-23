import typing

from pyowl2.abstracts.assertion import OWLAssertion
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.base.annotation import OWLAnnotation


class OWLClassAssertion(OWLAssertion):
    """
    This class represents a fundamental axiom in the Web Ontology Language (OWL) used to declare that a specific individual is an instance of a given class expression. It serves to classify entities within an ontology by linking an `OWLIndividual` to an `OWLClassExpression`, effectively stating that the individual belongs to the defined type. Users can instantiate this object to define type relationships, optionally providing a list of annotations to attach metadata to the assertion itself. The component allows for the modification of both the class expression and the individual after instantiation through its properties, and it integrates into the broader ontology structure by inheriting from `OWLAssertion`.

    :parm class_expression: The class expression that the individual is asserted to be an instance of.
    :type class_expression: OWLClassExpression
    :parm individual: The specific entity that is asserted to be an instance of the class expression.
    :type individual: OWLIndividual
    """

    def __init__(
        self,
        expression: OWLClassExpression,
        individual: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL class assertion axiom, which semantically declares that a specific individual is an instance of a given class expression. The constructor accepts the class expression describing the type and the individual entity being classified, along with an optional list of annotations for axiom metadata. It delegates annotation handling to the parent class and stores the core components internally for subsequent access.

        :param expression: The class expression that the individual is asserted to be an instance of.
        :type expression: OWLClassExpression
        :param individual: The individual that is asserted to be an instance of the class expression.
        :type individual: OWLIndividual
        :param annotations: Optional list of annotations to be attached to this axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._class_expression: OWLClassExpression = expression
        self._individual: OWLIndividual = individual

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def class_expression(self) -> OWLClassExpression:
        """
        Updates the class expression associated with this OWL class assertion by assigning the provided value. This operation overwrites the existing class expression stored internally, effectively changing the type or classification being asserted. The method expects an instance of OWLClassExpression as input to ensure the structural integrity of the axiom.

        :param value: The class expression to assign to this object.
        :type value: OWLClassExpression
        """

        return self._class_expression

    @class_expression.setter
    def class_expression(self, value: OWLClassExpression) -> None:
        """Setter for class_expression."""
        self._class_expression = value

    @property
    def individual(self) -> OWLIndividual:
        """
        Assigns the specified individual to this class assertion axiom, replacing any previously associated individual. This method updates the internal state of the object to reflect that the provided OWLIndividual is the subject of the assertion. It acts as a direct mutator and does not return a value.

        :param value: The OWL individual instance to assign.
        :type value: OWLIndividual
        """

        return self._individual

    @individual.setter
    def individual(self, value: OWLIndividual) -> None:
        """Setter for individual."""
        self._individual = value

    def __str__(self) -> str:
        """
        Returns a string representation of the class assertion axiom using a functional syntax format. The string includes the axiom annotations, the class expression, and the individual. If the object has no annotations, the representation explicitly includes an empty list placeholder to preserve the structural format.

        :return: A string representation of the class assertion, formatted as "ClassAssertion([annotations] class_expression individual)".

        :rtype: str
        """

        if self.axiom_annotations:
            return f"ClassAssertion({self.axiom_annotations} {self.class_expression} {self.individual})"
        else:
            return f"ClassAssertion([] {self.class_expression} {self.individual})"
