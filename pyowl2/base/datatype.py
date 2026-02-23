import typing

from rdflib import OWL, RDF, XSD, Namespace, URIRef

from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.abstracts.entity import OWLEntity
from pyowl2.base.iri import IRI


class OWLDatatype(OWLEntity, OWLDataRange):
    """
    This entity represents a specific category of data values within an ontology, such as integers, strings, or dates, effectively defining a set of permissible values. It is uniquely identified by an Internationalized Resource Identifier (IRI), which links the datatype to standard definitions like those found in the XML Schema (XSD) or OWL namespaces. Users can instantiate this class with an IRI to define custom or standard datatypes, and utilize the provided helper methods to verify if the instance corresponds to common numeric, boolean, string, or date types. As a subclass of `OWLEntity` and `OWLDataRange`, it serves as a fundamental building block for typing data properties and literals in semantic web applications.

    :parm iri: Stores the unique Internationalized Resource Identifier (IRI) that identifies the datatype. This value determines the specific nature of the data range (e.g., integer, string) and is used for unambiguous reference within the ontology.
    :type iri: typing.Union[IRI, URIRef]
    """

    def __init__(self, iri: typing.Union[IRI, URIRef]) -> None:
        """
        Initializes a new instance representing an OWL datatype identified by the specified Internationalized Resource Identifier (IRI). The constructor accepts either a custom IRI object or a URIRef, storing the provided value in a private attribute to serve as the unique identifier for this datatype. This method does not perform any validation or side effects beyond assigning the identifier to the instance.

        :param iri: The IRI or URI reference identifying the resource.
        :type iri: typing.Union[IRI, URIRef]
        """

        self._iri: typing.Union[IRI, URIRef] = iri

    @property
    def iri(self) -> typing.Union[IRI, URIRef]:
        """
        Sets the Internationalized Resource Identifier (IRI) for this OWL datatype instance. The method accepts either an IRI or a URIRef object as the new identifier value. This operation directly updates the internal state of the object, effectively changing the semantic identity of the datatype to the specified URI.

        :param value: The IRI or URI reference to assign to the object.
        :type value: typing.Union[IRI, URIRef]
        """

        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[IRI, URIRef]) -> None:
        self._iri = value

    def to_uriref(self) -> URIRef:
        """
        Returns the underlying RDF resource identifier as a URIRef object. If the internal identifier is currently stored as an IRI instance, the method delegates to that object's conversion logic; otherwise, it returns the identifier directly. This operation is stateless and does not modify the datatype instance.

        :return: The URIRef representation of the IRI, or the value itself if it is already a URIRef.

        :rtype: URIRef
        """

        return self.iri.to_uriref() if isinstance(self.iri, IRI) else self.iri

    def is_double(self) -> bool:
        """
        Checks if the current datatype represents the XML Schema Definition (XSD) double type. This method performs a strict equality check between the datatype's Internationalized Resource Identifier (IRI) and the standard IRI associated with the `xsd:double` namespace. It returns `True` if the identifiers match, indicating that the datatype is a double, and `False` otherwise.

        :return: True if the IRI corresponds to the XSD double datatype, False otherwise.

        :rtype: bool
        """

        return self.iri == IRI(Namespace(XSD._NS), XSD.double)

    def is_float(self) -> bool:
        """
        Checks if the current datatype corresponds to the XML Schema Definition (XSD) float type by comparing its Internationalized Resource Identifier (IRI) against the standard IRI for `xsd:float`. The method returns `True` only if the IRI matches exactly, indicating a 32-bit floating-point number, and returns `False` for any other datatype, including other numeric types like `xsd:double` or `xsd:decimal`. This operation is a pure comparison and has no side effects.

        :return: True if the IRI corresponds to the XSD float datatype.

        :rtype: bool
        """

        return self.iri == IRI(Namespace(XSD._NS), XSD.float)

    def is_decimal(self) -> bool:
        """
        Checks if the current datatype instance represents the standard XML Schema Definition (XSD) decimal type. This determination is made by comparing the datatype's Internationalized Resource Identifier (IRI) against the canonical IRI for `xsd:decimal`. The method returns `True` if the IRIs match, indicating the datatype is a decimal, and `False` otherwise.

        :return: True if the IRI represents the XML Schema decimal datatype, False otherwise.

        :rtype: bool
        """

        return str(self.iri) == str(IRI(Namespace(XSD._NS), XSD.decimal))

    def is_real(self) -> bool:
        """
        Determines if the current datatype represents the specific OWL datatype for real numbers. This is achieved by comparing the Internationalized Resource Identifier (IRI) of the instance against the canonical IRI for `owl:real` within the OWL namespace. The method returns `True` if the IRIs match, indicating the datatype is a real number, and `False` otherwise.

        :return: True if the object's IRI matches the OWL 'real' IRI, False otherwise.

        :rtype: bool
        """

        return str(self.iri) == str(IRI(Namespace(OWL._NS), OWL.real))

    def is_rational(self) -> bool:
        """
        Checks if the current datatype instance represents the OWL rational datatype. This is determined by comparing the instance's Internationalized Resource Identifier (IRI) against the canonical IRI for `owl:rational` defined in the OWL namespace. The method returns `True` if the IRIs match, indicating the datatype is specifically a rational number type, and `False` for any other datatype.

        :return: True if the object's IRI matches the OWL rational IRI, False otherwise.

        :rtype: bool
        """

        return str(self.iri) == str(IRI(Namespace(OWL._NS), OWL.rational))

    def is_integer(self) -> bool:
        """
        Determines whether the current datatype corresponds to an XML Schema Definition (XSD) integer type. This check is performed by comparing the datatype's IRI against a comprehensive list of numeric IRIs, including `xsd:integer`, `xsd:int`, `xsd:long`, `xsd:short`, `xsd:byte`, and their signed or unsigned variants (such as `xsd:nonNegativeInteger` or `xsd:unsignedLong`). The method returns `True` if a match is found, indicating the datatype is an integer, and `False` otherwise.

        :return: True if the IRI corresponds to an XSD integer datatype, otherwise False.

        :rtype: bool
        """

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
        """
        Determines whether the current OWL datatype corresponds to the XML Schema Definition (XSD) boolean datatype. This check is performed by comparing the datatype's Internationalized Resource Identifier (IRI) against the standard IRI for `xsd:boolean`. The method returns `True` if the IRIs match, indicating the datatype is the built-in boolean type, and `False` otherwise. This operation does not modify the state of the object.

        :return: True if the IRI corresponds to the XSD boolean datatype, otherwise False.

        :rtype: bool
        """

        return str(self.iri) == str(IRI(Namespace(XSD._NS), XSD.boolean))

    def is_string(self) -> bool:
        """
        Checks if the current datatype corresponds to a string-based data type within the RDF and OWL specifications. This determination is made by verifying whether the datatype's IRI matches a specific set of recognized string IRIs, including `xsd:string`, `xsd:normalizedString`, `rdf:langString`, `rdf:PlainLiteral`, and `rdf:CompoundLiteral`. The method returns `True` if the IRI is found within this set, indicating that the datatype is designed to represent textual content, and `False` otherwise. This check relies entirely on the IRI identifier and does not modify the state of the object.

        :return: True if the IRI corresponds to a string datatype (e.g., XSD string, normalizedString, or RDF langString), otherwise False.

        :rtype: bool
        """

        return str(self.iri) in (
            str(IRI(Namespace(XSD._NS), XSD.string)),
            str(IRI(Namespace(XSD._NS), XSD.normalizedString)),
            str(IRI(Namespace(RDF._NS), RDF.langString)),
            str(IRI(Namespace(RDF._NS), RDF.PlainLiteral)),
            str(IRI(Namespace(RDF._NS), RDF.CompoundLiteral)),
        )

    def is_date(self) -> bool:
        """
        Determines whether the current OWL datatype corresponds to specific XML Schema Definition (XSD) temporal types. This method checks the datatype's Internationalized Resource Identifier (IRI) and returns True if it matches `xsd:date`, `xsd:dateTime`, `xsd:dateTimeStamp`, or `xsd:dayTimeDuration`. It is a read-only check with no side effects, returning False for any other datatype IRI.

        :return: True if the IRI corresponds to an XSD date, dateTime, dateTimeStamp, or dayTimeDuration datatype; otherwise, False.

        :rtype: bool
        """

        return str(self.iri) in (
            str(IRI(Namespace(XSD._NS), XSD.date)),
            str(IRI(Namespace(XSD._NS), XSD.dateTime)),
            str(IRI(Namespace(XSD._NS), XSD.dateTimeStamp)),
            str(IRI(Namespace(XSD._NS), XSD.dayTimeDuration)),
        )

    def is_anyuri(self) -> bool:
        """
        Determines whether this OWL datatype corresponds to the XML Schema Definition (XSD) datatype `anyURI`. The method performs a strict string comparison between the IRI of the current datatype instance and the canonical IRI for `xsd:anyURI`. It returns `True` if the IRIs match, indicating that the datatype represents a URI reference, and `False` otherwise. This operation has no side effects and does not modify the state of the object.

        :return: True if the IRI corresponds to the XSD anyURI datatype, False otherwise.

        :rtype: bool
        """

        return str(self.iri) == str(IRI(Namespace(XSD._NS), XSD.anyURI))

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the OWL datatype instance. The output is formatted by wrapping the datatype's internal IRI (Internationalized Resource Identifier) within the text "Datatype(...)". This representation is primarily intended for debugging and logging, providing a concise summary of the datatype's identity.

        :return: A string representation of the datatype, including its IRI.

        :rtype: str
        """

        return f"Datatype({self._iri})"
