import typing

from rdflib import OWL, RDF, XSD, Literal, Namespace, URIRef

from pyowl2.abstracts.annotation_value import OWLAnnotationValue
from pyowl2.base.datatype import OWLDatatype
from pyowl2.base.iri import IRI


class OWLLiteral(OWLAnnotationValue):
    """
    This class serves as a unified wrapper for data values used within an ontology, such as strings, numbers, or dates. It encapsulates various underlying representations, including standard RDFLib Literals and specific OWL literal types like typed literals or language-tagged strings. By providing a common interface, it allows users to access the raw value through the `value` property while abstracting away the specific implementation details. Additionally, the class offers a suite of convenience methods—such as `is_integer`, `is_string`, and `is_boolean`—to inspect the datatype of the contained value, facilitating type checking and validation logic within ontology processing workflows.

    :parm value: The underlying data representation of the literal, supporting RDFLib Literals, typed literals, and language-tagged strings.
    :type value: typing.Union[Literal, OWLTypedLiteral, OWLStringLiteralNoLanguage, OWLStringLiteralWithLanguage]
    """

    pass


class OWLTypedLiteral(OWLLiteral):
    """
    Represents a typed literal value within an OWL ontology, distinguishing it from untyped strings by associating a specific data type with the value. It encapsulates a lexical form—the raw representation of the value—and an `OWLDatatype` instance that defines how that value should be interpreted (e.g., as an integer or a boolean). This class is typically used to construct precise data assertions in axioms and provides functionality to serialize the value into standard RDF formats via the `to_uriref` method.

    :parm lexical_form: The lexical form or value of the literal. This represents the actual data content of the literal as it appears in the ontology, interpreted according to the specified datatype.
    :type lexical_form: typing.Any
    :parm datatype: The specific type definition determining the interpretation of the literal's value.
    :type datatype: OWLDatatype
    """

    def __init__(self, lexical_form: typing.Any, datatype: OWLDatatype) -> None:
        """
        Initializes a new instance representing a typed literal within an OWL ontology, storing the provided lexical representation and its associated datatype. The constructor assigns the given lexical form and the OWLDatatype object directly to internal attributes, establishing the fundamental components of the literal without performing immediate validation of their semantic compatibility.

        :param lexical_form: The lexical representation of the literal value.
        :type lexical_form: typing.Any
        :param datatype: The OWL datatype that defines the interpretation of the lexical form.
        :type datatype: OWLDatatype
        """

        self._lexical_form: typing.Any = lexical_form
        self._datatype: OWLDatatype = datatype

    @property
    def lexical_form(self) -> typing.Any:
        """
        Updates the lexical form of the current `OWLTypedLiteral` instance. This setter accepts a value of any type and assigns it directly to the internal `_lexical_form` attribute, effectively overwriting the previous string representation of the literal. While the input type is unrestricted, it is typically expected to be a string representing the literal's value in a serialized format.

        :param lexical_form: The lexical representation of the value to be stored.
        :type lexical_form: typing.Any
        """

        return self._lexical_form

    @lexical_form.setter
    def lexical_form(self, lexical_form: typing.Any) -> None:
        self._lexical_form = lexical_form

    @property
    def datatype(self) -> OWLDatatype:
        """
        Sets the datatype associated with this OWL typed literal, replacing any previously assigned value. This method accepts an instance of OWLDatatype and updates the internal state of the object to reflect the new type. The operation modifies the object in place and does not return a value.

        :param datatype: The OWL datatype to assign to the object.
        :type datatype: OWLDatatype
        """

        return self._datatype

    @datatype.setter
    def datatype(self, datatype: OWLDatatype) -> None:
        self._datatype = datatype

    def to_uriref(self) -> URIRef:
        """
        Converts the OWL typed literal into an RDFLib Literal instance. This method constructs a new Literal using the object's lexical form and its associated datatype, where the datatype is resolved by converting the internal IRI to a URIRef. The operation does not modify the original object but rather returns a distinct representation suitable for RDF graph manipulation.

        :return: A Literal instance with the same lexical form and a datatype converted to a URIRef.

        :rtype: URIRef
        """

        return Literal(self.lexical_form, datatype=self.datatype.iri.to_uriref())

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the typed literal, formatted for debugging or display purposes. The output follows the pattern `TypedLiteral(lexical_form^^datatype)`, combining the literal's value and its specific data type using the standard RDF delimiter. This method relies on the `lexical_form` and `datatype` attributes being present and convertible to strings.

        :return: A string representation of the literal in the format 'TypedLiteral(lexical_form^^datatype)'.

        :rtype: str
        """

        return f"TypedLiteral({self.lexical_form}^^{self.datatype})"


class OWLStringLiteralWithLanguage(OWLLiteral):
    """
    This class represents a specific type of textual data used in ontologies where the content is explicitly associated with a natural language, such as English or French. It encapsulates a string value alongside a language tag that typically follows IETF BCP 47 standards, allowing for the precise representation of multilingual information like labels or annotations. By extending the base literal interface, it facilitates the integration of language-aware strings into semantic web structures and provides mechanisms to convert the data into standard RDF formats for serialization and interchange.

    :parm value: The actual text content of the literal as it appears in the ontology.
    :type value: str
    :parm language: The IETF BCP 47 language tag associated with the literal, indicating the language of the text content.
    :type language: str
    """

    def __init__(self, value: str, language: str) -> None:
        """
        Constructs a new object representing a string literal that is associated with a specific language tag. The method accepts the textual content and the language code as arguments, assigning them to internal attributes for storage. This allows the representation of lexical values within an OWL context where language distinctions are necessary.

        :param value: The string content to be stored.
        :type value: str
        :param language: The language code or identifier associated with the value.
        :type language: str
        """

        self._value: str = value
        self._language: str = language

    @property
    def value(self) -> str:
        """
        Sets the lexical value of the OWL string literal. This method assigns the provided string to the internal `_value` attribute, replacing any existing value. It serves as the setter for the `value` property, allowing the modification of the literal's content after instantiation.

        :param value: The new string value to assign to the object.
        :type value: str
        """

        return self._value

    @value.setter
    def value(self, value: str) -> None:
        self._value = value

    @property
    def language(self) -> str:
        """
        Sets the language tag for the OWL string literal. This method updates the internal state by assigning the provided string to the private `_language` attribute, effectively replacing any existing language designation.

        :param language: The language code or name to set for the instance.
        :type language: str
        """

        return self._language

    @language.setter
    def language(self, language: str) -> None:
        self._language = language

    def to_uriref(self) -> URIRef:
        """
        Constructs and returns an RDFLib Literal object representing the current string value and language tag. The Literal is created with the datatype explicitly set to RDF.PlainLiteral, ensuring proper semantic representation in RDF graphs. Note that despite the method name, the return type is a Literal, not a URI reference.

        :return: Returns a Literal object initialized with the instance's value, language, and the RDF.PlainLiteral datatype.

        :rtype: URIRef
        """

        return Literal(self.value, lang=self.language, datatype=RDF.PlainLiteral)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the object, formatted to display both the lexical value and the language tag. The representation encloses the value in double quotes and appends the language tag with an '@' separator, wrapping the entire expression in a descriptive class prefix. This method is primarily intended for debugging and logging purposes, providing a clear visual summary of the literal's content.

        :return: A string representation of the object in the format `StringLiteralWithLanguage("value"@language)`.

        :rtype: str
        """

        return f'StringLiteralWithLanguage("{self.value}"@{self.language})'


