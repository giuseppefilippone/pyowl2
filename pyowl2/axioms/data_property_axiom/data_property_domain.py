import typing

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLDataPropertyDomain(OWLDataPropertyAxiom):
    """
    Represents an axiom in the Web Ontology Language (OWL) that defines the domain restriction for a specific data property, asserting that any individual associated with the property must belong to a specified class. It links a data property expression—which connects individuals to literal values—with a class expression that defines the valid types of subjects for that property. Users can utilize this structure to enforce logical consistency within an ontology by specifying the property, its domain class, and optional annotations for metadata. The implementation supports both simple named classes and complex class expressions, allowing for nuanced constraints on the individuals that may participate in data property assertions.

    :param data_property_expression: The data property expression whose domain is defined by this axiom.
    :type data_property_expression: OWLDataPropertyExpression
    :param class_expression: Specifies the domain of the data property, defining the class of individuals that can be associated with it.
    :type class_expression: OWLClassExpression
    """

    def __init__(
        self,
        property: OWLDataPropertyExpression,
        expression: OWLClassExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL data property domain axiom, which constrains the individuals that can be the subject of a specific data property relationship. The constructor accepts a data property expression to define the property, a class expression to define the domain, and an optional list of annotations for metadata. It delegates the storage of annotations to the parent class and retains the property and class expressions as internal state.

        :param property: The data property expression for which the axiom is defined.
        :type property: OWLDataPropertyExpression
        :param expression: The class expression that defines the domain of the data property.
        :type expression: OWLClassExpression
        :param annotations: Optional list of annotations to be attached to the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._data_property_expression: OWLDataPropertyExpression = property
        self._class_expression: OWLClassExpression = expression

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
        Sets the data property expression for this OWL data property domain axiom. This method assigns the provided OWLDataPropertyExpression to the internal state, overwriting any previously stored value. It defines the specific data property whose domain is being restricted by this axiom.

        :param value: The OWL data property expression to assign.
        :type value: OWLDataPropertyExpression
        """

        return self._data_property_expression

    @data_property_expression.setter
    def data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expression."""
        self._data_property_expression = value

    @property
    def class_expression(self) -> OWLClassExpression:
        """
        Sets the class expression that defines the domain for this data property axiom. This method assigns the provided `OWLClassExpression` instance to the internal state, effectively replacing any previously associated domain expression. As a setter, it mutates the object in place and does not return a value.

        :param value: The OWL class expression to assign.
        :type value: OWLClassExpression
        """

        return self._class_expression

    @class_expression.setter
    def class_expression(self, value: OWLClassExpression) -> None:
        """Setter for class_expression."""
        self._class_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the data property domain axiom using a functional syntax style. The formatted string includes the axiom's annotations, the associated data property expression, and the class expression defining the domain. If the axiom does not contain any annotations, the representation explicitly includes an empty list `[]` in the annotations position to maintain structural consistency.

        :return: Returns a string representation of the data property domain axiom, including its annotations, data property expression, and class expression.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"DataPropertyDomain({self.axiom_annotations} {self.data_property_expression} {self.class_expression})"
        else:
            return f"DataPropertyDomain([] {self.data_property_expression} {self.class_expression})"
