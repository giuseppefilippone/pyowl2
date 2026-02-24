import typing

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectExactCardinality(OWLClassExpression):
    """
    Represents an object property restriction within an ontology that constrains an individual to be related to exactly a specific number of other individuals via a defined relationship. To utilize this restriction, one must provide a non-negative integer indicating the exact count and an object property expression that defines the relationship. An optional class expression can be included to create a qualified restriction, specifying that the related individuals must also be instances of a particular class; if this is omitted, the restriction applies to any individual connected via the specified property.

    :param cardinality: The exact non-negative integer count of distinct individuals that the subject must be related to via the object property to satisfy the restriction.
    :type cardinality: int
    :param object_property_expression: The object property expression that defines the relationship used to count the exact number of related individuals in the restriction.
    :type object_property_expression: OWLObjectPropertyExpression
    :param class_expression: The optional class expression defining the type of individuals that the subject must be related to via the object property. If provided, it creates a qualified restriction; otherwise, the restriction applies to any individual filling the property.
    :type class_expression: typing.Optional[OWLClassExpression]
    """

    def __init__(
        self,
        value: int,
        property: OWLObjectPropertyExpression,
        expression: typing.Optional[OWLClassExpression] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL object property restriction with an exact cardinality constraint. The method accepts an integer value specifying the exact number of distinct individuals that must be connected via the provided object property expression, as well as an optional class expression that acts as the filler for the restriction. It enforces a precondition that the cardinality value must be non-negative, raising an assertion error if this condition is violated. Finally, the constructor assigns the value, property, and optional expression to internal attributes to maintain the state of the restriction.

        :param value: The non-negative cardinality value for the restriction.
        :type value: int
        :param property: The object property expression on which the cardinality restriction is defined.
        :type property: OWLObjectPropertyExpression
        :param expression: The class expression acting as the filler for the restriction. If None, the restriction is unqualified.
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
        Updates the exact cardinality value for this OWL object restriction. The method accepts an integer representing the specific number of property values required and assigns it to the object's internal state. This operation directly modifies the underlying attribute without performing explicit validation on the provided integer.

        :param value: The new cardinality value to assign.
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
        Updates the object property expression associated with this exact cardinality restriction by assigning the provided value. This method modifies the internal state of the object, replacing the existing property expression with the new one specified.

        :param value: The OWL object property expression to assign to the instance.
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
        Updates the class expression associated with this OWL object exact cardinality restriction. This method accepts an optional OWLClassExpression instance, allowing the restriction's filler to be explicitly set or cleared by passing None. The operation directly mutates the instance's internal state, overwriting any previously stored class expression value.

        :param value: The new class expression to assign, or None to clear the value.
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
        Determines whether this exact cardinality restriction is qualified by verifying the presence of a specific class expression filler. In the context of OWL restrictions, a qualified restriction limits the count of relationships to objects that are instances of a particular class, whereas an unqualified restriction simply limits the count of relationships regardless of the object type. This property returns `True` if a class expression is defined, and `False` otherwise.

        :return: True if the object has an associated class expression, False otherwise.

        :rtype: bool
        """

        return self.class_expression is not None

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the object exact cardinality restriction, formatted to resemble functional syntax. The output dynamically adapts based on the presence of a class expression filler; if a class expression is defined, the string includes the cardinality, the object property expression, and the class expression. If the class expression is absent, the representation consists only of the cardinality and the object property expression.

        :return: A human-readable string representation of the object exact cardinality restriction, displaying the cardinality, object property, and optionally the class expression.

        :rtype: str
        """

        if self.class_expression:
            return f"ObjectExactCardinality({self.cardinality} {self.object_property_expression} {self.class_expression})"
        else:
            return f"ObjectExactCardinality({self.cardinality} {self.object_property_expression})"
