import typing

from rdflib import Literal

from pyowl.abstracts.data_range import OWLDataRange
from pyowl.abstracts.object import OWLObject
from pyowl.axioms.class_axiom.equivalent_classes import OWLEquivalentClasses
from pyowl.axioms.datatype_definition import OWLDatatypeDefinition
from pyowl.base.annotation import OWLAnnotation
from pyowl.base.datatype import OWLDatatype
from pyowl.base.iri import IRI
from pyowl.data_range.data_complement_of import OWLDataComplementOf
from pyowl.data_range.data_intersection_of import OWLDataIntersectionOf
from pyowl.data_range.data_one_of import OWLDataOneOf
from pyowl.data_range.data_union_of import OWLDataUnionOf
from pyowl.data_range.datatype_restriction import OWLDatatypeRestriction, OWLFacet
from pyowl.literal.literal import OWLLiteral


class OWLFullDataRange(OWLObject):

    def __init__(self, iri: IRI) -> None:
        self._data_range: OWLDataRange = OWLDatatype(iri)
        self._axioms: list[typing.Any] = []
        self._annotations: typing.Optional[list[OWLAnnotation]] = None

    @property
    def data_range(self) -> OWLDataRange:
        return self._data_range

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
    def intersections(self) -> list[OWLDataIntersectionOf]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLDataIntersectionOf)
        ]

    @property
    def unions(self) -> list[OWLDataUnionOf]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLDataUnionOf)]

    @property
    def ones_of(self) -> list[OWLDataComplementOf]:
        return [axiom for axiom in self.axioms if isinstance(axiom, OWLDataOneOf)]

    @property
    def restrictions(self) -> list[OWLDatatypeRestriction]:
        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLDatatypeRestriction)
        ]

    @property
    def is_complement(self) -> bool:
        return any(isinstance(axiom, OWLDataOneOf) for axiom in self.axioms)

    def is_intersection_of(
        self, data_ranges: typing.Union[list[OWLDataRange], list[typing.Self]]
    ) -> None:
        element = OWLDataIntersectionOf(
            [self.data_range] + data_ranges
            if all(isinstance(dr, OWLDataRange) for dr in data_ranges)
            else [self.data_range] + [dr.data_range for dr in data_ranges]
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_union_of(
        self, data_ranges: typing.Union[list[OWLDataRange], list[typing.Self]]
    ) -> None:
        element = OWLDataUnionOf(
            [self.data_range] + data_ranges
            if all(isinstance(dr, OWLDataRange) for dr in data_ranges)
            else [self.data_range] + [dr.data_range for dr in data_ranges]
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_one_of(
        self, literals: typing.Union[list[OWLLiteral], list[Literal]]
    ) -> None:
        self.is_equivalent_to(
            OWLDataOneOf(
                literals
                if all(isinstance(lt, Literal) for lt in literals)
                else [lt.value for lt in literals]
            )
        )
        # element = OWLDataOneOf(
        #     [self.data_range] + literals
        #     if all(isinstance(dr, OWLDataRange) for dr in literals)
        #     else [self.data_range] + [dr.data_range for dr in literals]
        # )
        # if element in self.axioms:
        #     return
        # self.axioms.append(element)

    def to_complement(self) -> None:
        element = OWLDataComplementOf(self.data_range)
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_equivalent_to(
        self,
        value: typing.Union[
            OWLDataRange, typing.Self, list[OWLDataRange], list[typing.Self]
        ],
    ) -> None:
        if isinstance(value, list):
            if all(isinstance(v, OWLDataRange) for v in value):
                element = OWLEquivalentClasses(
                    [
                        self.data_range,
                    ]
                    + value
                )
            elif all(isinstance(v, OWLFullDataRange) for v in value):
                element = OWLEquivalentClasses(
                    [
                        self.data_range,
                    ]
                    + [v.data_range for v in value]
                )
            else:
                raise TypeError
        else:
            element = OWLEquivalentClasses(
                [
                    self.data_range,
                    value if isinstance(value, OWLDataRange) else value.data_range,
                ]
            )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_complement_of(self, other: typing.Union[OWLDataRange, typing.Self]) -> None:
        self.is_equivalent_to(
            OWLDataComplementOf(
                other if isinstance(other, OWLDataRange) else other.data_range
            )
        )

    def define(self, datatype: OWLDatatype) -> None:
        element = OWLDatatypeDefinition(self.data_range, datatype)
        if element in self.axioms:
            return
        self.axioms.append(element)

    def restrict(self, datatype: OWLDatatype, facets: list[OWLFacet]) -> None:
        element = self.define(OWLDatatypeRestriction(datatype, facets))
        if element in self.axioms:
            return
        self.axioms.append(element)
