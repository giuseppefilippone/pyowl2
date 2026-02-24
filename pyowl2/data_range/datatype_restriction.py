import enum
import typing

from rdflib import XSD, URIRef

from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.base.datatype import OWLDatatype
from pyowl2.base.iri import IRI
from pyowl2.literal.literal import OWLLiteral


class OWLFacetTypes(enum.StrEnum):
    """
    This enumeration defines the standard set of constraints, known as facets, used to restrict datatypes in OWL ontologies. It provides specific constants for defining value boundaries, distinguishing between minimum and maximum limits that are either inclusive or exclusive. These types are utilized when constructing data ranges to enforce precise logical constraints on literal values, such as ensuring a number falls within a specific interval. By using this enumeration, developers can reliably specify the exact nature of a datatype restriction within the ontology model.

    :param MIN_INCLUSIVE: Represents the constraint that a data value must be greater than or equal to a specified lower bound.
    :type MIN_INCLUSIVE: typing.Any
    :param MIN_EXCLUSIVE: Restricts the data range to values strictly greater than a specified lower bound.
    :type MIN_EXCLUSIVE: typing.Any
    :param MAX_INCLUSIVE: Represents a constraint that restricts values to be less than or equal to a specified upper bound.
    :type MAX_INCLUSIVE: typing.Any
    :param MAX_EXCLUSIVE: Represents a restriction requiring the value to be strictly less than a specified upper bound.
    :type MAX_EXCLUSIVE: typing.Any
    """

    MIN_INCLUSIVE = enum.auto()
    MIN_EXCLUSIVE = enum.auto()
    MAX_INCLUSIVE = enum.auto()
    MAX_EXCLUSIVE = enum.auto()


