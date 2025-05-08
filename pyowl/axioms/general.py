import typing

from pyowl.abstracts.axiom import OWLAxiom
from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.base.annotation import OWLAnnotation
from pyowl.base.iri import IRI


class OWLGeneralClassAxiom(OWLAxiom):

    def __init__(
        self,
        left_expression: OWLClassExpression,
        property: IRI,
        right_expression: OWLClassExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        self._left_expression: OWLClassExpression = left_expression
        self._property_iri: IRI = property
        self._right_expression: OWLClassExpression = right_expression
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = sorted(annotations) if annotations else annotations

    @property
    def left_expression(self) -> OWLClassExpression:
        return self._left_expression

    @left_expression.setter
    def left_expression(self, value: OWLClassExpression) -> None:
        self._left_expression = value

    @property
    def property_iri(self) -> IRI:
        return self._property_iri

    @property_iri.setter
    def property_iri(self, value: IRI) -> None:
        self._property_iri = value

    @property
    def right_expression(self) -> OWLClassExpression:
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
        if self.axiom_annotations:
            return (
                f"GeneralClassAxiom([] {self.left_expression} {self.property_iri} {self.right_expression})"
            )
        else:
            return f"GeneralClassAxiom({self.axiom_annotations} {self.left_expression} {self.property_iri} {self.right_expression})"
