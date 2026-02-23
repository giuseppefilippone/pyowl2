import typing

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLObjectPropertyDomain(OWLObjectPropertyAxiom):
    """
    This class models an axiom within the Web Ontology Language (OWL) that constrains the types of individuals which may serve as the subject of a specific object property relationship. By associating an object property expression with a class expression, it asserts that any individual linked to another via the specified property must belong to the defined class. Users can instantiate this class by providing the target property, the defining class expression, and an optional list of annotations to attach metadata to the axiom.

    :parm object_property_expression: The object property expression for which the domain is being defined.
    :type object_property_expression: OWLObjectPropertyExpression
    :parm class_expression: The class expression defining the domain of the object property, specifying the class of individuals that can be the subject of the property relationship.
    :type class_expression: OWLClassExpression
    """

    def __init__(
        self,
        property: OWLObjectPropertyExpression,
        expression: OWLClassExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an axiom that defines the domain of an object property within an ontology. This constructor accepts an object property expression, a class expression representing the domain, and an optional list of annotations. It stores the property and the class expression as internal attributes, establishing the constraint that any individual acting as the subject of this property must be an instance of the specified class. Annotations are delegated to the parent class for storage and management.

        :param property: The object property expression involved in the axiom.
        :type property: OWLObjectPropertyExpression
        :param expression: The OWL class expression acting as the filler for the object property restriction.
        :type expression: OWLClassExpression
        :param annotations: A list of annotations to be attached to this axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = (
        #     sorted(annotations) if annotations else annotations
        # )
        self._object_property_expression: OWLObjectPropertyExpression = property
        self._class_expression: OWLClassExpression = expression

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Assigns the specified object property expression to this domain axiom, replacing any previously stored value. This method updates the internal state of the instance by setting the `_object_property_expression` attribute to the provided `OWLObjectPropertyExpression` instance. The operation directly mutates the object and does not return a value.

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
        Updates the domain class expression associated with this OWL object property domain axiom. It assigns the provided `OWLClassExpression` instance to the internal state, defining the specific class to which the property applies. This operation modifies the object's internal state by overwriting the existing class expression with the new value.

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
        Returns a string representation of the object property domain axiom in a functional syntax format. The output string begins with "ObjectPropertyDomain" followed by the axiom annotations, the object property expression, and the class expression, all enclosed in parentheses. If the object has associated annotations, they are included in the string; otherwise, an empty list representation is substituted in their place. This method does not modify the state of the object.

        :return: A string representation of the axiom in functional syntax, including annotations if available.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"ObjectPropertyDomain({self.axiom_annotations} {self.object_property_expression} {self.class_expression})"
        else:
            return f"ObjectPropertyDomain([] {self.object_property_expression} {self.class_expression})"
