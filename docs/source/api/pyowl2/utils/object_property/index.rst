pyowl2.utils.object_property
============================

.. py:module:: pyowl2.utils.object_property



.. ── LLM-GENERATED DESCRIPTION START ──

Provides a comprehensive interface for defining and manipulating OWL object properties, including their logical characteristics, domain and range constraints, and associated axioms.


Description
-----------


A high-level abstraction wraps a core property entity identified by an Internationalized Resource Identifier (IRI), aggregating its definition and logical rules into a single manageable object. It maintains an internal collection of axioms, enabling users to dynamically configure property characteristics such as symmetry, transitivity, and functionality through boolean flags that automatically update the underlying ontology structure. The design supports the creation of complex hierarchical relationships, such as sub-property and inverse property definitions, alongside class expression restrictions involving cardinality and value constraints. Furthermore, the software allows for the assertion of specific relationships between individuals, serving as a central hub for constructing and managing the complete logical profile of a relationship type.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.utils.object_property.OWLFullObjectProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_utils_object_property_OWLFullObjectProperty.png
       :alt: UML Class Diagram for OWLFullObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFullObjectProperty**

.. only:: latex

    .. figure:: /_uml/pyowl2_utils_object_property_OWLFullObjectProperty.pdf
       :alt: UML Class Diagram for OWLFullObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFullObjectProperty**

