from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectSomeValuesFrom(OWLClassExpression):
    """
    This class models an existential restriction within the Web Ontology Language (OWL), defining a set of individuals that must be connected to at least one member of a specific class through a particular object property. It serves as a complex class expression that constrains the existence of relationships, enabling the definition of classes based on the properties of their neighbors rather than their intrinsic attributes. To utilize this restriction, one must provide an object property expression, which defines the nature of the relationship, and a class expression, which specifies the type of the related individual. This construct is fundamental for creating nuanced ontological definitions, such as describing a "Parent" as an entity that has at least one child who is a "Person".

    :param object_property_expression: The object property expression defining the relationship between the subject individual and the class expression, which may be a simple property or a complex expression involving inverses.
    :type object_property_expression: OWLObjectPropertyExpression
    :param class_expression: The class expression defining the type of individuals that the subject individual must be related to via the object property expression.
    :type class_expression: OWLClassExpression
    """

    def __init__(
        self, property: OWLObjectPropertyExpression, expression: OWLClassExpression
    ) -> None:
        """
        Initializes a new instance representing an OWL ObjectSomeValuesFrom class expression, which semantically defines the set of individuals that have at least one relationship via the specified object property to an individual that belongs to the given class expression. The method stores the provided object property expression and class expression as internal attributes. It also invokes the superclass initializer to ensure proper object hierarchy initialization.

        :param property: The object property expression used in the restriction.
        :type property: OWLObjectPropertyExpression
        :param expression: The OWL class expression that serves as the filler for the restriction.
        :type expression: OWLClassExpression
        """

        super().__init__()
        self._object_property_expression: OWLObjectPropertyExpression = property
        self._class_expression: OWLClassExpression = expression

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Assigns the specified object property expression to this existential restriction instance. This method serves as the setter for the `object_property_expression` attribute, updating the internal state to reflect the new property relationship defined by the provided `OWLObjectPropertyExpression`. It directly modifies the underlying private attribute, potentially altering the semantic meaning of the class expression within the ontology structure.

        :param value: The object property expression to assign.
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
        Assigns a new class expression to this `OWLObjectSomeValuesFrom` restriction, replacing the existing filler. The provided value, which must be an instance of `OWLClassExpression`, is stored internally and defines the range of the existential restriction. This operation modifies the object's state in place and does not return a value.

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
        Returns a string representation of the OWL existential restriction defined by this object. The representation follows the format "ObjectSomeValuesFrom({property} {class})", where {property} corresponds to the object property expression and {class} corresponds to the class expression associated with the restriction. This method does not modify the object's state and relies on the string representations of the internal property and class expressions to construct the output.

        :return: A string representation of the object, formatted as 'ObjectSomeValuesFrom(property_expression class_expression)'.

        :rtype: str
        """

        return f"ObjectSomeValuesFrom({self.object_property_expression} {self.class_expression})"