class OWLStringLiteralNoLanguage(OWLLiteral):
    """
    This class represents a textual literal within an OWL ontology that is explicitly defined without an associated language tag, distinguishing it from localized string literals. It acts as a container for raw string data, allowing the text to be associated with entities or axioms where language-specific tagging is not required. To use this class, instantiate it with the desired string content and access or modify this content via the `value` property. The class also supports conversion to an RDF representation, specifically mapping the value to a plain literal data type for interoperability with semantic web standards.

    :parm value: The actual text content of the literal as it appears in the ontology.
    :type value: str
    """

    def __init__(self, value: str) -> None:
        """
        Initializes a new instance representing an OWL string literal that is not associated with a specific language tag. The constructor accepts a single string argument representing the lexical value of the literal and assigns it to the internal state of the object. This setup distinguishes the literal from language-tagged strings within the OWL ontology structure.

        :param value: The initial string value to be stored in the object.
        :type value: str
        """

        self._value: str = value

    @property
    def value(self) -> str:
        """
        Sets the lexical value of the OWL string literal to the provided string. This method acts as a setter for the `value` property, overwriting the internal `_value` attribute with the new content. It directly mutates the object's state without performing validation, ensuring that the provided argument is stored as the new literal value.

        :param value: The new string value to assign to the object's internal state.
        :type value: str
        """

        return self._value

    @value.setter
    def value(self, value: str) -> None:
        self._value = value

    def to_uriref(self) -> URIRef:
        """
        Converts the internal string value of this instance into an RDF Literal object explicitly typed as `RDF.PlainLiteral`. The method retrieves the value from the `value` attribute and wraps it in a `Literal` structure, ensuring it is represented as a plain literal in the RDF model. This operation is side-effect free, as it generates a new node without modifying the state of the current object.

        :return: An RDF Literal with the datatype rdf:PlainLiteral containing the instance's value.

        :rtype: URIRef
        """

        return Literal(self.value, datatype=RDF.PlainLiteral)

    def __str__(self) -> str:
        """
        Returns a string representation of the object, formatted to resemble a constructor invocation with the literal's value. The output consists of the class name followed by the internal value enclosed in double quotes. This method is primarily used for display and debugging purposes, providing a human-readable identifier that clearly distinguishes the specific type of string literal.

        :return: The string representation of the object, formatted as `StringLiteralNoLanguage("value")`.

        :rtype: str
        """

        return f'StringLiteralNoLanguage("{self.value}")'


