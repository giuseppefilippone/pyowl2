from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectHasSelf(OWLClassExpression):
    """
    This class models a specific type of existential restriction in the Web Ontology Language (OWL) where an individual is required to be related to itself via a designated object property. It encapsulates a property expression, which can be a simple property or a complex inverse or chain, to define the criteria for self-relation. To utilize this restriction, instantiate it with the desired object property expression; the resulting object can then be used within class expressions to define concepts such as "self-connected" entities. The property expression is mutable, allowing for dynamic modification of the restriction's definition after instantiation.

    :param object_property_expression: The object property expression that defines the relationship an individual must have with itself to satisfy the restriction.
    :type object_property_expression: OWLObjectPropertyExpression
    """

    def __init__(self, expression: OWLObjectPropertyExpression) -> None:
        """
        Initializes a new instance representing an OWL class expression that restricts individuals to those connected to themselves by a specific object property. The constructor accepts a single argument, an object property expression, which is stored internally to define the restriction. It ensures proper inheritance by calling the superclass initializer before assigning the provided expression to the instance's internal state, performing no additional validation or modification of the input.

        :param expression: The OWL object property expression to be encapsulated by this object.
        :type expression: OWLObjectPropertyExpression
        """

        super().__init__()
        self._object_property_expression: OWLObjectPropertyExpression = expression

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Updates the object property expression used to define this self-restriction. The method assigns the provided OWLObjectPropertyExpression to the internal state, overwriting any existing value. This modification directly alters the semantic definition of the class expression, affecting how it evaluates individuals in the ontology.

        :param value: The OWL object property expression to assign.
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the object restriction, formatted as "ObjectHasSelf" followed by the associated object property expression in parentheses. This method relies on the string representation of the underlying object property expression and is typically used for debugging or display purposes.

        :return: A string representation of the object, displaying the class name and the value of `object_property_expression`.

        :rtype: str
        """

        return f"ObjectHasSelf({self.object_property_expression})"
