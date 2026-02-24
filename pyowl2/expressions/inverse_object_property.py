from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.expressions.object_property import OWLObjectProperty


class OWLInverseObjectProperty(OWLObjectPropertyExpression):
    """
    This class represents an expression that defines the inverse of a specific object property, effectively reversing the direction of the relationship between two individuals. It is constructed by wrapping an existing `OWLObjectProperty`, allowing the ontology to infer that if the original property relates individual A to individual B, this expression relates B to A. This mechanism is essential for modeling reciprocal relationships—such as deriving "isParentOf" from "hasChild"—thereby enhancing the expressiveness and reasoning capabilities of the ontology without requiring explicit assertions for both directions.

    :param object_property: The object property that is being inverted to represent the relationship in the opposite direction.
    :type object_property: OWLObjectProperty
    """

    def __init__(self, property: OWLObjectProperty) -> None:
        """
        Initializes a new instance representing the inverse of a specific OWL object property. The constructor accepts a single argument, an `OWLObjectProperty`, which is stored internally within the `_object_property` attribute to define the relationship. It also invokes the initialization logic of the parent class to ensure proper setup of the object hierarchy.

        :param property: The object property associated with this instance.
        :type property: OWLObjectProperty
        """

        super().__init__()
        self._object_property: OWLObjectProperty = property

    @property
    def object_property(self) -> OWLObjectProperty:
        """
        Updates the internal state of the `OWLInverseObjectProperty` instance by assigning a new object property. This setter accepts an instance of `OWLObjectProperty` and stores it in the private `_object_property` attribute, effectively defining or modifying the property involved in the inverse relationship. The method modifies the instance in place and returns `None`.

        :param value: The OWL object property to set.
        :type value: OWLObjectProperty
        """

        return self._object_property

    @object_property.setter
    def object_property(self, value: OWLObjectProperty) -> None:
        """Setter for object_property."""
        self._object_property = value

    def is_top_object_property(self) -> bool:
        """
        Determines whether the underlying object property is the bottom object property. This method compares the internal object property reference against the standard bottom property defined in the OWL ontology. It returns True if the properties are identical, indicating that this inverse property represents the bottom property.

        :return: True if the object property is the bottom object property, False otherwise.

        :rtype: bool
        """

        return self.object_property == OWLObjectProperty.bottom()

    def is_bottom_object_property(self) -> bool:
        """
        Checks if the underlying object property is the top object property. The method returns True if the `object_property` attribute of the current instance is equal to the universal top object property, and False otherwise. This operation does not modify the state of the object or have any side effects.

        :return: True if the object property is the top object property, False otherwise.

        :rtype: bool
        """

        return self.object_property == OWLObjectProperty.top()

    def __str__(self) -> str:
        """
        Returns a string representation of the inverse object property formatted according to functional syntax conventions. The output explicitly wraps the underlying object property within the "ObjectInverseOf" constructor, providing a human-readable depiction of the logical structure. This method does not alter the state of the object and relies on the string conversion of the internal object property attribute.

        :return: A string representation of the object, formatted as 'ObjectInverseOf({object_property})'.

        :rtype: str
        """

        return f"ObjectInverseOf({self.object_property})"
