pyowl2.utils.individual
=======================

.. py:module:: pyowl2.utils.individual



.. ── LLM-GENERATED DESCRIPTION START ──

Provides a structured representation of an OWL individual that aggregates and manages logical axioms, property assertions, and identity conditions.


Description
-----------


The software implements a comprehensive wrapper for entities within the Web Ontology Language (OWL), designed to encapsulate both the identity of an individual and the logical axioms that define its characteristics. By supporting both named and anonymous entities, it allows for the flexible construction of ontology members that are identified either by Internationalized Resource Identifiers (IRIs) or unique node identifiers. Internally, the logic maintains a collection of axioms that describe class memberships, object and data property relationships, and identity conditions such as sameness or difference. The design ensures data integrity by preventing duplicate entries when new assertions are added, while also providing mechanisms to attach metadata annotations for richer semantic context. Through a fluent interface, users can programmatically define complex relationships and attributes, effectively building a detailed graph of knowledge assertions centered around a specific entity.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.utils.individual.OWLFullIndividual


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_utils_individual_OWLFullIndividual.png
       :alt: UML Class Diagram for OWLFullIndividual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFullIndividual**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_utils_individual_OWLFullIndividual.pdf
       :alt: UML Class Diagram for OWLFullIndividual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFullIndividual**

