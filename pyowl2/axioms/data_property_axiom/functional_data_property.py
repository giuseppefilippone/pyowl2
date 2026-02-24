import typing

from pyowl2.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLFunctionalDataProperty(OWLDataPropertyAxiom):
    """
    This class models an axiom used to define a data property as functional, meaning that any individual in the ontology can be associated with at most one distinct data value through that specific property. It enforces a uniqueness constraint where, if an individual is linked to multiple values, those values are inferred to be identical. Users can instantiate this object by providing the target data property expression and, optionally, a list of annotations to attach metadata to the axiom itself. This construct is essential for representing attributes that must have a single value, such as a unique identifier or a specific measurement, within an OWL ontology.

    :param data_property_expression: The data property expression that is declared to be functional.
    :type data_property_expression: OWLDataPropertyExpression
    """

    def __init__(
        self,
        property: OWLDataPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL functional data property axiom, which asserts that a specific data property can have at most one value for any given individual. The constructor requires a data property expression to define the subject of the axiom and accepts an optional list of annotations for metadata. It delegates the management of these annotations to the parent class and stores the provided property expression internally as a private attribute.

        :param property: The OWL data property expression associated with this axiom.
        :type property: OWLDataPropertyExpression
        :param annotations: A list of OWLAnnotation objects to be associated with the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._data_property_expression: OWLDataPropertyExpression = property

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
        Assigns the specified data property expression to this functional data property instance. This method updates the internal state by replacing the existing property expression with the provided value, effectively defining which data property is constrained by the functional characteristic.

        :param value: The data property expression to assign.
        :type value: OWLDataPropertyExpression
        """

        return self._data_property_expression

    @data_property_expression.setter
    def data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expression."""
        self._data_property_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the functional data property axiom in a functional syntax format. The output string includes the keyword 'FunctionalDataProperty' followed by the axiom annotations and the data property expression. If the object contains no annotations, the representation explicitly includes an empty list placeholder. This method does not modify the object's state and is intended for display or logging purposes.

        :return: The functional syntax string representation of the axiom, including annotations and the data property expression.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"FunctionalDataProperty({self.axiom_annotations} {self.data_property_expression})"
        else:
            return f"FunctionalDataProperty([] {self.data_property_expression})"
