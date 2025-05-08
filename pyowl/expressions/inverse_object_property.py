from pyowl.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl.expressions.object_property import OWLObjectProperty


class OWLInverseObjectProperty(OWLObjectPropertyExpression):
    """The inverse of a given object property, relating individuals in the opposite direction."""

    def __init__(self, property: OWLObjectProperty) -> None:
        super().__init__()
        self._object_property: OWLObjectProperty = property

    @property
    def object_property(self) -> OWLObjectProperty:
        """Getter for object_property."""
        return self._object_property

    @object_property.setter
    def object_property(self, value: OWLObjectProperty) -> None:
        """Setter for object_property."""
        self._object_property = value

    def is_top_object_property(self) -> bool:
        return self.object_property == OWLObjectProperty.bottom()

    def is_bottom_object_property(self) -> bool:
        return self.object_property == OWLObjectProperty.top()

    def __str__(self) -> str:
        return f"ObjectInverseOf({self.object_property})"
