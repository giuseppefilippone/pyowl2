import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLIrreflexiveObjectProperty(OWLObjectPropertyAxiom):
    """
    This class models an axiom within the Web Ontology Language (OWL) that declares a specific object property to be irreflexive. By asserting this axiom, a user specifies that no individual in the ontology can be related to itself through the given property expression. It is typically used to define constraints for relationships where self-reference is logically impossible or undesirable, such as "hasParent" or "isPredecessorOf". The class accepts the target property expression and an optional list of annotations to provide metadata about the axiom itself.

    :parm object_property_expression: The property expression that is asserted to be irreflexive by this axiom.
    :type object_property_expression: OWLObjectPropertyExpression
    """

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an axiom asserting that a specific object property is irreflexive, meaning no individual can be related to itself via this property. The constructor requires an `OWLObjectPropertyExpression` representing the property to be constrained and optionally accepts a list of `OWLAnnotation` objects to attach metadata to the axiom. It delegates the storage of annotations to the parent class and retains the property expression as a private attribute for subsequent access.

        :param expression: The object property expression (which may be a named property or an inverse property) to be encapsulated.
        :type expression: OWLObjectPropertyExpression
        :param annotations: Optional list of annotations to be associated with the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._object_property_expression: OWLObjectPropertyExpression = expression

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
        Updates the object property expression associated with this irreflexive object property axiom. It assigns the provided `OWLObjectPropertyExpression` instance to the internal storage, overwriting any previously held value. This setter allows the specific property being defined as irreflexive to be modified after the axiom's initialization.

        :param value: The object property expression to assign to the entity.
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the irreflexive object property axiom in a functional syntax format. The method checks for the presence of axiom annotations, including them in the output if they exist, or substituting an empty list otherwise. The resulting string always contains the specific object property expression associated with the axiom.

        :return: A string representation of the axiom, formatted as `IrreflexiveObjectProperty([annotations] object_property_expression)`.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"IrreflexiveObjectProperty({self.axiom_annotations} {self.object_property_expression})"
        else:
            return f"IrreflexiveObjectProperty([] {self.object_property_expression})"
