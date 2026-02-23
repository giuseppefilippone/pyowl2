from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectHasValue(OWLClassExpression):
    """
    This class represents an OWL object property restriction that defines a class of individuals which must be related to a specific, named individual via a particular object property. It is used to express exact value constraints, such as defining the class of "people who have a specific child" or "cities located at a specific coordinate." To use this class, instantiate it with an `OWLObjectPropertyExpression` that defines the relationship and an `OWLIndividual` that serves as the required target value. This restriction can then be employed as a class expression within axioms to construct complex logical definitions or to assert necessary conditions for class membership in an ontology.

    :parm object_property_expression: The object property expression defining the relationship between the subject individual and the specific individual value in the restriction.
    :type object_property_expression: OWLObjectPropertyExpression
    :parm individual: The specific individual instance that the subject must be related to via the object property expression to satisfy the restriction.
    :type individual: OWLIndividual
    """

    def __init__(
        self, property: OWLObjectPropertyExpression, individual: OWLIndividual
    ) -> None:
        """
        Initializes a new instance representing an OWL class expression that restricts the range of an object property to a specific individual. This constructor accepts an object property expression defining the relationship and an OWL individual serving as the filler value. It stores these components within the instance's private attributes and ensures the parent class is properly initialized. No validation logic is explicitly performed within this method, relying instead on the provided arguments conforming to the expected types.

        :param property: The object property expression representing the relationship.
        :type property: OWLObjectPropertyExpression
        :param individual: The individual that serves as the object (filler) of the object property expression.
        :type individual: OWLIndividual
        """

        super().__init__()
        self._object_property_expression: OWLObjectPropertyExpression = property
        self._individual: OWLIndividual = individual

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Sets the object property expression for this `OWLObjectHasValue` restriction, defining the specific property that is being constrained. This method updates the internal state by assigning the provided `OWLObjectPropertyExpression` to the instance, overwriting any previously set value. It effectively changes the predicate of the class expression to the new property supplied.

        :param value: The OWL object property expression to assign.
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    @property
    def individual(self) -> OWLIndividual:
        """
        Updates the specific individual filler for this object-has-value restriction by assigning the provided `OWLIndividual` instance to the internal state. This operation directly mutates the object, replacing any previously associated individual with the new value. It does not return a result, ensuring the restriction now references the specified individual.

        :param value: The individual to assign to the object.
        :type value: OWLIndividual
        """

        return self._individual

    @individual.setter
    def individual(self, value: OWLIndividual) -> None:
        """Setter for individual."""
        self._individual = value

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the object property value restriction, formatted to display the class name followed by the specific property and individual involved. The output follows the pattern "ObjectHasValue({property} {individual})", where the property and individual are converted to their respective string representations. This method is primarily used for debugging or logging purposes, providing a concise summary of the restriction's components without altering the object's state.

        :return: A human-readable string representation of the object, formatted as 'ObjectHasValue({object_property_expression} {individual})'.

        :rtype: str
        """

        return f"ObjectHasValue({self.object_property_expression} {self.individual})"
