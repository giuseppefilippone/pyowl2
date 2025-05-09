import typing

from rdflib import URIRef

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.abstracts.object import OWLObject
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.axioms.assertion.class_assertion import OWLClassAssertion
from pyowl2.axioms.assertion.data_property_assertion import OWLDataPropertyAssertion
from pyowl2.axioms.assertion.different_individuals import OWLDifferentIndividuals
from pyowl2.axioms.assertion.negative_data_property_assertion import (
    OWLNegativeDataPropertyAssertion,
)
from pyowl2.axioms.assertion.negative_object_property_assertion import (
    OWLNegativeObjectPropertyAssertion,
)
from pyowl2.axioms.assertion.object_property_assertion import OWLObjectPropertyAssertion
from pyowl2.axioms.assertion.same_individual import OWLSameIndividual
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.iri import IRI
from pyowl2.class_expression.object_one_of import OWLObjectOneOf
from pyowl2.individual.anonymous_individual import OWLAnonymousIndividual
from pyowl2.individual.named_individual import OWLNamedIndividual
from pyowl2.literal.literal import OWLLiteral


class OWLFullIndividual(OWLObject):

    def __init__(
        self, iri: typing.Union[IRI, URIRef], is_anonymous: bool = False
    ) -> None:
        self._individual = (
            OWLNamedIndividual(iri) if not is_anonymous else OWLAnonymousIndividual(iri)
        )
        self._axioms: list[typing.Any] = []
        self._annotations: typing.Optional[list[OWLAnnotation]] = None

    @property
    def axioms(self) -> list[typing.Any]:
        return self._axioms

    @property
    def annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        return self._annotations

    @annotations.setter
    def annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
        self._annotations = value

    @property
    def individual(self) -> OWLIndividual:
        return self._individual

    @property
    def assertions(self) -> list[OWLClassAssertion]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLClassAssertion)]

    @property
    def same_individuals(self) -> list[OWLSameIndividual]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLSameIndividual)]

    @property
    def different_individuals(self) -> list[OWLDifferentIndividuals]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLDifferentIndividuals)
        ]

    @property
    def class_assertions(self) -> list[OWLClassAssertion]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLClassAssertion)]

    @property
    def one_of(self) -> list[OWLObjectOneOf]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLObjectOneOf)]

    def is_different_from(
        self,
        individuals: typing.Union[
            OWLIndividual, list[OWLIndividual], typing.Self, list[typing.Self]
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        new_individuals: list[OWLIndividual] = [self.individual]
        if isinstance(individuals, list):
            if all(isinstance(i, OWLIndividual) for i in individuals):
                new_individuals.extend(individuals)
            elif all(isinstance(i, OWLFullIndividual) for i in individuals):
                new_individuals.extend([i.individual for i in individuals])
            else:
                return TypeError
        else:
            if isinstance(individuals, OWLIndividual):
                new_individuals.append(individuals)
            elif isinstance(individuals, OWLFullIndividual):
                new_individuals.append(individuals.individual)
            else:
                return TypeError

        different_from = OWLDifferentIndividuals(
            new_individuals,
            annotations,
        )
        if different_from in self.axioms:
            return
        self.axioms.append(different_from)

    def is_same_as(
        self,
        individuals: typing.Union[
            OWLIndividual, list[OWLIndividual], typing.Self, list[typing.Self]
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ):
        new_individuals: list[OWLIndividual] = [self.individual]
        if isinstance(individuals, list):
            if all(isinstance(i, OWLIndividual) for i in individuals):
                new_individuals.extend(individuals)
            elif all(isinstance(i, OWLFullIndividual) for i in individuals):
                new_individuals.extend([i.individual for i in individuals])
            else:
                return TypeError
        else:
            if isinstance(individuals, OWLIndividual):
                new_individuals.append(individuals)
            elif isinstance(individuals, OWLFullIndividual):
                new_individuals.append(individuals.individual)
            else:
                return TypeError

        same_as = OWLSameIndividual(
            new_individuals,
            annotations,
        )
        if same_as in self.axioms:
            return
        self.axioms.append(same_as)

    def add_assertion(
        self,
        cls: OWLClassExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        assertion = OWLClassAssertion(cls, self.individual, annotations)
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def add_object_property_assertion(
        self,
        object_property: OWLObjectPropertyExpression,
        target_individual: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        assertion = OWLObjectPropertyAssertion(
            object_property, self.individual, target_individual, annotations
        )
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def add_negative_object_property_assertion(
        self,
        object_property: OWLObjectPropertyExpression,
        target_individual: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        assertion = OWLNegativeObjectPropertyAssertion(
            object_property, self.individual, target_individual, annotations
        )
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def add_data_property_assertion(
        self,
        data_property: OWLDataPropertyExpression,
        value: OWLLiteral,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        assertion = OWLDataPropertyAssertion(
            data_property, self.individual, value, annotations
        )
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def add_negative_data_property_assertion(
        self,
        data_property: OWLDataPropertyExpression,
        value: OWLLiteral,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        assertion = OWLNegativeDataPropertyAssertion(
            data_property, self.individual, value, annotations
        )
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def is_one_of(self, individuals: list[OWLIndividual]) -> None:
        one_of = OWLObjectOneOf([self.individual] + individuals)
        if one_of in self.axioms:
            return
        self.axioms.append(one_of)
