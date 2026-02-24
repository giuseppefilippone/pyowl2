import typing

from rdflib import URIRef

from pyowl2.abstracts.axiom import OWLAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.abstracts.object import OWLObject
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.axioms.assertion.class_assertion import OWLClassAssertion
from pyowl2.axioms.assertion.data_property_assertion import OWLDataPropertyAssertion
from pyowl2.axioms.assertion.different_individuals import OWLDifferentIndividuals
from pyowl2.axioms.assertion.negative_data_property_assertion import (
    OWLNegativeDataPropertyAssertion,
)
from pyowl2.axioms.assertion.negative_object_property_assertion import (
    OWLNegativeObjectPropertyAssertion,
)
from pyowl2.axioms.assertion.object_property_assertion import OWLObjectPropertyAssertion
from pyowl2.axioms.assertion.same_individual import OWLSameIndividual
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.iri import IRI
from pyowl2.class_expression.object_one_of import OWLObjectOneOf
from pyowl2.individual.anonymous_individual import OWLAnonymousIndividual
from pyowl2.individual.named_individual import OWLNamedIndividual
from pyowl2.literal.literal import OWLLiteral


class OWLFullIndividual(OWLObject):
    """
    This class acts as a structured wrapper for an entity within an OWL ontology, combining the individual's core identity with a collection of logical axioms and optional metadata annotations. It supports the creation of both named individuals, identified by an Internationalized Resource Identifier (IRI), and anonymous individuals, which are identified by unique node identifiers. Through its methods, users can define the individual's properties by adding class assertions, object property assertions to establish relationships with other entities, and data property assertions to assign literal values. The class also facilitates the management of identity conditions, allowing for assertions that the individual is the same as or different from others. Internally, it maintains a list of axioms, automatically preventing duplicate entries, and provides properties to filter and retrieve specific types of assertions, such as class memberships or equivalence relationships.

    :param individual: The underlying OWL individual (named or anonymous) that acts as the subject for all axioms and assertions managed by this class.
    :type individual: typing.Any
    :param axioms: A list of axioms associated with the individual, encompassing class assertions, property assertions, and identity axioms that define its characteristics and relationships within the ontology.
    :type axioms: list[OWLAxiom]
    :param annotations: Stores an optional list of annotations that provide additional metadata or context about the individual, such as source information or confidence levels.
    :type annotations: typing.Optional[list[OWLAnnotation]]
    """

    def __init__(
        self, iri: typing.Union[IRI, URIRef], is_anonymous: bool = False
    ) -> None:
        """
        Constructs an OWL individual entity identified by the specified IRI, determining its internal representation based on the provided anonymity flag. If the `is_anonymous` flag is set to False, the individual is instantiated as a named entity using the provided IRI directly; if set to True, it is created as an anonymous individual with a unique identifier derived from that IRI. As a side effect of initialization, the method sets up internal storage for associated axioms and annotations, initializing the axiom list as empty and the annotation list as None.

        :param iri: The Internationalized Resource Identifier (IRI) or URI reference that uniquely identifies the individual. It serves as the primary identifier for the entity within the ontology, used to reference it in axioms and assertions, or to derive a unique identifier for anonymous individuals.
        :type iri: typing.Union[IRI, URIRef]
        :param is_anonymous: Determines if the individual is anonymous. If True, an `OWLAnonymousIndividual` is created with a derived identifier; if False (default), an `OWLNamedIndividual` is created using the provided IRI.
        :type is_anonymous: bool
        """

        self._individual = (
            OWLNamedIndividual(iri) if not is_anonymous else OWLAnonymousIndividual(iri)
        )
        self._axioms: list[OWLAxiom] = []
        self._annotations: typing.Optional[list[OWLAnnotation]] = None

    @property
    def axioms(self) -> list[OWLAxiom]:
        """
        Returns the list of OWL axioms associated with this individual. This property provides direct access to the internal storage of axioms; therefore, modifications to the returned list will directly alter the state of the object. If no axioms are currently associated, an empty list is returned.

        :return: Returns the list of OWL axioms contained in this object.

        :rtype: list[OWLAxiom]
        """

        return self._axioms

    @property
    def annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        """
        Updates the collection of annotations associated with this OWLFullIndividual instance. This setter accepts a list of OWLAnnotation objects or None, which replaces the current value stored in the internal `_annotations` attribute. Because the assignment is direct, passing a list object establishes a reference to that specific list rather than creating a copy, potentially allowing external modifications to affect the instance's state.

        :param value: The list of OWL annotations to set, or None to clear the existing annotations.
        :type value: typing.Optional[list[OWLAnnotation]]
        """

        return self._annotations

    @annotations.setter
    def annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
        self._annotations = value

    @property
    def individual(self) -> OWLIndividual:
        """
        Retrieves the underlying `OWLIndividual` object encapsulated by this `OWLFullIndividual` instance. This property provides direct access to the internal representation of the individual, allowing interaction with the specific ontology entity that the current object wraps. The method returns the reference stored in the private attribute without performing any computation or modification.

        :return: The OWL individual associated with this object.

        :rtype: OWLIndividual
        """

        return self._individual

    @property
    def assertions(self) -> list[OWLClassAssertion]:
        """
        Retrieves a list of class assertion axioms associated with the individual by filtering the general set of axioms for instances of `OWLClassAssertion`. These axioms explicitly define the specific classes that the individual instantiates within the ontology. The operation is read-only and returns a new list; if the individual has no associated class assertions, an empty list is returned.

        :return: A list of OWL class assertion axioms representing the classes that this individual is an instance of.

        :rtype: list[OWLClassAssertion]
        """

        return [axiom for axiom in self.axioms if isinstance(axiom, OWLClassAssertion)]

    @property
    def same_individuals(self) -> list[OWLSameIndividual]:
        """
        This property retrieves a list of axioms that explicitly assert this individual is the same as other individuals within the ontology. It filters the individual's associated axioms to return only instances of `OWLSameIndividual`, capturing any annotations attached to those equivalence statements. The method performs a read-only operation with no side effects and returns an empty list if no same-individual assertions are present.

        :return: A list of axioms asserting that this individual is the same as other individuals.

        :rtype: list[OWLSameIndividual]
        """

        return [axiom for axiom in self.axioms if isinstance(axiom, OWLSameIndividual)]

    @property
    def different_individuals(self) -> list[OWLDifferentIndividuals]:
        """
        This property retrieves a list of axioms that explicitly assert this individual is distinct from other individuals within the ontology. It filters the individual's internal collection of axioms to return only those of type `OWLDifferentIndividuals`, which may include associated annotations. The operation is read-only and returns an empty list if no such differentiation axioms are defined for this entity.

        :return: A list of axioms asserting that this individual is distinct from other individuals.

        :rtype: list[OWLDifferentIndividuals]
        """

        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLDifferentIndividuals)
        ]

    @property
    def class_assertions(self) -> list[OWLClassAssertion]:
        """
        This property provides access to the set of axioms that assert the individual's membership in specific classes. It filters the individual's associated axioms to return only those that are instances of OWLClassAssertion, effectively identifying the types this individual instantiates. The returned list is a new collection generated from the internal axioms; if no class assertions exist, an empty list is returned. Accessing this property does not modify the state of the individual or its axioms.

        :return: A list of axioms representing the classes that this individual is an instance of.

        :rtype: list[OWLClassAssertion]
        """

        return [axiom for axiom in self.axioms if isinstance(axiom, OWLClassAssertion)]

    @property
    def one_of(self) -> list[OWLObjectOneOf]:
        """
        Retrieves a list of `OWLObjectOneOf` axioms associated with this individual by filtering the internal axiom collection. These axioms represent class expressions defined by the explicit enumeration of individuals, potentially including associated annotations. The operation is read-only and returns an empty list if no matching axioms are found.

        :return: A list of OWLObjectOneOf axioms associated with this individual, representing class expressions defined by the explicit enumeration of individuals.

        :rtype: list[OWLObjectOneOf]
        """

        return [axiom for axiom in self.axioms if isinstance(axiom, OWLObjectOneOf)]

    def is_different_from(
        self,
        individuals: typing.Union[
            OWLIndividual, list[OWLIndividual], typing.Self, list[typing.Self]
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Asserts that the current individual is distinct from one or more other individuals by generating an `OWLDifferentIndividuals` axiom. The method accepts either a single individual or a list of individuals, supporting both `OWLIndividual` and `OWLFullIndividual` types, and optionally associates metadata annotations with the assertion. It ensures idempotency by checking the existing axioms list and only appending the new axiom if it is not already present. In cases where the input types are invalid or inconsistent, such as a mixed list of different individual types, the method returns a `TypeError` object rather than raising an exception.

        :param individuals: A single individual or a list of individuals that are asserted to be distinct from the current instance.
        :type individuals: typing.Union[OWLIndividual, list[OWLIndividual], typing.Self, list[typing.Self]]
        :param annotations: Optional list of annotations to attach to the generated `OWLDifferentIndividuals` axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        new_individuals: list[OWLIndividual] = [self.individual]
        if isinstance(individuals, list):
            if all(isinstance(i, OWLIndividual) for i in individuals):
                new_individuals.extend(individuals)
            elif all(isinstance(i, OWLFullIndividual) for i in individuals):
                new_individuals.extend([i.individual for i in individuals])
            else:
                return TypeError
        else:
            if isinstance(individuals, OWLIndividual):
                new_individuals.append(individuals)
            elif isinstance(individuals, OWLFullIndividual):
                new_individuals.append(individuals.individual)
            else:
                return TypeError

        different_from = OWLDifferentIndividuals(
            new_individuals,
            annotations,
        )
        if different_from in self.axioms:
            return
        self.axioms.append(different_from)

    def is_same_as(
        self,
        individuals: typing.Union[
            OWLIndividual, list[OWLIndividual], typing.Self, list[typing.Self]
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ):
        """
        Asserts that the current individual is identical to one or more specified individuals by creating and registering an `OWLSameIndividual` axiom. The method accepts either a single individual or a list of individuals, supporting both `OWLIndividual` and `OWLFullIndividual` instances (unwrapping the latter to their underlying representation). Optional annotations can be attached to the axiom to provide metadata. The operation is idempotent; if an equivalent axiom already exists within the individual's internal axiom set, it will not be added again. If the input types are inconsistent or invalid (e.g., a mixed list), the method returns a `TypeError` object rather than raising an exception.

        :param individuals: A single individual or a list of individuals to be asserted as identical to the current instance. Can be provided as `OWLIndividual` or `OWLFullIndividual` instances.
        :type individuals: typing.Union[OWLIndividual, list[OWLIndividual], typing.Self, list[typing.Self]]
        :param annotations: Optional list of annotations providing metadata for the sameness assertion.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        new_individuals: list[OWLIndividual] = [self.individual]
        if isinstance(individuals, list):
            if all(isinstance(i, OWLIndividual) for i in individuals):
                new_individuals.extend(individuals)
            elif all(isinstance(i, OWLFullIndividual) for i in individuals):
                new_individuals.extend([i.individual for i in individuals])
            else:
                return TypeError
        else:
            if isinstance(individuals, OWLIndividual):
                new_individuals.append(individuals)
            elif isinstance(individuals, OWLFullIndividual):
                new_individuals.append(individuals.individual)
            else:
                return TypeError

        same_as = OWLSameIndividual(
            new_individuals,
            annotations,
        )
        if same_as in self.axioms:
            return
        self.axioms.append(same_as)

    def add_assertion(
        self,
        cls: OWLClassExpression,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Asserts that the individual is an instance of the specified OWL class expression by creating and storing a corresponding class assertion axiom. This method accepts an optional list of annotations to attach metadata to the assertion. If an identical assertion already exists within the individual's axioms, the operation is skipped to prevent duplicates; otherwise, the new axiom is appended to the internal list of axioms.

        :param annotations: Optional list of annotations to attach to the class assertion axiom, providing additional metadata or context.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        assertion = OWLClassAssertion(cls, self.individual, annotations)
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def add_object_property_assertion(
        self,
        object_property: OWLObjectPropertyExpression,
        target_individual: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        This method adds an object property assertion to the individual, establishing a relationship with a target individual via the specified object property expression. It constructs an `OWLObjectPropertyAssertion` axiom, optionally attaching a list of annotations to provide metadata such as provenance or confidence. The method ensures idempotency by checking the existing axioms; if the specific assertion is already present, it is not added again. Otherwise, the new assertion is appended to the individual's internal collection of axioms, modifying the instance's state.

        :param object_property: The object property expression representing the relationship to be asserted between this individual and the target individual.
        :type object_property: OWLObjectPropertyExpression
        :param target_individual: The individual instance that is the object of the assertion, representing the entity related to the subject individual via the object property.
        :type target_individual: OWLIndividual
        :param annotations: Optional list of annotations to attach to the assertion, providing additional metadata or context.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        assertion = OWLObjectPropertyAssertion(
            object_property, self.individual, target_individual, annotations
        )
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def add_negative_object_property_assertion(
        self,
        object_property: OWLObjectPropertyExpression,
        target_individual: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Constructs an OWLNegativeObjectPropertyAssertion axiom asserting that this individual is not connected to the target individual via the specified object property and adds it to the individual's internal axiom collection. The method supports optional annotations to provide additional context or metadata for the assertion. It ensures idempotency by verifying that an identical axiom does not already exist within the individual's axioms before performing the addition.

        :param object_property: The object property expression representing the relationship that is asserted not to hold between this individual and the target individual.
        :type object_property: OWLObjectPropertyExpression
        :param target_individual: The individual that this individual is asserted not to be related to via the specified object property.
        :type target_individual: OWLIndividual
        :param annotations: Optional list of annotations providing additional metadata or context for the assertion, such as provenance or confidence levels.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        assertion = OWLNegativeObjectPropertyAssertion(
            object_property, self.individual, target_individual, annotations
        )
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def add_data_property_assertion(
        self,
        data_property: OWLDataPropertyExpression,
        value: OWLLiteral,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Creates and registers a data property assertion axiom that associates the current individual with a specific literal value through the provided data property expression. This method constructs the assertion using the specified property, value, and any optional annotations intended to provide contextual metadata. It enforces idempotency by verifying whether the generated assertion already exists within the individual's internal axiom collection; if a duplicate is found, the operation is aborted. Otherwise, the new assertion is appended to the collection, thereby modifying the individual's state within the ontology.

        :param data_property: The data property expression defining the relationship between the individual and the literal value.
        :type data_property: OWLDataPropertyExpression
        :param value: The literal value that the individual is asserted to have for the specified data property.
        :type value: OWLLiteral
        :param annotations: Optional list of annotations to attach to the assertion axiom, providing additional metadata or context.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        assertion = OWLDataPropertyAssertion(
            data_property, self.individual, value, annotations
        )
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def add_negative_data_property_assertion(
        self,
        data_property: OWLDataPropertyExpression,
        value: OWLLiteral,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Constructs a negative data property assertion axiom stating that this individual does not have the specified literal value for the given data property and adds it to the individual's axiom set. The method accepts an optional list of annotations to provide additional context or metadata for the assertion. If an identical axiom already exists within the individual's axioms, the method performs no action to prevent duplication.

        :param data_property: The data property expression for which the individual is asserted not to have the specified value.
        :type data_property: OWLDataPropertyExpression
        :param value: The literal value that the individual is asserted not to have for the specified data property.
        :type value: OWLLiteral
        :param annotations: Additional metadata to attach to the negative data property assertion.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        assertion = OWLNegativeDataPropertyAssertion(
            data_property, self.individual, value, annotations
        )
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def is_one_of(self, individuals: list[OWLIndividual]) -> None:
        """
        Creates an OWLObjectOneOf axiom that includes the current individual and the provided list of individuals, and adds it to the individual's axioms. This method ensures idempotency by verifying that the specific axiom does not already exist in the individual's axiom collection before appending it. The primary side effect is the modification of the individual's internal state to reflect this new assertion.

        :param individuals: A list of individuals to be included in the enumeration alongside the current individual.
        :type individuals: list[OWLIndividual]
        """

        one_of = OWLObjectOneOf([self.individual] + individuals)
        if one_of in self.axioms:
            return
        self.axioms.append(one_of)
