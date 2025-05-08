import typing

from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl.abstracts.data_range import OWLDataRange
from pyowl.abstracts.individual import OWLIndividual
from pyowl.abstracts.object import OWLObject
from pyowl.axioms.assertion.data_property_assertion import OWLDataPropertyAssertion
from pyowl.axioms.assertion.negative_data_property_assertion import (
    OWLNegativeDataPropertyAssertion,
)
from pyowl.axioms.data_property_axiom.data_property_domain import OWLDataPropertyDomain
from pyowl.axioms.data_property_axiom.data_property_range import OWLDataPropertyRange
from pyowl.axioms.data_property_axiom.disjoint_data_properties import (
    OWLDisjointDataProperties,
)
from pyowl.axioms.data_property_axiom.equivalent_data_properties import (
    OWLEquivalentDataProperties,
)
from pyowl.axioms.data_property_axiom.functional_data_property import (
    OWLFunctionalDataProperty,
)
from pyowl.axioms.data_property_axiom.sub_data_property_of import OWLSubDataPropertyOf
from pyowl.base.annotation import OWLAnnotation
from pyowl.base.iri import IRI
from pyowl.class_expression.data_all_values_from import OWLDataAllValuesFrom
from pyowl.class_expression.data_exact_cardinality import OWLDataExactCardinality
from pyowl.class_expression.data_has_value import OWLDataHasValue
from pyowl.class_expression.data_max_cardinality import OWLDataMaxCardinality
from pyowl.class_expression.data_min_cardinality import OWLDataMinCardinality
from pyowl.class_expression.data_some_values_from import OWLDataSomeValuesFrom
from pyowl.expressions.data_property import OWLDataProperty
from pyowl.literal.literal import OWLLiteral