.. py:class:: OWLFullObjectProperty(iri: pyowl2.base.iri.IRI, domain: Optional[pyowl2.abstracts.class_expression.OWLClassExpression] = None, range: Optional[pyowl2.abstracts.class_expression.OWLClassExpression] = None, is_symmetric: bool = False, is_asymmetric: bool = False, is_functional: bool = False, is_inverse_functional: bool = False, is_transitive: bool = False, is_reflexive: bool = False, is_irreflexive: bool = False)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`

   .. autoapi-inheritance-diagram:: pyowl2.utils.object_property.OWLFullObjectProperty
      :parts: 1
      :private-bases:


   This class provides a structured abstraction for an object property in an OWL ontology, aggregating its definition, logical characteristics, and associated metadata. It encapsulates a core property entity identified by an IRI, allowing users to specify and modify its domain and range constraints. Beyond basic definition, it facilitates the management of property axioms, including characteristics like symmetry, transitivity, and functionality, as well as complex restrictions such as cardinality and value constraints. The class also supports the assertion of relationships between specific individuals and the definition of hierarchical or equivalent relationships with other properties, serving as a central hub for constructing and manipulating the logical rules governing a specific relationship type.

   :param PROPERTY_CLASSES: A collection of axiom types that define the specific characteristics of an object property, such as symmetry, transitivity, and functionality. This list is used to filter and identify axioms that describe the property's behavior.
   :type PROPERTY_CLASSES: list[type]
   :parm object_property: The underlying OWLObjectProperty instance representing the fundamental relationship entity in the ontology, serving as the central reference for all associated axioms and characteristics.
   :type object_property: OWLObjectProperty
   :parm domain: Internal representation of the domain axiom, defining the class of individuals that can be the subject of this object property.
   :type domain: OWLObjectPropertyDomain
   :parm range: Internal storage for the range axiom, defining the class or classes of individuals that can be the object of this property.
   :type range: OWLObjectPropertyRange
   :parm axioms: A list of axioms defining the object property's logical characteristics, relationships, restrictions, and assertions.
   :type axioms: list[OWLAxiom]
   :parm annotations: Stores an optional list of annotations that provide metadata, such as comments or labels, for the object property. These annotations serve to document the property without influencing its logical semantics.
   :type annotations: typing.Optional[list[OWLAnnotation]]


   .. py:method:: _del_property(curr_value: bool, value: bool, cls: type) -> None

      Manages the presence of a specific axiom type within the object's axioms list based on a state transition. By comparing the current boolean value with the desired value, the method either adds or removes an instance of the specified class. If the property is being enabled, it creates a new axiom using the object property and adds it to the list, avoiding duplicates; if the property is being disabled, it locates and removes the corresponding axiom. No modifications are made if the current and desired states are identical.

      :param curr_value: Indicates whether the property is currently active or set to True.
      :type curr_value: bool
      :param value: The desired state of the property, determining whether the corresponding axiom should be added or removed.
      :type value: bool



   .. py:method:: add_assertion(individual_1: pyowl2.abstracts.individual.OWLIndividual, individual_2: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Adds an object property assertion to the axioms of this property, establishing a directed relationship between two specified individuals. This method constructs an assertion linking the first individual to the second via the current object property, optionally associating a list of annotations to provide additional metadata. The operation is idempotent; it checks the existing axioms to prevent duplication, ensuring that the assertion is only appended if an identical entry is not already present.

      :param individual_1: The subject individual in the assertion, representing the entity that holds the object property relationship with the second individual.
      :type individual_1: OWLIndividual
      :param individual_2: The individual that serves as the target of the object property relationship.
      :type individual_2: OWLIndividual
      :param annotations: An optional list of annotations to associate with the object property assertion, providing additional metadata such as comments or labels.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: add_domain_annotations(annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None

      Associates a list of OWL annotations with the domain of this object property. If the property does not currently have a domain defined, the method exits without taking any action. When a domain exists, this method updates the domain's axiom annotations with the provided list, overwriting any previously associated annotations.

      :param annotations: Metadata, such as comments or labels, to associate with the domain axiom of this object property.
      :type annotations: list[OWLAnnotation]



   .. py:method:: add_negative_assertion(individual_1: pyowl2.abstracts.individual.OWLIndividual, individual_2: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Appends a negative object property assertion to the internal collection of axioms associated with this object property, formally declaring that the first individual does not relate to the second individual via this specific relationship. The method constructs the assertion using the provided individuals and an optional list of annotations for metadata. It ensures idempotency by verifying that the assertion does not already exist within the axioms before adding it, preventing duplicate entries.

      :param individual_1: The first individual in the negative assertion, representing the subject that is not related to the second individual via this object property.
      :type individual_1: OWLIndividual
      :param individual_2: The individual that is asserted not to be related to the first individual via this object property.
      :type individual_2: OWLIndividual
      :param annotations: Optional list of annotations to associate with the negative object property assertion, providing metadata such as comments or labels.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: add_property_annotations(property_class: pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom, annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None

      Attaches a list of annotations to the first object property axiom found that is an instance of the specified class. The method iterates through the entity's axioms and replaces the `axiom_annotations` attribute of the first matching axiom with the provided list. If no axiom matches the given class, the method performs no action. Note that due to an immediate return upon finding a match, only the first encountered axiom of the specified type is modified, leaving any subsequent matching axioms unchanged.

      :param property_class: The class of object property axioms to target for annotation. Must be a subclass of OWLObjectPropertyAxiom.
      :type property_class: OWLObjectPropertyAxiom
      :param annotations: A list of OWLAnnotation objects containing metadata, such as comments or labels, to be associated with the object property axiom.
      :type annotations: list[OWLAnnotation]



   .. py:method:: add_range_annotations(annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None

      Associates a list of OWL annotations with the range axiom of this object property, providing metadata such as comments or labels. This method directly assigns the provided list to the range's annotation property, thereby replacing any existing annotations that may have been present. If the object property does not have a defined range, the method takes no action.

      :param annotations: A list of annotations to associate with the range of this object property, providing metadata such as comments or labels.
      :type annotations: list[OWLAnnotation]



   .. py:method:: all(cls: pyowl2.abstracts.class_expression.OWLClassExpression) -> None

      Adds a universal restriction (all values from axiom) to the object property, asserting that every value associated with this property must satisfy the specified class expression. The method constructs an `OWLObjectAllValuesFrom` instance and appends it to the internal list of axioms, provided that an identical axiom does not already exist. This check ensures that duplicate axioms are not added, maintaining the integrity of the ontology definition.



   .. py:method:: del_assertion(assertion: Union[pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion, pyowl2.axioms.assertion.negative_object_property_assertion.OWLNegativeObjectPropertyAssertion]) -> None

      Removes a specified object property assertion or negative object property assertion from the internal list of axioms maintained by this object property. The method iterates through the existing axioms to find a match for the provided assertion; if found, it deletes that specific axiom from the collection and returns immediately. If the assertion is not present, the method performs no action and exits without raising an error, effectively leaving the object's state unchanged.

      :param assertion: The object property assertion or negative object property assertion to remove from the axioms.
      :type assertion: typing.Union[OWLObjectPropertyAssertion, OWLNegativeObjectPropertyAssertion]



   .. py:method:: exact_cardinality(cardinality: int, cls: pyowl2.abstracts.class_expression.OWLClassExpression) -> None

      This method constructs and adds an exact cardinality axiom to the internal collection of axioms for the object property, enforcing that there must be precisely a specific number of values satisfying a given class expression. It accepts a non-negative integer representing the required count and an OWL class expression defining the type of the values. The operation is idempotent; if an identical axiom already exists in the axioms list, the method performs no action, otherwise, it appends the new axiom to the collection.

      :param cardinality: The exact number of values for the object property that must satisfy the specified class expression. Must be a non-negative integer.
      :type cardinality: int



   .. py:method:: has_self() -> None

      Adds a 'has self' axiom to the collection of axioms associated with this object property, asserting that the property relates an individual to itself. The operation is idempotent; it verifies whether the specific axiom already exists within the internal axioms list and only appends it if it is absent. This ensures that duplicate axioms are not created.



   .. py:method:: has_value(individual: pyowl2.abstracts.individual.OWLIndividual) -> None

      Adds a "has value" axiom to the internal list of axioms associated with this object property, asserting that the property relates to a specific individual. The method constructs an `OWLObjectHasValue` restriction using the provided `OWLIndividual` and the current object property. It ensures idempotency by verifying that the axiom does not already exist within the axioms collection before appending it, preventing duplicate entries. This operation modifies the state of the object by updating its axioms list.

      :param individual: The specific individual instance that serves as the value for the object property restriction.
      :type individual: OWLIndividual



   .. py:method:: is_disjoint_from(properties: Union[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Asserts that this object property is disjoint from the specified properties by creating and adding a corresponding axiom to the object's internal collection. The method accepts a single property or a list of properties, supporting both raw `OWLObjectPropertyExpression` objects and `OWLFullObjectProperty` instances. Optional annotations may be provided to attach metadata to the axiom. The operation ensures idempotency by checking for the existence of an equivalent axiom before adding it; if the axiom is already present, the method returns without making changes. Input types are validated to ensure all provided properties are of a compatible type.

      :param properties: One or more properties to be asserted as disjoint from this instance.
      :type properties: typing.Union[OWLObjectPropertyExpression, list[OWLObjectPropertyExpression], typing.Self, list[typing.Self]]
      :param annotations: Optional list of annotations to associate with the disjoint properties axiom, providing metadata such as comments or labels.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: is_equivalent_to(properties: Union[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      This method adds an equivalent object properties axiom to the current object property, defining it as equivalent to the specified property or list of properties. It handles inputs that are either raw `OWLObjectPropertyExpression` objects or `OWLFullObjectProperty` instances, extracting the underlying property expressions as needed. Optional annotations can be supplied to attach metadata, such as comments or labels, to the axiom. The method ensures idempotency by checking if the resulting axiom already exists within the property's axioms; if it does, no action is taken. In cases where the input types are invalid, the method returns a TypeError object.

      :param properties: The object properties to which this property is equivalent. Accepts a single property or a list of properties, where each property can be an OWLObjectPropertyExpression or an instance of OWLFullObjectProperty.
      :type properties: typing.Union[OWLObjectPropertyExpression, list[OWLObjectPropertyExpression], typing.Self, list[typing.Self]]
      :param annotations: Optional list of annotations to associate with the equivalent properties axiom, providing metadata such as comments or labels.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: is_inverse_of(property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None

      Asserts that the current object property is the inverse of the provided property expression by appending a corresponding axiom to the internal collection. This operation defines a symmetric relationship in the ontology, meaning that if an individual `x` relates to `y` via this property, `y` must relate to `x` via the specified property. The method is idempotent; it checks for the existence of the specific inverse property axiom before adding it, ensuring that no duplicate axioms are created.

      :param property: The object property expression that is the inverse of this property.
      :type property: OWLObjectPropertyExpression



   .. py:method:: is_sub_property_of(super_property: Union[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, Self], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Establishes a subproperty relationship between this object property and the specified super property by constructing and adding a subproperty axiom to the internal axioms list. The method handles the super property argument flexibly, accepting either a raw object property expression or another `OWLFullObjectProperty` instance, from which it extracts the underlying property. If an identical axiom is already present in the axioms collection, the method performs no action, ensuring that duplicate relationships are not created. Optional annotations can be provided to attach metadata to the newly created axiom.

      :param super_property: The parent property in the subproperty relationship, indicating that this property is a specialization of the specified property.
      :type super_property: typing.Union[OWLObjectPropertyExpression, typing.Self]
      :param annotations: Optional list of annotations to attach to the subproperty axiom, providing metadata such as comments or labels.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: is_super_property_of(sub_property: Union[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, pyowl2.axioms.object_property_axiom.object_property_chain.OWLObjectPropertyChain, Self], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Adds a superproperty axiom to the internal list of axioms, declaring that the current object property is a superproperty of the provided sub-property. The sub-property argument can be an object property expression, a property chain, or another instance of the same class. An optional list of annotations may be provided to associate metadata with the axiom. The method performs a check to ensure that the exact axiom does not already exist in the axioms collection; if it is found, the method returns without making changes, preventing duplicate entries. If the axiom is new, it is appended to the collection.

      :param sub_property: The object property expression, property chain, or object property instance that is a subproperty of the current property.
      :type sub_property: typing.Union[OWLObjectPropertyExpression, OWLObjectPropertyChain, typing.Self]
      :param annotations: An optional list of annotations to associate with the superproperty axiom, providing metadata such as comments or labels.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: max_cardinality(cardinality: int, cls: pyowl2.abstracts.class_expression.OWLClassExpression) -> None

      Adds a maximum cardinality axiom to the object property, asserting that the number of distinct values linked by this property which satisfy the specified class expression must not exceed the given integer. This method constructs an `OWLObjectMaxCardinality` instance and appends it to the property's internal axiom list, ensuring that no duplicate axioms are added if an identical restriction already exists. The `cardinality` argument represents the non-negative upper bound for the count of qualifying values, while the `cls` argument defines the `OWLClassExpression` that these values must instantiate to be included in the count.

      :param cardinality: The non-negative integer defining the maximum number of distinct values for the object property that satisfy the class expression.
      :type cardinality: int



   .. py:method:: min_cardinality(cardinality: int, cls: pyowl2.abstracts.class_expression.OWLClassExpression) -> None

      Adds a minimum cardinality restriction to the axioms of this object property, asserting that there must be at least the specified number of distinct values satisfying the provided class expression. The method constructs an `OWLObjectMinCardinality` instance and appends it to the internal list of axioms only if an identical axiom does not already exist, thereby preventing duplicates. This operation modifies the internal state of the object property by updating its associated axiom collection.

      :param cardinality: The non-negative integer representing the minimum number of values for the object property that must satisfy the specified class expression.
      :type cardinality: int



   .. py:method:: some(cls: pyowl2.abstracts.class_expression.OWLClassExpression) -> None

      Adds an existential restriction, known as a "some values from" axiom, to the internal list of axioms associated with this object property. This method asserts that there exists at least one value for this property that satisfies the specified class expression. The operation is idempotent; if the specific axiom already exists within the axioms collection, it will not be added again, otherwise, the newly constructed axiom is appended to the list.



   .. py:attribute:: PROPERTY_CLASSES
      :type:  list[type]


   .. py:attribute:: _annotations
      :type:  Optional[list[pyowl2.base.annotation.OWLAnnotation]]
      :value: None



   .. py:attribute:: _axioms
      :type:  list[pyowl2.abstracts.axiom.OWLAxiom]
      :value: []



   .. py:attribute:: _domain
      :type:  pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain
      :value: None



   .. py:attribute:: _object_property
      :type:  pyowl2.expressions.object_property.OWLObjectProperty


   .. py:attribute:: _range
      :type:  pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange
      :value: None



   .. py:property:: all_axioms
      :type: list[pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom]


      Retrieves a list of universal restriction axioms associated with this object property by filtering the general axiom collection for instances of `OWLObjectAllValuesFrom`. These axioms define constraints requiring that all values of this property for a given subject must belong to a specific class or satisfy a specific condition. The method returns a new list, ensuring that modifications to the result do not affect the internal state, and returns an empty list if no matching axioms are found.

      :return: A list of all universal restriction (all values from) axioms associated with this object property.

      :rtype: list[OWLObjectAllValuesFrom]


   .. py:property:: annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]


      Sets the annotations for the current OWL full object property instance. The provided value, which can be a list of OWLAnnotation objects or None, replaces the existing annotations stored in the private `_annotations` attribute. This operation overwrites the previous state rather than appending to it, effectively resetting the property's metadata to the new list or clearing it if None is provided.

      :param value: The annotations to assign to the object, or None to clear them.
      :type value: typing.Optional[list[OWLAnnotation]]


   .. py:property:: assertions
      :type: list[pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion]


      Retrieves a list of all specific assertions involving this object property by filtering the internal collection of axioms. This includes both positive assertions, which affirm a relationship between two individuals, and negative assertions, which explicitly deny such a relationship. The method returns a new list containing instances of `OWLObjectPropertyAssertion` and `OWLNegativeObjectPropertyAssertion`, providing access to all concrete usages of the property within the ontology. If no assertions are associated with the property, an empty list is returned.

      :return: A list of all object property assertions (both positive and negative) associated with this object property.

      :rtype: list[OWLObjectPropertyAssertion]


   .. py:property:: axioms
      :type: list[pyowl2.abstracts.axiom.OWLAxiom]


      Returns the list of axioms associated with this OWL Full object property. This property provides direct access to the internal collection of `OWLAxiom` instances. Because the reference to the underlying list is returned rather than a copy, any modifications made to the returned list will directly alter the state of the object.

      :return: A list of the axioms associated with this object.

      :rtype: list[OWLAxiom]


   .. py:property:: disjoint_properties
      :type: list[pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties]


      Retrieves a list of axioms that define disjointness relationships between this object property and other object properties within the ontology. The method filters the internal collection of axioms to return only those instances that explicitly declare a disjointness constraint. If no such axioms are associated with the property, an empty list is returned. This property is read-only and does not modify the state of the object or the underlying axioms.

      :return: A list of axioms indicating that this object property is disjoint with other object properties.

      :rtype: list[OWLDisjointObjectProperties]


   .. py:property:: domain
      :type: Optional[pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain]


      Sets the domain restriction for the object property to the specified class expression. This method constructs an `OWLObjectPropertyDomain` axiom that links the current object property with the provided value, defining the valid types of subjects for the property. The resulting axiom is stored internally, replacing any previously defined domain.

      :param value: The class expression defining the domain of the object property.
      :type value: OWLClassExpression


   .. py:property:: equivalent_properties
      :type: list[pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties]


      Retrieves all axioms that assert this object property is equivalent to another object property. This method filters the property's associated axioms to identify and return only those of type `OWLEquivalentObjectProperties`, which formally state that this property and another have the same extension. The returned list may be empty if no equivalent properties are defined for this entity.

      :return: A list of axioms indicating that this object property is equivalent to other object properties.

      :rtype: list[OWLEquivalentObjectProperties]


   .. py:property:: exact_axioms
      :type: list[pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality]


      Retrieves a list of exact cardinality axioms associated with this object property. These axioms define constraints requiring that a subject has precisely a specific number of distinct values for the property. The method filters the property's general axiom collection to isolate instances of `OWLObjectExactCardinality`. It returns an empty list if no matching axioms are found and does not modify the underlying state.

      :return: A list of axioms specifying that this object property must have exactly a certain number of values.

      :rtype: list[OWLObjectExactCardinality]


   .. py:property:: has_self_axioms
      :type: list[pyowl2.class_expression.object_has_self.OWLObjectHasSelf]


      Retrieves all axioms associated with this object property that assert a self-referential relationship. The method filters the internal collection of axioms to return only those instances of `OWLObjectHasSelf`. This is a read-only operation that returns a new list; if no matching axioms are found, the result is an empty list.

      :return: A list of `OWLObjectHasSelf` axioms associated with this object property. The list is empty if no such axioms are defined.

      :rtype: list[OWLObjectHasSelf]


   .. py:property:: has_value_axioms
      :type: list[pyowl2.class_expression.object_has_value.OWLObjectHasValue]


      Retrieves a list of all axioms associated with this object property that specify a particular value. This property filters the internal collection of axioms, returning only those that are instances of `OWLObjectHasValue`. The operation returns a new list, ensuring that modifications to the result do not affect the original data structure, and yields an empty list if no matching axioms are found.

      :return: A list of all `OWLObjectHasValue` axioms associated with this object property, or an empty list if no such axioms exist.

      :rtype: list[OWLObjectHasValue]


   .. py:property:: inverses
      :type: list[pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties]


      Retrieves a collection of axioms that define inverse relationships for this object property. By filtering the internal list of axioms, it identifies and returns only those instances of `OWLInverseObjectProperties`, which assert that this property is the semantic inverse of another. If no inverse relationships are currently asserted for this property, the method returns an empty list.

      :return: A list of axioms defining the inverse properties for this object property.

      :rtype: list[OWLInverseObjectProperties]


   .. py:property:: is_asymmetric
      :type: bool


      Updates the asymmetric characteristic of the object property based on the provided boolean value. If the value is True, the property is marked as asymmetric, implying that if it relates an individual A to B, it cannot relate B to A. If the value is False, the asymmetric characteristic is removed from the property definition. This operation modifies the underlying ontology by adding or removing the corresponding `OWLAsymmetricObjectProperty` axiom.

      :param value: Indicates whether the object property is asymmetric.
      :type value: bool


   .. py:property:: is_functional
      :type: bool


      Sets the functional characteristic of the object property, determining whether it relates an individual to at most one other individual. When the provided value is true, the method adds the corresponding `OWLFunctionalObjectProperty` axiom to the ontology; if false, it removes this assertion. This operation directly modifies the underlying ontology structure to reflect the change in property constraints.

      :param value: Boolean flag indicating whether the property is functional, meaning it can have only one value for each instance.
      :type value: bool


   .. py:property:: is_inverse_functional
      :type: bool


      Sets the inverse-functional characteristic of the object property to the specified boolean value. When set to True, this indicates that the inverse of the property is functional, meaning no two distinct individuals can be the target of the inverse property for the same source individual. The method updates the underlying ontology by adding or removing the corresponding `OWLInverseFunctionalObjectProperty` axiom depending on the provided value.

      :param value: True to mark the property as inverse functional, False otherwise.
      :type value: bool


   .. py:property:: is_irreflexive
      :type: bool


      Sets the irreflexive characteristic of the object property to the specified boolean value. If the value is True, the method asserts that the property is irreflexive, meaning no individual can be related to itself via this property. If the value is False, this assertion is removed. This operation modifies the underlying ontology structure by adding or removing the corresponding `OWLIrreflexiveObjectProperty` axiom.

      :param value: True if the property should be irreflexive, False otherwise.
      :type value: bool


   .. py:property:: is_reflexive
      :type: bool


      Sets the reflexive characteristic of the object property to the specified boolean value. When the value is True, this method asserts that the property relates every individual to itself, effectively adding or updating the corresponding axiom in the ontology. Conversely, setting the value to False removes the reflexive property assertion. This operation modifies the internal state of the entity by invoking the underlying `_del_property` mechanism to handle the `OWLReflexiveObjectProperty` axiom.

      :param value: True if the property should be reflexive, False otherwise.
      :type value: bool


   .. py:property:: is_symmetric
      :type: bool


      Configures the symmetric nature of the object property based on the provided boolean value. If the value is True, the property is marked as symmetric, meaning that if $x$ is related to $y$, then $y$ is related to $x$; if False, this characteristic is removed. This setter triggers an internal update to the ontology's axioms, specifically adding or deleting an instance of `OWLSymmetricObjectProperty` to reflect the new state.

      :param value: True if the object property is symmetric, False otherwise.
      :type value: bool


   .. py:property:: is_transitive
      :type: bool


      Sets the transitive characteristic of the object property by updating the underlying ontology axioms. This method acts as a setter for the `is_transitive` property, accepting a boolean value that determines whether the property should be treated as transitive. It delegates the actual modification of the ontology structure to an internal helper method, passing the provided value and the specific `OWLTransitiveObjectProperty` axiom type to either assert or retract the transitivity constraint.

      :param value: True if the property is transitive, False otherwise.
      :type value: bool


   .. py:property:: max_axioms
      :type: list[pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality]


      Retrieves all maximum cardinality axioms associated with this object property by filtering the internal collection of axioms. These axioms define constraints that limit the number of distinct values the property can have to a specific maximum. The method returns a new list containing only the instances of `OWLObjectMaxCardinality`; if no such constraints exist, an empty list is returned.

      :return: A list of maximum cardinality axioms associated with this object property, representing constraints that limit the maximum number of values the property can have.

      :rtype: list[OWLObjectMaxCardinality]


   .. py:property:: min_axioms
      :type: list[pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality]


      Retrieves a list of all minimum cardinality axioms associated with this object property by filtering the property's general collection of axioms. This method specifically identifies constraints that mandate a lower bound on the number of distinct values or relationships an entity must possess via this property. If no such constraints are defined, an empty list is returned. The operation is read-only and does not modify the underlying ontology structure.

      :return: A list of all minimum cardinality axioms associated with this object property.

      :rtype: list[OWLObjectMinCardinality]


   .. py:property:: object_property
      :type: pyowl2.expressions.object_property.OWLObjectProperty


      Sets the object property associated with this instance. It accepts a value of type OWLObjectProperty and assigns it to the internal attribute, replacing any existing value. This operation updates the state of the object to reflect the new property relationship.

      :param value: The object property to assign to the instance.
      :type value: OWLObjectProperty


   .. py:property:: properties
      :type: list[pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom]


      Retrieves a filtered list of axioms that specifically describe the characteristics and relationships of this object property. The method iterates over the internal collection of axioms and selects only those belonging to the predefined set of object property axiom types. This includes definitions of logical properties such as symmetry, transitivity, or functionality, as well as structural relationships like subproperty hierarchies or equivalences. The operation is read-only and returns a new list; if no relevant axioms are associated with the property, an empty list is returned.

      :return: A list of axioms associated with this object property, defining its characteristics (e.g., symmetry, transitivity) and relationships (e.g., subproperties, equivalence).

      :rtype: list[OWLObjectPropertyAxiom]


   .. py:property:: range
      :type: Optional[pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange]


      Sets the range of the object property to the specified class expression. This method updates the internal state by creating an `OWLObjectPropertyRange` axiom that links the current object property with the provided `OWLClassExpression`. Any previous range definition associated with this property is overwritten by this operation.

      :param value: The class expression that defines the range of the object property.
      :type value: OWLClassExpression


   .. py:property:: some_axioms
      :type: list[pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom]


      Retrieves a list of all existential restriction axioms, specifically those of type `OWLObjectSomeValuesFrom`, that are associated with this object property. This property filters the underlying collection of axioms to isolate constraints indicating that there must exist at least one value for the property belonging to a particular class. The operation is read-only and returns a new list; consequently, modifying the returned list will not affect the original set of axioms, and an empty list is returned if no such restrictions are defined.

      :return: A list of `OWLObjectSomeValuesFrom` axioms associated with this object property, representing existential restrictions where the property has at least one value satisfying a specific condition. Returns an empty list if no such axioms are found.

      :rtype: list[OWLObjectSomeValuesFrom]


   .. py:property:: sub_properties
      :type: list[pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]


      Retrieves a list of axioms that define other properties as sub-properties of the current object property. This method iterates over the internal axioms to find instances of `OWLSubObjectPropertyOf` where the super property expression matches the current property. It effectively identifies the direct hierarchy of properties descending from this one. If no such axioms exist, an empty list is returned, and the method does not modify the object's state.

      :return: A list of axioms defining object properties that are sub-properties of this object property.

      :rtype: list[OWLSubObjectPropertyOf]


   .. py:property:: super_properties
      :type: list[pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]


      Retrieves a list of axioms that define the super-properties of this object property by filtering the internal set of axioms. Specifically, it returns instances of `OWLSubObjectPropertyOf` where the current property is the sub-property expression, indicating that this property is a specialization of another property within the ontology hierarchy. If no such axioms exist, an empty list is returned.

      :return: A list of axioms asserting that this object property is a sub-property of another object property.

      :rtype: list[OWLSubObjectPropertyOf]

