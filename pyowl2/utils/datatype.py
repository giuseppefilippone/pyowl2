import typing

from rdflib import Literal

from pyowl2.abstracts.axiom import OWLAxiom
from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.abstracts.object import OWLObject
from pyowl2.axioms.class_axiom.equivalent_classes import OWLEquivalentClasses
from pyowl2.axioms.datatype_definition import OWLDatatypeDefinition
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.datatype import OWLDatatype
from pyowl2.base.iri import IRI
from pyowl2.data_range.data_complement_of import OWLDataComplementOf
from pyowl2.data_range.data_intersection_of import OWLDataIntersectionOf
from pyowl2.data_range.data_one_of import OWLDataOneOf
from pyowl2.data_range.data_union_of import OWLDataUnionOf
from pyowl2.data_range.datatype_restriction import OWLDatatypeRestriction, OWLFacet
from pyowl2.literal.literal import OWLLiteral


class OWLFullDataRange(OWLObject):
    """
    This class provides a structured representation of a data range in an OWL ontology, encapsulating the core datatype definition along with its associated logical axioms and metadata annotations. It functions as a builder object, allowing users to define complex data range expressions—such as intersections, unions, complements, and facet-based restrictions—through a fluent interface that generates and stores the necessary OWL axioms. By separating the identity of the data range from its logical constraints, it facilitates the programmatic construction of rich datatype definitions while automatically managing the internal list of axioms to prevent duplicates.

    :param data_range: The core OWLDataRange instance holding the fundamental definition and IRI of the data range, which acts as the foundation for associated axioms and restrictions.
    :type data_range: OWLDataRange
    :param axioms: Stores the axioms defining the logical structure and relationships of the data range, including intersections, unions, complements, and restrictions.
    :type axioms: list[OWLAxiom]
    :param annotations: Stores the optional list of annotations associated with the data range, providing metadata such as source or intended use.
    :type annotations: typing.Optional[list[OWLAnnotation]]

    :raises TypeError: Raised when the `value` argument is a list containing mixed types (e.g., both `OWLDataRange` and `OWLFullDataRange` instances) or invalid types.
    """

    def __init__(self, iri: IRI) -> None:
        """
        Initializes a new instance representing a data range in the OWL 2 Full profile, using the provided Internationalized Resource Identifier (IRI) as its unique identity. The constructor instantiates an internal OWLDatatype object based on this IRI, effectively defining the semantic type of the data range. Additionally, it prepares the instance by initializing internal collections to hold axioms and annotations associated with this data range, ensuring the object is ready for integration into an ontology structure.

        :param iri: The Internationalized Resource Identifier that uniquely identifies the data range within the ontology.
        :type iri: IRI
        """

        self._data_range: OWLDataRange = OWLDatatype(iri)
        self._axioms: list[OWLAxiom] = []
        self._annotations: typing.Optional[list[OWLAnnotation]] = None

    @property
    def data_range(self) -> OWLDataRange:
        """
        Returns the `OWLDataRange` object associated with this `OWLFullDataRange` instance. This property provides direct access to the underlying data range definition, which specifies the set of literal values or data types represented in the ontology. Since this is a read-only property, it does not modify the internal state of the object.

        :return: The OWL data range associated with this object.

        :rtype: OWLDataRange
        """

        return self._data_range

    @property
    def axioms(self) -> list[OWLAxiom]:
        """
        Retrieves the list of axioms associated with this OWL Full data range. This property provides direct access to the internal collection of `OWLAxiom` objects that define the logical constraints or characteristics of the data range. As a simple getter, it returns the stored list without performing any computation or modifying the object's state.

        :return: The list of axioms associated with this object.

        :rtype: list[OWLAxiom]
        """

        return self._axioms

    @property
    def annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        """
        Updates the collection of annotations associated with this OWL full data range by replacing the existing list with the provided value. The input should be a list of OWLAnnotation objects or None, where None effectively clears the stored annotations. This setter modifies the object's internal state directly.

        :param value: The list of OWL annotations to set, or None to clear existing annotations.
        :type value: typing.Optional[list[OWLAnnotation]]
        """

        return self._annotations

    @annotations.setter
    def annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
        self._annotations = value

    @property
    def intersections(self) -> list[OWLDataIntersectionOf]:
        """
        Retrieves a list of axioms that define this data range as an intersection of other data ranges by filtering the internal collection for instances of `OWLDataIntersectionOf`. This property provides a way to access complex data range expressions where the current range is a component of an intersection. The operation is read-only and returns an empty list if no matching axioms are found.

        :return: A list of axioms representing the intersection of data ranges associated with this data range.

        :rtype: list[OWLDataIntersectionOf]
        """

        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLDataIntersectionOf)
        ]

    @property
    def unions(self) -> list[OWLDataUnionOf]:
        """
        Retrieves a list of `OWLDataUnionOf` axioms associated with this data range by filtering the internal collection of axioms for instances of the union type. This property provides access to complex data range expressions where the current range is defined as a union of other data ranges. The returned list is a new list object generated at call time, and modifying it will not affect the internal state of the data range; if no union axioms are associated, an empty list is returned.

        :return: A list of axioms defining this data range as a union of other data ranges.

        :rtype: list[OWLDataUnionOf]
        """

        return [axiom for axiom in self.axioms if isinstance(axiom, OWLDataUnionOf)]

    @property
    def ones_of(self) -> list[OWLDataOneOf]:
        """
        Retrieves a list of `OWLDataOneOf` axioms associated with this data range by filtering the internal collection of axioms for instances of that specific type. Each returned axiom represents a data enumeration, defining a range that consists exclusively of a specified set of literal values. This property performs a read-only operation and returns an empty list if no such enumeration axioms are present.

        :return: A list of `OWLDataOneOf` axioms associated with this data range, representing enumerations of specific data values.

        :rtype: list[OWLDataOneOf]
        """

        return [axiom for axiom in self.axioms if isinstance(axiom, OWLDataOneOf)]

    @property
    def restrictions(self) -> list[OWLDatatypeRestriction]:
        """
        This property retrieves a list of datatype restrictions associated with this data range by filtering the internal collection of axioms for instances of `OWLDatatypeRestriction`. These restrictions represent specific constraints, such as minimum or maximum values, applied to the underlying datatype to form complex data range expressions. The returned list is a new list object; modifying it will not alter the state of the data range, and an empty list is returned if no matching restrictions are found.

        :return: A list of OWLDatatypeRestriction axioms associated with this data range, representing constraints or facets applied to the datatype.

        :rtype: list[OWLDatatypeRestriction]
        """

        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLDatatypeRestriction)
        ]

    @property
    def is_complement(self) -> bool:
        """
        Indicates whether this data range is defined as the logical complement of another data range within the ontology. This property evaluates the axioms associated with the entity to determine if it represents a negation of another range, returning True if an `OWLDataComplementOf` axiom is present. The check is performed by iterating over the entity's axioms, and it returns False if no such defining complement axiom exists.

        :return: True if this data range is defined as a complement of another data range, False otherwise.

        :rtype: bool
        """

        return any(isinstance(axiom, OWLDataComplementOf) for axiom in self.axioms)

    def is_intersection_of(
        self, data_ranges: typing.Union[list[OWLDataRange], list[typing.Self]]
    ) -> None:
        """
        Asserts that the current data range is equivalent to the intersection of itself and a provided list of other data ranges by constructing and registering an `OWLDataIntersectionOf` axiom. The method accepts a list of data ranges, which can be either base `OWLDataRange` objects or `OWLFullDataRange` instances, and normalizes them to extract the underlying data ranges for the intersection. It modifies the object's internal state by appending the new axiom to its `axioms` list, but only if the specific axiom does not already exist, ensuring that duplicate definitions are not added.

        :param data_ranges: A list of data ranges to intersect with the current data range. Elements may be OWLDataRange instances or instances of the current class, from which the underlying data range is extracted.
        :type data_ranges: typing.Union[list[OWLDataRange], list[typing.Self]]
        """

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
        """
        Asserts that this data range is equivalent to the union of itself and a provided list of other data ranges by constructing and registering an OWLDataUnionOf axiom. The method accepts a list containing either standard OWLDataRange instances or OWLFullDataRange instances; in the latter case, the underlying data range of each instance is extracted to form the union. This operation is idempotent, meaning that if an identical union axiom already exists within the object's axioms, no duplicate is added. As a side effect, the newly created axiom is appended to the internal list of axioms associated with this data range.

        :param data_ranges: A list of data ranges that constitute the union together with the current instance. Elements may be OWLDataRange objects or instances of the current class.
        :type data_ranges: typing.Union[list[OWLDataRange], list[typing.Self]]
        """

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
        """
        Restricts the data range to a specific enumeration of values by asserting equivalence to an `OWLDataOneOf` axiom. The method accepts a list of literals, which may be either `OWLLiteral` instances or RDF `Literal` instances. If the provided list consists entirely of RDF `Literal` objects, they are passed directly to the axiom constructor; otherwise, the underlying values are extracted from the `OWLLiteral` objects. This operation modifies the data range by adding an equivalence axiom, effectively defining a closed set of allowed values.

        :param literals: A list of literal values to enumerate as the valid set for this data range, accepting either OWLLiteral or rdflib Literal instances.
        :type literals: typing.Union[list[OWLLiteral], list[Literal]]
        """

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
        """Adds an OWLDataComplementOf axiom to the internal collection of axioms for this data range. The method constructs a complement object representing the logical negation of the current data range and appends it, provided that an identical axiom does not already exist. This ensures idempotency by preventing duplicate entries, and the method modifies the object's state without returning a value."""

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
        """
        Asserts that the current data range is semantically equivalent to one or more other data ranges by generating an `OWLEquivalentClasses` axiom. The method accepts either a single data range or a list of data ranges, which may be provided as `OWLDataRange` objects or `OWLFullDataRange` instances. If a list is supplied, all elements must be of the same consistent type; otherwise, a `TypeError` is raised. To prevent redundancy, the method verifies whether the generated axiom already exists within the instance's internal axiom collection and, if so, skips the addition. The primary side effect is the modification of the internal `axioms` list by appending the newly created equivalence relationship.

        :param value: A single data range or a list of data ranges to be asserted as equivalent to this data range.
        :type value: typing.Union[OWLDataRange, typing.Self, list[OWLDataRange], list[typing.Self]]

        :raises TypeError: Raised when the provided value is a list containing elements of inconsistent types, specifically if the list is not composed entirely of OWLDataRange instances or entirely of OWLFullDataRange instances.
        """

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
        """
        Asserts that this data range is equivalent to the complement of the provided data range by adding an appropriate equivalence axiom to the ontology. The method accepts either an `OWLDataRange` instance or another `OWLFullDataRange` instance, extracting the underlying data range from the latter if necessary. This establishes a semantic relationship where this range encompasses all values that are not members of the specified other range. The operation is idempotent, ensuring that the axiom is not added redundantly if it already exists within the entity's axioms.

        :param other: The data range that this data range is asserted to be the complement of. Can be an OWLDataRange or an instance of the current class.
        :type other: typing.Union[OWLDataRange, typing.Self]
        """

        self.is_equivalent_to(
            OWLDataComplementOf(
                other if isinstance(other, OWLDataRange) else other.data_range
            )
        )

    def define(self, datatype: OWLDatatype) -> None:
        """
        This method creates and adds an `OWLDatatypeDefinition` axiom to the current data range, asserting that the range is semantically defined by the specified `OWLDatatype`. This association links a custom data range, such as "Age", to a concrete underlying type, such as "Integer", thereby defining the set of valid values for the range within the ontology. The method ensures idempotency by checking the existing axioms; if the specific definition is already present, no duplicate is added. As a side effect, the new axiom is appended to the internal list of axioms associated with this data range.

        :param datatype: The datatype that defines this data range, asserting that the range consists of values belonging to the specified datatype.
        :type datatype: OWLDatatype
        """

        element = OWLDatatypeDefinition(self.data_range, datatype)
        if element in self.axioms:
            return
        self.axioms.append(element)

    def restrict(self, datatype: OWLDatatype, facets: list[OWLFacet]) -> None:
        """
        Adds a datatype restriction axiom to the current data range, constraining its values to a specific datatype and a set of facet restrictions. The method constructs an `OWLDatatypeRestriction` using the provided datatype and facets, then appends it to the internal list of axioms. If an identical restriction already exists within the axioms, the method performs no action to prevent duplication.

        :param datatype: The base OWL datatype being restricted, defining the underlying type of values that are further constrained by the provided facets.
        :type datatype: OWLDatatype
        :param facets: A list of OWLFacet instances specifying the constraints applied to the datatype to define the valid values for this data range.
        :type facets: list[OWLFacet]
        """

        element = self.define(OWLDatatypeRestriction(datatype, facets))
        if element in self.axioms:
            return
        self.axioms.append(element)
