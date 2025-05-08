import typing

from rdflib import OWL, RDF, XSD, Namespace, URIRef
from pyowl.abstracts.data_range import OWLDataRange
from pyowl.abstracts.entity import OWLEntity
from pyowl.base.iri import IRI


class OWLDatatype(OWLEntity, OWLDataRange):
    """A category of data values, such as integers or strings, defined by a set of permissible values."""

    def __init__(self, iri: typing.Union[IRI, URIRef]) -> None:
        self._iri: typing.Union[IRI, URIRef] = iri

    @property
    def iri(self) -> typing.Union[IRI, URIRef]:
        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[IRI, URIRef]) -> None:
        self._iri = value

    def to_uriref(self) -> URIRef:
        return self.iri.to_uriref() if isinstance(self.iri, IRI) else self.iri

    def is_double(self) -> bool:
        return self.iri == IRI(Namespace(XSD._NS), XSD.double)

    def is_float(self) -> bool:
        return self.iri == IRI(Namespace(XSD._NS), XSD.float)

    def is_decimal(self) -> bool:
        return str(self.iri) == str(IRI(Namespace(XSD._NS), XSD.decimal))

    def is_real(self) -> bool:
        return str(self.iri) == str(IRI(Namespace(OWL._NS), OWL.real))

    def is_rational(self) -> bool:
        return str(self.iri) == str(IRI(Namespace(OWL._NS), OWL.rational))

    def is_integer(self) -> bool:
        return str(self.iri) in (
            str(IRI(Namespace(XSD._NS), XSD.int)),
            str(IRI(Namespace(XSD._NS), XSD.integer)),
            str(IRI(Namespace(XSD._NS), XSD.nonNegativeInteger)),
            str(IRI(Namespace(XSD._NS), XSD.nonPositiveInteger)),
            str(IRI(Namespace(XSD._NS), XSD.negativeInteger)),
            str(IRI(Namespace(XSD._NS), XSD.positiveInteger)),
            str(IRI(Namespace(XSD._NS), XSD.long)),
            str(IRI(Namespace(XSD._NS), XSD.short)),
            str(IRI(Namespace(XSD._NS), XSD.byte)),
            str(IRI(Namespace(XSD._NS), XSD.unsignedInt)),
            str(IRI(Namespace(XSD._NS), XSD.unsignedShort)),
            str(IRI(Namespace(XSD._NS), XSD.unsignedLong)),
            str(IRI(Namespace(XSD._NS), XSD.unsignedByte)),
        )

    def is_boolean(self) -> bool:
        return str(self.iri) == str(IRI(Namespace(XSD._NS), XSD.boolean))

    def is_string(self) -> bool:
        return str(self.iri) in (
            str(IRI(Namespace(XSD._NS), XSD.string)),
            str(IRI(Namespace(XSD._NS), XSD.normalizedString)),
            str(IRI(Namespace(RDF._NS), RDF.langString)),
            str(IRI(Namespace(RDF._NS), RDF.PlainLiteral)),
            str(IRI(Namespace(RDF._NS), RDF.CompoundLiteral)),
        )

    def is_date(self) -> bool:
        return str(self.iri) in (
            str(IRI(Namespace(XSD._NS), XSD.date)),
            str(IRI(Namespace(XSD._NS), XSD.dateTime)),
            str(IRI(Namespace(XSD._NS), XSD.dateTimeStamp)),
            str(IRI(Namespace(XSD._NS), XSD.dayTimeDuration)),
        )

    def is_anyuri(self) -> bool:
        return str(self.iri) == str(IRI(Namespace(XSD._NS), XSD.anyURI))

    def __str__(self) -> str:
        return f"Datatype({self._iri})"
