from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectAllValuesFrom(OWLClassExpression):
    """
    This class represents a universal restriction in the Web Ontology Language (OWL), defining a condition where every individual related via a specific object property must be an instance of a designated class expression. It is initialized with an object property expression, which establishes the relationship, and a class expression, which acts as the constraint that all related individuals must satisfy. Semantically, an individual belongs to this restriction if and only if all values reachable through the specified property are members of the provided class expression, enabling the precise definition of complex class hierarchies and domain constraints.

    :parm object_property_expression: The object property expression defining the relationship between the subject individual and the objects that must satisfy the class expression.
    :type object_property_expression: OWLObjectPropertyExpression
    :parm class_expression: Defines the class that all values of the object property must be instances of.
    :type class_expression: OWLClassExpression
    """

    def __init__(
        self, property: OWLObjectPropertyExpression, expression: OWLClassExpression
    ) -> None:
        """
        Initializes a new instance representing an OWL universal restriction, which asserts that for a given individual, all values of the specified object property must belong to a particular class. The constructor accepts an object property expression defining the relationship and a class expression defining the constraint or filler class. These arguments are stored internally as attributes to define the logical structure of the restriction.

        :param property: The object property expression used in this restriction.
        :type property: OWLObjectPropertyExpression
        :param expression: The OWL class expression that serves as the filler or range for the object property.
        :type expression: OWLClassExpression
        """

        super().__init__()
        self._object_property_expression: OWLObjectPropertyExpression = property
        self._class_expression: OWLClassExpression = expression

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Updates the object property expression used in this universal restriction by assigning the provided value. The input must be an instance of `OWLObjectPropertyExpression`, which defines the property over which the 'all values from' condition is applied. This operation modifies the internal state of the `OWLObjectAllValuesFrom` object, replacing any previously stored property expression.

        :param value: The OWL object property expression to assign to the instance.
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    @property
    def class_expression(self) -> OWLClassExpression:
        """
        Assigns the specified OWL class expression to this restriction, replacing any existing value. This method accepts an instance of `OWLClassExpression` and updates the internal state by setting the `_class_expression` attribute. As a side effect, it mutates the object, altering the semantic definition of the "all values from" restriction to reflect the new class expression.

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
        Returns a human-readable string representation of the OWL object all values from restriction, formatted to display the class name followed by the object property expression and the class expression enclosed in parentheses. This method is primarily used for debugging and logging, providing a concise textual summary of the restriction's components without modifying the object's state.

        :return: A human-readable string representation of the object, formatted as 'ObjectAllValuesFrom(object_property_expression class_expression)'.

        :rtype: str
        """

        return f"ObjectAllValuesFrom({self.object_property_expression} {self.class_expression})"
