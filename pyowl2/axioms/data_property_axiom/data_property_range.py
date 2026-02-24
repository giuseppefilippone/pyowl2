import typing

from pyowl2.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.abstracts.property_range import OWLPropertyRange
from pyowl2.base.annotation import OWLAnnotation


class OWLDataPropertyRange(OWLPropertyRange, OWLDataPropertyAxiom):
    """
    This class represents an axiom within an ontology that defines the permissible types of literal values for a specific data property. It functions by associating a data property expression with a data range, thereby enforcing constraints such as requiring a property to hold only integers, strings, or values satisfying specific facet restrictions. Users can instantiate this entity to declare these type restrictions, optionally attaching annotations to provide additional metadata or context regarding the axiom itself.

    :param data_property_expression: The data property expression for which the range is being specified.
    :type data_property_expression: OWLDataPropertyExpression
    :param data_range: The set of data values or data types permitted for the associated data property.
    :type data_range: OWLDataRange
    """

    def __init__(
        self,
        property: OWLDataPropertyExpression,
        data_range: OWLDataRange,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL Data Property Range axiom, which asserts that the values of the specified data property must belong to the provided data range. The constructor requires the data property expression and the data range as arguments, while annotations are optional and default to None. It stores the property and range as private attributes and passes the annotations to the superclass for initialization.

        :param property: The data property expression that is the subject of the axiom.
        :type property: OWLDataPropertyExpression
        :param data_range: The data range to be associated with the data property.
        :type data_range: OWLDataRange
        :param annotations: Optional list of annotations to be associated with the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._data_property_expression: OWLDataPropertyExpression = property
        self._data_range: OWLDataRange = data_range

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
        Assigns the specified data property expression to this instance, replacing any previously held value. The method accepts an object of type `OWLDataPropertyExpression` and updates the internal state to reflect this change. This operation mutates the object in place and does not return a value.

        :param value: The data property expression to assign to this object.
        :type value: OWLDataPropertyExpression
        """

        return self._data_property_expression

    @data_property_expression.setter
    def data_property_expression(self, value: OWLDataPropertyExpression) -> None:
        """Setter for data_property_expression."""
        self._data_property_expression = value

    @property
    def data_range(self) -> OWLDataRange:
        """
        Updates the data range associated with this OWL data property range axiom by assigning the provided value to the internal storage attribute. This operation overwrites any previously defined range without performing explicit validation. The method returns None and modifies the object's state in place.

        :param value: The data range to assign to the object.
        :type value: OWLDataRange
        """

        return self._data_range

    @data_range.setter
    def data_range(self, value: OWLDataRange) -> None:
        """Setter for data_range."""
        self._data_range = value

    def __str__(self) -> str:
        """
        Returns a string representation of the OWL data property range axiom, formatted according to a specific functional syntax. The representation always includes the axiom annotations, defaulting to an empty list if none are present, followed by the data property expression and the data range. This method does not modify the object's state and is primarily intended for debugging or display purposes.

        :return: A string representation of the axiom, including its annotations, data property expression, and data range.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"DataPropertyRange({self.axiom_annotations} {self.data_property_expression} {self.data_range})"
        else:
            return f"DataPropertyRange([] {self.data_property_expression} {self.data_range})"
