import typing

from pyowl2.abstracts.class_axiom import OWLClassAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.base.annotation import OWLAnnotation


class OWLSubClassOf(OWLClassAxiom):
    """
    Represents a fundamental axiom in the Web Ontology Language that defines a hierarchical relationship between two class expressions, asserting that all instances of the subclass are necessarily instances of the superclass. This construct allows for the creation of taxonomies and logical constraints by linking either simple named classes or complex, anonymous class expressions. To use this entity, instantiate it with the specific subclass and superclass expressions, optionally providing a list of annotations to attach metadata such as provenance or confidence levels to the logical statement.

    :parm sub_class_expression: The class expression that is declared to be a subclass of the superclass expression.
    :type sub_class_expression: OWLClassExpression
    :parm super_class_expression: The superclass expression in the axiom, representing the more general concept that the subclass is a subset of.
    :type super_class_expression: OWLClassExpression
    """

    def __init__(
        self,
        sub_class: OWLClassExpression,
        super_class: OWLClassExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes an OWL SubClassOf axiom, representing the semantic assertion that every instance of the specified subclass expression is also an instance of the superclass expression. This constructor requires the subclass and superclass expressions as arguments, storing them internally to define the hierarchical relationship. It also accepts an optional list of annotations, which are passed to the parent class to attach metadata to the axiom.

        :param sub_class: The class expression representing the subclass (the more specific concept) in the relationship.
        :type sub_class: OWLClassExpression
        :param super_class: The class expression representing the superclass in the subclass relationship.
        :type super_class: OWLClassExpression
        :param annotations: Optional list of annotations to be attached to the axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._sub_class_expression: OWLClassExpression = sub_class
        self._super_class_expression: OWLClassExpression = super_class

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def sub_class_expression(self) -> OWLClassExpression:
        """
        Updates the subclass expression component of the OWL SubClassOf axiom by assigning the provided `OWLClassExpression` to the internal attribute. This method modifies the object's state in place, overwriting any previously stored subclass expression with the new value.

        :param value: The OWL class expression to be set as the subclass.
        :type value: OWLClassExpression
        """

        return self._sub_class_expression

    @sub_class_expression.setter
    def sub_class_expression(self, value: OWLClassExpression) -> None:
        """Setter for sub_class_expression."""
        self._sub_class_expression = value

    @property
    def super_class_expression(self) -> OWLClassExpression:
        """
        Sets the superclass expression for this `OWLSubClassOf` axiom to the provided value. This method updates the internal state of the object, replacing the existing superclass definition with the new `OWLClassExpression`. As a property setter, it directly modifies the axiom's structure to reflect that the subclass is a sub-class of the specified expression.

        :param value: The expression representing the superclass to be set.
        :type value: OWLClassExpression
        """

        return self._super_class_expression

    @super_class_expression.setter
    def super_class_expression(self, value: OWLClassExpression) -> None:
        """Setter for super_class_expression."""
        self._super_class_expression = value

    def __str__(self) -> str:
        """
        Returns a string representation of the SubClassOf axiom, formatted according to a functional syntax style. The output string includes the axiom annotations, the sub-class expression, and the super-class expression. If the axiom contains annotations, they are included in the string; otherwise, an empty list is explicitly rendered to ensure the structure remains consistent. This method has no side effects and is primarily used for debugging or logging purposes.

        :return: A string representation of the SubClassOf axiom, formatted as 'SubClassOf([annotations] sub_class_expression super_class_expression)'.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"SubClassOf({self.axiom_annotations} {self.sub_class_expression} {self.super_class_expression})"
        else:
            return f"SubClassOf([] {self.sub_class_expression} {self.super_class_expression})"
