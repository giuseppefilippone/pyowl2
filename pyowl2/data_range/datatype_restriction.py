import enum
import typing

from rdflib import XSD, URIRef

from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.base.datatype import OWLDatatype
from pyowl2.base.iri import IRI
from pyowl2.literal.literal import OWLLiteral


class OWLFacetTypes(enum.StrEnum):
    MIN_INCLUSIVE = enum.auto()
    MIN_EXCLUSIVE = enum.auto()
    MAX_INCLUSIVE = enum.auto()
    MAX_EXCLUSIVE = enum.auto()


class OWLFacet:

    valid_restrictions: list[URIRef] = [
        XSD.minExclusive,
        XSD.minInclusive,
        XSD.maxExclusive,
        XSD.maxInclusive,
    ]

    MIN_INCLUSIVE: URIRef = XSD.minInclusive
    MIN_EXCLUSIVE: URIRef = XSD.minExclusive
    MAX_INCLUSIVE: URIRef = XSD.maxInclusive
    MAX_EXCLUSIVE: URIRef = XSD.maxExclusive

    def __init__(
        self, constraint: typing.Union[URIRef, IRI], value: OWLLiteral
    ) -> None:
        if isinstance(constraint, IRI):
            assert constraint.to_uriref() in OWLFacet.valid_restrictions
        elif isinstance(constraint, URIRef):
            assert constraint in OWLFacet.valid_restrictions
        self._constraint: typing.Union[URIRef, IRI] = constraint
        self._value: OWLLiteral = value

    @property
    def constraint(self) -> typing.Union[URIRef, IRI]:
        return self._constraint

    @constraint.setter
    def constraint(self, value: typing.Union[URIRef, IRI]) -> None:
        self._constraint = value

    @property
    def value(self) -> OWLLiteral:
        return self._value

    @value.setter
    def value(self, value: OWLLiteral) -> None:
        self._value = value

    def constraint_to_uriref(self) -> URIRef:
        return (
            self.constraint.to_uriref()
            if isinstance(self.constraint, IRI)
            else self.constraint
        )

    def __eq__(self, value: object) -> bool:
        return str(self) == str(value)

    def __ne__(self, value: object) -> bool:
        return str(self) != str(value)

    def __lt__(self, value: object) -> bool:
        return str(self) < str(value)

    def __le__(self, value: object) -> bool:
        return str(self) <= str(value)

    def __gt__(self, value: object) -> bool:
        return str(self) > str(value)

    def __ge__(self, value: object) -> bool:
        return str(self) >= str(value)

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"Facet({self.constraint} {self.value})"


class OWLDatatypeRestriction(OWLDataRange):
    """A datatype that is constrained by specific facets, such as value ranges or lengths."""

    def __init__(self, datatype: OWLDatatype, restrictions: list[OWLFacet]) -> None:
        super().__init__()
        assert len(restrictions) >= 1
        self._datatype: OWLDatatype = datatype
        self._restrictions: list[OWLFacet] = sorted(restrictions)

    @property
    def datatype(self) -> OWLDatatype:
        """Getter for datatype."""
        return self._datatype

    @datatype.setter
    def datatype(self, value: OWLDatatype) -> None:
        """Setter for datatype."""
        self._datatype = value

    @property
    def restrictions(self) -> list[OWLFacet]:
        """Getter for facets."""
        return self._restrictions

    @restrictions.setter
    def restrictions(self, value: list[OWLFacet]) -> None:
        """Setter for facets."""
        self._restrictions = sorted(value)

    def __str__(self) -> str:
        return f"DatatypeRestriction({self.datatype} {' '.join(map(str, self.restrictions))})"
