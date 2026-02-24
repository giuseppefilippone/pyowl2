import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLSymmetricObjectProperty(OWLObjectPropertyAxiom):
    """
    This class models an axiom in the Web Ontology Language (OWL) that asserts the symmetric nature of an object property. Semantically, it enforces the rule that if a specific property connects entity A to entity B, it must also connect entity B to entity A, which is characteristic of relationships like 'isSiblingOf' or 'isSpouseOf'. Users can instantiate this object by providing the target object property expression, and optionally include a list of annotations to attach supplementary metadata or context to the axiom.

    :param object_property_expression: The object property expression that is asserted to be symmetric by this axiom.
    :type object_property_expression: OWLObjectPropertyExpression
    """

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an axiom asserting that a specific object property is symmetric within an OWL ontology. The constructor accepts the object property expression to be characterized as symmetric and an optional list of annotations to associate with the axiom. It stores the property expression internally and delegates the initialization of annotations to the parent class.

        :param expression: The object property expression (which may be a named property or an inverse property) that is the subject of this axiom.
        :type expression: OWLObjectPropertyExpression
        :param annotations: Optional list of OWL annotations to be associated with the object.
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
        Assigns the specified object property expression to this symmetric object property instance, updating the internal state to reflect the new property that is being defined as symmetric. The provided value must be an instance of `OWLObjectPropertyExpression`, and this operation will overwrite any previously stored expression.

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
        Returns a string representation of the symmetric object property axiom formatted in a functional syntax style. The output string begins with the axiom type followed by the list of annotations; if no annotations are present, an empty list is explicitly displayed. The representation concludes with the object property expression to which the symmetry property applies.

        :return: A string representation of the axiom, formatted as 'SymmetricObjectProperty([annotations] object_property_expression)'.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"SymmetricObjectProperty({self.axiom_annotations} {self.object_property_expression})"
        else:
            return f"SymmetricObjectProperty([] {self.object_property_expression})"
