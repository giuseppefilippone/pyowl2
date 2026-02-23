import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLInverseFunctionalObjectProperty(OWLObjectPropertyAxiom):
    """
    This class represents an axiom within the Web Ontology Language (OWL) that declares a specific object property to be inverse-functional. Semantically, this imposes a uniqueness constraint such that if two individuals are found to be related to the same target individual through this property, a reasoner must infer that the two individuals are actually identical. This is commonly used to model unique identifiers, such as social security numbers or email addresses, where a specific value should map back to a single entity. To utilize this class, instantiate it with the target `OWLObjectPropertyExpression` and, optionally, a list of annotations to provide additional metadata about the axiom.

    :parm object_property_expression: The specific property that is declared to be inverse functional, ensuring that if two individuals are related to the same individual via this property, they must be the same individual.
    :type object_property_expression: OWLObjectPropertyExpression
    """

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an instance representing an OWL axiom that declares a specific object property to be inverse-functional. This constructor requires the property expression to be axiomatized and accepts an optional list of annotations for attaching metadata to the axiom. It invokes the superclass constructor to handle the annotation storage and assigns the provided property expression to an internal attribute for subsequent retrieval.

        :param expression: The object property expression involved in the axiom.
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
        Assigns the specified object property expression to this inverse functional object property axiom, replacing any previously held value. The input value represents the specific property that is being asserted to have inverse functionality within the ontology. This method mutates the instance's state by updating the internal reference to the provided expression.

        :param value:
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the inverse functional object property axiom, formatted in a style resembling OWL functional syntax. The method constructs the string by combining the axiom type identifier with the associated annotations and the object property expression. If annotations are present, they are included in the output; otherwise, an empty list is explicitly rendered to ensure the structure remains consistent.

        :return: A string representation of the inverse functional object property axiom in functional syntax, including the annotations and the object property expression.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"InverseFunctionalObjectProperty({self.axiom_annotations} {self.object_property_expression})"
        else:
            return (
                f"InverseFunctionalObjectProperty([] {self.object_property_expression})"
            )
