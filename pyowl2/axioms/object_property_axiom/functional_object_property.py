import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLFunctionalObjectProperty(OWLObjectPropertyAxiom):
    """
    This axiom defines a constraint within an ontology stating that a specific object property is functional, meaning any given individual can be linked to at most one other individual via this property. Semantically, this allows reasoners to infer that if an individual is related to two distinct entities through this property, those entities must be identical (for example, if a person has two social security numbers, the numbers must refer to the same identifier). To utilize this, instantiate the class with the target `OWLObjectPropertyExpression` and an optional list of `OWLAnnotation` objects to provide metadata about the axiom itself.

    :parm object_property_expression: The object property expression that is declared to be functional, meaning it can relate an individual to at most one other individual.
    :type object_property_expression: OWLObjectPropertyExpression
    """

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Constructs an OWL axiom representing the declaration that a specific object property is functional, meaning it can have at most one distinct value for any given subject. The method accepts a required `OWLObjectPropertyExpression` defining the property in question and an optional list of `OWLAnnotation` objects for attaching metadata. Initialization involves passing the annotations to the superclass constructor and storing the property expression as an internal attribute.

        :param expression: The object property expression (which may be a named property or an inverse property) that this axiom is about.
        :type expression: OWLObjectPropertyExpression
        :param annotations: Optional list of annotations to be attached to the axiom.
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
        Assigns the provided object property expression to this instance, defining the specific property that is subject to the functional constraint. This method updates the internal state of the axiom by replacing the existing property expression with the new value. It expects an `OWLObjectPropertyExpression` as input, ensuring that the axiom refers to a valid object property within the ontology.

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
        Returns a string representation of the axiom, formatted in a functional syntax style. The output string begins with the keyword 'FunctionalObjectProperty' and includes the object property expression associated with the instance. If the instance contains axiom annotations, they are included in the string; otherwise, an empty list is displayed in their place.

        :return: A string representation of the axiom in functional syntax, including the annotations and the object property expression.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"FunctionalObjectProperty({self.axiom_annotations} {self.object_property_expression})"
        else:
            return f"FunctionalObjectProperty([] {self.object_property_expression})"
