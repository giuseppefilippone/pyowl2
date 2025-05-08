import typing

from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.abstracts.individual import OWLIndividual
from pyowl.abstracts.object import OWLObject
from pyowl.abstracts.object_property_axiom import OWLObjectPropertyAxiom
from pyowl.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl.axioms.assertion.negative_object_property_assertion import (
    OWLNegativeObjectPropertyAssertion,
)
from pyowl.axioms.assertion.object_property_assertion import OWLObjectPropertyAssertion
from pyowl.axioms.object_property_axiom.asymmetric_object_property import (
    OWLAsymmetricObjectProperty,
)
from pyowl.axioms.object_property_axiom.disjoint_object_properties import (
    OWLDisjointObjectProperties,
)
from pyowl.axioms.object_property_axiom.equivalent_object_properties import (
    OWLEquivalentObjectProperties,
)
from pyowl.axioms.object_property_axiom.functional_object_property import (
    OWLFunctionalObjectProperty,
)
from pyowl.axioms.object_property_axiom.inverse_functional_object_property import (
    OWLInverseFunctionalObjectProperty,
)
from pyowl.axioms.object_property_axiom.inverse_object_properties import (
    OWLInverseObjectProperties,
)
from pyowl.axioms.object_property_axiom.irreflexive_object_property import (
    OWLIrreflexiveObjectProperty,
)
from pyowl.axioms.object_property_axiom.object_property_chain import (
    OWLObjectPropertyChain,
)
from pyowl.axioms.object_property_axiom.object_property_domain import (
    OWLObjectPropertyDomain,
)
from pyowl.axioms.object_property_axiom.object_property_range import (
    OWLObjectPropertyRange,
)
from pyowl.axioms.object_property_axiom.reflexive_object_property import (
    OWLReflexiveObjectProperty,
)
from pyowl.axioms.object_property_axiom.sub_object_property_of import (
    OWLSubObjectPropertyOf,
)
from pyowl.axioms.object_property_axiom.symmetric_object_property import (
    OWLSymmetricObjectProperty,
)
from pyowl.axioms.object_property_axiom.transitive_object_property import (
    OWLTransitiveObjectProperty,
)
from pyowl.base.annotation import OWLAnnotation
from pyowl.base.iri import IRI
from pyowl.class_expression.object_all_values_from import OWLObjectAllValuesFrom
from pyowl.class_expression.object_exact_cardinality import OWLObjectExactCardinality
from pyowl.class_expression.object_has_self import OWLObjectHasSelf
from pyowl.class_expression.object_has_value import OWLObjectHasValue
from pyowl.class_expression.object_max_cardinality import OWLObjectMaxCardinality
from pyowl.class_expression.object_min_cardinality import OWLObjectMinCardinality
from pyowl.class_expression.object_some_values_from import OWLObjectSomeValuesFrom
from pyowl.expressions.object_property import OWLObjectProperty


