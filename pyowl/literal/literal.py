import typing

from rdflib import OWL, RDF, XSD, Literal, Namespace, URIRef

from pyowl.abstracts.annotation_value import OWLAnnotationValue
from pyowl.base.datatype import OWLDatatype
from pyowl.base.iri import IRI


class OWLLiteral(OWLAnnotationValue):
    pass


class OWLTypedLiteral(OWLLiteral):
    """A literal that includes an explicit datatype."""

    def __init__(self, lexical_form: typing.Any, datatype: OWLDatatype) -> None:
        self._lexical_form: typing.Any = lexical_form
        self._datatype: OWLDatatype = datatype

    @property
    def lexical_form(self) -> typing.Any:
        return self._lexical_form

    @lexical_form.setter
    def lexical_form(self, lexical_form: typing.Any) -> None:
        self._lexical_form = lexical_form

    @property
    def datatype(self) -> OWLDatatype:
        return self._datatype

    @datatype.setter
    def datatype(self, datatype: OWLDatatype) -> None:
        self._datatype = datatype

    def to_uriref(self) -> URIRef:
        return Literal(self.lexical_form, datatype=self.datatype.iri.to_uriref())

    def __str__(self) -> str:
        return f"TypedLiteral({self.lexical_form}^^{self.datatype})"


class OWLStringLiteralWithLanguage(OWLLiteral):

    def __init__(self, value: str, language: str) -> None:
        self._value: str = value
        self._language: str = language

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        self._value = value

    @property
    def language(self) -> str:
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        self._language = language

    def to_uriref(self) -> URIRef:
        return Literal(self.value, lang=self.language, datatype=RDF.PlainLiteral)

    def __str__(self) -> str:
        return f'StringLiteralWithLanguage("{self.value}"@{self.language})'


class OWLStringLiteralNoLanguage(OWLLiteral):
    def __init__(self, value: str) -> None:
        self._value: str = value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        self._value = value

    def to_uriref(self) -> URIRef:
        return Literal(self.value, datatype=RDF.PlainLiteral)

    def __str__(self) -> str:
        return f'StringLiteralNoLanguage("{self.value}")'


class OWLLiteral(OWLAnnotationValue):
    """A data value, such as a string or number, used in an ontology."""

    def __init__(
        self,
        value: typing.Union[
            Literal,
            OWLTypedLiteral,
            OWLStringLiteralNoLanguage,
            OWLStringLiteralWithLanguage,
        ],
    ) -> None:
        self._value: typing.Union[
            Literal,
            OWLTypedLiteral,
            OWLStringLiteralNoLanguage,
            OWLStringLiteralWithLanguage,
        ] = value

    @property
    def value(
        self,
    ) -> typing.Union[
        Literal,
        OWLTypedLiteral,
        OWLStringLiteralNoLanguage,
        OWLStringLiteralWithLanguage,
    ]:
        """Getter for value."""
        return self._value

    @value.setter
    def value(
        self,
        value: typing.Union[
            Literal,
            OWLTypedLiteral,
            OWLStringLiteralNoLanguage,
            OWLStringLiteralWithLanguage,
        ],
    ) -> None:
        """Setter for value."""
        self._value = value

    @property
    def datatype(self) -> typing.Optional[OWLDatatype]:
        if isinstance(self.value, Literal):
            return OWLDatatype(IRI(Namespace(self.value.datatype), self.value.datatype))
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype
        return None

    def to_uriref(self) -> URIRef:
        if isinstance(self.value, Literal):
            return self.value
        return self.value.to_uriref()

    def is_double(self) -> bool:
        if isinstance(self.value, Literal):
            return self.value.datatype == XSD.double
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == XSD.double
        return False

    def is_float(self) -> bool:
        if isinstance(self.value, Literal):
            return self.value.datatype == XSD.float
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == XSD.float
        return False

    def is_decimal(self) -> bool:
        if isinstance(self.value, Literal):
            return self.value.datatype == XSD.decimal
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == XSD.decimal
        return False

    def is_real(self) -> bool:
        if isinstance(self.value, Literal):
            return self.value.datatype == OWL.real
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == OWL.real
        return False

    def is_rational(self) -> bool:
        if isinstance(self.value, Literal):
            return self.value.datatype == OWL.rational
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == OWL.rational
        return False

    def is_integer(self) -> bool:
        if isinstance(self.value, Literal):
            dt = self.value.datatype
        elif isinstance(self.value, OWLTypedLiteral):
            dt = self.value.datatype.iri.to_uriref()
        else:
            return False
        return dt in (
            XSD.int,
            XSD.integer,
            XSD.nonNegativeInteger,
            XSD.nonPositiveInteger,
            XSD.negativeInteger,
            XSD.positiveInteger,
            XSD.long,
            XSD.short,
            XSD.byte,
            XSD.unsignedInt,
            XSD.unsignedShort,
            XSD.unsignedLong,
            XSD.unsignedByte,
        )

    def is_boolean(self) -> bool:
        if isinstance(self.value, Literal):
            return self.value.datatype == XSD.boolean
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == XSD.boolean
        return False

    def is_string(self) -> bool:
        if isinstance(self.value, Literal):
            dt = self.value.datatype
        elif isinstance(self.value, OWLTypedLiteral):
            dt = self.value.datatype.iri.to_uriref()
        else:
            return False
        return dt in (
            XSD.string,
            XSD.normalizedString,
            RDF.langString,
            RDF.PlainLiteral,
            RDF.CompoundLiteral,
        )

    def is_date(self) -> bool:
        if isinstance(self.value, Literal):
            dt = self.value.datatype
        elif isinstance(self.value, OWLTypedLiteral):
            dt = self.value.datatype.iri.to_uriref()
        else:
            return False
        return dt in (
            XSD.date,
            XSD.dateTime,
            XSD.dateTimeStamp,
            XSD.dayTimeDuration,
        )

    def is_anyuri(self) -> bool:
        if isinstance(self.value, Literal):
            return self.value.datatype == XSD.anyURI
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == XSD.anyURI
        return False

    def __str__(self) -> str:
        return str(self.value)
