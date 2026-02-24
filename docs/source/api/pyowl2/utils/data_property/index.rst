pyowl2.utils.data_property
==========================

.. py:module:: pyowl2.utils.data_property



.. ── LLM-GENERATED DESCRIPTION START ──

A high-level wrapper that centralizes the management of an OWL data property's identity, domain, range, and associated logical axioms.


Description
-----------


The software provides a structured abstraction for an OWL data property, encapsulating its core identity defined by an Internationalized Resource Identifier (IRI) alongside optional domain and range constraints. It maintains an internal registry of axioms that define the property's logical characteristics, such as functionality, hierarchical relationships with other properties, and equivalence or disjointness constraints. Through its interface, users can assert specific data property values for individuals, including both positive and negative assertions, and apply complex restrictions like existential, universal, and cardinality constraints. The design simplifies ontology manipulation by offering dedicated methods to add, filter, and manage these logical statements and annotations, ensuring that the property's definition remains consistent and semantically valid within the broader ontology structure.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.utils.data_property.OWLFullDataProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_utils_data_property_OWLFullDataProperty.png
       :alt: UML Class Diagram for OWLFullDataProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFullDataProperty**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_utils_data_property_OWLFullDataProperty.pdf
       :alt: UML Class Diagram for OWLFullDataProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFullDataProperty**