class OWLFullDataProperty(OWLObject):

    PROPERTY_CLASSES: list[type] = [
        OWLFunctionalDataProperty,
    ]

    def __init__(
        self,
        iri: IRI,
        domain: typing.Optional[OWLClassExpression] = None,
        range: typing.Optional[OWLDataRange] = None,
        is_functional: bool = False,
    ) -> None:
        self._data_property: OWLDataProperty = OWLDataProperty(iri)
        self._domain: OWLDataPropertyDomain = (
            OWLDataPropertyDomain(self._data_property, domain) if domain else None
        )
        self._range: OWLDataPropertyRange = (
            OWLDataPropertyRange(self._data_property, range) if range else None
        )
        self._axioms: list[typing.Any] = []
        self._annotations: typing.Optional[list[OWLAnnotation]] = None

        if is_functional:
            self._axioms.append(OWLFunctionalDataProperty(self._data_property))

    @property
    def data_property(self) -> OWLDataProperty:
        return self._data_property

    @data_property.setter
    def data_property(self, value: OWLDataProperty) -> None:
        self._data_property = value

    @property
    def domain(self) -> typing.Optional[OWLDataPropertyDomain]:
        return self._domain

    @domain.setter
    def domain(self, value: OWLClassExpression) -> None:
        self._domain = OWLDataPropertyDomain(self.data_property, value)

    @property
    def range(self) -> typing.Optional[OWLDataPropertyRange]:
        return self._range

    @range.setter
    def range(self, value: OWLDataRange) -> None:
        self._range = OWLDataPropertyRange(self.data_property, value)

    @property
    def annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        return self._annotations

    @annotations.setter
    def annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
        self._annotations = value

    @property
    def properties(self) -> list[OWLDataPropertyAxiom]:
        return [
            axiom
            for axiom in self.axioms
            if type(axiom) in OWLFullDataProperty.PROPERTY_CLASSES
        ]

    @property
    def assertions(self) -> list[OWLDataPropertyAssertion]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(
                axiom, (OWLDataPropertyAssertion, OWLNegativeDataPropertyAssertion)
            )
        ]

    @property
    def axioms(self) -> list[typing.Any]:
        return self._axioms

    @property
    def sub_properties(self) -> list[OWLSubDataPropertyOf]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLSubDataPropertyOf)
            and axiom.super_data_property_expression == self.data_property
        ]

    @property
    def super_properties(self) -> list[OWLSubDataPropertyOf]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLSubDataPropertyOf)
            and axiom.sub_data_property_expression == self.data_property
        ]

    @property
    def equivalent_properties(self) -> list[OWLEquivalentDataProperties]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLEquivalentDataProperties)
        ]

    @property
    def disjoint_properties(self) -> list[OWLDisjointDataProperties]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLDisjointDataProperties)
        ]

    @property
    def some_axioms(self) -> list[OWLDataSomeValuesFrom]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLDataSomeValuesFrom)
        ]

    @property
    def all_axioms(self) -> list[OWLDataAllValuesFrom]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLDataAllValuesFrom)
        ]

    @property
    def has_value_axioms(self) -> list[OWLDataHasValue]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLDataHasValue)]

    @property
    def min_axioms(self) -> list[OWLDataMinCardinality]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLDataMinCardinality)
        ]

    @property
    def max_axioms(self) -> list[OWLDataMaxCardinality]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLDataMaxCardinality)
        ]

    @property
    def exact_axioms(self) -> list[OWLDataExactCardinality]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLDataExactCardinality)
        ]

    @property
    def is_functional(self) -> bool:
        return any(isinstance(p, OWLFunctionalDataProperty) for p in self.properties)

    @is_functional.setter
    def is_functional(self, value: bool) -> None:
        curr_value: bool = self.is_functional
        if not curr_value and not value:
            return
        if curr_value and value:
            return
        if curr_value and not value:
            for i in range(len(self.axioms)):
                if not isinstance(i, OWLFunctionalDataProperty):
                    continue
                del self.axioms[i]
                return
            return
        element = OWLFunctionalDataProperty(self.data_property)
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_sub_property_of(
        self,
        super_property: typing.Union[OWLDataPropertyExpression, typing.Self],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        curr = OWLSubDataPropertyOf(
            self.data_property,
            (
                super_property
                if isinstance(super_property, OWLDataPropertyExpression)
                else super_property.data_property
            ),
            annotations,
        )
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def is_super_property_of(
        self,
        sub_property: typing.Union[OWLDataPropertyExpression, typing.Self],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        curr = OWLSubDataPropertyOf(
            (
                sub_property
                if isinstance(sub_property, OWLDataPropertyExpression)
                else sub_property.data_property
            ),
            self.data_property,
            annotations,
        )
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def is_equivalent_to(
        self,
        properties: typing.Union[
            OWLDataPropertyExpression,
            list[OWLDataPropertyExpression],
            typing.Self,
            list[typing.Self],
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        new_properties: list[OWLDataPropertyExpression] = [self.data_property]
        if isinstance(properties, list):
            if all(isinstance(p, OWLDataPropertyExpression) for p in properties):
                new_properties.extend(properties)
            elif all(isinstance(p, OWLFullDataProperty) for p in properties):
                new_properties.extend([p.data_property for p in properties])
            else:
                return TypeError
        else:
            if isinstance(properties, OWLDataPropertyExpression):
                new_properties.append(properties)
            elif isinstance(properties, OWLFullDataProperty):
                new_properties.append(properties.data_property)
            else:
                return TypeError

        eq = OWLEquivalentDataProperties(
            new_properties,
            annotations,
        )
        if eq in self.axioms:
            return
        self.axioms.append(eq)

    def is_disjoint_from(
        self,
        properties: typing.Union[
            OWLDataPropertyExpression,
            list[OWLDataPropertyExpression],
            typing.Self,
            list[typing.Self],
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        new_properties: list[OWLDataPropertyExpression] = [self.data_property]
        if isinstance(properties, list):
            if all(isinstance(p, OWLDataPropertyExpression) for p in properties):
                new_properties.extend(properties)
            elif all(isinstance(p, OWLFullDataProperty) for p in properties):
                new_properties.extend([p.data_property for p in properties])
            else:
                return TypeError
        else:
            if isinstance(properties, OWLDataPropertyExpression):
                new_properties.append(properties)
            elif isinstance(properties, OWLFullDataProperty):
                new_properties.append(properties.data_property)
            else:
                return TypeError

        disj = OWLDisjointDataProperties(
            new_properties,
            annotations,
        )
        if disj in self.axioms:
            return
        self.axioms.append(disj)

    def add_negative_assertion(
        self,
        individual: OWLIndividual,
        literal: OWLLiteral,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        assertion = OWLNegativeDataPropertyAssertion(
            self.data_property, individual, literal, annotations
        )
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def add_assertion(
        self,
        individual: OWLIndividual,
        literal: OWLLiteral,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        assertion = OWLDataPropertyAssertion(
            self.data_property, individual, literal, annotations
        )
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def del_assertion(
        self,
        assertion: typing.Union[
            OWLNegativeDataPropertyAssertion, OWLDataPropertyAssertion
        ],
    ) -> None:
        for i in range(len(self.axioms)):
            if assertion != self.axioms[i]:
                continue
            del self.axioms[i]
            return

    def add_domain_annotations(self, annotations: list[OWLAnnotation]) -> None:
        if not self.domain:
            return
        self.domain.axiom_annotations = annotations

    def add_range_annotations(self, annotations: list[OWLAnnotation]) -> None:
        if not self.domain:
            return
        self.range.axiom_annotations = annotations

    def add_property_annotations(
        self, property_class: OWLDataPropertyAxiom, annotations: list[OWLAnnotation]
    ) -> None:
        for p in self.axioms:
            if not isinstance(p, property_class):
                continue
            p.axiom_annotations = annotations
            return

    def some(self, data_range: OWLDataRange) -> None:
        curr = OWLDataSomeValuesFrom(self.data_property, data_range)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def all(self, data_range: OWLDataRange) -> None:
        curr = OWLDataAllValuesFrom(self.data_property, data_range)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def has_value(self, literal: OWLLiteral) -> None:
        curr = OWLDataHasValue(self.data_property, literal)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def min_cardinality(self, cardinality: int, data_range: OWLDataRange) -> None:
        curr = OWLDataMinCardinality(cardinality, self.data_property, data_range)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def max_cardinality(self, cardinality: int, data_range: OWLDataRange) -> None:
        curr = OWLDataMaxCardinality(cardinality, self.data_property, data_range)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def exact_cardinality(self, cardinality: int, data_range: OWLDataRange) -> None:
        curr = OWLDataExactCardinality(cardinality, self.data_property, data_range)
        if curr in self.axioms:
            return
        self.axioms.append(curr)
