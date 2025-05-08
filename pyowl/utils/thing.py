import typing

from pyowl.abstracts.class_expression import OWLClassExpression
from pyowl.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl.abstracts.individual import OWLIndividual
from pyowl.abstracts.object import OWLObject
from pyowl.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl.axioms.assertion.class_assertion import OWLClassAssertion
from pyowl.axioms.class_axiom.disjoint_classes import OWLDisjointClasses
from pyowl.axioms.class_axiom.disjoint_union import OWLDisjointUnion
from pyowl.axioms.class_axiom.equivalent_classes import OWLEquivalentClasses
from pyowl.axioms.class_axiom.sub_class_of import OWLSubClassOf
from pyowl.axioms.has_key import OWLHasKey
from pyowl.base.annotation import OWLAnnotation
from pyowl.base.iri import IRI
from pyowl.base.owl_class import OWLClass
from pyowl.class_expression.object_all_values_from import OWLObjectAllValuesFrom
from pyowl.class_expression.object_complement_of import OWLObjectComplementOf
from pyowl.class_expression.object_exact_cardinality import OWLObjectExactCardinality
from pyowl.class_expression.object_intersection_of import OWLObjectIntersectionOf
from pyowl.class_expression.object_max_cardinality import OWLObjectMaxCardinality
from pyowl.class_expression.object_min_cardinality import OWLObjectMinCardinality
from pyowl.class_expression.object_one_of import OWLObjectOneOf
from pyowl.class_expression.object_some_values_from import OWLObjectSomeValuesFrom
from pyowl.class_expression.object_union_of import OWLObjectUnionOf


class OWLFullClass(OWLObject):

    def __init__(self, iri: IRI) -> None:
        self._class: OWLClass = OWLClass(iri)
        self._axioms: list[typing.Any] = []
        self._annotations: typing.Optional[list[OWLAnnotation]] = None

    @staticmethod
    def thing() -> typing.Self:
        return OWLFullClass(IRI.thing_iri())

    @staticmethod
    def nothing() -> typing.Self:
        return OWLFullClass(IRI.nothing_iri())

    @property
    def class_(self) -> OWLClass:
        return self._class

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
    def assertions(self) -> list[OWLClassAssertion]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLClassAssertion)]

    @property
    def intersections(self) -> list[OWLObjectIntersectionOf]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectIntersectionOf)
        ]

    @property
    def unions(self) -> list[OWLObjectOneOf]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLObjectOneOf)]

    @property
    def is_complement(self) -> bool:
        return any(isinstance(axiom, OWLObjectComplementOf) for axiom in self.axioms)

    @property
    def subclasses(self) -> list[OWLSubClassOf]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLSubClassOf)
            and axiom.super_class_expression == self.class_
        ]

    @property
    def superclasses(self) -> list[OWLSubClassOf]:
        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLSubClassOf)
            and axiom.sub_class_expression == self.class_
        ]

    @property
    def equivalent_classes(self) -> list[OWLEquivalentClasses]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLEquivalentClasses)
        ]

    @property
    def disjoint_classes(self) -> list[OWLDisjointClasses]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLDisjointClasses)]

    @property
    def disjoint_union_classes(self) -> list[OWLDisjointUnion]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLDisjointUnion)]

    @property
    def all_axioms(self) -> list[OWLObjectAllValuesFrom]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectAllValuesFrom)
        ]

    @property
    def some_axioms(self) -> list[OWLObjectSomeValuesFrom]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectSomeValuesFrom)
        ]

    @property
    def has_key_axioms(self) -> list[OWLHasKey]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLHasKey)]

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

    def add_assertion(
        self,
        individual: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        assertion = OWLClassAssertion(self.class_, individual, annotations)
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def is_subclass_of(
        self,
        super_class: typing.Union[OWLClassExpression, typing.Self],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        element = OWLSubClassOf(
            self.class_,
            (
                super_class
                if isinstance(super_class, OWLClassExpression)
                else super_class.class_
            ),
            annotations,
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_superclass_of(
        self,
        sub_class: typing.Union[OWLClassExpression, typing.Self],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        element = OWLSubClassOf(
            (
                sub_class
                if isinstance(sub_class, OWLClassExpression)
                else sub_class.class_
            ),
            self.class_,
            annotations,
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def _get_classes(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
    ) -> list[OWLClassExpression]:
        new_classes: list[OWLClassExpression] = []
        if isinstance(classes, list):
            if all(isinstance(c, OWLClassExpression) for c in classes):
                new_classes.extend(classes)
            elif all(isinstance(c, OWLFullClass) for c in classes):
                new_classes.extend([c.class_ for c in classes])
            else:
                return TypeError
        else:
            if isinstance(classes, OWLClassExpression):
                new_classes.append(classes)
            elif isinstance(classes, OWLFullClass):
                new_classes.append(classes.class_)
            else:
                return TypeError
        return new_classes

    def is_equivalent_to(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        element = OWLEquivalentClasses(
            [self.class_] + self._get_classes(classes), annotations
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_disjoint_from(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        element = OWLDisjointClasses(
            [self.class_] + self._get_classes(classes), annotations
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_disjoint_union_from(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        element = OWLDisjointUnion(self.class_, self._get_classes(classes), annotations)
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_intersection_of(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
    ) -> None:
        intersection = OWLObjectIntersectionOf(
            [self.class_] + self._get_classes(classes)
        )
        if intersection in self.axioms:
            return
        self.axioms.append(intersection)

    def is_union_of(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
    ) -> None:
        union = OWLObjectUnionOf([self.class_] + self._get_classes(classes))
        if union in self.axioms:
            return
        self.axioms.append(union)

    def to_complement(self) -> None:
        complement = OWLObjectComplementOf(self.class_)
        if complement in self.axioms:
            return
        self.axioms.append(complement)

    def all_values(
        self,
        object: OWLObjectPropertyExpression,
    ) -> None:
        element = OWLObjectAllValuesFrom(object, self.class_)
        if element in self.axioms:
            return
        self.axioms.append(element)

    def some_values(
        self,
        object: OWLObjectPropertyExpression,
    ) -> None:
        element = OWLObjectSomeValuesFrom(object, self.class_)
        if element in self.axioms:
            return
        self.axioms.append(element)

    def has_key(
        self,
        object_properties: list[OWLObjectPropertyExpression],
        data_properties: list[OWLDataPropertyExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        element = OWLHasKey(
            self.class_, object_properties, data_properties, annotations
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def min_cardinality(
        self, cardinality: int, object_property: OWLObjectPropertyExpression
    ) -> None:
        curr = OWLObjectMinCardinality(cardinality, object_property, self.class_)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def max_cardinality(
        self, cardinality: int, object_property: OWLObjectPropertyExpression
    ) -> None:
        curr = OWLObjectMaxCardinality(cardinality, object_property, self.class_)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def exact_cardinality(
        self, cardinality: int, object_property: OWLObjectPropertyExpression
    ) -> None:
        curr = OWLObjectExactCardinality(cardinality, object_property, self.class_)
        if curr in self.axioms:
            return
        self.axioms.append(curr)
