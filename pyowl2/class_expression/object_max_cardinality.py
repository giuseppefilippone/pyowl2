import typing

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectMaxCardinality(OWLClassExpression):
    """
    This class represents a restriction in an ontology that defines an upper bound on the number of distinct individuals an entity can be related to via a specific object property. It is used to construct class expressions where instances must satisfy a condition of having at most a certain number of relationships, such as a person having no more than two siblings. The restriction can be unqualified, applying to any individual connected by the property, or qualified, where the connected individuals must also belong to a specific class expression. To utilize this class, instantiate it with a non-negative integer representing the maximum cardinality, the object property expression defining the relationship, and an optional class expression to further constrain the type of the related individuals.

    :param cardinality: The non-negative integer defining the maximum number of distinct individuals an instance can be related to via the specified object property.
    :type cardinality: int
    :param object_property_expression: The object property expression defining the relationship being restricted, which may be a simple property or a complex expression involving property chains or inverses.
    :type object_property_expression: OWLObjectPropertyExpression
    :param class_expression: Optional class expression that restricts the type of individuals the subject can be related to. If provided, it creates a qualified cardinality restriction; otherwise, the restriction applies to any individual.
    :type class_expression: typing.Optional[OWLClassExpression]
    """

    def __init__(
        self,
        value: int,
        property: OWLObjectPropertyExpression,
        expression: typing.Optional[OWLClassExpression] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL object maximum cardinality restriction, which constrains the number of relationships an individual can have via a specific object property. The constructor accepts a non-negative integer defining the maximum count, an object property expression to restrict, and an optional class expression that specifies the type of the related individuals. It validates that the cardinality value is not negative and stores these components within the instance for use in ontology reasoning and representation.

        :param value: The non-negative cardinality of the restriction.
        :type value: int
        :param property: The object property expression to which the cardinality restriction applies.
        :type property: OWLObjectPropertyExpression
        :param expression: The class expression that restricts the values of the object property. If None, the restriction is unqualified.
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
        Sets the maximum cardinality value for this OWL object restriction. This method updates the internal state by assigning the provided integer to the private `_cardinality` attribute. It modifies the instance in place and does not return a value, allowing the constraint limit to be changed after object creation.

        :param value: The desired cardinality to set.
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
        Assigns the specified object property expression to this maximum cardinality restriction, defining the property whose occurrences are being limited. This method updates the internal state of the restriction, replacing any previously associated property expression with the new value. The input is expected to be a valid object property expression compatible with the underlying OWL ontology structure.

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
        Assigns a new class expression to this maximum cardinality restriction, replacing the existing value. The method accepts an `OWLClassExpression` object or `None` and updates the internal `_class_expression` attribute accordingly. This operation directly mutates the object's state without returning a value.

        :param value: The OWL class expression to assign, or None to clear the current value.
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
        Determines whether the object max cardinality restriction is qualified by checking for the presence of a specific class expression. In the context of OWL restrictions, a qualified restriction explicitly defines the class of the filler, whereas an unqualified restriction implicitly defaults to the universal class. This property returns True if the internal `class_expression` attribute is not None, indicating that a specific filler class has been defined, and False otherwise.

        :return: True if a class expression is defined, False otherwise.

        :rtype: bool
        """

        return self.class_expression is not None

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the object using a functional syntax format. The representation includes the cardinality value and the object property expression. If a class expression is defined, it is appended to the output; otherwise, the string is generated using only the cardinality and property components.

        :return: A string representation of the object max cardinality restriction in functional syntax format.

        :rtype: str
        """

        if self.class_expression:
            return f"ObjectMaxCardinality({self.cardinality} {self.object_property_expression} {self.class_expression})"
        else:
            return f"ObjectMaxCardinality({self.cardinality} {self.object_property_expression})"