class OWLLiteral(OWLAnnotationValue):
    """
    A data value, such as a string or number, used in an ontology.

    Attributes
    ----------
    value: typing.Union[
        Literal,
        OWLTypedLiteral,
        OWLStringLiteralNoLanguage,
        OWLStringLiteralWithLanguage,
    ]
        The value of the literal, which can be represented in different forms depending on the specific type of literal. This value can be a simple RDFLib Literal, an OWLTypedLiteral that includes an explicit datatype, an OWLStringLiteralNoLanguage that represents a string literal without a language tag, or an OWLStringLiteralWithLanguage that represents a string literal with an associated language tag. For example, if the literal represents a typed literal with a datatype of xsd:integer and a lexical form of "42", the value would be an instance of OWLTypedLiteral with the appropriate lexical form and datatype. The value attribute allows for the representation of various types of literals in a unified way, enabling the expression of different data values that can be associated with entities and axioms within the ontology, and providing a common interface for handling literals in the ontology regardless of their specific type or representation.
    """

    def __init__(
        self,
        value: typing.Union[
            Literal,
            OWLTypedLiteral,
            OWLStringLiteralNoLanguage,
            OWLStringLiteralWithLanguage,
        ],
    ) -> None:
        """
        Initializes a new instance representing an OWL literal by encapsulating a specific value object. The constructor accepts a single argument, `value`, which can be a standard `Literal`, an `OWLTypedLiteral`, or string literals with or without language tags. This input is stored internally within the instance, serving as the underlying data representation for the literal.

        :param value: The literal value to be stored, which can be a generic Literal, a typed literal, or a string literal with or without a language tag.
        :type value: typing.Union[Literal, OWLTypedLiteral, OWLStringLiteralNoLanguage, OWLStringLiteralWithLanguage]
        """

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
        """
        Sets the underlying lexical or typed value of the `OWLLiteral` instance. This method accepts a range of literal representations, such as generic `Literal` objects, `OWLTypedLiteral`, or specific string literal types with or without language tags. By invoking this setter, the internal state of the object is mutated, replacing the previously stored value with the new one provided.

        :param value: The literal value to assign, supporting generic literals, typed literals, and string literals with or without language tags.
        :type value: typing.Union[Literal, OWLTypedLiteral, OWLStringLiteralNoLanguage, OWLStringLiteralWithLanguage]
        """

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
        """
        Retrieves the specific data type associated with the literal's value. If the underlying value is an RDFLib `Literal`, the method constructs an `OWLDatatype` object based on the literal's datatype IRI. If the value is an instance of `OWLTypedLiteral`, the datatype is returned directly. In cases where the value does not conform to these recognized types or lacks a datatype, the method returns `None`.

        :return: Returns the OWL datatype of the underlying value if it is a literal, otherwise None.

        :rtype: typing.Optional[OWLDatatype]
        """

        if isinstance(self.value, Literal):
            return OWLDatatype(IRI(Namespace(self.value.datatype), self.value.datatype))
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype
        return None

    def to_uriref(self) -> URIRef:
        """
        Converts the internal value of the literal into a URI reference or returns the value directly if it is already a Literal. If the underlying value is an object that supports conversion to a URI reference, the method delegates the conversion to that object. This approach handles cases where the literal wraps either a raw RDFLib Literal or an entity that needs to be resolved to a URI reference.

        :return: Returns the underlying value if it is a Literal, otherwise returns the URIRef representation of the underlying value.

        :rtype: URIRef
        """

        if isinstance(self.value, Literal):
            return self.value
        return self.value.to_uriref()

    def is_double(self) -> bool:
        """
        Checks if the literal represents a double-precision floating-point number according to the XML Schema Definition (XSD). It verifies the datatype of the underlying value, handling both standard RDF literals and OWL typed literals by comparing their datatype identifiers to the XSD double IRI. The method returns False if the value is not one of these types or if the datatype does not match, and it does not modify the object's state.

        :return: True if the value is typed as an XSD double, False otherwise.

        :rtype: bool
        """

        if isinstance(self.value, Literal):
            return self.value.datatype == XSD.double
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == XSD.double
        return False

    def is_float(self) -> bool:
        """
        Determines whether the literal is explicitly typed as an XSD float by inspecting the datatype of the underlying value. This check supports both standard `Literal` and `OWLTypedLiteral` representations, returning True only if the datatype corresponds to `XSD.float`. If the value is not one of these types or has a different datatype, the method returns False.

        :return: True if the value is a Literal or OWLTypedLiteral with the datatype XSD.float, False otherwise.

        :rtype: bool
        """

        if isinstance(self.value, Literal):
            return self.value.datatype == XSD.float
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == XSD.float
        return False

    def is_decimal(self) -> bool:
        """
        Determines whether the current literal represents a decimal value based on its XML Schema Definition (XSD) datatype. This method inspects the underlying value object, supporting both standard `Literal` and `OWLTypedLiteral` instances, and verifies if the datatype corresponds specifically to `XSD.decimal`. It returns `True` only if the datatype matches the XSD decimal type; otherwise, it returns `False`, handling cases where the value is of a different type or lacks a matching datatype.

        :return: True if the value is typed as an XSD decimal, False otherwise.

        :rtype: bool
        """

        if isinstance(self.value, Literal):
            return self.value.datatype == XSD.decimal
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == XSD.decimal
        return False

    def is_real(self) -> bool:
        """
        Determines whether the current literal represents a real number by verifying its datatype against the OWL real specification. This method inspects the internal value object, supporting both standard `Literal` and `OWLTypedLiteral` instances; for the former, it directly compares the datatype, while for the latter, it resolves the datatype's IRI. If the underlying value is not one of these recognized types or does not correspond to the OWL real datatype, the method returns False. This operation is read-only and does not modify the object's state.

        :return: True if the value is a real number literal, False otherwise.

        :rtype: bool
        """

        if isinstance(self.value, Literal):
            return self.value.datatype == OWL.real
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == OWL.real
        return False

    def is_rational(self) -> bool:
        """
        Determines whether the current literal represents a rational number by inspecting its underlying datatype. This method accommodates different internal representations of the value, checking both standard `Literal` and `OWLTypedLiteral` instances to see if their datatype corresponds to the OWL rational IRI. It returns `True` if the datatype matches the specific rational type, and `False` for all other datatypes or if the value is not a recognized literal type.

        :return: True if the value is an OWL rational literal, False otherwise.

        :rtype: bool
        """

        if isinstance(self.value, Literal):
            return self.value.datatype == OWL.rational
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == OWL.rational
        return False

    def is_integer(self) -> bool:
        """
        Checks if the current literal represents an integer value based on its XML Schema datatype. This method evaluates the datatype of the underlying value, supporting both `Literal` and `OWLTypedLiteral` representations. It returns `True` if the datatype is one of the standard XSD integer types, including `xsd:integer`, `xsd:int`, `xsd:long`, `xsd:short`, `xsd:byte`, and their signed or unsigned variants. If the value is not a typed literal or the datatype falls outside the integer category, the method returns `False`.

        :return: True if the value is a Literal or OWLTypedLiteral with an XML Schema integer datatype, otherwise False.

        :rtype: bool
        """

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
        """
        Determines whether the current literal represents a boolean value by inspecting the datatype of its underlying value. This method checks if the datatype corresponds to the XML Schema Definition (XSD) boolean type, handling both standard RDFLib literals and specific OWL typed literals by comparing their datatype URIs. If the internal value is not one of these recognized types or does not possess the boolean datatype, the method returns False.

        :return: True if the value is a boolean literal (XSD boolean), False otherwise.

        :rtype: bool
        """

        if isinstance(self.value, Literal):
            return self.value.datatype == XSD.boolean
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == XSD.boolean
        return False

    def is_string(self) -> bool:
        """
        Determines if the underlying value represents a string datatype by inspecting its specific type identifier. The method handles both standard `Literal` and `OWLTypedLiteral` instances, extracting the datatype IRI to compare against a predefined set of string-compatible types. It returns `True` if the datatype is `XSD.string`, `XSD.normalizedString`, `RDF.langString`, `RDF.PlainLiteral`, or `RDF.CompoundLiteral`, and `False` otherwise, including cases where the value is not a recognized literal type.

        :return: True if the value is a literal with a string datatype (e.g., XSD.string, RDF.langString), otherwise False.

        :rtype: bool
        """

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
        """
        Determines whether the underlying value of this literal represents a date or time-related entity by inspecting its datatype. This method handles both standard RDF Literals and OWLTypedLiterals, extracting the specific datatype IRI to perform the check. It returns True if the datatype matches one of the specific XML Schema (XSD) temporal types, such as date, dateTime, dateTimeStamp, or dayTimeDuration, and returns False for any other datatype or value type.

        :return: True if the value's datatype is a date or time type (XSD date, dateTime, dateTimeStamp, or dayTimeDuration), False otherwise.

        :rtype: bool
        """

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
        """
        Determines whether the current literal represents a value of the XML Schema `anyURI` datatype. This method inspects the underlying value object, handling both standard `Literal` instances and `OWLTypedLiteral` instances by comparing their datatypes against the `XSD.anyURI` constant. It returns `True` if the datatype matches, and `False` for all other cases, including when the internal value is of an unsupported type.

        :return: True if the value is typed as an XSD anyURI, False otherwise.

        :rtype: bool
        """

        if isinstance(self.value, Literal):
            return self.value.datatype == XSD.anyURI
        elif isinstance(self.value, OWLTypedLiteral):
            return self.value.datatype.iri.to_uriref() == XSD.anyURI
        return False

    def __str__(self) -> str:
        """
        Returns a string representation of the literal by delegating to the string conversion of its underlying value attribute. This method is invoked implicitly by the `str()` built-in function and print operations, providing a human-readable format of the literal's content. The output depends entirely on the string representation of the stored value.

        :return: The string representation of the object's value.

        :rtype: str
        """

        return str(self.value)
