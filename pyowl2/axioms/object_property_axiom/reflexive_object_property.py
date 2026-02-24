import typing

from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLReflexiveObjectProperty(OWLObjectPropertyAxiom):
    """
    This class represents an axiom in the Web Ontology Language (OWL) that declares a specific object property to be reflexive, meaning that every individual in the ontology is necessarily related to itself through that property. It is typically used to model relationships where self-reference is a universal truth, such as a 'hasIdentity' property. To utilize this class, instantiate it with the target `OWLObjectPropertyExpression` and, optionally, a list of `OWLAnnotation` objects to provide metadata about the axiom. Once asserted, this axiom enables logical reasoners to infer that for any individual $x$, the statement $P(x, x)$ holds true.

    :param object_property_expression: The object property expression that is asserted to be reflexive, meaning it relates every individual to itself.
    :type object_property_expression: OWLObjectPropertyExpression
    """

    def __init__(
        self,
        expression: OWLObjectPropertyExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an instance representing an OWL axiom that asserts a specific object property expression is reflexive. The constructor accepts the required object property expression and an optional list of annotations, which are passed to the superclass for handling. It stores the property expression internally as an instance attribute, thereby defining the subject of the axiom.

        :param expression: The object property expression (which may be a named property or an inverse property) to be encapsulated by this instance.
        :type expression: OWLObjectPropertyExpression
        :param annotations: A list of annotations to be attached to this axiom.
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
        Assigns the specified object property expression to this axiom, defining the property that is asserted to be reflexive. This method updates the internal state by replacing the existing property expression with the provided `OWLObjectPropertyExpression` instance. It serves as the setter for the corresponding property, allowing the subject of the reflexive axiom to be modified after initialization.

        :param value: The object property expression to assign.
        :type value: OWLObjectPropertyExpression
        """

        return self._object_property_expression

    @object_property_expression.setter
    def object_property_expression(self, value: OWLObjectPropertyExpression) -> None:
        """Setter for object_property_expression."""
        self._object_property_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the reflexive object property axiom, formatted to display the axiom type, its annotations, and the associated object property expression. The output string follows the pattern 'ReflexiveObjectProperty([annotations] property_expression)', where the annotations list is populated if annotations exist or displayed as an empty list otherwise. This method does not modify the object's state and is primarily used for generating human-readable output for debugging or display.

        :return: A string representation of the reflexive object property axiom, including its annotations and object property expression.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"ReflexiveObjectProperty({self.axiom_annotations} {self.object_property_expression})"
        else:
            return f"ReflexiveObjectProperty([] {self.object_property_expression})"
