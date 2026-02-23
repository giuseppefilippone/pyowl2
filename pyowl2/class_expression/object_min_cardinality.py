import typing

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectMinCardinality(OWLClassExpression):
    """
    This class models a restriction that requires an individual to be linked to at least a specific number of other individuals through a defined object property. To use it, instantiate the class with a non-negative integer representing the minimum count, an object property expression describing the relationship, and an optional class expression to filter the type of the target individuals. If the class expression is omitted, the restriction applies to any related individual; if included, it creates a qualified restriction where the targets must also belong to the specified class. As a subclass of class expression, it can be nested within other logical constructs to define complex ontology axioms.

    :parm cardinality: The non-negative integer value representing the minimum number of individuals that the subject individual must be related to via the specified object property.
    :type cardinality: int
    :parm object_property_expression: The object property expression defining the relationship that the subject individual must satisfy a minimum number of times. It can be a simple property or a complex expression involving inverses or property chains.
    :type object_property_expression: OWLObjectPropertyExpression
    :parm class_expression: Optional class expression that restricts the type of individuals counted towards the minimum cardinality. If provided, the restriction is qualified, requiring related individuals to be instances of this class; if omitted, the restriction applies to any related individual.
    :type class_expression: typing.Optional[OWLClassExpression]
    """

    def __init__(
        self,
        value: int,
        property: OWLObjectPropertyExpression,
        expression: typing.Optional[OWLClassExpression] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL minimum cardinality restriction on an object property. This constructor accepts a non-negative integer value defining the minimum number of distinct individuals an entity must be connected to via the specified object property expression. An optional class expression can be provided to restrict the type of the connected individuals; if omitted, the restriction applies to any individual. The method asserts that the cardinality value is non-negative and stores the provided arguments as internal attributes.

        :param value: The non-negative integer value representing the cardinality.
        :type value: int
        :param property: The object property expression on which the restriction is applied.
        :type property: OWLObjectPropertyExpression
        :param expression: The class expression acting as the filler for the restriction, defining the type of objects counted by the cardinality constraint.
        :type expression: typing.Optional[OWLClassExpression]
        """

        super().__init__()
        assert value >= 0
        self._cardinality: int = value
        self._object_property_expression: OWLObjectPropertyExpression = property
        self._class_expression: typing.Optional[OWLClassExpression] = expression

    @property
    def cardinality(self) -> int:
        """
        Updates the minimum cardinality value for this OWL object restriction by assigning the provided integer to the internal state. This method allows the constraint to be modified after the object has been created, replacing the existing cardinality with the new value. The provided value should be a non-negative integer representing the minimum number of times the associated property must participate in a relationship.

        :param value: The integer value to set as the cardinality.
        :type value: int
        """

        return self._cardinality

    @cardinality.setter
    def cardinality(self, value: int) -> None:
        """Setter for cardinality."""
        self._cardinality = value

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Sets the object property expression for this minimum cardinality restriction, defining the specific relationship that the cardinality constraint applies to. The provided value, which must be an instance of OWLObjectPropertyExpression, replaces any previously assigned property expression. This method mutates the internal state of the object by updating the private attribute storing the property.

        :param value: The OWL object property expression to assign.
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    @property
    def class_expression(self) -> typing.Optional[OWLClassExpression]:
        """
        Sets the class expression (filler) associated with this minimum cardinality restriction. It accepts an optional `OWLClassExpression` instance and updates the object's internal state by assigning the provided value to the private `_class_expression` attribute, overwriting any existing value.

        :param value: The OWL class expression to assign to the property, or None.
        :type value: typing.Optional[OWLClassExpression]
        """

        return self._class_expression

    @class_expression.setter
    def class_expression(self, value: typing.Optional[OWLClassExpression]) -> None:
        """Setter for class_expression."""
        self._class_expression = value

    @property
    def is_qualified(self) -> bool:
        """
        Indicates whether this minimum cardinality restriction is qualified by a specific class expression. It returns True if the restriction defines a filler class that the property values must instantiate, and False otherwise. This distinction separates simple cardinality constraints from those that restrict the range to a particular type.

        :return: True if the class expression is not None, False otherwise.

        :rtype: bool
        """

        return self.class_expression is not None

    def __str__(self) -> str:
        """
        Returns a string representation of the OWL minimum cardinality restriction, formatted to display the restriction type, the specific cardinality value, and the associated object property expression. The method conditionally includes the class expression in the output if it is present; otherwise, the representation is limited to the cardinality and property components. This implementation is primarily intended for debugging or logging purposes and does not alter the state of the object.

        :return: A string representation of the object min cardinality restriction, including the cardinality, object property expression, and optionally the class expression.

        :rtype: str
        """

        if self.class_expression:
            return f"ObjectMinCardinality({self.cardinality} {self.object_property_expression} {self.class_expression})"
        else:
            return f"ObjectMinCardinality({self.cardinality} {self.object_property_expression})"