class OWLFacet:
    """
    Represents a specific constraint applied to a datatype within an OWL ontology, serving to define precise data ranges by pairing a restriction type with a literal value. To use this entity, instantiate it with a constraint type—referenced by a URIRef or IRI—and an OWLLiteral representing the specific bound, such as a minimum or maximum value. The constructor validates that the provided constraint corresponds to a recognized OWL facet type, raising an error if the restriction is invalid. Furthermore, the implementation supports standard comparison and hashing operations based on the string representation of the facet, allowing for easy integration into sets and sorted collections.

    :param valid_restrictions: A whitelist of URI references defining the supported facet types (e.g., minInclusive, maxExclusive) used to validate constraints during instance initialization.
    :type valid_restrictions: list[URIRef]
    :param MIN_INCLUSIVE: URI reference representing the "minInclusive" facet, which restricts a datatype to values greater than or equal to a specified lower bound.
    :type MIN_INCLUSIVE: URIRef
    :param MIN_EXCLUSIVE: Represents the "minExclusive" facet type, indicating that values must be strictly greater than a specified lower bound.
    :type MIN_EXCLUSIVE: URIRef
    :param MAX_INCLUSIVE: URI reference for the "maxInclusive" facet, indicating that values for the associated datatype must be less than or equal to a specified upper bound.
    :type MAX_INCLUSIVE: URIRef
    :param MAX_EXCLUSIVE: A URI reference representing the "maxExclusive" facet, which restricts datatype values to be strictly less than a specified upper bound.
    :type MAX_EXCLUSIVE: URIRef
    :param constraint: The specific type of restriction applied to the datatype, identified by a URI reference or IRI. It defines the nature of the constraint (e.g., minimum or maximum value) and is restricted to valid OWL facet types.
    :type constraint: typing.Union[URIRef, IRI]
    :param value: The specific literal value defining the boundary or limit for the datatype restriction.
    :type value: OWLLiteral
    """

    # OWL facet types as defined in the OWL 2 specification, represented as URI references.
    valid_restrictions: list[URIRef] = [
        XSD.minExclusive,
        XSD.minInclusive,
        XSD.maxExclusive,
        XSD.maxInclusive,
    ]

    # OWL facet types as defined in the OWL 2 specification, represented as URI references.
    MIN_INCLUSIVE: URIRef = XSD.minInclusive
    MIN_EXCLUSIVE: URIRef = XSD.minExclusive
    MAX_INCLUSIVE: URIRef = XSD.maxInclusive
    MAX_EXCLUSIVE: URIRef = XSD.maxExclusive

    def __init__(
        self, constraint: typing.Union[URIRef, IRI], value: OWLLiteral
    ) -> None:
        """
        Constructs an OWLFacet instance, representing a specific type of constraint applied to a data range within the OWL 2 specification. The method accepts a constraint identifier, provided as either a URIRef or IRI, and a literal value that defines the boundary of the restriction. It performs a validation step to ensure the constraint corresponds to a valid OWL facet restriction, raising an assertion error if the identifier is not recognized. Upon successful validation, the constraint and value are stored internally as private attributes.

        :param constraint: The URI or IRI identifying the specific OWL facet restriction applied to the literal value, which must be a valid restriction defined in the OWL specification.
        :type constraint: typing.Union[URIRef, IRI]
        :param value: The OWL literal value associated with the facet restriction.
        :type value: OWLLiteral
        """

        if isinstance(constraint, IRI):
            assert constraint.to_uriref() in OWLFacet.valid_restrictions
        elif isinstance(constraint, URIRef):
            assert constraint in OWLFacet.valid_restrictions
        self._constraint: typing.Union[URIRef, IRI] = constraint
        self._value: OWLLiteral = value

    @property
    def constraint(self) -> typing.Union[URIRef, IRI]:
        """
        Sets the constraint property of the OWL facet to the specified value. The value must be a URI reference or IRI that identifies the specific facet constraint. This method updates the internal state of the instance by assigning the provided value to the underlying `_constraint` attribute.

        :param value: The URI or IRI representing the constraint to be set.
        :type value: typing.Union[URIRef, IRI]
        """

        return self._constraint

    @constraint.setter
    def constraint(self, value: typing.Union[URIRef, IRI]) -> None:
        self._constraint = value

    @property
    def value(self) -> OWLLiteral:
        """
        Sets the literal constraint value associated with this OWL facet. It accepts an OWLLiteral object and updates the internal state of the facet to reflect the new restriction. This operation mutates the current instance, overwriting any previously defined value for this facet.

        :param value: The OWL literal value to assign.
        :type value: OWLLiteral
        """

        return self._value

    @value.setter
    def value(self, value: OWLLiteral) -> None:
        self._value = value

    def constraint_to_uriref(self) -> URIRef:
        """
        Returns the constraint associated with the OWL facet as a URIRef object. If the constraint is currently represented as an IRI instance, the method converts it by calling its `to_uriref` method. Otherwise, the constraint is returned directly, assuming it is already a URIRef or compatible type. This method does not modify the state of the object.

        :return: The constraint represented as a URIRef, converting it from an IRI if necessary.

        :rtype: URIRef
        """

        return (
            self.constraint.to_uriref()
            if isinstance(self.constraint, IRI)
            else self.constraint
        )

    def __eq__(self, value: object) -> bool:
        """
        Checks if the current instance is equal to the provided object by comparing their string representations. The method converts both the `OWLFacet` instance and the input value to strings and returns `True` if these strings are identical. This implementation allows for equality checks against objects of varying types, provided their string outputs match exactly.

        :param value: The object to compare against. Equality is determined by comparing the string representations of the two objects.
        :type value: object

        :return: True if the string representation of the current instance is equal to the string representation of the specified value, otherwise False.

        :rtype: bool
        """

        return str(self) == str(value)

    def __ne__(self, value: object) -> bool:
        """
        Determines whether the current instance is not equal to the specified object by comparing their string representations. The method converts both the `OWLFacet` instance and the provided value to strings using the built-in `str()` function and returns `True` if the resulting strings differ. This implementation implies that inequality is based solely on the textual output of the objects, meaning that two distinct objects with identical string representations will be considered equal.

        :param value: The object to compare against the current instance.
        :type value: object

        :return: True if the string representation of the instance is not equal to the string representation of the provided value, False otherwise.

        :rtype: bool
        """

        return str(self) != str(value)

    def __lt__(self, value: object) -> bool:
        """
        Determines if the current instance is considered less than the provided value based on their string representations. This method enables the use of the less-than operator (`<`) for `OWLFacet` objects, allowing them to be sorted or compared within sequences. The comparison is performed by converting both the instance and the argument to strings using the built-in `str()` function and evaluating the resulting strings lexicographically. It returns `True` if the string representation of the current instance precedes that of the value, and `False` otherwise.

        :param value: The object to compare against, which is converted to a string for the comparison.
        :type value: object

        :return: True if the string representation of the instance is lexicographically less than the string representation of the provided value.

        :rtype: bool
        """

        return str(self) < str(value)

    def __le__(self, value: object) -> bool:
        """
        Determines if the current instance is less than or equal to a specified value by comparing their string representations. The method converts both the instance and the provided value to strings and performs a standard lexicographical comparison, returning the result. This allows `OWLFacet` objects to be sorted or compared using the `<=` operator, even against objects of different types, provided they can be converted to strings, without modifying the state of either object.

        :param value: The object to compare against. The comparison is performed using the string representation of the provided object.
        :type value: object

        :return: True if the string representation of the current object is less than or equal to the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) <= str(value)

    def __gt__(self, value: object) -> bool:
        """
        Determines whether the current instance is considered greater than the provided value by comparing their string representations. The comparison is performed lexicographically after converting both the instance and the argument to strings. This method enables sorting and ordering operations, relying on the string output rather than the internal structure of the objects.

        :param value: The object to compare against the current instance.
        :type value: object

        :return: True if the string representation of the object is greater than the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) > str(value)

    def __ge__(self, value: object) -> bool:
        """
        Determines whether the current instance is greater than or equal to the specified value by comparing their string representations. This method converts both the object and the provided argument to strings and performs a standard lexicographical comparison, returning True if the string representation of the current instance is greater than or equal to that of the value.

        :param value: The object to compare against.
        :type value: object

        :return: True if the string representation of the current object is greater than or equal to the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) >= str(value)

    def __hash__(self) -> int:
        """
        Computes the hash value for the OWL facet instance by hashing its string representation. This allows the object to be used as a key in dictionaries or as a member of sets, assuming that the string representation remains stable for the lifetime of the instance. The method delegates the calculation to the built-in hash function applied to the result of `str(self)`.

        :return: An integer representing the hash value of the object, derived from its string representation.

        :rtype: int
        """

        return hash(str(self))

    def __repr__(self) -> str:
        """
        Returns the official string representation of the OWLFacet instance. This method delegates directly to the __str__ method, ensuring that the representation used for debugging and logging is identical to the informal string representation. The resulting string provides a human-readable description of the facet.

        :return: Returns the string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Provides a human-readable string representation of the OWL facet, primarily intended for display or debugging purposes. The returned string follows the format "Facet(constraint value)", incorporating the specific constraint type and the value associated with the facet. This method has no side effects on the object's state.

        :return: A string representation of the object in the format 'Facet(constraint value)'.

        :rtype: str
        """

        return f"Facet({self.constraint} {self.value})"


class OWLDatatypeRestriction(OWLDataRange):
    """
    Represents a constrained data range within an ontology that narrows the value space of a base datatype through the application of specific facet restrictions. This class is utilized to define precise data characteristics, such as limiting integers to a specific interval or strings to a maximum length, by associating a parent `OWLDatatype` with a collection of `OWLFacet` constraints. Upon instantiation, the provided list of restrictions must contain at least one facet, and the class automatically sorts these facets to maintain a canonical internal order. It serves as a specialized `OWLDataRange` that allows for the granular definition of data property domains in semantic web applications.

    :param datatype: The base datatype that serves as the foundation for the restriction, to which the specific facet constraints are applied.
    :type datatype: OWLDatatype
    :param restrictions: A sorted list of facets defining the constraints applied to the base datatype.
    :type restrictions: list[OWLFacet]
    """

    def __init__(self, datatype: OWLDatatype, restrictions: list[OWLFacet]) -> None:
        """
        Initializes a restriction of a specific OWL datatype by applying a set of facet constraints. This constructor requires a base datatype and a non-empty list of facet restrictions, such as minimum or maximum values. A side effect of the initialization is that the provided list of restrictions is sorted internally to ensure a consistent, canonical representation. If an empty list of restrictions is passed, an assertion error is raised.

        :param datatype: The base OWL datatype to which the facet restrictions are applied.
        :type datatype: OWLDatatype
        :param restrictions: A non-empty list of facets defining the constraints on the datatype.
        :type restrictions: list[OWLFacet]
        """

        super().__init__()
        assert len(restrictions) >= 1
        self._datatype: OWLDatatype = datatype
        self._restrictions: list[OWLFacet] = sorted(restrictions)

    @property
    def datatype(self) -> OWLDatatype:
        """
        Updates the OWL datatype associated with this restriction by assigning a new value to the internal state. This setter accepts an instance of `OWLDatatype` and replaces the existing datatype reference, effectively changing the base type upon which the restriction's facets are applied. The operation modifies the object in place and does not return a value.

        :param value: The OWL datatype to assign to the object.
        :type value: OWLDatatype
        """

        return self._datatype

    @datatype.setter
    def datatype(self, value: OWLDatatype) -> None:
        """Setter for datatype."""
        self._datatype = value

    @property
    def restrictions(self) -> list[OWLFacet]:
        """
        Updates the collection of facet constraints applied to the datatype restriction by assigning the provided list of OWLFacet objects. The input list is sorted before being stored in the internal state, ensuring a canonical order for the restrictions. This operation overwrites any previously defined facets.

        :param value: The list of OWL facets to assign as restrictions. The list will be sorted before storage.
        :type value: list[OWLFacet]
        """

        return self._restrictions

    @restrictions.setter
    def restrictions(self, value: list[OWLFacet]) -> None:
        """Setter for facets."""
        self._restrictions = sorted(value)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the OWL datatype restriction, encapsulating the specific datatype and the set of facet restrictions applied to it. The output format places the datatype identifier followed by a space-separated list of the restriction conditions within parentheses, prefixed by 'DatatypeRestriction'. This method is side-effect free and serves primarily to facilitate debugging and logging by providing a concise textual summary of the object's internal state.

        :return: A string representation of the restriction, displaying the datatype and the list of applied restrictions.

        :rtype: str
        """

        return f"DatatypeRestriction({self.datatype} {' '.join(map(str, self.restrictions))})"