.. py:class:: OWLFullIndividual(iri: Union[pyowl2.base.iri.IRI, rdflib.URIRef], is_anonymous: bool = False)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`

   .. autoapi-inheritance-diagram:: pyowl2.utils.individual.OWLFullIndividual
      :parts: 1
      :private-bases:


   This class acts as a structured wrapper for an entity within an OWL ontology, combining the individual's core identity with a collection of logical axioms and optional metadata annotations. It supports the creation of both named individuals, identified by an Internationalized Resource Identifier (IRI), and anonymous individuals, which are identified by unique node identifiers. Through its methods, users can define the individual's properties by adding class assertions, object property assertions to establish relationships with other entities, and data property assertions to assign literal values. The class also facilitates the management of identity conditions, allowing for assertions that the individual is the same as or different from others. Internally, it maintains a list of axioms, automatically preventing duplicate entries, and provides properties to filter and retrieve specific types of assertions, such as class memberships or equivalence relationships.

   :param individual: The underlying OWL individual (named or anonymous) that acts as the subject for all axioms and assertions managed by this class.
   :type individual: typing.Any
   :param axioms: A list of axioms associated with the individual, encompassing class assertions, property assertions, and identity axioms that define its characteristics and relationships within the ontology.
   :type axioms: list[OWLAxiom]
   :param annotations: Stores an optional list of annotations that provide additional metadata or context about the individual, such as source information or confidence levels.
   :type annotations: typing.Optional[list[OWLAnnotation]]


   .. py:method:: add_assertion(cls: pyowl2.abstracts.class_expression.OWLClassExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Asserts that the individual is an instance of the specified OWL class expression by creating and storing a corresponding class assertion axiom. This method accepts an optional list of annotations to attach metadata to the assertion. If an identical assertion already exists within the individual's axioms, the operation is skipped to prevent duplicates; otherwise, the new axiom is appended to the internal list of axioms.

      :param annotations: Optional list of annotations to attach to the class assertion axiom, providing additional metadata or context.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: add_data_property_assertion(data_property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, value: pyowl2.literal.literal.OWLLiteral, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Creates and registers a data property assertion axiom that associates the current individual with a specific literal value through the provided data property expression. This method constructs the assertion using the specified property, value, and any optional annotations intended to provide contextual metadata. It enforces idempotency by verifying whether the generated assertion already exists within the individual's internal axiom collection; if a duplicate is found, the operation is aborted. Otherwise, the new assertion is appended to the collection, thereby modifying the individual's state within the ontology.

      :param data_property: The data property expression defining the relationship between the individual and the literal value.
      :type data_property: OWLDataPropertyExpression
      :param value: The literal value that the individual is asserted to have for the specified data property.
      :type value: OWLLiteral
      :param annotations: Optional list of annotations to attach to the assertion axiom, providing additional metadata or context.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: add_negative_data_property_assertion(data_property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, value: pyowl2.literal.literal.OWLLiteral, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Constructs a negative data property assertion axiom stating that this individual does not have the specified literal value for the given data property and adds it to the individual's axiom set. The method accepts an optional list of annotations to provide additional context or metadata for the assertion. If an identical axiom already exists within the individual's axioms, the method performs no action to prevent duplication.

      :param data_property: The data property expression for which the individual is asserted not to have the specified value.
      :type data_property: OWLDataPropertyExpression
      :param value: The literal value that the individual is asserted not to have for the specified data property.
      :type value: OWLLiteral
      :param annotations: Additional metadata to attach to the negative data property assertion.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: add_negative_object_property_assertion(object_property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, target_individual: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Constructs an OWLNegativeObjectPropertyAssertion axiom asserting that this individual is not connected to the target individual via the specified object property and adds it to the individual's internal axiom collection. The method supports optional annotations to provide additional context or metadata for the assertion. It ensures idempotency by verifying that an identical axiom does not already exist within the individual's axioms before performing the addition.

      :param object_property: The object property expression representing the relationship that is asserted not to hold between this individual and the target individual.
      :type object_property: OWLObjectPropertyExpression
      :param target_individual: The individual that this individual is asserted not to be related to via the specified object property.
      :type target_individual: OWLIndividual
      :param annotations: Optional list of annotations providing additional metadata or context for the assertion, such as provenance or confidence levels.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: add_object_property_assertion(object_property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, target_individual: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      This method adds an object property assertion to the individual, establishing a relationship with a target individual via the specified object property expression. It constructs an `OWLObjectPropertyAssertion` axiom, optionally attaching a list of annotations to provide metadata such as provenance or confidence. The method ensures idempotency by checking the existing axioms; if the specific assertion is already present, it is not added again. Otherwise, the new assertion is appended to the individual's internal collection of axioms, modifying the instance's state.

      :param object_property: The object property expression representing the relationship to be asserted between this individual and the target individual.
      :type object_property: OWLObjectPropertyExpression
      :param target_individual: The individual instance that is the object of the assertion, representing the entity related to the subject individual via the object property.
      :type target_individual: OWLIndividual
      :param annotations: Optional list of annotations to attach to the assertion, providing additional metadata or context.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: is_different_from(individuals: Union[pyowl2.abstracts.individual.OWLIndividual, list[pyowl2.abstracts.individual.OWLIndividual], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Asserts that the current individual is distinct from one or more other individuals by generating an `OWLDifferentIndividuals` axiom. The method accepts either a single individual or a list of individuals, supporting both `OWLIndividual` and `OWLFullIndividual` types, and optionally associates metadata annotations with the assertion. It ensures idempotency by checking the existing axioms list and only appending the new axiom if it is not already present. In cases where the input types are invalid or inconsistent, such as a mixed list of different individual types, the method returns a `TypeError` object rather than raising an exception.

      :param individuals: A single individual or a list of individuals that are asserted to be distinct from the current instance.
      :type individuals: typing.Union[OWLIndividual, list[OWLIndividual], typing.Self, list[typing.Self]]
      :param annotations: Optional list of annotations to attach to the generated `OWLDifferentIndividuals` axiom.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: is_one_of(individuals: list[pyowl2.abstracts.individual.OWLIndividual]) -> None

      Creates an OWLObjectOneOf axiom that includes the current individual and the provided list of individuals, and adds it to the individual's axioms. This method ensures idempotency by verifying that the specific axiom does not already exist in the individual's axiom collection before appending it. The primary side effect is the modification of the individual's internal state to reflect this new assertion.

      :param individuals: A list of individuals to be included in the enumeration alongside the current individual.
      :type individuals: list[OWLIndividual]



   .. py:method:: is_same_as(individuals: Union[pyowl2.abstracts.individual.OWLIndividual, list[pyowl2.abstracts.individual.OWLIndividual], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

      Asserts that the current individual is identical to one or more specified individuals by creating and registering an `OWLSameIndividual` axiom. The method accepts either a single individual or a list of individuals, supporting both `OWLIndividual` and `OWLFullIndividual` instances (unwrapping the latter to their underlying representation). Optional annotations can be attached to the axiom to provide metadata. The operation is idempotent; if an equivalent axiom already exists within the individual's internal axiom set, it will not be added again. If the input types are inconsistent or invalid (e.g., a mixed list), the method returns a `TypeError` object rather than raising an exception.

      :param individuals: A single individual or a list of individuals to be asserted as identical to the current instance. Can be provided as `OWLIndividual` or `OWLFullIndividual` instances.
      :type individuals: typing.Union[OWLIndividual, list[OWLIndividual], typing.Self, list[typing.Self]]
      :param annotations: Optional list of annotations providing metadata for the sameness assertion.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:attribute:: _annotations
      :type:  Optional[list[pyowl2.base.annotation.OWLAnnotation]]
      :value: None



   .. py:attribute:: _axioms
      :type:  list[pyowl2.abstracts.axiom.OWLAxiom]
      :value: []



   .. py:attribute:: _individual


   .. py:property:: annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]


      Updates the collection of annotations associated with this OWLFullIndividual instance. This setter accepts a list of OWLAnnotation objects or None, which replaces the current value stored in the internal `_annotations` attribute. Because the assignment is direct, passing a list object establishes a reference to that specific list rather than creating a copy, potentially allowing external modifications to affect the instance's state.

      :param value: The list of OWL annotations to set, or None to clear the existing annotations.
      :type value: typing.Optional[list[OWLAnnotation]]


   .. py:property:: assertions
      :type: list[pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]


      Retrieves a list of class assertion axioms associated with the individual by filtering the general set of axioms for instances of `OWLClassAssertion`. These axioms explicitly define the specific classes that the individual instantiates within the ontology. The operation is read-only and returns a new list; if the individual has no associated class assertions, an empty list is returned.

      :return: A list of OWL class assertion axioms representing the classes that this individual is an instance of.

      :rtype: list[OWLClassAssertion]


   .. py:property:: axioms
      :type: list[pyowl2.abstracts.axiom.OWLAxiom]


      Returns the list of OWL axioms associated with this individual. This property provides direct access to the internal storage of axioms; therefore, modifications to the returned list will directly alter the state of the object. If no axioms are currently associated, an empty list is returned.

      :return: Returns the list of OWL axioms contained in this object.

      :rtype: list[OWLAxiom]


   .. py:property:: class_assertions
      :type: list[pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]


      This property provides access to the set of axioms that assert the individual's membership in specific classes. It filters the individual's associated axioms to return only those that are instances of OWLClassAssertion, effectively identifying the types this individual instantiates. The returned list is a new collection generated from the internal axioms; if no class assertions exist, an empty list is returned. Accessing this property does not modify the state of the individual or its axioms.

      :return: A list of axioms representing the classes that this individual is an instance of.

      :rtype: list[OWLClassAssertion]


   .. py:property:: different_individuals
      :type: list[pyowl2.axioms.assertion.different_individuals.OWLDifferentIndividuals]


      This property retrieves a list of axioms that explicitly assert this individual is distinct from other individuals within the ontology. It filters the individual's internal collection of axioms to return only those of type `OWLDifferentIndividuals`, which may include associated annotations. The operation is read-only and returns an empty list if no such differentiation axioms are defined for this entity.

      :return: A list of axioms asserting that this individual is distinct from other individuals.

      :rtype: list[OWLDifferentIndividuals]


   .. py:property:: individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Retrieves the underlying `OWLIndividual` object encapsulated by this `OWLFullIndividual` instance. This property provides direct access to the internal representation of the individual, allowing interaction with the specific ontology entity that the current object wraps. The method returns the reference stored in the private attribute without performing any computation or modification.

      :return: The OWL individual associated with this object.

      :rtype: OWLIndividual


   .. py:property:: one_of
      :type: list[pyowl2.class_expression.object_one_of.OWLObjectOneOf]


      Retrieves a list of `OWLObjectOneOf` axioms associated with this individual by filtering the internal axiom collection. These axioms represent class expressions defined by the explicit enumeration of individuals, potentially including associated annotations. The operation is read-only and returns an empty list if no matching axioms are found.

      :return: A list of OWLObjectOneOf axioms associated with this individual, representing class expressions defined by the explicit enumeration of individuals.

      :rtype: list[OWLObjectOneOf]


   .. py:property:: same_individuals
      :type: list[pyowl2.axioms.assertion.same_individual.OWLSameIndividual]


      This property retrieves a list of axioms that explicitly assert this individual is the same as other individuals within the ontology. It filters the individual's associated axioms to return only instances of `OWLSameIndividual`, capturing any annotations attached to those equivalence statements. The method performs a read-only operation with no side effects and returns an empty list if no same-individual assertions are present.

      :return: A list of axioms asserting that this individual is the same as other individuals.

      :rtype: list[OWLSameIndividual]