.. py:class:: OWLFullDataProperty(iri: pyowl2.base.iri.IRI, domain: Optional[pyowl2.abstracts.class_expression.OWLClassExpression] = None, range: Optional[pyowl2.abstracts.data_range.OWLDataRange] = None, is_functional: bool = False)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`

   .. autoapi-inheritance-diagram:: pyowl2.utils.data_property.OWLFullDataProperty
      :parts: 1
      :private-bases:


   This class serves as a comprehensive wrapper for a data property within an OWL ontology, facilitating the management of its logical definition, characteristics, and metadata. It encapsulates the property's core identity—defined by an Internationalized Resource Identifier (IRI)—along with optional domain and range constraints, while maintaining a centralized list of associated axioms. Through its interface, users can define property characteristics such as functionality, establish hierarchical relationships (sub-properties and super-properties), and specify equivalence or disjointness with other properties. Additionally, it provides utility methods to handle property assertions linking individuals to literal values, as well as to apply various cardinality and value restrictions. The class also supports the attachment of annotations to the property, its domain, range, and specific axioms, thereby enhancing the ontology's documentation without affecting its logical semantics.

   :param PROPERTY_CLASSES: A list of axiom types that define the intrinsic characteristics of the data property, used to categorize and filter relevant axioms.
   :type PROPERTY_CLASSES: list[type]
   :param data_property: The core definition of the data property identified by its IRI, serving as the subject for all associated axioms, domains, ranges, and assertions.
   :type data_property: OWLDataProperty
   :param domain: Internal storage for the domain restriction axiom, defining the class of individuals that can be the subject of this data property. It holds an OWLDataPropertyDomain instance or None if no domain is specified.
   :type domain: OWLDataPropertyDomain
   :param range: Encapsulates the range restriction for the data property, defining the permissible data types or values for the property's objects.
   :type range: OWLDataPropertyRange
   :param axioms: Internal storage for the axioms associated with the data property, encompassing characteristics, relationships, assertions, and restrictions.
   :type axioms: list[OWLAxiom]
   :param annotations: Stores the optional list of annotations associated with the data property, providing metadata such as comments or labels to enhance documentation without affecting logical meaning.
   :type annotations: typing.Optional[list[OWLAnnotation]]


   .. py:method:: add_assertion(individual: pyowl2.abstracts.individual.OWLIndividual, literal: pyowl2.literal.literal.OWLLiteral, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      This method creates and stores a data property assertion that links a specific individual to a literal value through the current data property. It accepts an optional list of annotations to attach metadata to the assertion, which does not affect the logical semantics but aids in documentation. The method modifies the internal state by appending the new assertion to the collection of axioms, provided that an identical assertion does not already exist; this check ensures that duplicate assertions are not added.

      :param individual: The entity or instance that is the subject of the assertion, possessing the specified literal value for this data property.
      :type individual: OWLIndividual
      :param literal: The literal value associated with the individual for this data property.
      :type literal: OWLLiteral
      :param annotations: Optional list of annotations to attach to the assertion, providing metadata like comments or labels that do not affect logical semantics.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: add_domain_annotations(annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None

      Associates a list of OWLAnnotation objects with the domain of the data property. If the data property does not currently have a domain defined, the method returns without making any changes. Otherwise, it assigns the provided list to the domain's annotation collection, overwriting any existing annotations. These annotations serve as metadata, such as labels or comments, and do not alter the logical semantics of the domain.

      :param annotations: Metadata objects (e.g., comments, labels) to associate with the domain of the data property, providing descriptive context without affecting logical meaning.
      :type annotations: list[OWLAnnotation]



   .. py:method:: add_negative_assertion(individual: pyowl2.abstracts.individual.OWLIndividual, literal: pyowl2.literal.literal.OWLLiteral, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Adds a negative data property assertion to the collection of axioms associated with this data property, logically stating that the specified individual does not possess the given literal value for this property. The method accepts an optional list of annotations to attach metadata to the assertion without affecting its logical meaning. If an identical assertion already exists within the internal axioms list, the method performs no operation to prevent redundancy.

      :param individual: The subject of the negative assertion, representing the entity that is being stated not to have the specified data property value.
      :type individual: OWLIndividual
      :param literal: The specific value that the individual is asserted not to have for the data property.
      :type literal: OWLLiteral
      :param annotations: An optional list of annotations to associate with the assertion, providing metadata such as comments or labels without affecting its logical meaning.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: add_property_annotations(property_class: pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom, annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None

      This method modifies the metadata associated with a specific type of axiom belonging to this data property. It iterates through the property's existing axioms to locate the first instance that matches the provided `property_class` and replaces that axiom's current annotations with the supplied list. If the property does not contain an axiom of the specified type, the method performs no action and returns silently.

      :param property_class: The specific class of data property axiom to target. The method searches the existing axioms for the first instance of this class to apply the annotations.
      :type property_class: OWLDataPropertyAxiom
      :param annotations: Metadata objects, such as comments or labels, to be associated with the first matching data property axiom.
      :type annotations: list[OWLAnnotation]



   .. py:method:: add_range_annotations(annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None

      Associates a list of OWL annotations with the range of the data property, effectively setting the metadata for the range definition. The method assigns the provided list of annotations to the range's annotation collection. If the data property does not currently have a defined range, the method returns immediately without making changes. Note that this operation replaces any existing annotations previously associated with the range rather than appending to them.

      :param annotations: A list of OWLAnnotation objects containing metadata such as comments or labels to be associated with the range of the data property.
      :type annotations: list[OWLAnnotation]



   .. py:method:: all(data_range: pyowl2.abstracts.data_range.OWLDataRange) -> None

      Adds a universal restriction to the data property, asserting that all values for this property must belong to the specified data range. This is achieved by constructing an `OWLDataAllValuesFrom` axiom and appending it to the internal collection of axioms. The method performs a check to prevent redundancy; if an identical axiom already exists within the collection, the operation is aborted and the state remains unchanged.

      :param data_range: The data range defining the set of permissible values that all values of the data property must belong to.
      :type data_range: OWLDataRange



   .. py:method:: del_assertion(assertion: Union[pyowl2.axioms.assertion.negative_data_property_assertion.OWLNegativeDataPropertyAssertion, pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion]) -> None

      Removes a specific data property assertion, which can be either positive or negative, from the internal collection of axioms associated with this data property. The method iterates through the existing axioms and deletes the first occurrence that matches the provided assertion object. If the assertion is not found within the collection, the method performs no action and returns without error. This operation directly modifies the object's state by altering the list of stored axioms.

      :param assertion: The positive or negative data property assertion to remove from the property's axioms.
      :type assertion: typing.Union[OWLNegativeDataPropertyAssertion, OWLDataPropertyAssertion]



   .. py:method:: exact_cardinality(cardinality: int, data_range: pyowl2.abstracts.data_range.OWLDataRange) -> None

      Adds an exact cardinality restriction to the data property, specifying that the property must have exactly the defined number of values falling within the provided data range. This method creates an `OWLDataExactCardinality` axiom and appends it to the internal list of axioms. To prevent redundancy, it first verifies that an identical axiom does not already exist; if a duplicate is found, the method returns without modifying the state.

      :param cardinality: The exact count of values the data property must have within the given data range. Must be a non-negative integer.
      :type cardinality: int
      :param data_range: The data range or datatype defining the set of permissible values for the data property within the restriction.
      :type data_range: OWLDataRange



   .. py:method:: has_value(literal: pyowl2.literal.literal.OWLLiteral) -> None

      This method creates and registers a "has value" restriction for the data property, constraining it to a specific literal value. It instantiates an `OWLDataHasValue` axiom using the provided `OWLLiteral` and adds it to the object's collection of axioms. The operation is idempotent; if an equivalent restriction is already present in the axiom list, the method returns without making changes.

      :param literal: The specific concrete value that the data property is restricted to having.
      :type literal: OWLLiteral



   .. py:method:: is_disjoint_from(properties: Union[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Asserts that the current data property is disjoint from one or more specified data properties, meaning no individual can possess both properties simultaneously. The method accepts a single property or a list of properties, which can be provided as `OWLDataPropertyExpression` instances or `OWLFullDataProperty` objects (where the underlying data property is extracted), and constructs a corresponding `OWLDisjointDataProperties` axiom. Optional annotations can be attached to this axiom to provide metadata without affecting logical meaning. The resulting axiom is appended to the object's internal list of axioms only if an identical axiom does not already exist, preventing duplicates. If the input arguments contain mixed or invalid types, the method returns a `TypeError` object.

      :param properties: One or more data properties that are mutually exclusive with the current property. Accepts property expressions or instances of the current class, provided either singly or as a list.
      :type properties: typing.Union[OWLDataPropertyExpression, list[OWLDataPropertyExpression], typing.Self, list[typing.Self]]
      :param annotations: An optional list of annotations to associate with the disjoint properties axiom, providing metadata such as comments or labels without affecting logical semantics.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: is_equivalent_to(properties: Union[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Establishes a logical equivalence between the current data property and one or more specified data property expressions by creating and registering an `OWLEquivalentDataProperties` axiom. The method accepts either a single property or a list of properties, handling both raw property expressions and wrapper instances by extracting the underlying data property as needed. To ensure consistency, the operation checks the internal collection of axioms and skips registration if an equivalent axiom already exists. Optional annotations can be provided to attach metadata to the axiom, which serves to document the relationship without affecting the logical semantics.

      :param properties: One or more properties that are semantically equivalent to the current data property. Can be provided as OWLDataPropertyExpression objects or instances of the current class, extracting the underlying data property from the latter.
      :type properties: typing.Union[OWLDataPropertyExpression, list[OWLDataPropertyExpression], typing.Self, list[typing.Self]]
      :param annotations: An optional list of annotations to associate with the equivalent properties axiom, providing metadata such as comments or labels without affecting logical meaning.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: is_sub_property_of(super_property: Union[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, Self], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Establishes a hierarchical relationship by asserting that the current data property is a sub-property of the specified super property. This method creates an `OWLSubDataPropertyOf` axiom, handling input flexibility by accepting either a direct property expression or a wrapper object from which the underlying property is extracted. The resulting axiom is appended to the internal list of axioms, though the operation is idempotent; if an identical axiom already exists, the method returns without modification. Optional annotations may be provided to attach metadata to the axiom, which does not alter its logical meaning but enhances documentation.

      :param super_property: The more general data property to which the current property is subordinate. Accepts either a direct property expression or another full data property instance, extracting the underlying expression in the latter case.
      :type super_property: typing.Union[OWLDataPropertyExpression, typing.Self]
      :param annotations: Optional list of annotations to associate with the sub-property axiom, providing metadata such as comments or labels without affecting the logical meaning of the relationship.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: is_super_property_of(sub_property: Union[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, Self], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None

      Establishes a sub-property relationship by asserting that the current data property instance is a super-property of the provided `sub_property`. This method creates an `OWLSubDataPropertyOf` axiom and appends it to the internal list of axioms associated with the current instance, provided that an identical axiom does not already exist. The `sub_property` can be specified either as a direct `OWLDataPropertyExpression` or as another `OWLFullDataProperty` object, in which case its underlying data property is used. Additionally, optional annotations may be supplied to attach metadata to the axiom without altering its logical meaning.

      :param sub_property: The data property expression to be designated as a sub-property of the current property. It accepts either an OWLDataPropertyExpression or an instance of the current class, extracting the underlying data property in the latter case.
      :type sub_property: typing.Union[OWLDataPropertyExpression, typing.Self]
      :param annotations: Optional list of annotations to attach to the sub-property axiom, providing metadata such as comments or labels.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: max_cardinality(cardinality: int, data_range: pyowl2.abstracts.data_range.OWLDataRange) -> None

      Adds a maximum cardinality restriction to the data property, limiting the number of values it can have to the specified integer within the provided data range. This method constructs an `OWLDataMaxCardinality` axiom and appends it to the internal list of axioms associated with the property. If an identical axiom is already present in the list, the method returns without making changes, ensuring that duplicate restrictions are not added.

      :param cardinality: The maximum number of values the data property can have within the specified data range.
      :type cardinality: int
      :param data_range: Defines the set of permissible values for the data property that are subject to the maximum cardinality restriction.
      :type data_range: OWLDataRange



   .. py:method:: min_cardinality(cardinality: int, data_range: pyowl2.abstracts.data_range.OWLDataRange) -> None

      Adds a minimum cardinality restriction to the data property, asserting that it must be associated with at least a specific number of values falling within a defined data range. It constructs an `OWLDataMinCardinality` axiom using the provided integer cardinality and the specified `OWLDataRange`, associating it with the current data property. The resulting axiom is appended to the internal list of axioms maintained by the property, effectively updating the ontology definition. To prevent redundancy, the method checks for the existence of an identical axiom before adding it; if a matching restriction is already present, the operation performs no modification.

      :param cardinality: The non-negative integer specifying the minimum number of values the data property must have within the given data range.
      :type cardinality: int
      :param data_range: Defines the set of permissible values or datatype for the data property within the restriction.
      :type data_range: OWLDataRange



   .. py:method:: some(data_range: pyowl2.abstracts.data_range.OWLDataRange) -> None

      Adds an existential restriction to the data property, asserting that it must have at least one value falling within the specified data range. This method constructs an `OWLDataSomeValuesFrom` axiom and appends it to the internal list of axioms associated with the property. To prevent redundancy, the method checks if an identical axiom already exists; if so, it returns without making any changes.

      :param data_range: The set of values defining the existential restriction, requiring the property to take at least one value from this range. Duplicate restrictions are ignored.
      :type data_range: OWLDataRange



   .. py:attribute:: PROPERTY_CLASSES
      :type:  list[type]


   .. py:attribute:: _annotations
      :type:  Optional[list[pyowl2.base.annotation.OWLAnnotation]]
      :value: None



   .. py:attribute:: _axioms
      :type:  list[pyowl2.abstracts.axiom.OWLAxiom]
      :value: []



   .. py:attribute:: _data_property
      :type:  pyowl2.expressions.data_property.OWLDataProperty


   .. py:attribute:: _domain
      :type:  pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain
      :value: None



   .. py:attribute:: _range
      :type:  pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange
      :value: None



   .. py:property:: all_axioms
      :type: list[pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom]


      Retrieves a list of universal restrictions (all-values-from axioms) associated with this data property. This property filters the underlying collection of axioms to return only those of type `OWLDataAllValuesFrom`, which assert that every value of the data property must belong to a specific data range. If no such restrictions are defined, an empty list is returned.

      :return: A list of `OWLDataAllValuesFrom` axioms associated with the data property, indicating that all values must satisfy a specific data range.

      :rtype: list[OWLDataAllValuesFrom]


   .. py:property:: annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]


      Updates the annotations associated with this OWL data property by replacing the existing collection with the provided value. The method accepts a list of `OWLAnnotation` objects or `None`, assigning it directly to the internal state. This operation overwrites any previous annotations stored on the property.

      :param value: A list of OWL annotations to set, or None.
      :type value: typing.Optional[list[OWLAnnotation]]


   .. py:property:: assertions
      :type: list[pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion]


      Retrieves all data property assertions associated with this property by filtering its internal collection of axioms. The resulting list encompasses both positive assertions, which affirm that an individual possesses a specific data value, and negative assertions, which deny such an association. If no relevant assertions exist within the axioms, an empty list is returned. This operation is read-only and does not alter the state of the property or its underlying axioms.

      :return: A list of positive and negative data property assertions associated with this property.

      :rtype: list[OWLDataPropertyAssertion]


   .. py:property:: axioms
      :type: list[pyowl2.abstracts.axiom.OWLAxiom]


      Retrieves the list of axioms associated with this OWL full data property. This property provides access to the internal collection of `OWLAxiom` objects that define the logical constraints and characteristics of the property within the ontology. Since the method returns the underlying list reference, any modifications made to the returned list will directly affect the state of the property instance.

      :return: The list of axioms associated with this object.

      :rtype: list[OWLAxiom]


   .. py:property:: data_property
      :type: pyowl2.expressions.data_property.OWLDataProperty


      Sets the value of the data property for this instance. This method assigns the provided `OWLDataProperty` object to the internal `_data_property` attribute, overwriting any previously stored value. No validation or side effects beyond the assignment are performed.

      :param value: The OWL data property to assign to the object.
      :type value: OWLDataProperty


   .. py:property:: disjoint_properties
      :type: list[pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties]


      Retrieves a list of axioms that define disjointness relationships between this data property and other data properties. In the context of OWL, disjoint properties are mutually exclusive, meaning an individual cannot simultaneously possess values for both properties. This property filters the internal set of axioms associated with the current property, returning only those instances of `OWLDisjointDataProperties`. The returned list will be empty if no disjointness axioms are present.

      :return: A list of axioms representing the disjoint data properties associated with the current entity, asserting that the properties are mutually exclusive.

      :rtype: list[OWLDisjointDataProperties]


   .. py:property:: domain
      :type: Optional[pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain]


      Sets the domain restriction for the data property to the specified class expression. This method updates the internal state by constructing a new `OWLDataPropertyDomain` axiom that associates the current data property with the provided value. Any previously defined domain restriction for this property will be overwritten as a side effect of this assignment.

      :param value: The OWL class expression that defines the domain of the data property.
      :type value: OWLClassExpression


   .. py:property:: equivalent_properties
      :type: list[pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties]


      This property retrieves the axioms that assert the current data property is semantically equivalent to other data properties. It filters the entity's internal collection of axioms, returning a list containing only instances of `OWLEquivalentDataProperties`. The result provides direct access to the equivalence relationships defined in the ontology, returning an empty list if no such axioms exist.

      :return: A list of axioms asserting that the current data property is equivalent to other data properties.

      :rtype: list[OWLEquivalentDataProperties]


   .. py:property:: exact_axioms
      :type: list[pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality]


      Retrieves all exact cardinality axioms associated with this data property by filtering the property's general collection of axioms. Each returned axiom, represented as an `OWLDataExactCardinality` instance, constrains the number of data values an individual can have for this property to a specific integer. The result is a list containing only those axioms that define an exact count requirement.

      :return: A list of exact cardinality axioms associated with the data property, specifying the exact number of values it must have.

      :rtype: list[OWLDataExactCardinality]


   .. py:property:: has_value_axioms
      :type: list[pyowl2.class_expression.data_has_value.OWLDataHasValue]


      Retrieves a collection of axioms that assert specific value constraints for this data property. This property filters the internal set of axioms associated with the entity, returning only those that are instances of OWLDataHasValue. The result is a newly created list, meaning modifications to the returned collection will not affect the underlying state of the property; an empty list is returned if no such axioms exist.

      :return: A list of `OWLDataHasValue` axioms associated with the data property, representing assertions that the property has a specific literal value.

      :rtype: list[OWLDataHasValue]


   .. py:property:: is_functional
      :type: bool


      Updates the functional characteristic of the data property by modifying the internal list of axioms. When the value is set to True, the method ensures that an OWLFunctionalDataProperty axiom is present in the axioms list, enforcing the semantic restriction that an individual can have at most one value for this property. If the value is set to False, any existing functional axiom is removed from the list, thereby eliminating the restriction on the number of values. The operation is idempotent, performing no action if the property's current state already matches the specified value.

      :param value: Specifies whether the data property is functional, meaning each individual can have at most one value. True adds the corresponding OWL axiom, while False removes it.
      :type value: bool


   .. py:property:: max_axioms
      :type: list[pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality]


      Retrieves a list of maximum cardinality axioms associated with this data property by filtering the general collection of axioms. Each returned axiom is an instance of `OWLDataMaxCardinality`, which asserts the upper bound on the number of distinct values the property may possess. The result may be an empty list if no such restrictions are defined, and invoking this method does not alter the state of the property or its axioms.

      :return: A list of maximum cardinality axioms for the data property, representing constraints on the maximum number of values the property can have.

      :rtype: list[OWLDataMaxCardinality]


   .. py:property:: min_axioms
      :type: list[pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality]


      This property accessor filters the underlying set of axioms to isolate those asserting minimum cardinality constraints on the data property. It returns a list of `OWLDataMinCardinality` objects, each defining the lower bound of values an individual must have. If the property has no minimum cardinality restrictions defined within its axiom set, the method returns an empty list.

      :return: A list of minimum cardinality axioms associated with the data property.

      :rtype: list[OWLDataMinCardinality]


   .. py:property:: properties
      :type: list[pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom]


      Retrieves a collection of axioms that define the characteristics and relationships of the data property. The method filters the entity's internal list of axioms, returning only those that belong to specific classes designated as property-related axioms, such as functionality constraints or subproperty hierarchies. The resulting list provides a comprehensive view of the property's definition within the ontology; if no matching axioms are found, an empty list is returned. This operation is read-only and does not alter the state of the object.

      :return: A list of axioms defining the characteristics and relationships of the data property.

      :rtype: list[OWLDataPropertyAxiom]


   .. py:property:: range
      :type: Optional[pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange]


      Sets the data range for the OWL data property by associating the provided `OWLDataRange` value with the current property instance. This method constructs a new `OWLDataPropertyRange` object linking the data property to the specified range and assigns it to the internal `_range` attribute. As a setter, it overwrites any previously defined range for this property, effectively updating the property's definition within the ontology structure.

      :param value: The data range defining the set of permissible values for the data property.
      :type value: OWLDataRange


   .. py:property:: some_axioms
      :type: list[pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom]


      Retrieves a list of existential restriction axioms associated with this data property. Specifically, it filters the property's general axiom set to return only those instances of `OWLDataSomeValuesFrom`, which assert the existence of at least one value for the property that falls within a specified data range. This method returns a new list, ensuring that modifications to the result do not affect the internal state of the property, and it will return an empty list if no matching axioms are present.

      :return: A list of `OWLDataSomeValuesFrom` axioms representing existential restrictions on this data property, indicating that at least one value for the property satisfies a specific data range.

      :rtype: list[OWLDataSomeValuesFrom]


   .. py:property:: sub_properties
      :type: list[pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf]


      Retrieves a list of axioms representing the direct sub-properties of the current data property within the ontology. This property filters the internal set of axioms to identify instances of `OWLSubDataPropertyOf` where the current property is designated as the super-property, effectively finding properties that are more specific specializations of this one. The result is a list of these relationship axioms; if no sub-properties are defined, an empty list is returned. This operation is read-only and does not modify the underlying ontology structure.

      :return: A list of axioms representing data properties that are sub-properties of the current data property.

      :rtype: list[OWLSubDataPropertyOf]


   .. py:property:: super_properties
      :type: list[pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf]


      Retrieves a list of axioms representing the super-properties of this data property by filtering the internal set of axioms. Specifically, it identifies and returns all `OWLSubDataPropertyOf` axioms where the sub-data property expression corresponds to the current property instance. This method is read-only and will return an empty list if no super-property relationships are defined for this property.

      :return: A list of axioms representing the super-properties of the current data property, where each axiom asserts a sub-property relationship with the current property as the sub-property.

      :rtype: list[OWLSubDataPropertyOf]