class OWLFullObjectProperty(OWLObject):

    PROPERTY_CLASSES: list[type] = [
        OWLSymmetricObjectProperty,
        OWLAsymmetricObjectProperty,
        OWLFunctionalObjectProperty,
        OWLInverseFunctionalObjectProperty,
        OWLTransitiveObjectProperty,
        OWLReflexiveObjectProperty,
        OWLIrreflexiveObjectProperty,
    ]

    def __init__(
        self,
        iri: IRI,
        domain: typing.Optional[OWLClassExpression] = None,
        range: typing.Optional[OWLClassExpression] = None,
        is_symmetric: bool = False,
        is_asymmetric: bool = False,
        is_functional: bool = False,
        is_inverse_functional: bool = False,
        is_transitive: bool = False,
        is_reflexive: bool = False,
        is_irreflexive: bool = False,
    ) -> None:
        self._object_property: OWLObjectProperty = OWLObjectProperty(iri)
        self._domain: OWLObjectPropertyDomain = (
            OWLObjectPropertyDomain(self._object_property, domain) if domain else None
        )
        self._range: OWLObjectPropertyRange = (
            OWLObjectPropertyRange(self._object_property, range) if range else None
        )
        self._axioms: list[typing.Any] = []
        self._annotations: typing.Optional[list[OWLAnnotation]] = None
        if is_symmetric:
            self._axioms.append(OWLSymmetricObjectProperty(self._object_property))
        if is_asymmetric:
            self._axioms.append(OWLAsymmetricObjectProperty(self._object_property))
        if is_functional:
            self._axioms.append(OWLFunctionalObjectProperty(self._object_property))
        if is_inverse_functional:
            self._axioms.append(
                OWLInverseFunctionalObjectProperty(self._object_property)
            )
        if is_transitive:
            self._axioms.append(OWLTransitiveObjectProperty(self._object_property))
        if is_reflexive:
            self._axioms.append(OWLReflexiveObjectProperty(self._object_property))
        if is_irreflexive:
            self._axioms.append(OWLIrreflexiveObjectProperty(self._object_property))

    @property
    def object_property(self) -> OWLObjectProperty:
        return self._object_property

    @object_property.setter
    def object_property(self, value: OWLObjectProperty) -> None:
        self._object_property = value

    @property
    def domain(self) -> typing.Optional[OWLObjectPropertyDomain]:
        return self._domain

    @domain.setter
    def domain(self, value: OWLClassExpression) -> None:
        self._domain = OWLObjectPropertyDomain(self.object_property, value)

    @property
    def range(self) -> typing.Optional[OWLObjectPropertyRange]:
        return self._range

    @range.setter
    def range(self, value: OWLClassExpression) -> None:
        self._range = OWLObjectPropertyRange(self.object_property, value)

    @property
    def annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        return self._annotations

    @annotations.setter
    def annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
        self._annotations = value

    @property
    def properties(self) -> list[OWLObjectPropertyAxiom]:
        return [
            axiom
            for axiom in self.axioms
            if type(axiom) in OWLFullObjectProperty.PROPERTY_CLASSES
        ]

    @property
    def assertions(self) -> list[OWLObjectPropertyAssertion]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(
                axiom, (OWLObjectPropertyAssertion, OWLNegativeObjectPropertyAssertion)
            )
        ]

    @property
    def axioms(self) -> list[typing.Any]:
        return self._axioms

    @property
    def inverses(self) -> list[OWLInverseObjectProperties]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLInverseObjectProperties)
        ]

    @property
    def sub_properties(self) -> list[OWLSubObjectPropertyOf]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLSubObjectPropertyOf)
            and axiom.super_object_property_expression == self.object_property
        ]

    @property
    def super_properties(self) -> list[OWLSubObjectPropertyOf]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLSubObjectPropertyOf)
            and axiom.sub_object_property_expression == self.object_property
        ]

    @property
    def equivalent_properties(self) -> list[OWLEquivalentObjectProperties]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLEquivalentObjectProperties)
        ]

    @property
    def disjoint_properties(self) -> list[OWLDisjointObjectProperties]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLDisjointObjectProperties)
        ]

    @property
    def some_axioms(self) -> list[OWLObjectSomeValuesFrom]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectSomeValuesFrom)
        ]

    @property
    def all_axioms(self) -> list[OWLObjectAllValuesFrom]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectAllValuesFrom)
        ]

    @property
    def has_value_axioms(self) -> list[OWLObjectHasValue]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLObjectHasValue)]

    @property
    def has_self_axioms(self) -> list[OWLObjectHasSelf]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLObjectHasSelf)]

    @property
    def min_axioms(self) -> list[OWLObjectMinCardinality]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectMinCardinality)
        ]

    @property
    def max_axioms(self) -> list[OWLObjectMaxCardinality]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectMaxCardinality)
        ]

    @property
    def exact_axioms(self) -> list[OWLObjectExactCardinality]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLObjectExactCardinality)
        ]

    def _del_property(self, curr_value: bool, value: bool, cls: type) -> None:
        if not curr_value and not value:
            return
        if curr_value and value:
            return
        if curr_value and not value:
            for i in range(len(self.axioms)):
                if not isinstance(i, cls):
                    continue
                del self.axioms[i]
                return
            return
        element = cls(self.object_property)
        if element in self.axioms:
            return
        self.axioms.append(element)

    @property
    def is_symmetric(self) -> bool:
        return any(isinstance(p, OWLSymmetricObjectProperty) for p in self.properties)

    @is_symmetric.setter
    def is_symmetric(self, value: bool) -> None:
        self._del_property(self.is_symmetric, value, OWLSymmetricObjectProperty)

    @property
    def is_asymmetric(self) -> bool:
        return any(isinstance(p, OWLAsymmetricObjectProperty) for p in self.properties)

    @is_asymmetric.setter
    def is_asymmetric(self, value: bool) -> None:
        self._del_property(self.is_asymmetric, value, OWLAsymmetricObjectProperty)

    @property
    def is_transitive(self) -> bool:
        return any(isinstance(p, OWLTransitiveObjectProperty) for p in self.properties)

    @is_transitive.setter
    def is_transitive(self, value: bool) -> None:
        self._del_property(self.is_transitive, value, OWLTransitiveObjectProperty)

    @property
    def is_functional(self) -> bool:
        return any(isinstance(p, OWLFunctionalObjectProperty) for p in self.properties)

    @is_functional.setter
    def is_functional(self, value: bool) -> None:
        self._del_property(self.is_functional, value, OWLFunctionalObjectProperty)

    @property
    def is_inverse_functional(self) -> bool:
        return any(
            isinstance(p, OWLInverseFunctionalObjectProperty) for p in self.properties
        )

    @is_inverse_functional.setter
    def is_inverse_functional(self, value: bool) -> None:
        self._del_property(
            self.is_inverse_functional, value, OWLInverseFunctionalObjectProperty
        )

    @property
    def is_irreflexive(self) -> bool:
        return any(isinstance(p, OWLIrreflexiveObjectProperty) for p in self.properties)

    @is_irreflexive.setter
    def is_irreflexive(self, value: bool) -> None:
        self._del_property(self.is_irreflexive, value, OWLIrreflexiveObjectProperty)

    @property
    def is_reflexive(self) -> bool:
        return any(isinstance(p, OWLReflexiveObjectProperty) for p in self.properties)

    @is_reflexive.setter
    def is_reflexive(self, value: bool) -> None:
        self._del_property(self.is_reflexive, value, OWLReflexiveObjectProperty)

    def is_sub_property_of(
        self,
        super_property: typing.Union[OWLObjectPropertyExpression, typing.Self],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        curr = OWLSubObjectPropertyOf(
            self.object_property,
            (
                super_property
                if not isinstance(super_property, OWLFullObjectProperty)
                else super_property.object_property
            ),
            annotations,
        )
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def is_super_property_of(
        self,
        sub_property: typing.Union[
            OWLObjectPropertyExpression, OWLObjectPropertyChain, typing.Self
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        curr = OWLSubObjectPropertyOf(
            (
                sub_property
                if not isinstance(sub_property, OWLFullObjectProperty)
                else sub_property.object_property
            ),
            self.object_property,
            annotations,
        )
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def is_equivalent_to(
        self,
        properties: typing.Union[
            OWLObjectPropertyExpression,
            list[OWLObjectPropertyExpression],
            typing.Self,
            list[typing.Self],
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        new_properties: list[OWLObjectPropertyExpression] = [self.object_property]
        if isinstance(properties, list):
            if all(isinstance(p, OWLObjectPropertyExpression) for p in properties):
                new_properties.extend(properties)
            elif all(isinstance(p, OWLFullObjectProperty) for p in properties):
                new_properties.extend([p.object_property for p in properties])
            else:
                return TypeError
        else:
            if isinstance(properties, OWLObjectPropertyExpression):
                new_properties.append(properties)
            elif isinstance(properties, OWLFullObjectProperty):
                new_properties.append(properties.object_property)
            else:
                return TypeError

        eq = OWLEquivalentObjectProperties(
            new_properties,
            annotations,
        )
        if eq in self.axioms:
            return
        self.axioms.append(eq)

    def is_disjoint_from(
        self,
        properties: typing.Union[
            OWLObjectPropertyExpression,
            list[OWLObjectPropertyExpression],
            typing.Self,
            list[typing.Self],
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        new_properties: list[OWLObjectPropertyExpression] = [self.object_property]
        if isinstance(properties, list):
            if all(isinstance(p, OWLObjectPropertyExpression) for p in properties):
                new_properties.extend(properties)
            elif all(isinstance(p, OWLFullObjectProperty) for p in properties):
                new_properties.extend([p.object_property for p in properties])
            else:
                return TypeError
        else:
            if isinstance(properties, OWLObjectPropertyExpression):
                new_properties.append(properties)
            elif isinstance(properties, OWLFullObjectProperty):
                new_properties.append(properties.object_property)
            else:
                return TypeError

        disj = OWLDisjointObjectProperties(
            new_properties,
            annotations,
        )
        if disj in self.axioms:
            return
        self.axioms.append(disj)

    def is_inverse_of(self, property: OWLObjectPropertyExpression) -> None:
        curr = OWLInverseObjectProperties(self.object_property, property)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def add_negative_assertion(
        self,
        individual_1: OWLIndividual,
        individual_2: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        negative_assertion = OWLNegativeObjectPropertyAssertion(
            self.object_property, individual_1, individual_2, annotations
        )
        if negative_assertion in self.axioms:
            return
        self.axioms.append(negative_assertion)

    def add_assertion(
        self,
        individual_1: OWLIndividual,
        individual_2: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        assertion = OWLObjectPropertyAssertion(
            self.object_property, individual_1, individual_2, annotations
        )
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def del_assertion(
        self,
        assertion: typing.Union[
            OWLObjectPropertyAssertion, OWLNegativeObjectPropertyAssertion
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
        self, property_class: OWLObjectPropertyAxiom, annotations: list[OWLAnnotation]
    ) -> None:
        for p in self.axioms:
            if not isinstance(p, property_class):
                continue
            p.axiom_annotations = annotations
            return

    def some(self, cls: OWLClassExpression) -> None:
        curr = OWLObjectSomeValuesFrom(self.object_property, cls)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def all(self, cls: OWLClassExpression) -> None:
        curr = OWLObjectAllValuesFrom(self.object_property, cls)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def has_value(self, individual: OWLIndividual) -> None:
        curr = OWLObjectHasValue(self.object_property, individual)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def has_self(self) -> None:
        curr = OWLObjectHasSelf(self.object_property)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def min_cardinality(self, cardinality: int, cls: OWLClassExpression) -> None:
        curr = OWLObjectMinCardinality(cardinality, self.object_property, cls)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def max_cardinality(self, cardinality: int, cls: OWLClassExpression) -> None:
        curr = OWLObjectMaxCardinality(cardinality, self.object_property, cls)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def exact_cardinality(self, cardinality: int, cls: OWLClassExpression) -> None:
        curr = OWLObjectExactCardinality(cardinality, self.object_property, cls)
        if curr in self.axioms:
            return
        self.axioms.append(curr)
