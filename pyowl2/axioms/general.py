import typing

from pyowl2.abstracts.axiom import OWLAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.iri import IRI


class OWLGeneralClassAxiom(OWLAxiom):
    """
    This class models a logical assertion within an ontology that defines a relationship between two class expressions via a specific property. It enables the representation of complex constraints and associations by linking a subject class expression to an object class expression through an intermediate property identified by an IRI. To use this component, instantiate it with the left and right class expressions along with the property IRI, optionally providing a list of annotations to attach metadata to the axiom. The structure is fully mutable, allowing users to update the class expressions, the property IRI, or the annotations after creation to reflect changes in the underlying ontology model.

    :parm left_expression: The class expression on the left side of the axiom, representing the subject of the relationship asserted by the property.
    :type left_expression: OWLClassExpression
    :parm property_iri: The IRI representing the property that connects the left and right class expressions, defining the specific relationship asserted by the axiom.
    :type property_iri: IRI
    :parm right_expression: The class expression on the right side of the axiom, acting as the target of the relationship asserted by the property IRI.
    :type right_expression: OWLClassExpression
    """

    def __init__(
        self,
        left_expression: OWLClassExpression,
        property: IRI,
        right_expression: OWLClassExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes the axiom with the specified left and right class expressions and the intervening property IRI. This method stores the provided expressions and property as internal attributes to define the logical structure of the axiom. It also accepts an optional list of annotations, delegating their storage to the superclass constructor to support metadata attachment.

        :param left_expression:
        :type left_expression: OWLClassExpression
        :param property: The IRI of the property connecting the left and right class expressions.
        :type property: IRI
        :param right_expression: The class expression on the right side of the relationship.
        :type right_expression: OWLClassExpression
        :param annotations: Optional list of annotations to be associated with this axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        self._left_expression: OWLClassExpression = left_expression
        self._property_iri: IRI = property
        self._right_expression: OWLClassExpression = right_expression
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = sorted(annotations) if annotations else annotations

    @property
    def left_expression(self) -> OWLClassExpression:
        """
        Sets the left-hand side class expression for the axiom, replacing the current value. This method updates the internal state of the object by assigning the provided OWLClassExpression to the underlying private attribute. It serves as the setter for the left_expression property, enabling modification of the axiom's structure after instantiation.

        :param value: The class expression to assign as the left operand.
        :type value: OWLClassExpression
        """

        return self._left_expression

    @left_expression.setter
    def left_expression(self, value: OWLClassExpression) -> None:
        self._left_expression = value

    @property
    def property_iri(self) -> IRI:
        """
        Sets the Internationalized Resource Identifier (IRI) for the property associated with this OWL general class axiom. This method updates the internal state of the instance by assigning the provided IRI object to the underlying private attribute. It directly replaces the existing property reference without performing additional validation, meaning the caller is responsible for ensuring the input is a valid IRI object.

        :param value: The IRI to assign to the property.
        :type value: IRI
        """

        return self._property_iri

    @property_iri.setter
    def property_iri(self, value: IRI) -> None:
        self._property_iri = value

    @property
    def right_expression(self) -> OWLClassExpression:
        """
        Sets the right-hand side class expression for the general class axiom. This method updates the internal state of the object by assigning the provided OWLClassExpression to the corresponding private attribute. It is typically used to define or modify the operand on the right side of logical relationships represented by the axiom.

        :param value: The OWL class expression to assign as the right operand.
        :type value: OWLClassExpression
        """

        return self._right_expression

    @right_expression.setter
    def right_expression(self, value: OWLClassExpression) -> None:
        self._right_expression = value

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     self._axiom_annotations = sorted(value) if value else value

    def __str__(self) -> str:
        """
        Returns a string representation of the axiom, formatted to display the left expression, property IRI, and right expression. The output string begins with 'GeneralClassAxiom' followed by the annotation component and the core components of the axiom. The formatting of the annotation component depends on the truthiness of the `axiom_annotations` attribute: if the attribute is truthy, the string representation uses an empty list `[]`, while if it is falsy, the actual value of the attribute is included in the string.

        :return: A string representation of the axiom, displaying the annotations, left expression, property IRI, and right expression.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"GeneralClassAxiom([] {self.left_expression} {self.property_iri} {self.right_expression})"
        else:
            return f"GeneralClassAxiom({self.axiom_annotations} {self.left_expression} {self.property_iri} {self.right_expression})"
