import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLTransitiveObjectProperty(OWLObjectPropertyAxiom):
    """
    This class represents an axiom in the Web Ontology Language (OWL) that declares a specific object property to be transitive. By defining a property as transitive, the ontology enables logical inference where if the property relates individual A to individual B and individual B to individual C, it must also relate individual A to individual C. To use this class, instantiate it with the target `OWLObjectPropertyExpression` that requires this characteristic, optionally providing a list of annotations to attach metadata or context to the axiom.

    :param object_property_expression: The object property expression that is declared to be transitive.
    :type object_property_expression: OWLObjectPropertyExpression
    """

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an instance representing an OWL axiom that declares a specific object property to be transitive. The constructor requires an `OWLObjectPropertyExpression` defining the property to which the transitivity characteristic applies, along with an optional list of `OWLAnnotation` objects for attaching metadata to the axiom. It invokes the superclass constructor to handle the annotations and stores the provided property expression as a private attribute for subsequent access.

        :param expression: The object property expression (named or inverse) that constitutes the core property of this axiom.
        :type expression: OWLObjectPropertyExpression
        :param annotations: A list of annotations to be attached to this axiom. If None, no annotations are added.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = (
        #     sorted(annotations) if annotations else annotations
        # )
        self._object_property_expression: OWLObjectPropertyExpression = expression

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = sorted(value) if value else value

    @property
    def object_property_expression(self) -> OWLObjectPropertyExpression:
        """
        Assigns the object property expression to which the transitivity rule applies. This method accepts an instance of OWLObjectPropertyExpression and updates the internal state of the axiom, overwriting any previously defined property. It effectively defines the specific property that is being asserted as transitive within the ontology structure.

        :param value: The OWL object property expression to assign to the instance.
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the axiom, formatted in a style resembling OWL functional syntax. The output string encapsulates the annotations and the object property expression within a "TransitiveObjectProperty" declaration. If the instance contains annotations, they are included in the string; otherwise, an empty list is substituted to maintain a consistent format.

        :return: A string representation of the transitive object property axiom, including its annotations and the object property expression.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"TransitiveObjectProperty({self.axiom_annotations} {self.object_property_expression})"
        else:
            return f"TransitiveObjectProperty([] {self.object_property_expression})"
