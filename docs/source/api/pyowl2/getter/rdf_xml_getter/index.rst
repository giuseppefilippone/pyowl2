pyowl2.getter.rdf_xml_getter
============================

.. py:module:: pyowl2.getter.rdf_xml_getter



.. ── LLM-GENERATED DESCRIPTION START ──

The software implements a comprehensive parser and transformer that extracts OWL 2 entities and axioms from an RDF/XML ontology using ``owlready2`` and ``rdflib``, converting them into a structured object model.


Description
-----------


The core functionality revolves around the ``RDFXMLGetter`` class, which acts as an adapter to bridge the gap between the raw RDF graph representation and a high-level object-oriented model of OWL 2 concepts. Upon initialization, the class converts the ontology into an ``rdflib`` graph to facilitate SPARQL querying and establishes a complex caching system to store transformed entities, ensuring that repeated access to the same ontology element returns the same object instance. It systematically retrieves various ontology components—ranging from classes, object and data properties, and individuals to complex class expressions like unions, intersections, and restrictions—by executing targeted SPARQL queries and mapping the results to specific abstract classes. The design emphasizes robustness and compatibility, handling edge cases such as OWL 1 DL constructs, reified annotations, and property chains, while a dispatcher method allows consumers to request specific axiom types defined in the ``AxiomsType`` enumeration. By separating the logic for querying the graph from the logic for constructing object representations, the architecture efficiently transforms low-level RDF triples into a semantic hierarchy of axioms and expressions.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   pyowl2.getter.rdf_xml_getter.BASE_DATATYPES


Classes
-------

.. autoapisummary::

   pyowl2.getter.rdf_xml_getter.AxiomsType
   pyowl2.getter.rdf_xml_getter.RDFXMLGetter


Functions
---------

.. autoapisummary::

   pyowl2.getter.rdf_xml_getter.get_abbreviation
   pyowl2.getter.rdf_xml_getter.is_named_individual


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_getter_rdf_xml_getter_AxiomsType.png
       :alt: UML Class Diagram for AxiomsType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **AxiomsType**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_getter_rdf_xml_getter_AxiomsType.pdf
       :alt: UML Class Diagram for AxiomsType
       :align: center
       :width: 3.4cm
       :class: uml-diagram

       UML Class Diagram for **AxiomsType**

.. py:class:: AxiomsType

   Bases: :py:obj:`enum.StrEnum`

   .. autoapi-inheritance-diagram:: pyowl2.getter.rdf_xml_getter.AxiomsType
      :parts: 1
      :private-bases:


   This enumeration defines the specific categories of axioms found within the Web Ontology Language (OWL). It provides a standardized set of labels to identify and differentiate between various logical constructs, such as class declarations, property hierarchies, and individual assertions. The members cover a broad spectrum of ontology elements, including class expressions, property characteristics, and data restrictions. By inheriting from `StrEnum`, it allows these types to be treated as strings while maintaining the benefits of an enumeration for type safety and code clarity.

   :param GENERAL_CLASS_AXIOMS: Represents axioms where the subject is a complex class expression (e.g., an intersection or restriction) rather than a named class.
   :type GENERAL_CLASS_AXIOMS: typing.Any
   :param CLASSES: Represents axioms or entities specifically pertaining to OWL classes.
   :type CLASSES: typing.Any
   :param DECLARATIONS: Represents OWL declaration axioms, which introduce entities to the ontology.
   :type DECLARATIONS: typing.Any
   :param OBJECT_PROPERTIES: Represents axioms associated with object properties, which define relationships between individuals in the ontology.
   :type OBJECT_PROPERTIES: typing.Any
   :param DATA_PROPERTIES: Represents axioms concerning data properties, which define relationships between individuals and literal data values.
   :type DATA_PROPERTIES: typing.Any
   :param ANNOTATION_PROPERTIES: Represents axioms involving annotation properties, which provide metadata for ontology elements.
   :type ANNOTATION_PROPERTIES: typing.Any
   :param INDIVIDUALS: Represents axioms that involve or describe individuals (instances) in the ontology.
   :type INDIVIDUALS: typing.Any
   :param SUBCLASSES: Represents axioms that define a subclass relationship between two classes.
   :type SUBCLASSES: typing.Any
   :param EQUIVALENT_CLASSES: Represents axioms asserting that two or more classes are equivalent.
   :type EQUIVALENT_CLASSES: typing.Any
   :param DISJOINT_CLASSES: Represents axioms asserting that a set of classes are mutually exclusive and cannot share any instances.
   :type DISJOINT_CLASSES: typing.Any
   :param OBJECT_UNION_OF: Represents the OWL class expression for the union of object classes.
   :type OBJECT_UNION_OF: typing.Any
   :param DATA_UNION_OF: Represents a data range that is the union of one or more other data ranges.
   :type DATA_UNION_OF: typing.Any
   :param OBJECT_INTERSECTION_OF: Represents the OWL ObjectIntersectionOf construct, defining a class as the intersection of two or more object class expressions.
   :type OBJECT_INTERSECTION_OF: typing.Any
   :param DATA_INTERSECTION_OF: Represents the intersection of data ranges.
   :type DATA_INTERSECTION_OF: typing.Any
   :param OBJECT_COMPLEMENT_OF: Represents the OWL axiom or class expression corresponding to the complement (negation) of an object class.
   :type OBJECT_COMPLEMENT_OF: typing.Any
   :param DATA_COMPLEMENT_OF: Represents the OWL data complement of construct, defining a data range consisting of all literals not contained within a specified data range.
   :type DATA_COMPLEMENT_OF: typing.Any
   :param OBJECTS_ONE_OF: Represents an OWL class expression that defines a class by enumerating a specific set of individuals.
   :type OBJECTS_ONE_OF: typing.Any
   :param DATA_ONE_OF: Represents an OWL axiom defining a data range as a specific enumeration of literal values.
   :type DATA_ONE_OF: typing.Any
   :param DATATYPE_RESTRICTIONS: Represents axioms that restrict the value space of a datatype using specific facets.
   :type DATATYPE_RESTRICTIONS: typing.Any
   :param INVERSE_OBJECT_PROPERTIES: Represents the type of OWL axiom that defines two object properties as inverses of one another.
   :type INVERSE_OBJECT_PROPERTIES: typing.Any
   :param HAS_KEYS: Represents axioms that define a key property or set of properties used to uniquely identify instances of a class.
   :type HAS_KEYS: typing.Any
   :param DATATYPES: Represents axioms or declarations associated with datatypes.
   :type DATATYPES: typing.Any
   :param NEGATIVE_OBJECT_PROPERTY_ASSERTIONS: Represents axioms asserting that a specific object property relationship does not hold between two individuals.
   :type NEGATIVE_OBJECT_PROPERTY_ASSERTIONS: typing.Any
   :param NEGATIVE_DATA_PROPERTY_ASSERTIONS: Represents axioms asserting that a specific individual does not have a particular data property value.
   :type NEGATIVE_DATA_PROPERTY_ASSERTIONS: typing.Any
   :param CLASS_ASSERTIONS: Represents axioms asserting that an individual is a member of a specific class.
   :type CLASS_ASSERTIONS: typing.Any
   :param OBJECT_PROPERTY_ASSERTIONS: Axioms asserting that a specific object property holds between two individuals.
   :type OBJECT_PROPERTY_ASSERTIONS: typing.Any
   :param DATA_PROPERTY_ASSERTIONS: Represents axioms that assert a data property relationship between an individual and a literal value.
   :type DATA_PROPERTY_ASSERTIONS: typing.Any
   :param SAME_INDIVIDUALS: Represents axioms asserting that two or more individuals are identical.
   :type SAME_INDIVIDUALS: typing.Any
   :param DIFFERENT_INDIVIDUALS: Represents axioms asserting that a set of individuals are pairwise distinct.
   :type DIFFERENT_INDIVIDUALS: typing.Any
   :param SUB_OBJECT_PROPERTIES: Represents axioms stating that one object property is a sub-property of another.
   :type SUB_OBJECT_PROPERTIES: typing.Any
   :param SUB_DATA_PROPERTIES: Represents axioms asserting that one data property is a sub-property of another data property.
   :type SUB_DATA_PROPERTIES: typing.Any
   :param SUB_ANNOTATION_PROPERTIES: Axioms defining a sub-property relationship between annotation properties.
   :type SUB_ANNOTATION_PROPERTIES: typing.Any
   :param EQUIVALENT_OBJECT_PROPERTIES: Represents the OWL axiom type asserting that two or more object properties are equivalent.
   :type EQUIVALENT_OBJECT_PROPERTIES: typing.Any
   :param DISJOINT_OBJECT_PROPERTIES: Represents the OWL axiom stating that a set of object properties are disjoint, meaning no pair of individuals can be connected by more than one of the properties.
   :type DISJOINT_OBJECT_PROPERTIES: typing.Any
   :param ANNOTATIONS: Represents annotation axioms used to attach metadata or comments to ontology entities.
   :type ANNOTATIONS: typing.Any
   :param OBJECTS_SOME_VALUES_FROM: Represents existential restrictions on object properties, indicating that an individual must be connected via the property to at least one instance of a specified class.
   :type OBJECTS_SOME_VALUES_FROM: typing.Any
   :param OBJECTS_ALL_VALUES_FROM: Represents the OWL universal restriction on object properties, constraining all values of the property to be members of a specific class.
   :type OBJECTS_ALL_VALUES_FROM: typing.Any
   :param OBJECTS_HAS_VALUE: Represents an OWL ObjectHasValue restriction, which defines a class of individuals connected to a specific named individual via an object property.
   :type OBJECTS_HAS_VALUE: typing.Any
   :param OBJECTS_HAS_SELF: Represents the OWL ObjectHasSelf restriction, which defines a class of individuals that are connected to themselves by a specific object property.
   :type OBJECTS_HAS_SELF: typing.Any
   :param OBJECTS_MIN_CARDINALITY: Represents an OWL axiom defining a minimum cardinality restriction on an object property.
   :type OBJECTS_MIN_CARDINALITY: typing.Any
   :param OBJECTS_MAX_CARDINALITY: Represents an OWL axiom defining a maximum cardinality restriction for an object property.
   :type OBJECTS_MAX_CARDINALITY: typing.Any
   :param OBJECTS_EXACT_CARDINALITY: Represents an OWL axiom defining an exact cardinality restriction on an object property, requiring exactly a specific number of relationships.
   :type OBJECTS_EXACT_CARDINALITY: typing.Any
   :param DATA_SOME_VALUES_FROM: Represents an existential restriction on a data property, requiring at least one value from a specified data range.
   :type DATA_SOME_VALUES_FROM: typing.Any
   :param DATA_ALL_VALUES_FROM: Represents a universal restriction on data properties, requiring that all values of the property belong to a specified data range.
   :type DATA_ALL_VALUES_FROM: typing.Any
   :param DATAS_HAS_VALUE: Represents the OWL axiom type for data property restrictions that require a specific literal value.
   :type DATAS_HAS_VALUE: typing.Any
   :param DATA_MIN_CARDINALITY: Represents an OWL axiom specifying the minimum number of data property values an individual must possess.
   :type DATA_MIN_CARDINALITY: typing.Any
   :param DATA_MAX_CARDINALITY: Represents an OWL axiom restricting the maximum number of values a data property can have for an individual.
   :type DATA_MAX_CARDINALITY: typing.Any
   :param DATA_EXACT_CARDINALITY: Represents an OWL axiom restricting a data property to have exactly a specific number of values.
   :type DATA_EXACT_CARDINALITY: typing.Any
   :param DISJOINT_UNIONS: Represents axioms that define a class as the union of a collection of pairwise disjoint classes.
   :type DISJOINT_UNIONS: typing.Any
   :param FUNCIONAL_DATA_PROPERTIES: Represents axioms asserting that a data property is functional, meaning an individual can have at most one value for that property.
   :type FUNCIONAL_DATA_PROPERTIES: typing.Any
   :param FUNCTIONAL_OBJECT_PROPERTIES: Represents axioms that assert an object property is functional, meaning each subject is associated with at most one object.
   :type FUNCTIONAL_OBJECT_PROPERTIES: typing.Any
   :param INVERSE_FUNCTIONAL_OBJECT_PROPERTIES: Represents axioms declaring an object property to be inverse functional, meaning no two distinct individuals can be related to the same individual via this property.
   :type INVERSE_FUNCTIONAL_OBJECT_PROPERTIES: typing.Any
   :param TRANSITIVE_OBJECT_PROPERTIES: Represents the axiom type for transitive object properties.
   :type TRANSITIVE_OBJECT_PROPERTIES: typing.Any
   :param SYMMETRIC_OBJECT_PROPERTIES: Represents axioms that declare an object property to be symmetric.
   :type SYMMETRIC_OBJECT_PROPERTIES: typing.Any
   :param ASYMMETRIC_OBJECT_PROPERTIES: Represents axioms that declare an object property to be asymmetric, meaning that if the property relates $x$ to $y$, it cannot relate $y$ to $x$.
   :type ASYMMETRIC_OBJECT_PROPERTIES: typing.Any
   :param REFLEXIVE_OBJECT_PROPERTIES: Represents axioms asserting that an object property is reflexive.
   :type REFLEXIVE_OBJECT_PROPERTIES: typing.Any
   :param IRREFLEXIVE_OBJECT_PROPERTIES: Represents the OWL axiom type for irreflexive object properties, which asserts that a property cannot relate an individual to itself.
   :type IRREFLEXIVE_OBJECT_PROPERTIES: typing.Any
   :param EQUIVALENT_DATA_PROPERTIES: Represents axioms that declare two or more data properties to be equivalent.
   :type EQUIVALENT_DATA_PROPERTIES: typing.Any
   :param DISJOINT_DATA_PROPERTIES: Represents axioms asserting that specified data properties are disjoint, meaning they cannot share the same value for the same individual.
   :type DISJOINT_DATA_PROPERTIES: typing.Any
   :param OBJECT_PROPERTY_DOMAIN: Represents an axiom defining the domain of an object property.
   :type OBJECT_PROPERTY_DOMAIN: typing.Any
   :param OBJECT_PROPERTY_RANGE: Represents an axiom restricting the range of an object property, defining the class of individuals that may serve as the property's value.
   :type OBJECT_PROPERTY_RANGE: typing.Any
   :param DATA_PROPERTY_DOMAIN: Represents the OWL axiom type that defines the domain of a data property.
   :type DATA_PROPERTY_DOMAIN: typing.Any
   :param DATA_PROPERTY_RANGE: Represents an axiom that restricts the range of a data property to a specific datatype.
   :type DATA_PROPERTY_RANGE: typing.Any
   :param DATATYPE_DEFINITION: Represents an OWL axiom that defines a new datatype by restricting an existing datatype with facet restrictions.
   :type DATATYPE_DEFINITION: typing.Any
   :param ANNOTATION_PROPERTY_DOMAINS: Represents axioms that define the domain of annotation properties.
   :type ANNOTATION_PROPERTY_DOMAINS: typing.Any
   :param ANNOTATION_PROPERTY_RANGES: Represents the axiom type that defines the range of values for an annotation property.
   :type ANNOTATION_PROPERTY_RANGES: typing.Any


   .. py:attribute:: ANNOTATIONS


   .. py:attribute:: ANNOTATION_PROPERTIES


   .. py:attribute:: ANNOTATION_PROPERTY_DOMAINS


   .. py:attribute:: ANNOTATION_PROPERTY_RANGES


   .. py:attribute:: ASYMMETRIC_OBJECT_PROPERTIES


   .. py:attribute:: CLASSES


   .. py:attribute:: CLASS_ASSERTIONS


   .. py:attribute:: DATAS_HAS_VALUE


   .. py:attribute:: DATATYPES


   .. py:attribute:: DATATYPE_DEFINITION


   .. py:attribute:: DATATYPE_RESTRICTIONS


   .. py:attribute:: DATA_ALL_VALUES_FROM


   .. py:attribute:: DATA_COMPLEMENT_OF


   .. py:attribute:: DATA_EXACT_CARDINALITY


   .. py:attribute:: DATA_INTERSECTION_OF


   .. py:attribute:: DATA_MAX_CARDINALITY


   .. py:attribute:: DATA_MIN_CARDINALITY


   .. py:attribute:: DATA_ONE_OF


   .. py:attribute:: DATA_PROPERTIES


   .. py:attribute:: DATA_PROPERTY_ASSERTIONS


   .. py:attribute:: DATA_PROPERTY_DOMAIN


   .. py:attribute:: DATA_PROPERTY_RANGE


   .. py:attribute:: DATA_SOME_VALUES_FROM


   .. py:attribute:: DATA_UNION_OF


   .. py:attribute:: DECLARATIONS


   .. py:attribute:: DIFFERENT_INDIVIDUALS


   .. py:attribute:: DISJOINT_CLASSES


   .. py:attribute:: DISJOINT_DATA_PROPERTIES


   .. py:attribute:: DISJOINT_OBJECT_PROPERTIES


   .. py:attribute:: DISJOINT_UNIONS


   .. py:attribute:: EQUIVALENT_CLASSES


   .. py:attribute:: EQUIVALENT_DATA_PROPERTIES


   .. py:attribute:: EQUIVALENT_OBJECT_PROPERTIES


   .. py:attribute:: FUNCIONAL_DATA_PROPERTIES


   .. py:attribute:: FUNCTIONAL_OBJECT_PROPERTIES


   .. py:attribute:: GENERAL_CLASS_AXIOMS


   .. py:attribute:: HAS_KEYS


   .. py:attribute:: INDIVIDUALS


   .. py:attribute:: INVERSE_FUNCTIONAL_OBJECT_PROPERTIES


   .. py:attribute:: INVERSE_OBJECT_PROPERTIES


   .. py:attribute:: IRREFLEXIVE_OBJECT_PROPERTIES


   .. py:attribute:: NEGATIVE_DATA_PROPERTY_ASSERTIONS


   .. py:attribute:: NEGATIVE_OBJECT_PROPERTY_ASSERTIONS


   .. py:attribute:: OBJECTS_ALL_VALUES_FROM


   .. py:attribute:: OBJECTS_EXACT_CARDINALITY


   .. py:attribute:: OBJECTS_HAS_SELF


   .. py:attribute:: OBJECTS_HAS_VALUE


   .. py:attribute:: OBJECTS_MAX_CARDINALITY


   .. py:attribute:: OBJECTS_MIN_CARDINALITY


   .. py:attribute:: OBJECTS_ONE_OF


   .. py:attribute:: OBJECTS_SOME_VALUES_FROM


   .. py:attribute:: OBJECT_COMPLEMENT_OF


   .. py:attribute:: OBJECT_INTERSECTION_OF


   .. py:attribute:: OBJECT_PROPERTIES


   .. py:attribute:: OBJECT_PROPERTY_ASSERTIONS


   .. py:attribute:: OBJECT_PROPERTY_DOMAIN


   .. py:attribute:: OBJECT_PROPERTY_RANGE


   .. py:attribute:: OBJECT_UNION_OF


   .. py:attribute:: REFLEXIVE_OBJECT_PROPERTIES


   .. py:attribute:: SAME_INDIVIDUALS


   .. py:attribute:: SUBCLASSES


   .. py:attribute:: SUB_ANNOTATION_PROPERTIES


   .. py:attribute:: SUB_DATA_PROPERTIES


   .. py:attribute:: SUB_OBJECT_PROPERTIES


   .. py:attribute:: SYMMETRIC_OBJECT_PROPERTIES


   .. py:attribute:: TRANSITIVE_OBJECT_PROPERTIES


.. only:: html

    .. figure:: /_uml/class_pyowl2_getter_rdf_xml_getter_RDFXMLGetter.png
       :alt: UML Class Diagram for RDFXMLGetter
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RDFXMLGetter**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_getter_rdf_xml_getter_RDFXMLGetter.pdf
       :alt: UML Class Diagram for RDFXMLGetter
       :align: center
       :width: 11.7cm
       :class: uml-diagram

       UML Class Diagram for **RDFXMLGetter**

.. py:class:: RDFXMLGetter(ontology: owlready2.Ontology)

   This utility class serves as an adapter for extracting and transforming OWL concepts from an ontology represented in RDF/XML. It leverages `owlready2` for ontology management and `rdflib` for executing SPARQL queries to traverse the underlying RDF graph. Upon initialization with an `owlready2.Ontology`, the class systematically retrieves various OWL entities—such as classes, properties, individuals, and axioms—and converts them into a structured object model representing OWL 2 semantics. To ensure efficiency and consistency, it caches these transformed entities in internal dictionaries, mapping raw ontology elements to their corresponding OWL representations. The class handles a comprehensive range of constructs, including class expressions, property restrictions, and annotations, effectively bridging the gap between raw RDF triples and high-level OWL axioms.

   :param STANDARD_ANNOTATIONS: Maps internal storage IDs of standard OWL annotation properties to their corresponding AnnotationPropertyClass instances.
   :type STANDARD_ANNOTATIONS: dict[int, AnnotationPropertyClass]
   :param ontology:
   :type ontology: Ontology
   :param world: The OWL world instance associated with the ontology, used for SPARQL queries and entity retrieval.
   :type world: World
   :param graph: The RDF graph representation of the OWL ontology, used for SPARQL queries and direct graph manipulations.
   :type graph: Graph
   :param declarations: A dictionary mapping OWL entity classes to their corresponding OWLDeclaration instances.
   :type declarations: dict[EntityClass, EntityClass]
   :param classes: A dictionary mapping OWL thing classes to their corresponding OWLClass instances.
   :type classes: dict[ThingClass, OWLClass]
   :param class_expressions: A dictionary mapping OWL entity classes to their corresponding OWLClassExpression instances.
   :type class_expressions: dict[EntityClass, OWLClassExpression]
   :param object_properties: A dictionary mapping source object property classes to their corresponding OWL object property instances, serving as a cache for converted properties.
   :type object_properties: dict[ObjectPropertyClass, OWLObjectProperty]
   :param data_properties: A dictionary mapping data property classes to their corresponding OWL data property instances.
   :type data_properties: dict[DataPropertyClass, OWLDataProperty]
   :param annotation_properties: A dictionary mapping annotation property classes to their corresponding OWLAnnotationProperty instances, used to cache converted entities.
   :type annotation_properties: dict[AnnotationPropertyClass, OWLAnnotationProperty]
   :param individuals: A dictionary mapping named individuals to their corresponding OWLIndividual instances.
   :type individuals: dict[NamedIndividual, OWLIndividual]
   :param class_assertions: A dictionary mapping tuples of OWL classes and named individuals to their corresponding OWLClassAssertion axioms.
   :type class_assertions: dict[tuple[ThingClass, NamedIndividual], OWLClassAssertion]
   :param subclasses_of: A dictionary mapping tuples of OWL thing classes (subclass, superclass) to their corresponding OWLSubClassOf instances.
   :type subclasses_of: dict[tuple[ThingClass, ThingClass], OWLSubClassOf]
   :param equivalent_classes: A dictionary mapping tuples of OWL classes to their corresponding OWLEquivalentClasses axiom instances.
   :type equivalent_classes: dict[tuple[ThingClass, ...], OWLEquivalentClasses]
   :param disjoint_classes: A dictionary mapping tuples of OWL classes or AllDifferent instances to their corresponding OWLDisjointClasses axioms.
   :type disjoint_classes: dict[typing.Union[tuple[ThingClass, ...], AllDifferent], OWLDisjointClasses]
   :param data_unions_of: A dictionary mapping `Or` expressions to their corresponding `OWLDataUnionOf` instances.
   :type data_unions_of: dict[tuple[Or], OWLDataUnionOf]
   :param object_unions_of: A dictionary mapping Or expressions to their corresponding OWLObjectUnionOf instances in the ontology.
   :type object_unions_of: dict[tuple[Or], OWLObjectUnionOf]
   :param data_intersections_of: A dictionary mapping tuples of And expressions to their corresponding OWLDataIntersectionOf instances.
   :type data_intersections_of: dict[tuple[And], OWLDataIntersectionOf]
   :param object_intersections_of: A dictionary mapping And expressions to their corresponding OWLObjectIntersectionOf instances.
   :type object_intersections_of: dict[tuple[And], OWLObjectIntersectionOf]
   :param data_complements_of: A dictionary mapping `Not` expressions to their corresponding `OWLDataComplementOf` instances.
   :type data_complements_of: dict[tuple[Not], OWLDataComplementOf]
   :param object_complements_of: A dictionary mapping `Not` expressions to their corresponding `OWLObjectComplementOf` instances.
   :type object_complements_of: dict[tuple[Not], OWLObjectComplementOf]
   :param data_ones_of: A dictionary mapping `OneOf` expressions to their corresponding `OWLDataOneOf` instances in the ontology.
   :type data_ones_of: dict[tuple[OneOf], OWLDataOneOf]
   :param object_ones_of: A dictionary mapping `OneOf` expressions to their corresponding `OWLObjectOneOf` instances.
   :type object_ones_of: dict[tuple[OneOf], OWLObjectOneOf]
   :param datatypes: A dictionary mapping ontology datatype classes to their corresponding OWLDatatype instances.
   :type datatypes: dict[DatatypeClass, OWLDatatype]
   :param datatype_restrictions: A dictionary mapping constrained datatypes to their corresponding OWL datatype restriction instances in the ontology.
   :type datatype_restrictions: dict[ConstrainedDatatype, OWLDatatypeRestriction]
   :param object_property_assertions: A dictionary mapping tuples of an object property class, a source individual, and a target individual to their corresponding OWL object property assertion instances.
   :type object_property_assertions: dict[tuple[ObjectPropertyClass, NamedIndividual, NamedIndividual], OWLObjectPropertyAssertion]
   :param data_property_assertions: A dictionary mapping tuples of data properties, named individuals, and literal values to their corresponding OWLDataPropertyAssertion instances.
   :type data_property_assertions: dict[tuple[DataPropertyClass, NamedIndividual, Literal], OWLDataPropertyAssertion]
   :param same_individuals: A dictionary mapping tuples of named individuals to their corresponding OWL SameIndividual axioms, serving as a cache for assertions that multiple individuals represent the same entity.
   :type same_individuals: dict[tuple[NamedIndividual, ...], OWLSameIndividual]
   :param different_individuals: A dictionary mapping tuples of named individuals or AllDifferent instances to their corresponding OWLDifferentIndividuals instances.
   :type different_individuals: dict[typing.Union[tuple[NamedIndividual, ...], AllDifferent], OWLDifferentIndividuals]
   :param subobject_properties_of: A dictionary mapping tuples of OWL object property classes to their corresponding OWLSubObjectPropertyOf instances in the ontology.
   :type subobject_properties_of: dict[tuple[ObjectPropertyClass, ObjectPropertyClass], OWLSubObjectPropertyOf]
   :param subdata_properties_of: A dictionary mapping tuples of data properties to their corresponding OWLSubDataPropertyOf instances.
   :type subdata_properties_of: dict[tuple[DataPropertyClass, DataPropertyClass], OWLSubDataPropertyOf]
   :param subannotation_properties_of: A dictionary mapping tuples of OWL annotation property classes to their corresponding OWLSubAnnotationPropertyOf instances in the ontology.
   :type subannotation_properties_of: dict[tuple[AnnotationPropertyClass, AnnotationPropertyClass], OWLSubAnnotationPropertyOf]
   :param annotations: A dictionary mapping ontology entities to their corresponding OWLAnnotation instances, used to cache annotations retrieved from the RDF graph.
   :type annotations: dict[EntityClass, tuple[URIRef, OWLAnnotation]]
   :param general_axioms: A dictionary mapping tuples of annotated property, source, and target to OWLGeneralClassAxiom instances representing general axioms in the ontology.
   :type general_axioms: dict[EntityClass, OWLAnnotationAssertion]
   :param objects_some_values_from: A dictionary mapping Restriction entities to their corresponding OWLObjectSomeValuesFrom instances in the ontology.
   :type objects_some_values_from: dict[Restriction, OWLObjectSomeValuesFrom]
   :param objects_all_values_from: A dictionary mapping Restriction entities to their corresponding OWLObjectAllValuesFrom instances in the ontology.
   :type objects_all_values_from: dict[Restriction, OWLObjectAllValuesFrom]
   :param objects_has_value: A dictionary mapping Restriction entities to their corresponding OWLObjectHasValue instances.
   :type objects_has_value: dict[Restriction, OWLObjectHasValue]
   :param objects_has_self: A dictionary mapping Restriction entities to their corresponding OWLObjectHasSelf instances in the ontology.
   :type objects_has_self: dict[Restriction, OWLObjectHasSelf]
   :param objects_min_cardinality: A dictionary mapping Restriction entities to their corresponding OWLObjectMinCardinality instances.
   :type objects_min_cardinality: dict[Restriction, OWLObjectMinCardinality]
   :param objects_max_cardinality: A dictionary mapping Restriction entities to their corresponding OWLObjectMaxCardinality instances.
   :type objects_max_cardinality: dict[Restriction, OWLObjectMaxCardinality]
   :param objects_exact_cardinality: A dictionary mapping Restriction entities to their corresponding OWLObjectExactCardinality instances in the ontology.
   :type objects_exact_cardinality: dict[Restriction, OWLObjectExactCardinality]
   :param data_some_values_from: A dictionary mapping Restriction expressions to their corresponding OWLDataSomeValuesFrom instances in the ontology.
   :type data_some_values_from: dict[Restriction, OWLDataSomeValuesFrom]
   :param data_all_values_from: A dictionary mapping Restriction entities to their corresponding OWLDataAllValuesFrom instances in the ontology.
   :type data_all_values_from: dict[Restriction, OWLDataAllValuesFrom]
   :param data_has_value: A dictionary mapping Restriction entities to their corresponding OWLDataHasValue instances in the ontology.
   :type data_has_value: dict[Restriction, OWLDataHasValue]
   :param data_min_cardinality: A dictionary mapping Restriction entities to their corresponding OWLDataMinCardinality instances, representing minimum cardinality restrictions on data properties.
   :type data_min_cardinality: dict[Restriction, OWLDataMinCardinality]
   :param data_max_cardinality: A dictionary mapping Restriction entities to their corresponding OWLDataMaxCardinality instances.
   :type data_max_cardinality: dict[Restriction, OWLDataMaxCardinality]
   :param data_exact_cardinality: A dictionary mapping Restriction entities to their corresponding OWLDataExactCardinality instances in the ontology.
   :type data_exact_cardinality: dict[Restriction, OWLDataExactCardinality]
   :param disjoint_unions: A dictionary mapping tuples of OWL thing classes to their corresponding OWLDisjointUnion instances in the ontology.
   :type disjoint_unions: dict[tuple[ThingClass, ...], OWLDisjointUnion]
   :param equivalent_object_properties: A dictionary mapping tuples of object property classes to their corresponding OWL equivalent object properties axioms.
   :type equivalent_object_properties: dict[tuple[ObjectPropertyClass, ...], OWLEquivalentObjectProperties]
   :param disjoint_object_properties: A dictionary mapping tuples of OWL object property classes or AllDifferent instances to their corresponding OWLDisjointObjectProperties instances in the ontology.
   :type disjoint_object_properties: dict[typing.Union[tuple[ObjectPropertyClass, ...], AllDifferent], OWLDisjointObjectProperties]
   :param inverse_object_properties: A dictionary mapping tuples of OWL object property classes to their corresponding OWLInverseObjectProperties instances in the ontology.
   :type inverse_object_properties: dict[tuple[ObjectPropertyClass, ...], OWLInverseObjectProperties]
   :param functional_object_properties: A dictionary mapping object properties to their corresponding functional property axioms, used to cache and retrieve these axioms during ontology processing.
   :type functional_object_properties: dict[ObjectPropertyClass, OWLFunctionalObjectProperty]
   :param inverse_functional_object_properties: A dictionary mapping object properties to their corresponding inverse functional property axioms.
   :type inverse_functional_object_properties: dict[ObjectPropertyClass, OWLInverseFunctionalObjectProperty]
   :param transitive_object_properties: A dictionary mapping OWL object property classes to their corresponding transitive object property instances.
   :type transitive_object_properties: dict[ObjectPropertyClass, OWLTransitiveObjectProperty]
   :param symmetric_object_properties: A dictionary mapping object properties to their corresponding symmetric property axioms.
   :type symmetric_object_properties: dict[ObjectPropertyClass, OWLSymmetricObjectProperty]
   :param asymmetric_object_properties: A dictionary mapping OWL object property classes to their corresponding OWLAsymmetricObjectProperty instances.
   :type asymmetric_object_properties: dict[ObjectPropertyClass, OWLAsymmetricObjectProperty]
   :param reflexive_object_properties: A dictionary mapping OWL object property classes to their corresponding OWLReflexiveObjectProperty instances.
   :type reflexive_object_properties: dict[ObjectPropertyClass, OWLReflexiveObjectProperty]
   :param irreflexive_object_properties: A dictionary mapping object property classes to their corresponding irreflexive object property axioms.
   :type irreflexive_object_properties: dict[ObjectPropertyClass, OWLIrreflexiveObjectProperty]
   :param functional_data_properties: A dictionary mapping OWL data property classes to their corresponding OWLFunctionalDataProperty instances in the ontology.
   :type functional_data_properties: dict[DataPropertyClass, OWLFunctionalDataProperty]
   :param equivalent_data_properties: A dictionary mapping tuples of data properties to the axioms representing their equivalence relationships.
   :type equivalent_data_properties: dict[tuple[DataPropertyClass, ...], OWLEquivalentDataProperties]
   :param disjoint_data_properties: A dictionary mapping tuples of data properties or AllDifferent instances to their corresponding OWLDisjointDataProperties axioms.
   :type disjoint_data_properties: dict[typing.Union[tuple[DataPropertyClass, ...], AllDifferent], OWLDisjointDataProperties]
   :param object_property_domains: A dictionary mapping OWL object property classes to their corresponding OWLObjectPropertyDomain instances.
   :type object_property_domains: dict[ObjectPropertyClass, OWLObjectPropertyDomain]
   :param object_property_ranges: A dictionary mapping OWL object property classes to their corresponding OWLObjectPropertyRange instances in the ontology.
   :type object_property_ranges: dict[ObjectPropertyClass, OWLObjectPropertyRange]
   :param data_property_domains: A dictionary mapping data property classes to their corresponding OWL data property domain axioms.
   :type data_property_domains: dict[DataPropertyClass, OWLDataPropertyDomain]
   :param data_property_ranges: A dictionary mapping data properties to their corresponding range axioms.
   :type data_property_ranges: dict[DataPropertyClass, OWLDataPropertyRange]
   :param datatype_definitions: A dictionary mapping OWL datatype classes to their corresponding OWLDatatypeDefinition instances in the ontology.
   :type datatype_definitions: dict[DatatypeClass, OWLDatatypeDefinition]
   :param has_keys: A dictionary mapping OWL thing classes to their corresponding OWLHasKey instances, representing the properties that uniquely identify instances of each class.
   :type has_keys: dict[ThingClass, OWLHasKey]
   :param negative_object_property_assertions: A dictionary mapping a tuple of an object property, a source individual, and a target individual to the corresponding negative object property assertion instance.
   :type negative_object_property_assertions: dict[tuple[ObjectPropertyClass, NamedIndividual, NamedIndividual], OWLNegativeObjectPropertyAssertion]
   :param negative_data_property_assertions: A dictionary mapping tuples of data properties, named individuals, and literals to their corresponding negative data property assertion instances.
   :type negative_data_property_assertions: dict[tuple[DataPropertyClass, NamedIndividual, Literal], OWLNegativeDataPropertyAssertion]
   :param annotation_property_domains: A dictionary mapping OWL annotation property classes to their corresponding OWLAnnotationPropertyDomain instances in the ontology.
   :type annotation_property_domains: dict[AnnotationPropertyClass, OWLAnnotationPropertyDomain]
   :param annotation_property_ranges: A dictionary mapping annotation property classes to their corresponding range axioms, used to cache and retrieve range restrictions defined in the ontology.
   :type annotation_property_ranges: dict[AnnotationPropertyClass, OWLAnnotationPropertyRange]
   :param annotation_assertions: Maps a tuple of subject, annotation property, and value to the corresponding OWLAnnotationAssertion axiom instance.
   :type annotation_assertions: dict[tuple[typing.Union[NamedIndividual, URIRef, str], AnnotationPropertyClass, typing.Union[NamedIndividual, URIRef, Literal]], OWLAnnotationAssertion]

   :raises TypeError: Raised when the provided entity or arguments are of an invalid type for the requested conversion. This typically occurs if the input is not a recognized owlready2 entity class (e.g., ThingClass, ObjectPropertyClass), an integer identifier for standard properties, or if the argument combination does not match any available conversion logic.
   :raises ValueError: Raised when the provided axiom type is not recognized or supported for retrieval.


   .. py:method:: _get_owl_chain(marked: dict[owlready2.ThingClass, bool], chain: dict[owlready2.ThingClass, owlready2.ThingClass], annotations: dict[owlready2.EntityClass, set[pyowl2.base.annotation.OWLAnnotation]]) -> Generator[tuple[tuple[owlready2.ThingClass], Optional[list[pyowl2.base.annotation.OWLAnnotation]]], None, None]

      This method generates chains of equivalent OWL classes by traversing the relationships defined in the `chain` dictionary. It iterates through the keys of the `marked` dictionary, and for each unmarked class, it follows the linked list of equivalents to collect all related classes and their associated annotations. The traversal stops when it encounters a class that is already marked, has no further equivalent entry, or would create a cycle within the current chain. For each discovered group, the method yields a tuple containing the sequence of classes and a list of annotations, or None if no annotations are found. As a side effect, the method updates the `marked` dictionary in-place to indicate that the processed classes have been visited.

      :param marked: Tracks which OWL classes have been processed to prevent cycles and ensure each class is visited exactly once.
      :type marked: dict[ThingClass, bool]
      :param chain: A dictionary mapping each OWL class to its equivalent counterpart, used to traverse the chain of equivalence relationships.
      :type chain: dict[ThingClass, ThingClass]
      :param annotations: Dictionary mapping classes to sets of OWL annotations. Annotations for classes encountered in an equivalence chain are aggregated and yielded alongside the chain.
      :type annotations: dict[EntityClass, set[OWLAnnotation]]

      :return: A generator yielding tuples containing a sequence of equivalent OWL classes and a list of their associated annotations, or None if no annotations are present.

      :rtype: typing.Generator[tuple[tuple[ThingClass], typing.Optional[list[OWLAnnotation]]], None, None]



   .. py:method:: _get_owl_negative_property_assertion_annotations(property_type: type, params: tuple[owlready2.EntityClass, Ellipsis]) -> list[pyowl2.base.annotation.OWLAnnotation]

      Retrieves annotations associated with a specific OWL negative property assertion by executing a SPARQL query against the underlying ontology. The method dynamically constructs the query based on the provided assertion type (object or data property) and the specific parameters (source individual, property, and target). It searches for blank nodes representing the assertion and extracts any attached annotation properties and their literal values. During processing, it validates annotation properties against a cache or standard set, populating the cache if necessary, and constructs `OWLAnnotation` instances for valid entries.

      :param property_type: The class of the negative property assertion (e.g., `OWLNegativeObjectPropertyAssertion` or `OWLNegativeDataPropertyAssertion`), which determines whether the SPARQL query targets an individual or a literal value.
      :type property_type: type
      :param params: A tuple containing the source individual, the assertion property, and the target individual or value that define the negative property assertion.
      :type params: tuple[EntityClass, ...]

      :raises TypeError: Raised when the annotation property identifier obtained from the SPARQL query results is neither an integer nor an instance of AnnotationPropertyClass.

      :return: A list of OWLAnnotation objects attached to the specified negative property assertion, filtered to include only valid annotation properties.

      :rtype: list[OWLAnnotation]



   .. py:method:: _get_owl_property_from_integer(int_property: int, predicate_ref: rdflib.URIRef) -> rdflib.URIRef

      Resolves an integer identifier to its corresponding OWL property URI by first checking a global mapping of standard abbreviations. If the integer is not found in the standard mapping, the method attempts to retrieve the property from the internal graph by locating a subject associated with the integer and extracting the value associated with the provided predicate reference. This process assumes that the integer exists as a node within the graph if it is not a standard abbreviation, and it performs read-only operations without modifying the graph's state.

      :param int_property: An integer identifier used to look up the corresponding OWL property, either as a standard abbreviation or as a graph node reference.
      :type int_property: int
      :param predicate_ref: The predicate used to look up the property in the graph if the integer is not a standard OWL abbreviation.
      :type predicate_ref: URIRef

      :return: The URIRef of the OWL property associated with the integer identifier, resolved from a standard mapping or the graph.

      :rtype: URIRef



   .. py:method:: _map_functions(functions: list[Callable], *params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.object.OWLObject

      Iterates over a sequence of callable objects to find the first one that successfully processes the provided arguments. Before invoking a function, the method verifies that the number of parameters matches the function's signature; functions with mismatched argument counts are skipped. Each matching function is called with the provided arguments, and the first truthy result is returned immediately. If all functions are skipped or return falsy values, a TypeError is raised. Note that any exceptions raised during the execution of a function are not caught and will propagate to the caller.

      :param functions: A list of callable functions to be applied to the provided parameters. The functions are tried in order until one returns a truthy result.
      :type functions: list[typing.Callable]
      :param params: A variable-length tuple of OWLObject instances passed as arguments to the functions. The number of parameters must match the signature of a function for it to be invoked.
      :type params: tuple[OWLObject, ...]

      :raises TypeError: Raised when none of the provided functions accept the given parameters or return a non-None result.

      :return: The first truthy result returned by a function in the list that accepts the provided parameters.

      :rtype: OWLObject



   .. py:method:: _to_annotation_property(property: Union[int, owlready2.AnnotationPropertyClass]) -> Union[rdflib.URIRef, owlready2.AnnotationPropertyClass]

      This method normalizes a property identifier into a standardized representation for RDF/XML processing, supporting both integer codes and existing property class instances. It first consults an internal cache to return previously processed values without duplication. If the input is an integer, the method attempts to resolve it against a dictionary of standard annotations or a universal abbreviation mapping; upon success, it generates a `URIRef`, creates and stores a corresponding `OWLAnnotationProperty` instance in the cache, and returns the `URIRef`. When the input is an instance of `AnnotationPropertyClass`, the method creates an `OWLAnnotationProperty` based on the input's IRI, stores it in the cache, and returns the original input object. Unresolvable integer inputs result in a `None` return value, whereas inputs of unsupported types raise a `TypeError`.

      :param property: The annotation property to resolve, provided as either an integer identifier corresponding to a standard annotation or an existing AnnotationPropertyClass instance.
      :type property: typing.Union[int, AnnotationPropertyClass]

      :raises TypeError: Raised when the provided property is not an integer or an instance of AnnotationPropertyClass.

      :return: Returns the resolved annotation property as a URIRef for integer inputs or the original AnnotationPropertyClass instance. Returns None if an integer input cannot be resolved to a URI.

      :rtype: typing.Union[URIRef, AnnotationPropertyClass]



   .. py:method:: exists_annotation_property(property: rdflib.URIRef) -> bool

      Verifies the presence of an annotation property within the ontology by checking if an element with the specified IRI is explicitly typed as an `owl:AnnotationProperty`. This method performs a read-only query on the underlying data structure and returns a boolean value indicating whether the property definition exists. It is primarily used to validate the availability of metadata-related properties before further operations are attempted.

      :param property: The IRI of the annotation property to check for existence in the ontology.
      :type property: URIRef

      :return: True if an annotation property with the specified IRI exists in the ontology, False otherwise.

      :rtype: bool



   .. py:method:: exists_class(class_: rdflib.URIRef) -> bool

      Verifies the presence of a class within the ontology by checking for an entity with the specified IRI that is explicitly typed as `owl:Class`. This method performs a targeted lookup to ensure that the provided IRI corresponds to a class definition rather than a generic resource or a different type of ontology element. It returns `True` if such a class is found, and `False` otherwise.

      :param class_: The IRI of the class to check for existence in the ontology.
      :type class_: URIRef

      :return: True if a class with the given IRI exists in the ontology, False otherwise.

      :rtype: bool



   .. py:method:: exists_data_property(data: rdflib.URIRef) -> bool

      Verifies whether a data property with the specified Internationalized Resource Identifier (IRI) is present in the ontology. The method performs a strict check to determine if the provided IRI is defined as an OWL DatatypeProperty, delegating the actual query to the `exists_element_by_iri_type` helper. It returns a boolean value indicating the presence of the property, ensuring that object properties or other entity types are not erroneously identified as data properties.

      :param data: The IRI of the data property to check for existence in the ontology.
      :type data: URIRef

      :return: True if a data property with the given IRI exists in the ontology, False otherwise.

      :rtype: bool



   .. py:method:: exists_data_range(data_range: rdflib.URIRef) -> bool

      Determines whether a specific data range is defined within the ontology by verifying the existence of an element with the provided IRI that is typed as an OWL DataRange. The method delegates the lookup to an internal helper that checks the RDF type of the resource against the DataRange class. It returns a boolean value indicating presence, performing a read-only query without modifying the underlying graph.

      :param data_range: The IRI of the data range to check for existence in the ontology.
      :type data_range: URIRef

      :return: True if a data range with the specified IRI exists in the ontology, False otherwise.

      :rtype: bool



   .. py:method:: exists_datatype(datatype: rdflib.URIRef) -> bool

      This method verifies the presence of a specific datatype within the ontology by checking if an element with the provided IRI is explicitly typed as an RDF Schema Datatype. It accepts a URIRef representing the datatype's identifier and returns True only if the IRI exists and matches the `RDFS.Datatype` type; otherwise, it returns False. The operation is read-only and delegates the lookup logic to the `exists_element_by_iri_type` method.

      :param datatype: The IRI of the datatype to check for existence in the ontology.
      :type datatype: URIRef

      :return: True if a datatype with the given IRI exists in the ontology, False otherwise.

      :rtype: bool



   .. py:method:: exists_element_by_iri_type(iri: rdflib.URIRef, type=URIRef) -> bool

      Queries the ontology to determine if an element with the specified Internationalized Resource Identifier (IRI) and type exists. The method utilizes the underlying world's search functionality, passing the IRI and an abbreviated version of the type parameter to filter results. It returns True if the search returns at least one matching entity, and False otherwise. This is a read-only operation that does not alter the ontology; if the type argument is omitted, it defaults to the generic URIRef class, effectively checking for the existence of the IRI across all entity types.

      :param iri: The IRI of the element to check for existence in the ontology.
      :type iri: URIRef
      :param type: The specific class or type of the entity to check for. Defaults to the base entity type, which matches any entity with the provided IRI.
      :type type: typing.Any

      :return: True if an element with the specified IRI and type exists in the ontology, False otherwise.

      :rtype: bool



   .. py:method:: exists_object_property(object: rdflib.URIRef) -> bool

      This method determines whether an object property with the specified IRI is defined in the ontology. It specifically checks for the existence of an element that is typed as an OWL Object Property, ensuring that the identifier corresponds to the correct semantic category. The function returns True if such a property is found and False otherwise, including cases where the IRI does not exist or represents a different type of entity. This operation is read-only and does not modify the underlying ontology structure.

      :param object: The IRI of the object property to check for existence in the ontology.
      :type object: URIRef

      :return: True if an object property with the specified IRI exists in the ontology, False otherwise.

      :rtype: bool



   .. py:method:: get(element: AxiomsType) -> list[owlready2.EntityClass]

      Retrieves a list of ontology entities that correspond to a specific axiom type, identified by the provided `AxiomsType` enumeration value. Acting as a dispatcher, this method delegates the extraction logic to specialized internal handlers for each supported category, such as classes, properties, or logical restrictions. For the `DECLARATIONS` type, it aggregates entities from all major categories, including classes, object and datatype properties, individuals, and datatypes. If the input does not match a known axiom type, a `ValueError` is raised.

      :param element: An enumeration value specifying the type of axiom or entity category to retrieve.
      :type element: AxiomsType

      :raises ValueError: Raised if the provided `element` is not a recognized or supported axiom type.

      :return: A list of EntityClass instances corresponding to the specified axiom type.

      :rtype: list[EntityClass]



   .. py:method:: get_owl_annotation_axiom(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom

      This method attempts to construct an OWL annotation axiom by interpreting a variable-length sequence of OWL objects. It sequentially attempts to map the input parameters to specific axiom types, such as annotation assertions, sub-annotation property relationships, or annotation property domains and ranges. The process relies on an internal mapping utility to identify the first compatible factory method for the given arguments. If the provided parameters do not match the expected signature for any supported annotation axiom, the method raises a TypeError.

      :param params: A variable number of OWLObject instances representing the components required to construct an annotation axiom. The method attempts to match these arguments against valid patterns for assertion, sub-property, domain, or range axioms.
      :type params: tuple[OWLObject, ...]

      :return: The OWLAnnotationAxiom constructed from the provided parameters.

      :rtype: OWLAnnotationAxiom



   .. py:method:: get_owl_annotation_properties() -> list[pyowl2.base.annotation_property.OWLAnnotationProperty]

      Retrieves and constructs a list of all OWL annotation properties defined in the ontology by executing a SPARQL query that searches for both direct type declarations and reified axioms. The method iterates through the query results, ensuring each candidate is an instance of `AnnotationPropertyClass` before invoking helper methods to generate the corresponding OWL objects and their declarations, which populates the internal state of the getter. Finally, it returns a list of these properties by filtering the internal declarations registry to include only those identified as annotation properties.

      :return: A list of all OWL annotation properties defined in the ontology, represented as `OWLAnnotationProperty` instances.

      :rtype: list[OWLAnnotationProperty]



   .. py:method:: get_owl_annotation_property_domains() -> list[pyowl2.axioms.annotations.OWLAnnotationPropertyDomain]

      Retrieves and constructs a list of domain restrictions defined for OWL annotation properties within the ontology. The method executes a SPARQL query to locate properties typed as `owl:AnnotationProperty` that possess an `rdfs:domain` relationship. It iterates through the query results, filtering out entities that are not instances of `AnnotationPropertyClass`, and retrieves the specific domain value along with any associated axiom annotations. These details are used to generate `OWLAnnotationPropertyDomain` instances, which are stored internally and returned as a list.

      :return: A list of OWLAnnotationPropertyDomain instances representing the domains associated with annotation properties in the ontology.

      :rtype: list[OWLAnnotationPropertyDomain]



   .. py:method:: get_owl_annotation_property_ranges() -> list[pyowl2.axioms.annotations.OWLAnnotationPropertyRange]

      Retrieves a list of OWL annotation property ranges defined within the ontology by executing a SPARQL query that identifies properties typed as `owl:AnnotationProperty` possessing an `rdfs:range`. The method iterates through the query results, filtering out any entries where the property is not an instance of `AnnotationPropertyClass`. For valid properties, it extracts the range value and any associated annotations, utilizing the `to_owl_annotation_property_range` method to construct and store the corresponding object. Finally, it returns the accumulated list of `OWLAnnotationPropertyRange` instances.

      :return: A list of OWLAnnotationPropertyRange instances representing all annotation properties in the ontology that have a specified range.

      :rtype: list[OWLAnnotationPropertyRange]



   .. py:method:: get_owl_annotations() -> list[pyowl2.base.annotation.OWLAnnotation]

      Retrieves and constructs a list of OWL annotations found within the RDF graph by scanning for triples that utilize annotation properties. The method first ensures that individuals and annotation properties are loaded, potentially triggering side effects in those internal caches. It identifies annotations by checking every triple in the graph, accepting predicates that are either standard annotation properties (such as `rdfs:label`, `rdfs:comment`, or specific SKOS and Dublin Core terms) or properties explicitly defined as annotation properties in the ontology. For each valid triple, the method instantiates an `OWLAnnotation` object, converting the object value to a literal, individual, or IRI as appropriate, and caches the result within the instance before returning the full list.

      :return: A list of OWLAnnotation instances representing all annotations found in the ontology graph. These annotations are identified by triples where the predicate is a standard annotation property (e.g., rdfs:label) or a property explicitly defined as an annotation property within the ontology.

      :rtype: list[OWLAnnotation]



   .. py:method:: get_owl_assertion(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.assertion.OWLAssertion

      Attempts to construct an OWLAssertion from a variable number of OWLObject arguments by applying a prioritized list of conversion strategies. The method internally delegates to specific handlers for various assertion types, including class assertions, object and data property assertions (both positive and negative), and same/different individual axioms. It returns the first successfully generated assertion; if the provided parameters do not match the signature of any internal conversion function, a TypeError is raised.

      :param params: A variable number of OWLObject instances to be converted into an OWLAssertion. The specific combination of objects determines which conversion function is applied.
      :type params: tuple[OWLObject, ...]

      :return: The OWLAssertion object resulting from the first successful conversion of the input parameters.

      :rtype: OWLAssertion



   .. py:method:: get_owl_asymmetric_object_properties() -> list[pyowl2.expressions.object_property.OWLObjectProperty]

      Retrieves all asymmetric object properties defined in the ontology by executing a SPARQL query to identify properties typed as `owl:AsymmetricProperty`. For each property found, the method converts it into an internal object representation and stores it, effectively populating the internal cache of asymmetric object properties as a side effect. The function returns a list of these converted properties, representing the complete set of asymmetric object properties available in the ontology.

      :return: A list of all asymmetric object properties defined in the ontology using `owl:AsymmetricProperty`.

      :rtype: list[OWLObjectProperty]



   .. py:method:: get_owl_axiom(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.axiom.OWLAxiom

      Attempts to construct an OWL axiom from a variable number of OWL object parameters by delegating to specialized helper methods. It iterates through a predefined sequence of axiom-specific functions—such as those handling declarations, class axioms, or property assertions—applying the provided arguments to each until a valid axiom is produced. If the provided parameters do not match the signature or requirements of any of the internal conversion functions, a TypeError is raised to indicate the inability to construct an axiom.

      :param params: A variable number of OWLObject instances representing the components required to construct a specific OWLAxiom.
      :type params: tuple[OWLObject, ...]

      :return: The OWLAxiom resulting from the first successful conversion of the provided OWLObject parameters.

      :rtype: OWLAxiom



   .. py:method:: get_owl_axiom_annotations_for(source: owlready2.EntityClass, property: Optional[owlready2.EntityClass] = None, target: Optional[owlready2.EntityClass] = None) -> Optional[list[pyowl2.base.annotation.OWLAnnotation]]

      This method retrieves annotations associated with a specific OWL axiom by executing a SPARQL query that searches for instances of `owl:Axiom` or `owl:Annotation`. The query filters results based on the mandatory `source` entity and the optional `property` and `target` entities, treating any omitted optional arguments as wildcards. For each matching annotation, the method converts the predicate to an `OWLAnnotationProperty` and wraps the literal value into an `OWLLiteral` to create an `OWLAnnotation` object. It returns a list of these annotations if any are found, or `None` if no annotations exist for the specified criteria.

      :param source: The subject entity of the OWL axiom for which annotations are being retrieved.
      :type source: EntityClass
      :param property: The specific property of the axiom to filter by. If None, annotations are retrieved for axioms with any property.
      :type property: typing.Optional[EntityClass]
      :param target: The target entity of the axiom to filter by. If None, retrieves annotations for axioms with any target.
      :type target: typing.Optional[EntityClass]

      :return: A list of OWLAnnotation instances associated with the specified axiom, or None if no annotations are found.

      :rtype: typing.Optional[list[OWLAnnotation]]



   .. py:method:: get_owl_class_assertions() -> list[pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]

      Retrieves all OWL class assertions from the ontology by executing a SPARQL query that identifies individuals explicitly typed as `owl:NamedIndividual` and associated with specific classes. The query filters out the generic `owl:NamedIndividual` type to ensure only specific class memberships are returned. For each matching pair, the method invokes `to_owl_class_assertion` to process and store the assertion, effectively populating the internal `class_assertions` collection. The method returns a list of the resulting `OWLClassAssertion` objects.

      :return: A list of OWLClassAssertion objects representing the valid class assertions (type declarations) for named individuals found in the ontology.

      :rtype: list[OWLClassAssertion]



   .. py:method:: get_owl_class_axiom(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.class_axiom.OWLClassAxiom

      Attempts to construct an OWL class axiom from the provided OWLObject parameters by sequentially applying a set of specific conversion strategies. The method tests the input against patterns for SubClassOf, EquivalentClasses, DisjointClasses, and DisjointUnion axioms, returning the first valid instance generated. If the provided parameters do not match any of the supported axiom structures, a TypeError is raised.

      :param params: A variable-length sequence of OWL objects (e.g., classes or expressions) that define the components of a class axiom, such as a subclass, equivalent classes, or disjoint classes relationship.
      :type params: tuple[OWLObject, ...]

      :return: The OWL class axiom constructed from the provided parameters based on the first applicable conversion function.

      :rtype: OWLClassAxiom



   .. py:method:: get_owl_class_expression(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Attempts to construct an OWL class expression from the provided OWL object parameters by sequentially applying a suite of specific conversion methods. The method maintains an ordered list of conversion functions corresponding to various OWL constructs, such as class intersections, unions, complements, and property restrictions. It delegates to the internal `_map_functions` utility to apply these converters to the input arguments, returning the result of the first successful conversion. If the provided parameters do not match the signature or requirements of any registered conversion function, a TypeError is raised.

      :param params: Input objects to be interpreted and converted into a class expression by matching them against the available conversion functions.
      :type params: tuple[OWLObject, ...]

      :return: An OWLClassExpression derived from the provided parameters by applying the first applicable conversion strategy.

      :rtype: OWLClassExpression



   .. py:method:: get_owl_classes() -> list[pyowl2.base.owl_class.OWLClass]

      Retrieves all OWL classes defined in the ontology by executing SPARQL queries and constructing corresponding object instances. The method primarily identifies subjects explicitly typed as `owl:Class` or declared via axioms, filtering out complex class expressions such as intersections, unions, and restrictions. It additionally handles specific edge cases for OWL 1 DL compatibility, including resolving classes defined as unions or intersections with a single member to that member, and processing special constructs for `owl:Thing` and `owl:Nothing`. As a side effect, this method populates the internal class and declaration registries. Finally, it returns a list of the created `OWLClass` objects.

      :return: A list of OWLClass instances representing all classes defined in the ontology, including those identified through direct declarations, axioms, and OWL 1 DL compatibility patterns such as single-member unions or intersections.

      :rtype: list[OWLClass]



   .. py:method:: get_owl_data_all_values_from() -> list[pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom]

      Retrieves all OWL data property restrictions of type `owl:allValuesFrom` from the ontology by executing a SPARQL query. The query identifies blank nodes representing restrictions that link a property—defined either via `owl:onProperty` or a list structure using `owl:onProperties`—to a specific data range. As a side effect, this method iterates through the query results and invokes `to_owl_data_all_values_from` to populate an internal cache of restriction objects. Finally, it returns a list of `OWLDataAllValuesFrom` instances representing the valid restrictions found in the graph.

      :return: A list of OWLDataAllValuesFrom instances representing all valid data property restrictions (owl:allValuesFrom) found in the ontology.

      :rtype: list[OWLDataAllValuesFrom]



   .. py:method:: get_owl_data_complement_of() -> list[pyowl2.data_range.data_complement_of.OWLDataComplementOf]

      Retrieves and constructs `OWLDataComplementOf` instances by querying the RDF graph for data range definitions that utilize `owl:datatypeComplementOf` or `owl:oneOf`. The method executes a SPARQL query targeting blank nodes representing these complements, filtering out self-referential definitions. For each match, it attempts to resolve the target datatype within the ontology; if the datatype exists, it instantiates the complement relationship and stores it internally. As a side effect, it prints a warning to standard output regarding the lack of native support for this construct in the underlying library. The method returns a list of all successfully created `OWLDataComplementOf` objects.

      :return: A list of OWLDataComplementOf instances representing the datatype complement relationships found in the ontology.

      :rtype: list[OWLDataComplementOf]



   .. py:method:: get_owl_data_exact_cardinality() -> list[pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality]

      Executes a SPARQL query to identify and retrieve OWL data exact cardinality restrictions from the ontology, specifically targeting blank nodes that define restrictions using `owl:cardinality` or `owl:qualifiedCardinality` in conjunction with `owl:onDataRange`. The query filters for restrictions where the cardinality value is a non-negative integer, ensuring only valid numeric constraints are processed. For each identified restriction, the method processes the blank node to generate an `OWLDataExactCardinality` instance, populating an internal cache, and finally returns the complete list of these processed restrictions. This process effectively maps the raw RDF structure of property restrictions into a structured object representation.

      :return: A list of OWL data exact-cardinality restrictions extracted from the ontology, corresponding to valid `owl:cardinality` or `owl:qualifiedCardinality` restrictions on data properties.

      :rtype: list[OWLDataExactCardinality]



   .. py:method:: get_owl_data_has_value() -> list[pyowl2.class_expression.data_has_value.OWLDataHasValue]

      Executes a SPARQL query to locate blank nodes representing OWL restrictions defined with `owl:onProperty` and `owl:hasValue`, specifically filtering for cases where the value is a literal. This ensures that only data property restrictions are captured, as opposed to object property restrictions. The method iterates over the query results, processing each restriction to construct and store `OWLDataHasValue` instances, and finally returns the complete list of these objects from the internal cache.

      :return: A list of OWLDataHasValue instances representing all data property restrictions of type owl:hasValue found in the ontology, where a property is constrained to a specific literal value.

      :rtype: list[OWLDataHasValue]



   .. py:method:: get_owl_data_intersection_of() -> list[pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf]

      Retrieves and processes OWL data range intersections defined using `owl:intersectionOf` by executing a SPARQL query against the ontology. The query specifically targets blank nodes that are typed as `rdfs:Datatype` and contain an intersection list with at least two members, filtering out invalid or incomplete definitions. As a side effect, this method populates an internal registry by invoking `to_owl_data_intersection_of` for each identified blank node. It returns a list of `OWLDataIntersectionOf` instances representing all valid data intersections found in the underlying data model.

      :return: A list of OWLDataIntersectionOf instances representing the data range intersections found in the ontology, filtered to include only those with at least two members.

      :rtype: list[OWLDataIntersectionOf]



   .. py:method:: get_owl_data_max_cardinality() -> list[pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality]

      Retrieves all OWL data property restrictions defining a maximum cardinality from the ontology by executing a SPARQL query. The query targets blank nodes representing `owl:Restriction` instances that possess an `owl:onProperty` and either a simple `owl:maxCardinality` or a qualified `owl:maxQualifiedCardinality` paired with an `owl:onDataRange`. It filters results to ensure the cardinality value is a non-negative integer. As a side effect, the method populates an internal collection by processing each valid restriction node, ultimately returning a list of the corresponding `OWLDataMaxCardinality` objects.

      :return: A list of OWLDataMaxCardinality instances representing all valid data property max-cardinality restrictions found in the ontology.

      :rtype: list[OWLDataMaxCardinality]



   .. py:method:: get_owl_data_min_cardinality() -> list[pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality]

      This method retrieves all OWL data minimum cardinality restrictions from the ontology by executing a SPARQL query. It specifically targets blank nodes representing `owl:Restriction` instances that define a minimum cardinality constraint on a data property using either `owl:minCardinality` or `owl:minQualifiedCardinality`. For qualified cardinality restrictions, the query ensures that an `owl:onDataRange` is also present. The method filters the results to include only restrictions where the cardinality value is a non-negative integer. It then iterates through the valid results, converting each into an `OWLDataMinCardinality` instance via a helper method, and returns the complete list of these restrictions.

      :return: A list of OWLDataMinCardinality instances representing all data property restrictions with minimum cardinality constraints found in the ontology.

      :rtype: list[OWLDataMinCardinality]



   .. py:method:: get_owl_data_one_of() -> list[pyowl2.data_range.data_one_of.OWLDataOneOf]

      Retrieves all enumerated data ranges defined by `owl:oneOf` within the ontology by executing a SPARQL query. The query specifically targets entities typed as `rdfs:Datatype` or `owl:DataRange` that contain a list of literal values, filtering out any enumerations that lack members. For each valid identifier returned by the query, the method invokes `to_owl_data_one_of` to process the data, which populates an internal collection, and finally returns a list of the corresponding `OWLDataOneOf` instances.

      :return: A list of `OWLDataOneOf` instances representing the enumerated data ranges found in the ontology.

      :rtype: list[OWLDataOneOf]



   .. py:method:: get_owl_data_property_assertions() -> list[pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion]

      Retrieves all data property assertions defined in the ontology by executing a SPARQL query that filters for triples involving a named individual, a datatype property, and a literal value. The method iterates over the query results, ensuring that the object value is explicitly treated as a literal if it is not already an instance of the `Literal` class. Each valid triple is processed into an `OWLDataPropertyAssertion` object via a helper method, which populates an internal collection, and the method returns the full list of these assertions.

      :return: A list of OWL data property assertions representing triples where a named individual is associated with a literal value through a datatype property.

      :rtype: list[OWLDataPropertyAssertion]



   .. py:method:: get_owl_data_property_axiom(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom

      Attempts to construct an OWL data property axiom by evaluating the provided OWL objects against a set of specific conversion strategies. It supports the creation of sub-data-property, equivalent data properties, disjoint data properties, domain, range, and functional data property axioms. The method delegates the actual conversion logic to the internal `_map_functions` helper, which applies these strategies sequentially and returns the first successfully generated axiom. If the input parameters do not correspond to any of the supported axiom structures, a TypeError is raised.

      :param params: The OWL objects serving as the components (e.g., properties, domains, or ranges) required to construct a specific data property axiom.
      :type params: tuple[OWLObject, ...]

      :return: The OWLDataPropertyAxiom instance representing the logical relationship defined by the provided parameters.

      :rtype: OWLDataPropertyAxiom



   .. py:method:: get_owl_data_property_domains() -> list[pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain]

      Executes a SPARQL query to identify all data property domains defined within the ontology, specifically targeting properties typed as `owl:DatatypeProperty` that possess an `rdfs:domain` relationship to a class. For each valid property-class pair found, the method processes the relationship using the `to_owl_data_property_domain` helper, which populates an internal registry. The method concludes by returning a list of `OWLDataPropertyDomain` instances representing these processed relationships.

      :return: A list of OWL data property domain instances representing the domains of datatype properties defined using rdfs:domain in the ontology.

      :rtype: list[OWLDataPropertyDomain]



   .. py:method:: get_owl_data_property_ranges() -> list[pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange]

      Retrieves data property ranges from the ontology by executing a SPARQL query that identifies properties explicitly typed as `owl:DatatypeProperty` and associated with a class via `rdfs:range`. For each property discovered, the method invokes `to_owl_data_property_range` to construct and store the corresponding range object within the internal `data_property_ranges` dictionary. The function returns a list of all `OWLDataPropertyRange` instances currently stored in that dictionary, effectively populating the internal cache during execution.

      :return: A list of OWLDataPropertyRange instances representing the data property ranges defined in the ontology, identified by querying for properties of type owl:DatatypeProperty that have an rdfs:range.

      :rtype: list[OWLDataPropertyRange]



   .. py:method:: get_owl_data_range(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.data_range.OWLDataRange

      Attempts to construct an OWLDataRange instance from the provided OWLObject parameters by evaluating a predefined sequence of conversion strategies. This method aggregates specific factory functions—such as those for datatypes, intersections, unions, complements, one-of enumerations, and datatype restrictions—and delegates the matching process to the internal _map_functions utility. The utility applies each strategy to the input arguments in order, returning the result of the first successful conversion. If the supplied parameters cannot be interpreted by any of the registered strategies, the method raises a TypeError, indicating that the input does not correspond to a valid OWL data range structure.

      :param params: A variable-length sequence of OWLObject instances to be processed by conversion functions to generate an OWLDataRange.
      :type params: tuple[OWLObject, ...]

      :return: The OWLDataRange obtained by converting the provided parameters using the first applicable conversion function.

      :rtype: OWLDataRange



   .. py:method:: get_owl_data_some_values_from() -> list[pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom]

      Retrieves all OWL data property restrictions of type `owl:someValuesFrom` by executing a SPARQL query against the ontology. The query specifically targets blank nodes representing restrictions that define a data range and are associated with one or more properties via `owl:onProperty` or `owl:onProperties`, including support for property lists using RDF collection syntax. As a side effect, the method iterates through the query results and invokes `to_owl_data_some_values_from` for each valid restriction to populate an internal collection. It returns a list of `OWLDataSomeValuesFrom` instances corresponding to the restrictions found, ensuring that only restrictions with at least one valid property are included.

      :return: A list of OWLDataSomeValuesFrom instances representing all valid existential restrictions on data properties (owl:someValuesFrom) found in the ontology.

      :rtype: list[OWLDataSomeValuesFrom]



   .. py:method:: get_owl_data_union_of() -> list[pyowl2.data_range.data_union_of.OWLDataUnionOf]

      Retrieves all OWL data union relationships defined in the ontology by executing a SPARQL query that identifies blank nodes representing a union of datatypes. The query specifically targets nodes typed as `rdfs:Datatype` that possess an `owl:unionOf` property, filtering the results to include only those unions containing at least two members. For each valid union found, the method processes the data to populate an internal collection and returns a list of the corresponding `OWLDataUnionOf` instances.

      :return: A list of OWLDataUnionOf instances representing all valid data unions found in the ontology. Only unions defined as blank nodes of type rdfs:Datatype with at least two members are included.

      :rtype: list[OWLDataUnionOf]



   .. py:method:: get_owl_datatype_definition(datatype: Union[owlready2.DatatypeClass, owlready2.ConstrainedDatatype], data_range: Union[owlready2.DatatypeClass, owlready2.ConstrainedDatatype, owlready2.And]) -> Optional[pyowl2.axioms.datatype_definition.OWLDatatypeDefinition]

      Retrieves an OWL datatype definition for the specified datatype and data range, employing an internal cache to store and retrieve previously computed definitions. If the provided datatype is not a valid instance of `DatatypeClass` or `ConstrainedDatatype`, or if the conversion to an OWL datatype fails, the method returns None. When a definition is not cached, the method constructs it by converting the datatype and processing the data range according to its specific type—handling intersections, restrictions, or standard datatypes accordingly—and attaching relevant annotations found in the graph. The newly created definition is stored in the instance's cache before being returned.

      :param datatype: The source datatype instance (DatatypeClass or ConstrainedDatatype) for which the OWL datatype definition is to be retrieved or constructed.
      :type datatype: typing.Union[DatatypeClass, ConstrainedDatatype]
      :param data_range: The data range defining the value space or constraints for the datatype, which can be a constrained datatype, an intersection expression, or a base datatype.
      :type data_range: typing.Union[DatatypeClass, ConstrainedDatatype, And]

      :return: The OWLDatatypeDefinition for the specified datatype and data range, or None if the datatype is invalid or cannot be converted.

      :rtype: typing.Optional[OWLDatatypeDefinition]



   .. py:method:: get_owl_datatype_definitions() -> list[pyowl2.axioms.datatype_definition.OWLDatatypeDefinition]

      Retrieves a list of OWL datatype definitions defined in the ontology using `owl:equivalentClass` restrictions. The method executes a SPARQL query to identify classes linked to blank node restrictions that possess facets and values, iterating through these results to process each definition. It relies on `get_owl_datatype_definition` to handle the construction of individual definitions, which populates an internal collection before the values are returned as a list.

      :return: A list of OWL datatype definitions found in the ontology, specifically those defined using `owl:equivalentClass` with a datatype restriction.

      :rtype: list[OWLDatatypeDefinition]



   .. py:method:: get_owl_datatype_properties() -> list[pyowl2.expressions.data_property.OWLDataProperty]

      Retrieves all OWL datatype properties from the ontology by executing a SPARQL query that searches for both direct type assertions and axioms defining properties as `owl:DatatypeProperty`. During iteration, it filters out any results that are not instances of `DataPropertyClass`. This method has side effects, as it invokes helper methods to generate and store the property instances and their declarations within the object's internal state. It returns a list of `OWLDataProperty` instances corresponding to the valid datatype properties found.

      :return: A list of OWLDataProperty instances representing all datatype properties defined in the ontology.

      :rtype: list[OWLDataProperty]



   .. py:method:: get_owl_datatype_restrictions() -> list[pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction]

      Executes a SPARQL query to identify and retrieve OWL datatype restrictions defined via `owl:withRestrictions` within the ontology. The search specifically targets blank nodes that act as datatypes, ensuring they are associated with a base datatype via `owl:onDatatype` and contain at least one specific restriction facet. As a side effect, this method populates an internal registry of restrictions by processing each discovered blank node through a conversion helper. The final output is a list of `OWLDatatypeRestriction` objects representing all valid, restricted datatypes found.

      :return: A list of OWLDatatypeRestriction objects representing all valid datatype restrictions found in the ontology. The list includes only restrictions defined with owl:withRestrictions that contain at least one facet.

      :rtype: list[OWLDatatypeRestriction]



   .. py:method:: get_owl_datatypes() -> list[pyowl2.base.datatype.OWLDatatype]

      Retrieves all defined OWL datatypes from the ontology by executing a SPARQL query that identifies entities typed as `rdfs:Datatype` or declared via OWL axioms. The query explicitly excludes datatypes that are defined as complements of other datatypes, as these are not supported by the underlying `owlready2` library. As a side effect of retrieval, this method instantiates and registers both the datatype objects and their corresponding declaration axioms within the internal state of the object. Finally, it returns a list of the instantiated `OWLDatatype` objects found in the ontology.

      :return: A list of OWLDatatype instances representing the valid datatypes defined in the ontology, excluding datatype complements.

      :rtype: list[OWLDatatype]



   .. py:method:: get_owl_declaration(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.axioms.declaration.OWLDeclaration

      This method attempts to construct an OWLDeclaration axiom by dispatching the provided OWLObject parameters to a specific conversion handler based on their type. It iterates through a predefined set of strategies designed to handle classes, datatypes, object properties, data properties, annotation properties, and named individuals. The process relies on the internal `_map_functions` utility to apply these strategies in order, returning the first successfully generated declaration. If the input parameters cannot be resolved into a valid declaration by any of the available handlers, the method raises a TypeError.

      :param params: One or more OWL objects to be converted into an OWL declaration. The method attempts to match these inputs to a specific declaration type, such as a class, datatype, property, or individual.
      :type params: tuple[OWLObject, ...]

      :return: The OWLDeclaration derived from the provided OWLObject parameters using the first applicable conversion function.

      :rtype: OWLDeclaration



   .. py:method:: get_owl_declaration_annotations_for(source: owlready2.EntityClass, target: owlready2.EntityClass = None) -> Optional[list[pyowl2.base.annotation.OWLAnnotation]]

      This method retrieves OWL annotations for a specific entity declaration by querying the RDF graph for triples where the subject is the source entity and the predicate is an annotation property. It optionally filters the results based on a target entity class type, allowing the retrieval of annotations specific to a certain declaration context. The method processes the query results by converting the annotation properties and literal values into `OWLAnnotation` instances, returning a list of these objects if matches are found, or None otherwise.

      :param source: The source entity of the declaration for which annotations are to be retrieved.
      :type source: EntityClass
      :param target: The target entity of the declaration. Defaults to None, which retrieves annotations for any target.
      :type target: EntityClass

      :return: A list of OWLAnnotation instances associated with the specified declaration, or None if no annotations are found.

      :rtype: typing.Optional[list[OWLAnnotation]]



   .. py:method:: get_owl_different_individuals() -> list[pyowl2.axioms.assertion.OWLDifferentIndividuals]

      Retrieves all assertions of distinctness between individuals from the ontology by executing two SPARQL queries. The first query identifies direct `owl:differentFrom` relationships between pairs of named individuals, explicitly filtering out cases where an individual is asserted to be different from itself. The second query detects `owl:AllDifferent` axioms—specifically those defined on blank nodes—which specify sets of individuals that are mutually distinct via `owl:members` or `owl:distinctMembers`. For each valid assertion found, the method invokes a helper function to construct `OWLDifferentIndividuals` instances, populating an internal collection before returning the complete list of these distinctness axioms.

      :return: A list of OWLDifferentIndividuals objects representing all distinctness assertions between named individuals in the ontology, including both direct owl:differentFrom statements and owl:AllDifferent axioms.

      :rtype: list[OWLDifferentIndividuals]



   .. py:method:: get_owl_disjoint_classes() -> list[pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses]

      Retrieves all disjoint class relationships defined in the ontology by executing two distinct SPARQL queries. The first query identifies pairs of classes linked directly by the `owl:disjointWith` property, while the second query detects groups of mutually disjoint classes defined via the `owl:AllDisjointClasses` construct. For each result, the method processes the identified classes to create `OWLDisjointClasses` instances, ensuring that only valid class expressions are included. The method returns a list of these instances, which are derived from the internal collection populated during the query processing.

      :return: A list of OWLDisjointClasses instances representing all disjoint class relationships in the ontology, derived from both direct owl:disjointWith statements and owl:AllDisjointClasses constructs.

      :rtype: list[OWLDisjointClasses]



   .. py:method:: get_owl_disjoint_data_properties() -> list[pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties]

      Retrieves disjoint data property relationships from the ontology by executing SPARQL queries to identify pairs and sets of mutually disjoint datatype properties. The method first searches for direct `owl:propertyDisjointWith` assertions between two distinct `owl:DatatypeProperty` instances, explicitly filtering out self-referential relationships. It then searches for `owl:AllDisjointProperties` axioms, ensuring that the associated list of members contains at least two valid datatype properties. As it processes these results, the method populates an internal registry of disjoint relationships and finally returns a list of `OWLDisjointDataProperties` instances representing the valid axioms found.

      :return: A list of OWLDisjointDataProperties instances representing all disjoint data property axioms defined in the ontology, including both pairwise disjointness and sets of mutually disjoint properties.

      :rtype: list[OWLDisjointDataProperties]



   .. py:method:: get_owl_disjoint_object_properties() -> list[pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties]

      Retrieves all disjoint object property axioms from the ontology using SPARQL, handling both binary and n-ary disjointness declarations. The method executes two distinct queries: one to find pairs linked by `owl:propertyDisjointWith` and another to identify sets of properties grouped under `owl:AllDisjointProperties`. It ensures data integrity by filtering for properties explicitly typed as `owl:ObjectProperty`, excluding self-disjoint pairs, and ignoring disjoint sets with fewer than two members. Valid results are processed and stored internally via `to_owl_disjoint_object_properties`, and the method returns the complete list of identified disjoint property relationships.

      :return: A list of OWL disjoint object properties axioms defined in the ontology, covering both pairwise disjointness and disjoint sets.

      :rtype: list[OWLDisjointObjectProperties]



   .. py:method:: get_owl_disjoint_unions() -> list[pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion]

      Executes a SPARQL query to identify classes defined as disjoint unions of other classes via the `owl:disjointUnionOf` property. The method iterates over the query results to aggregate member classes into a mapping, ensuring that the class itself is not included as a member. It then processes these mappings by invoking `to_owl_disjoint_union`, which populates an internal registry of disjoint unions. To prevent redundant processing, the method skips any classes already present in this registry. The result is a list of `OWLDisjointUnion` objects representing the disjoint union axioms found in the ontology.

      :return: A list of OWLDisjointUnion instances representing all disjoint union axioms found in the ontology.

      :rtype: list[OWLDisjointUnion]



   .. py:method:: get_owl_equivalent_classes() -> list[pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses]

      Retrieves and constructs OWL equivalent class axioms by querying the ontology for direct `owl:equivalentClass` relationships and complex class expressions. It processes direct equivalence assertions by grouping connected classes into chains and preserving any associated annotations found on the axioms. To ensure compatibility with OWL 1 DL, the method also interprets class definitions involving `owl:complementOf`, `owl:unionOf`, `owl:intersectionOf`, and `owl:oneOf` as equivalent class relationships, handling edge cases such as empty or singleton lists by mapping them to standard OWL concepts like `owl:Nothing` or `owl:Thing`. The resulting `OWLEquivalentClasses` instances are cached internally within the instance and returned as a list.

      :return: A list of OWLEquivalentClasses instances representing all equivalent class axioms in the ontology. This includes direct owl:equivalentClass declarations as well as relationships derived from complex class expressions (unions, intersections, complements, and enumerations) for OWL 1 DL compatibility, along with any associated annotations.

      :rtype: list[OWLEquivalentClasses]



   .. py:method:: get_owl_equivalent_data_properties() -> list[pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties]

      This method retrieves all equivalent data property relationships defined using `owl:equivalentProperty` in the ontology by executing a SPARQL query. The query specifically targets pairs of properties where both are instances of `owl:DatatypeProperty` and ensures that the subject and object are distinct to exclude self-equivalence. During processing, the method validates that the query results are instances of `DataPropertyClass`, collects any annotations associated with the equivalence axioms, and resolves equivalence chains. It constructs `OWLEquivalentDataProperties` instances for these relationships, populating an internal cache, and finally returns a list of these objects.

      :return: A list of OWLEquivalentDataProperties instances representing the equivalent data property relationships defined in the ontology. These relationships are derived from owl:equivalentProperty axioms between owl:DatatypeProperty entities, excluding self-equivalence and invalid properties.

      :rtype: list[OWLEquivalentDataProperties]



   .. py:method:: get_owl_equivalent_object_properties() -> list[pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties]

      Executes a SPARQL query to identify pairs of distinct `owl:ObjectProperty` entities linked by the `owl:equivalentProperty` predicate within the ontology. The method validates the query results by ensuring both subjects and objects are instances of `ObjectPropertyClass`, skipping any entries that do not meet this criteria. It also retrieves and aggregates annotations associated with the equivalence axioms. The identified relationships are processed to handle equivalence chains, and corresponding `OWLEquivalentObjectProperties` objects are instantiated and stored within the class. The method returns a list of these generated objects representing the valid equivalent object properties found in the ontology.

      :return: A list of OWLEquivalentObjectProperties instances representing all valid equivalent object property axioms defined in the ontology, excluding self-equivalence.

      :rtype: list[OWLEquivalentObjectProperties]



   .. py:method:: get_owl_functional_data_properties() -> list[pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty]

      Executes a SPARQL query to retrieve all resources in the ontology that are explicitly typed as `owl:FunctionalProperty`. For each identified property, the method invokes `to_owl_functional_data_property` to process the resource and update the internal collection of functional data properties. The method returns a list of `OWLFunctionalDataProperty` instances derived from the internal `functional_data_properties` dictionary, representing the functional properties discovered in the ontology.

      :return: A list of OWLFunctionalDataProperty instances representing the functional data properties defined in the ontology.

      :rtype: list[OWLFunctionalDataProperty]



   .. py:method:: get_owl_functional_object_properties() -> list[pyowl2.axioms.object_property_axiom.functional_object_property.OWLFunctionalObjectProperty]

      Executes a SPARQL query to retrieve all properties in the ontology that are explicitly defined as `owl:FunctionalProperty`. For each property identified, the method invokes `to_owl_functional_object_property` to process and cache the property instance. The method returns a list of these cached functional object properties, effectively populating the internal collection as a side effect of the retrieval process.

      :return: A list of `OWLFunctionalObjectProperty` instances corresponding to the functional object properties defined in the ontology.

      :rtype: list[OWLFunctionalObjectProperty]



   .. py:method:: get_owl_general_axiom() -> list[owlready2.EntityClass]

      Executes a SPARQL query to identify and construct OWL general class axioms based on reified axiom statements found in the RDF graph. The method specifically targets axioms where the annotated source is a complex class expression—such as intersections, unions, complements, or restrictions—filtering out simpler structures. It processes any annotations associated with the axiom node, converting them into structured annotation objects, and resolves internal integer identifiers to their corresponding ontology entities. To ensure consistency and prevent duplication, the method maintains an internal cache of processed axioms; if an axiom is encountered again, its annotations are updated rather than creating a new entry. The result is a list of fully constructed general axioms represented as `EntityClass` objects.

      :return: A list of EntityClass instances representing OWL general class axioms where the annotated source is a complex class expression (e.g., And, Or, Not, Restriction), including any associated annotations.

      :rtype: list[EntityClass]



   .. py:method:: get_owl_has_key(entity: owlready2.EntityClass, objects: tuple[owlready2.ObjectPropertyClass, Ellipsis], data: tuple[owlready2.DataPropertyClass, Ellipsis]) -> Optional[pyowl2.axioms.has_key.OWLHasKey]

      Retrieves or constructs an OWLHasKey axiom representing a key constraint for a specific entity, defined by a combination of object and data properties. The method first validates the input types, ensuring the entity is an instance of EntityClass and the properties are tuples of the correct classes; it returns None if validation fails. To optimize performance, it checks an internal cache keyed by the entity, returning the existing axiom if available. If a new axiom is required, the method converts the entity and properties into their OWL representations, retrieves associated annotations, and instantiates a new OWLHasKey object which is then stored in the cache and returned.

      :param entity: The entity for which the has-key axiom is being retrieved.
      :type entity: EntityClass
      :param objects: Object properties to be included in the has-key axiom for the entity.
      :type objects: tuple[ObjectPropertyClass, ...]
      :param data: A tuple of data properties that form part of the unique key for the entity.
      :type data: tuple[DataPropertyClass, ...]

      :return: The OWLHasKey axiom for the specified entity and properties, or None if the inputs are invalid.

      :rtype: typing.Optional[OWLHasKey]



   .. py:method:: get_owl_has_keys() -> list[pyowl2.axioms.has_key.OWLHasKey]

      Retrieves all `owl:hasKey` restrictions defined in the ontology by executing a SPARQL query that identifies classes and their associated key properties. The query traverses RDF lists to collect properties, categorizing them as either object properties or datatype properties. To optimize performance, the method checks an internal cache to skip classes that have already been processed. For each new class, it aggregates the properties and invokes a helper method to construct and store the corresponding `OWLHasKey` instance. The method returns a list of all processed `OWLHasKey` objects found in the ontology.

      :return: A list of `OWLHasKey` instances representing the key property sets defined in the ontology.

      :rtype: list[OWLHasKey]



   .. py:method:: get_owl_individuals() -> list[pyowl2.abstracts.individual.OWLIndividual]

      Retrieves a list of all OWL individuals defined in the ontology by executing a SPARQL query that matches entities typed as `owl:NamedIndividual`, those defined via annotated axioms, or instances of any `owl:Class`. As it processes the query results, the method filters out entities that are not valid named individuals and invokes internal helper methods to generate the corresponding `OWLIndividual` objects, declarations, and class assertions, thereby populating the object's internal state. The final result is a list of these generated individual objects extracted from the internal declarations registry.

      :return: A list of OWLIndividual instances representing all valid individuals identified in the ontology.

      :rtype: list[OWLIndividual]



   .. py:method:: get_owl_inverse_functional_object_properties() -> list[pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty]

      Retrieves all inverse functional object properties defined in the ontology by executing a SPARQL query that identifies resources typed as `owl:InverseFunctionalProperty`. The method iterates through the query results and processes each property using the `to_owl_inverse_functional_object_property` helper method, which handles the instantiation and validation logic. This process populates the internal cache of inverse functional object properties as a side effect. Finally, the method returns a list of `OWLInverseFunctionalObjectProperty` instances representing the properties found in the ontology.

      :return: A list of OWLInverseFunctionalObjectProperty instances representing all inverse functional object properties defined in the ontology.

      :rtype: list[OWLInverseFunctionalObjectProperty]



   .. py:method:: get_owl_inverse_object_properties() -> list[pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties]

      Retrieves all pairs of inverse object properties defined in the ontology by executing a SPARQL query that searches for triples using the `owl:inverseOf` predicate. The method explicitly filters out self-inverse properties to ensure only distinct pairs are processed. As it iterates through the query results, it populates the internal collection of inverse properties by calling `to_owl_inverse_object_properties` for each valid pair. The method returns a list of `OWLInverseObjectProperties` instances representing the accumulated inverse relationships.

      :return: A list of `OWLInverseObjectProperties` instances representing the inverse property pairs defined in the ontology via `owl:inverseOf`, excluding self-inverse properties.

      :rtype: list[OWLInverseObjectProperties]



   .. py:method:: get_owl_irreflexive_object_properties() -> list[pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty]

      Retrieves all irreflexive object properties defined in the ontology by executing a SPARQL query that identifies resources explicitly typed as `owl:IrreflexiveProperty`. For each property found, the method invokes `to_owl_irreflexive_object_property` to convert the raw identifier into a structured `OWLIrreflexiveObjectProperty` instance, which has the side effect of populating the instance's internal `irreflexive_object_properties` dictionary. The method returns a list of these instances, which may be empty if the ontology contains no such definitions or if the underlying conversion logic filters out invalid entries.

      :return: A list of OWLIrreflexiveObjectProperty instances representing all irreflexive object properties defined in the ontology.

      :rtype: list[OWLIrreflexiveObjectProperty]



   .. py:method:: get_owl_negative_data_property_assertions() -> list[pyowl2.axioms.assertion.OWLNegativeDataPropertyAssertion]

      Executes a SPARQL query to identify negative property assertions involving data properties, specifically targeting blank nodes typed as `owl:NegativePropertyAssertion` that link a named individual, a datatype property, and a literal value. During processing, the method ensures that the target value is correctly instantiated as a Literal object, handling potential type mismatches from the query results. It constructs `OWLNegativeDataPropertyAssertion` objects for each valid match and returns the complete collection of these assertions stored within the instance.

      :return: A list of `OWLNegativeDataPropertyAssertion` instances representing all negative data property assertions in the ontology, indicating that a specific data property does not hold between a source individual and a literal target value.

      :rtype: list[OWLNegativeDataPropertyAssertion]



   .. py:method:: get_owl_negative_object_property_assertions() -> list[pyowl2.axioms.assertion.OWLNegativeObjectPropertyAssertion]

      Retrieves negative object property assertions from the ontology by executing a SPARQL query that identifies blank nodes representing `owl:NegativePropertyAssertion` instances. The query specifically filters for assertions where the source and target are named individuals and the property is an object property. For each valid result, the method processes the data to construct an internal representation, updating the internal collection of assertions. It returns a list of these fully resolved negative object property assertion objects.

      :return: A list of OWLNegativeObjectPropertyAssertion objects representing all negative object property assertions found in the ontology. The list contains only valid assertions where the source and target are named individuals and the property is an object property.

      :rtype: list[OWLNegativeObjectPropertyAssertion]



   .. py:method:: get_owl_object_all_values_from() -> list[pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom]

      Retrieves all universal property restrictions (owl:allValuesFrom) defined in the ontology by executing a SPARQL query. The query specifically identifies blank nodes representing `owl:Restriction` instances that include both an `owl:onProperty` and an `owl:allValuesFrom` predicate. For each matching node, the method invokes `to_owl_object_all_values_from` to construct and store the corresponding object representation. Finally, it returns a list of `OWLObjectAllValuesFrom` instances derived from the internal collection of restrictions.

      :return: A list of `OWLObjectAllValuesFrom` instances representing all valid `owl:allValuesFrom` restrictions found in the ontology.

      :rtype: list[OWLObjectAllValuesFrom]



   .. py:method:: get_owl_object_complement_of() -> list[pyowl2.class_expression.object_complement_of.OWLObjectComplementOf]

      Retrieves and constructs OWL object complement expressions defined within the ontology by executing a SPARQL query. The query specifically targets triples where a subject of type `owl:Class` possesses an `owl:complementOf` relationship with another class, applying filters to exclude blank nodes and ensure the subject and object are distinct. For each valid pair identified, the method processes the relationship to populate an internal collection and returns a list of the resulting `OWLObjectComplementOf` instances.

      :return: A list of `OWLObjectComplementOf` instances representing the class complement relationships (owl:complementOf) found in the ontology.

      :rtype: list[OWLObjectComplementOf]



   .. py:method:: get_owl_object_exact_cardinality() -> list[pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality]

      Retrieves a list of OWL object exact cardinality restrictions present in the ontology by executing a SPARQL query. The query identifies blank nodes representing `owl:Restriction` instances that are defined with an object property and either a standard `owl:cardinality` or a qualified `owl:qualifiedCardinality` (which requires an accompanying `owl:onClass`). It filters the results to ensure that the cardinality values are non-negative integers. As a side effect, this method processes each matching restriction through a helper function to populate an internal cache, ultimately returning the list of constructed restriction objects.

      :return: A list of OWLObjectExactCardinality instances representing all valid exact cardinality restrictions on object properties found in the ontology, including those defined using owl:cardinality or owl:qualifiedCardinality.

      :rtype: list[OWLObjectExactCardinality]



   .. py:method:: get_owl_object_has_self() -> list[pyowl2.class_expression.object_has_self.OWLObjectHasSelf]

      Executes a SPARQL query to locate blank nodes within the ontology that represent OWL restrictions with a true `owl:hasSelf` property. For each valid restriction found, the method processes the node using a helper function to generate an `OWLObjectHasSelf` instance, which is stored in an internal collection. The method returns a list of these instances, effectively retrieving all self-restrictions defined on object properties while ignoring non-blank nodes or restrictions where the self-value is false.

      :return: A list of OWLObjectHasSelf instances representing all valid owl:hasSelf restrictions in the ontology, filtered to include only those defined on blank nodes with a hasSelf value of true.

      :rtype: list[OWLObjectHasSelf]



   .. py:method:: get_owl_object_has_value() -> list[pyowl2.class_expression.object_has_value.OWLObjectHasValue]

      Retrieves all OWL object property restrictions defined with `owl:hasValue` by executing a SPARQL query that targets blank nodes of type `owl:Restriction`. The query identifies restrictions possessing both an `owl:onProperty` and an `owl:hasValue` predicate. For each valid restriction found, the method processes the data using `to_owl_object_has_value`, which populates an internal cache, and subsequently returns a list of the corresponding `OWLObjectHasValue` instances. Note that the query is restricted to blank nodes, meaning restrictions defined on named nodes are ignored.

      :return: A list of OWLObjectHasValue instances representing all object property has-value restrictions (owl:hasValue) found in the ontology.

      :rtype: list[OWLObjectHasValue]



   .. py:method:: get_owl_object_intersection_of() -> list[pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf]

      Retrieves all OWL object intersection axioms defined in the ontology by executing a SPARQL query. The query specifically targets blank nodes representing classes that are defined using the `owl:intersectionOf` property, ensuring that only intersections with at least two member classes are considered valid. As a side effect, this method populates an internal collection of intersection objects by processing each valid blank node through a conversion routine. Finally, it returns a list of `OWLObjectIntersectionOf` instances representing the complete set of class intersections found in the data.

      :return: A list of OWLObjectIntersectionOf instances representing the class intersections found in the ontology, filtered to include only those with at least two members.

      :rtype: list[OWLObjectIntersectionOf]



   .. py:method:: get_owl_object_max_cardinality() -> list[pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality]

      Executes a SPARQL query to identify and retrieve all object property restrictions that define a maximum cardinality, supporting both standard `owl:maxCardinality` and qualified `owl:maxQualifiedCardinality` constraints. The search targets blank nodes representing `owl:Restriction` instances, ensuring that the associated cardinality values are non-negative integers and that qualified restrictions include a valid `owl:onClass`. For each valid restriction discovered, the method invokes a helper function to process the blank node and populate an internal collection. Finally, it returns a list of the constructed `OWLObjectMaxCardinality` objects representing these restrictions.

      :return: A list of OWLObjectMaxCardinality instances representing all object property maximum cardinality restrictions found in the ontology, including those defined using owl:maxCardinality and owl:maxQualifiedCardinality.

      :rtype: list[OWLObjectMaxCardinality]



   .. py:method:: get_owl_object_min_cardinality() -> list[pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality]

      Retrieves all OWL object min-cardinality restrictions from the ontology by executing a SPARQL query that identifies blank nodes of type `owl:Restriction`. The query specifically targets restrictions involving `owl:onProperty` combined with either `owl:minCardinality` or `owl:minQualifiedCardinality` (which also requires an `owl:onClass`), ensuring that the cardinality value is a valid non-negative integer. As a side effect, the method processes each discovered restriction by invoking `to_owl_object_min_cardinality`, which populates an internal cache of restriction objects. The method returns a list of these cached `OWLObjectMinCardinality` instances.

      :return: A list of all OWL object minimum cardinalinality restrictions found in the ontology, including both standard and qualified restrictions.

      :rtype: list[OWLObjectMinCardinality]



   .. py:method:: get_owl_object_one_of() -> list[pyowl2.class_expression.object_one_of.OWLObjectOneOf]

      Retrieves all enumerated classes defined by the `owl:oneOf` construct within the ontology. This method executes a SPARQL query to locate classes of type `owl:Class` that are associated with an `owl:oneOf` property containing a non-empty list of members. For each class discovered, it processes the enumeration by calling `to_owl_object_one_of`, which constructs and stores the corresponding `OWLObjectOneOf` instance in the internal state. The method returns a list of these instances, ensuring that only valid enumerations with at least one member are included.

      :return: A list of OWLObjectOneOf instances representing all enumerated classes (owl:oneOf) found in the ontology.

      :rtype: list[OWLObjectOneOf]



   .. py:method:: get_owl_object_properties() -> list[pyowl2.expressions.object_property.OWLObjectProperty]

      Retrieves all OWL object properties defined in the underlying RDF graph by executing a SPARQL query that identifies properties either through direct `rdf:type` assertions or via axioms where the property is the annotated source and the type is the annotated target. For each result, the method verifies that the entity is an instance of `ObjectPropertyClass` before invoking helper methods to generate the corresponding OWL object property and declaration representations, thereby populating the internal state of the instance. The method ultimately returns a list of `OWLObjectProperty` instances derived from the internal declarations registry, ensuring that only valid and processed properties are included.

      :return: A list of OWLObjectProperty instances representing all valid object properties defined in the ontology, identified through direct type assertions or axioms.

      :rtype: list[OWLObjectProperty]



   .. py:method:: get_owl_object_property_assertions() -> list[pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion]

      Retrieves all OWL object property assertions defined in the ontology by executing a SPARQL query that filters for triples where both the subject and object are explicitly typed as `owl:NamedIndividual`. It iterates over the query results, delegating the construction and storage of assertion objects to the `to_owl_object_property_assertion` method, which populates the internal collection of assertions as a side effect. The method returns a list of these `OWLObjectPropertyAssertion` instances, ensuring that only relationships between named individuals are considered and duplicates are excluded.

      :return: A list of OWLObjectPropertyAssertion instances representing all object property assertions in the ontology where both the subject and object are named individuals.

      :rtype: list[OWLObjectPropertyAssertion]



   .. py:method:: get_owl_object_property_axiom(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom

      Attempts to construct an OWL object property axiom from the provided OWLObject instances by sequentially applying a predefined set of conversion strategies. These strategies cover a wide range of axiom types, including sub-property relationships, property characteristics (such as transitivity, symmetry, or functionality), and domain or range restrictions. The method returns the result of the first successful conversion; if the input parameters do not satisfy the requirements of any internal conversion function, a TypeError is raised.

      :param params: A variable number of OWLObject instances (such as properties or classes) that serve as the arguments for constructing the target object property axiom.
      :type params: tuple[OWLObject, ...]

      :return: The OWLObjectPropertyAxiom corresponding to the provided OWLObject parameters, derived by applying the first matching conversion function.

      :rtype: OWLObjectPropertyAxiom



   .. py:method:: get_owl_object_property_domains() -> list[pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain]

      Retrieves all object property domains defined in the ontology by executing a SPARQL query that identifies triples where a property of type `owl:ObjectProperty` is linked to a class via the `rdfs:domain` predicate. For each result, the method processes the property and class pair to create an `OWLObjectPropertyDomain` instance, which populates the internal collection of object property domains. It returns a list of these instances, ensuring that only valid object properties and their associated domains are included.

      :return: A list of OWLObjectPropertyDomain instances representing the object property domains defined in the ontology using rdfs:domain for properties of type owl:ObjectProperty.

      :rtype: list[OWLObjectPropertyDomain]



   .. py:method:: get_owl_object_property_ranges() -> list[pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange]

      Executes a SPARQL query to retrieve all `owl:ObjectProperty` instances that have a defined `rdfs:range` in the ontology. For each property and class pair returned by the query, the method invokes `to_owl_object_property_range` to process and store the range information. It returns a list of `OWLObjectPropertyRange` objects representing the valid ranges currently stored in the internal collection. Note that this method has the side effect of populating the `object_property_ranges` dictionary, and the returned list reflects the cumulative state of this storage rather than strictly the results of the current query.

      :return: A list of OWLObjectPropertyRange instances representing the ranges defined for object properties in the ontology.

      :rtype: list[OWLObjectPropertyRange]



   .. py:method:: get_owl_object_some_values_from() -> list[pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom]

      Retrieves all existential restrictions on object properties defined within the ontology by executing a SPARQL query. The search is specifically scoped to blank nodes that are typed as `owl:Restriction` and include both `owl:onProperty` and `owl:someValuesFrom` assertions. For each valid restriction found, the method processes the data to generate a structured representation and returns the aggregated list of these objects. Note that restrictions defined on named nodes (URIs) are excluded from the results, and the method populates an internal cache of restrictions during execution.

      :return: A list of OWLObjectSomeValuesFrom instances representing all valid existential restrictions (owl:someValuesFrom) for object properties found in the ontology.

      :rtype: list[OWLObjectSomeValuesFrom]



   .. py:method:: get_owl_object_union_of() -> list[pyowl2.class_expression.object_union_of.OWLObjectUnionOf]

      Retrieves all OWL object union constructs defined within the ontology by executing a SPARQL query. The query specifically targets blank nodes typed as `owl:Class` that utilize the `owl:unionOf` predicate to reference a list of member classes. To ensure validity, the method filters out any nodes that do not contain at least two members in their union list. As it processes each result, it populates an internal registry by converting the raw data into `OWLObjectUnionOf` instances. The method returns a list of these instances, representing the complete set of valid object unions found.

      :return: A list of OWLObjectUnionOf instances representing all valid object union relationships (owl:unionOf) found in the ontology. Only unions containing at least two members are included.

      :rtype: list[OWLObjectUnionOf]



   .. py:method:: get_owl_ontology_annotations() -> Optional[list[pyowl2.base.annotation.OWLAnnotation]]

      Executes a SPARQL query to retrieve ontology-level annotations where the annotation value is a literal. The method identifies triples where the subject is the ontology, the predicate is an annotation property, and the object is a literal, then converts these into `OWLAnnotation` objects using internal mappings for properties and literal wrappers. It returns a list of these annotations if any are found, or `None` if no such annotations exist.

      :return: A list of OWLAnnotation instances representing the ontology's literal-valued annotations, or None if no annotations are found.

      :rtype: typing.Optional[list[OWLAnnotation]]



   .. py:method:: get_owl_reflexive_object_properties() -> list[pyowl2.axioms.object_property_axiom.reflexive_object_property.OWLReflexiveObjectProperty]

      Retrieves all reflexive object properties defined in the ontology by executing a SPARQL query that searches for entities explicitly typed as `owl:ReflexiveProperty`. The method iterates through the query results, converting each property into an `OWLReflexiveObjectProperty` instance using the `to_owl_reflexive_object_property` helper method, which also populates an internal cache. It returns a list of these instances, providing a comprehensive collection of the reflexive properties found in the underlying data store.

      :return: A list of OWLReflexiveObjectProperty instances representing all reflexive object properties defined in the ontology using owl:ReflexiveProperty.

      :rtype: list[OWLReflexiveObjectProperty]



   .. py:method:: get_owl_same_individuals() -> list[pyowl2.axioms.assertion.OWLSameIndividual]

      This method retrieves all `owl:sameAs` assertions between named individuals within the ontology by executing a SPARQL query that identifies distinct pairs of `owl:NamedIndividual` instances. It filters out self-referential statements and collects any annotations associated with the equivalence axioms. The results are processed to resolve transitive equivalence chains, ensuring that individuals linked through a series of `sameAs` statements are grouped together. Finally, it constructs and returns a list of `OWLSameIndividual` instances representing these equivalence classes, while also populating the internal registry of same-individual data.

      :return: A list of OWLSameIndividual objects representing the owl:sameAs assertions between named individuals in the ontology.

      :rtype: list[OWLSameIndividual]



   .. py:method:: get_owl_sub_annotation_property_of() -> list[pyowl2.axioms.annotations.OWLSubAnnotationPropertyOf]

      Retrieves all sub-annotation property relationships defined in the ontology using a SPARQL query. The method specifically looks for triples where a subject is a sub-property of an object via `rdfs:subPropertyOf`, ensuring that both the sub-property and super-property are explicitly typed as `owl:AnnotationProperty` and are distinct entities to avoid self-referential relationships. For each valid pair discovered, the method constructs an `OWLSubAnnotationPropertyOf` instance, attaching any relevant axiom annotations, and updates the internal state accordingly. Finally, it returns a list of these instances representing the valid sub-annotation property hierarchies found in the data.

      :return: A list of OWLSubAnnotationPropertyOf instances representing all valid rdfs:subPropertyOf relationships between owl:AnnotationProperty entities in the ontology.

      :rtype: list[OWLSubAnnotationPropertyOf]



   .. py:method:: get_owl_sub_data_property_of() -> list[pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf]

      Retrieves and processes sub-data property relationships defined within the ontology by executing a SPARQL query. The query identifies pairs of properties linked by `rdfs:subPropertyOf`, ensuring that both the subproperty and superproperty are explicitly typed as `owl:DatatypeProperty` and are not the same entity. For each valid pair discovered, the method populates an internal collection by creating an `OWLSubDataPropertyOf` instance. It returns a list of these instances, representing the valid sub-data property hierarchies extracted from the data.

      :return: A list of OWLSubDataPropertyOf instances representing the sub-data-property relationships defined in the ontology, specifically those linking distinct owl:DatatypeProperty entities via rdfs:subPropertyOf.

      :rtype: list[OWLSubDataPropertyOf]



   .. py:method:: get_owl_sub_object_property_chain() -> list[pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]

      Retrieves and processes subproperty relationships defined via OWL property chain axioms by executing a SPARQL query to identify subproperties associated with a chain of object properties. The query specifically filters for chains containing at least two distinct properties to ensure validity. These properties are aggregated into a set to construct an `OWLObjectPropertyChain`, which is then mapped to the corresponding subproperty and stored within the instance's internal collection via the `to_owl_sub_object_property_of` method. The method returns a list of `OWLSubObjectPropertyOf` instances representing all currently stored subobject property relationships, which may include entries added by previous operations.

      :return: A list of OWLSubObjectPropertyOf instances representing subproperty relationships defined using property chains in the ontology.

      :rtype: list[OWLSubObjectPropertyOf]



   .. py:method:: get_owl_sub_object_property_of() -> list[pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]

      Retrieves and constructs a list of `OWLSubObjectPropertyOf` axioms by querying the ontology for `rdfs:subPropertyOf` relationships between object properties. The method executes a SPARQL query to identify distinct pairs of sub-properties and super-properties, filtering to ensure both entities are explicitly typed as `owl:ObjectProperty` and are not identical. For each valid pair found, it processes the relationship and subsequently triggers the resolution of property chains via `get_owl_sub_object_property_chain`. The method returns the populated list of sub-object property relationships stored internally.

      :return: A list of OWLSubObjectPropertyOf instances representing valid sub-property relationships between distinct object properties defined in the ontology.

      :rtype: list[OWLSubObjectPropertyOf]



   .. py:method:: get_owl_subclass_relationships() -> list[pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf]

      Retrieves all subclass relationships from the ontology by executing a SPARQL query that identifies relationships through direct `rdfs:subClassOf` assertions and via annotated `owl:Axiom` structures. The query filters out self-referential relationships and ensures distinct results. For each valid pair, the method processes any associated annotations, converts the entities into the appropriate OWL format, and stores the relationship internally. The method returns a list of `OWLSubClassOf` instances representing the accumulated subclass relationships.

      :return: A list of OWLSubClassOf instances representing all subclass relationships found in the ontology, including those derived from direct rdfs:subClassOf declarations and annotated axioms.

      :rtype: list[OWLSubClassOf]



   .. py:method:: get_owl_symmetric_object_properties() -> list[pyowl2.axioms.object_property_axiom.symmetric_object_property.OWLSymmetricObjectProperty]

      Retrieves all symmetric object properties defined in the ontology by executing a SPARQL query that selects resources explicitly typed as `owl:SymmetricProperty`. During iteration over the query results, the method invokes `to_owl_symmetric_object_property` for each property, which processes the entity and populates an internal collection. The method returns a list of the resulting `OWLSymmetricObjectProperty` instances, representing the symmetric object properties currently stored within the object.

      :return: A list of OWLSymmetricObjectProperty instances representing all symmetric object properties defined in the ontology.

      :rtype: list[OWLSymmetricObjectProperty]



   .. py:method:: get_owl_transitive_object_properties() -> list[pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty]

      Retrieves all transitive object properties defined in the ontology by executing a SPARQL query to locate resources typed as `owl:TransitiveProperty`. For each property identified, the method processes the entity using `to_owl_transitive_object_property`, which populates the internal collection of transitive properties. The method returns a list of `OWLTransitiveObjectProperty` instances corresponding to the values stored in this internal collection.

      :return: A list of OWLTransitiveObjectProperty instances representing all transitive object properties defined in the ontology.

      :rtype: list[OWLTransitiveObjectProperty]



   .. py:method:: nothing_to_owl_class() -> pyowl2.base.owl_class.OWLClass

      Retrieves the `OWLClass` representation of the OWL Nothing entity (owl:Nothing) by checking an internal cache. If the class has not been instantiated previously, the method constructs a new `OWLClass` using the IRI derived from the standard OWL namespace and stores it within the `self.classes` dictionary. This approach ensures that subsequent calls return the same object instance, preventing duplication while modifying the internal state of the object.

      :return: An OWLClass instance representing the OWL Nothing entity.

      :rtype: OWLClass



   .. py:method:: nothing_to_owl_class_declaration(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]

      Generates an OWL declaration axiom for the OWL.Nothing entity, utilizing an internal cache to ensure that the declaration is created only once. If the declaration is not already cached, the method attempts to construct the corresponding OWL class object and then instantiates an `OWLDeclaration`, attaching either the explicitly provided annotations or default annotations retrieved from the source. If the entity is already cached, the provided annotations are ignored, and the existing instance is returned. The method returns the resulting declaration, or None if the underlying class construction fails.

      :param annotations: Optional list of OWLAnnotation instances to attach to the declaration. If omitted, default annotations are retrieved automatically.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLDeclaration axiom representing the declaration of OWL.Nothing, or None if the underlying class object cannot be generated.

      :rtype: typing.Optional[OWLDeclaration]



   .. py:method:: thing_to_owl_class() -> pyowl2.base.owl_class.OWLClass

      Retrieves the `OWLClass` representation of the OWL Thing entity, ensuring that a corresponding object exists within the instance's internal cache. If the class has not yet been initialized, the method constructs a new `OWLClass` instance using the standard OWL namespace IRI and stores it in the `self.classes` dictionary. This approach guarantees that repeated invocations return the same cached object rather than creating duplicates.

      :return: An OWLClass instance representing the OWL Thing entity.

      :rtype: OWLClass



   .. py:method:: thing_to_owl_class_declaration(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]

      Generates and caches an OWL declaration axiom for the universal class `owl:Thing`. The method first checks an internal registry to prevent redundant creation; if the declaration does not exist, it attempts to construct the underlying OWL class object. If the class object cannot be generated, the method returns `None`. The resulting declaration is associated with annotations, using a provided list if available, or otherwise retrieving default annotations specific to the entity. This method modifies the internal state by storing the new declaration in the `self.declarations` cache.

      :param annotations: Optional list of OWLAnnotation instances to associate with the declaration. If omitted, default annotations are used.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLDeclaration instance representing the declaration of OWL.Thing, or None if the declaration cannot be created.

      :rtype: typing.Optional[OWLDeclaration]



   .. py:method:: to_owl_annotation_assertion(subject: Union[owlready2.NamedIndividual, rdflib.URIRef, str], property: owlready2.AnnotationPropertyClass, value: Union[owlready2.NamedIndividual, rdflib.URIRef, rdflib.Literal], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.annotations.OWLAnnotationAssertion]

      This method constructs an OWL annotation assertion axiom by validating and converting the provided subject, property, and value into their corresponding OWL representations. It performs strict type checking on the inputs, returning None if the subject is not a named individual, URI reference, or string, or if the value is not a named individual, URI reference, or literal. To optimize performance and ensure consistency, the method maintains an internal cache of previously created assertions; if the specific combination of inputs already exists, it returns the cached instance. Otherwise, it resolves the subject and value into OWL entities—using the `to_owl_individual` method for named individuals and constructing IRIs or literals for other types—and resolves the property via `to_owl_annotation_property`. The resulting `OWLAnnotationAssertion` object is stored in the cache and returned, optionally decorated with the provided list of annotations.

      :param subject: The entity being annotated, specified as a NamedIndividual, URIRef, or string representing an IRI.
      :type subject: typing.Union[NamedIndividual, URIRef, str]
      :param property: The annotation property used to link the subject to the value in the assertion.
      :type property: AnnotationPropertyClass
      :param value: The value of the annotation assertion, which can be a NamedIndividual, a URI reference, or a Literal.
      :type value: typing.Union[NamedIndividual, URIRef, Literal]
      :param annotations: An optional list of annotations to be applied to the resulting annotation assertion axiom.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLAnnotationAssertion instance corresponding to the subject, property, and value, retrieved from cache or newly created, or None if the inputs are invalid or conversion fails.

      :rtype: typing.Optional[OWLAnnotationAssertion]



   .. py:method:: to_owl_annotation_property(property: owlready2.AnnotationPropertyClass) -> Optional[pyowl2.base.annotation_property.OWLAnnotationProperty]

      Retrieves or creates an OWLAnnotationProperty representation corresponding to the provided AnnotationPropertyClass instance. The method performs a validation check on the input, returning None if the argument is invalid or not of the expected type. It relies on an internal dictionary to cache instances, ensuring object consistency; if the property is not already present in the cache, a new OWLAnnotationProperty is instantiated using the current namespace and the property's name before being stored and returned.

      :param property: The annotation property class instance to convert into an OWL annotation property.
      :type property: AnnotationPropertyClass

      :return: The OWLAnnotationProperty instance associated with the input property, creating it if needed. Returns None if the input is invalid or not an AnnotationPropertyClass.

      :rtype: typing.Optional[OWLAnnotationProperty]



   .. py:method:: to_owl_annotation_property_declaration(property: owlready2.AnnotationPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]

      Converts an `AnnotationPropertyClass` instance into an `OWLDeclaration` axiom, utilizing an internal cache to ensure idempotency. The method validates the input type and returns `None` if the property is invalid or not an instance of `AnnotationPropertyClass`. If the property has not been previously processed, it attempts to generate the corresponding OWL annotation property expression; if this conversion fails, the method returns `None`. Otherwise, it instantiates a new `OWLDeclaration`, associating it with either the explicitly provided annotations or a set of default annotations derived from the property context. The newly created declaration is stored in the internal declarations dictionary before being returned.

      :param property: The annotation property to be converted into an OWL declaration.
      :type property: AnnotationPropertyClass
      :param annotations: A list of OWLAnnotation instances to associate with the resulting OWLDeclaration. If omitted, default annotations are used.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLDeclaration representing the provided annotation property, or None if the property is invalid or the conversion fails.

      :rtype: typing.Optional[OWLDeclaration]



   .. py:method:: to_owl_annotation_property_domain(property: owlready2.AnnotationPropertyClass, domain: rdflib.URIRef, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.annotations.OWLAnnotationPropertyDomain]

      Constructs an OWL axiom that specifies the domain restriction for a given annotation property. The method first validates that the input property is an instance of AnnotationPropertyClass and the domain is a URIRef, returning None if these checks fail. To ensure efficiency and consistency, it maintains an internal cache of previously created domain axioms; if the property has already been processed, the cached instance is returned immediately. Otherwise, it resolves the property to its OWL expression, constructs an IRI for the domain using the current namespace, and instantiates a new OWLAnnotationPropertyDomain object, optionally attaching a list of annotations. This new instance is stored in the cache before being returned.

      :param property: The annotation property for which the domain is being defined.
      :type property: AnnotationPropertyClass
      :param domain: The IRI of the domain to which the annotation property applies.
      :type domain: URIRef
      :param annotations: Optional list of OWLAnnotation instances to attach to the resulting axiom.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLAnnotationPropertyDomain axiom representing the domain relationship for the provided property and domain, or None if the inputs are invalid.

      :rtype: typing.Optional[OWLAnnotationPropertyDomain]



   .. py:method:: to_owl_annotation_property_range(property: owlready2.AnnotationPropertyClass, range: rdflib.URIRef, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.annotations.OWLAnnotationPropertyRange]

      Constructs an OWL axiom representing the range restriction for a given annotation property. The method validates the input types, ensuring the property is an instance of AnnotationPropertyClass and the range is a URIRef. Upon successful validation, it attempts to retrieve or create the corresponding OWL annotation property expression. If the expression is valid, it instantiates an OWLAnnotationPropertyRange object, incorporating the range IRI and any optional annotations. The method maintains an internal cache keyed by the annotation property; if the property has already been processed, the cached instance is returned immediately. It returns None if inputs are invalid, if the underlying property conversion fails, or if the resulting axiom cannot be constructed.

      :param property: The annotation property for which the range axiom is being defined.
      :type property: AnnotationPropertyClass
      :param range: The IRI representing the range of the annotation property, defining the type of values the property can take.
      :type range: URIRef
      :param annotations: Optional list of OWLAnnotation instances to attach to the resulting axiom.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLAnnotationPropertyRange axiom representing the range of the specified annotation property, or None if the inputs are invalid or the property expression cannot be retrieved.

      :rtype: typing.Optional[OWLAnnotationPropertyRange]



   .. py:method:: to_owl_asymmetric_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.asymmetric_object_property.OWLAsymmetricObjectProperty]

      This method converts a given `ObjectPropertyClass` into its corresponding `OWLAsymmetricObjectProperty` representation, provided the property is defined as asymmetric. It performs validation to ensure the input is a valid `ObjectPropertyClass` and explicitly checks for the presence of the `AsymmetricProperty` characteristic in the property's hierarchy; if these conditions are not met, or if the base object property expression cannot be retrieved, the method returns None. The method employs a caching mechanism, storing generated instances in an internal dictionary to avoid redundant processing, and constructs the OWL object with relevant annotations if the property is being converted for the first time.

      :param property: The object property to be converted, which must be defined as an asymmetric property.
      :type property: ObjectPropertyClass

      :return: An OWLAsymmetricObjectProperty instance corresponding to the input property, or None if the property is invalid, lacks the AsymmetricProperty characteristic, or cannot be converted.

      :rtype: typing.Optional[OWLAsymmetricObjectProperty]



   .. py:method:: to_owl_class(entity: owlready2.ThingClass) -> Optional[pyowl2.base.owl_class.OWLClass]

      Retrieves or creates the OWLClass representation corresponding to a specific ThingClass entity. The method first validates the input, returning None if the entity is invalid or not an instance of ThingClass. It specifically handles OWL built-ins by mapping entities equivalent to OWL Nothing or OWL Thing to their standard OWL namespace IRIs. If the entity is not already present in the internal classes dictionary, a new OWLClass is instantiated using the appropriate namespace and name, then stored in the dictionary for future reference. The method returns the cached or newly created OWLClass instance.

      :param entity: The ThingClass instance to be mapped to its corresponding OWLClass representation.
      :type entity: ThingClass

      :return: The OWLClass instance corresponding to the provided ThingClass entity, or None if the entity is invalid.

      :rtype: typing.Optional[OWLClass]



   .. py:method:: to_owl_class_assertion(individual: owlready2.NamedIndividual, individual_class: owlready2.ThingClass) -> Optional[pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]

      This method constructs an OWLClassAssertion axiom representing the relationship where a specific named individual is an instance of a given class. It employs a caching mechanism, checking an internal dictionary to see if the assertion for the provided individual and class pair already exists. If the assertion is not cached, the method attempts to resolve the OWL class expression and the OWL individual expression; if either resolution fails or if the inputs are invalid, it returns None. Upon successful resolution, it creates a new OWLClassAssertion instance, populates it with annotations derived from the source data, stores the instance in the cache for future use, and returns it.

      :param individual: The specific named individual entity that is being asserted to be an instance of the provided class.
      :type individual: NamedIndividual
      :param individual_class: The class that the individual is asserted to be an instance of.
      :type individual_class: ThingClass

      :return: An OWLClassAssertion axiom asserting the individual is an instance of the class, or None if the inputs are invalid or conversion fails.

      :rtype: typing.Optional[OWLClassAssertion]



   .. py:method:: to_owl_class_declaration(entity: owlready2.EntityClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]

      Converts a given EntityClass instance into an OWLDeclaration axiom, managing caching and annotation resolution. The method validates the input entity, returning None if it is invalid or not an instance of EntityClass. If the declaration is not already present in the internal cache, it attempts to construct the OWL class expression using the `to_owl_class` method; if this conversion fails, the method returns None. Once created, the declaration is stored in the `declarations` dictionary to ensure idempotency. Regarding annotations, the method uses the provided list if available; otherwise, it automatically generates them using the `get_owl_declaration_annotations_for` helper method.

      :param entity: The instance to be converted into an OWL declaration axiom.
      :type entity: EntityClass
      :param annotations: Optional list of OWLAnnotation objects to attach to the declaration. If provided, these override the default annotations; otherwise, default annotations are retrieved automatically.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLDeclaration axiom representing the provided entity, or None if the entity is invalid or the OWL class expression cannot be retrieved.

      :rtype: typing.Optional[OWLDeclaration]



   .. py:method:: to_owl_data_all_values_from(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom]

      Converts a Restriction entity into an OWLDataAllValuesFrom object, provided the entity represents a data property restriction where all values must belong to a specific data range. The method validates the input by checking that the entity is a Restriction, its type corresponds to `OWL.allValuesFrom`, and its property is an instance of `DataPropertyClass`. If these criteria are not met, or if the underlying graph does not contain a valid data range for the restriction, the method returns None. To optimize performance, it caches the resulting object in an internal dictionary, returning the cached instance on subsequent calls for the same entity.

      :param entity: The Restriction entity to convert into an OWLDataAllValuesFrom representation. It must be of type OWL.allValuesFrom and have a property of type DataPropertyClass.
      :type entity: Restriction

      :return: An OWLDataAllValuesFrom instance representing the restriction, or None if the entity is invalid, not an all-values-from restriction, or does not use a data property.

      :rtype: typing.Optional[OWLDataAllValuesFrom]



   .. py:method:: to_owl_data_complement_of(entity: owlready2.Not, data_range: owlready2.EntityClass) -> Optional[pyowl2.data_range.data_complement_of.OWLDataComplementOf]

      Retrieves or constructs the OWL data complement representation corresponding to a specific logical negation entity. The method validates the input entity to ensure it is an instance of the `Not` class and checks an internal cache to prevent redundant processing. If the entity is not cached, it attempts to convert the provided data range into its OWL representation; if this conversion fails, the method returns `None`. Successfully constructed objects are stored in the instance's cache and returned.

      :param entity: An instance representing the logical negation to be converted into an OWL data complement.
      :type entity: Not
      :param data_range: The entity representing the data range to be complemented.
      :type data_range: EntityClass

      :return: An OWLDataComplementOf instance representing the complement of the specified data range, or None if the entity is invalid or the data range cannot be processed.

      :rtype: typing.Optional[OWLDataComplementOf]



   .. py:method:: to_owl_data_exact_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality]

      This method attempts to construct an `OWLDataExactCardinality` object from a given `Restriction` entity, ensuring the entity represents a data property restriction with an exact cardinality constraint. It performs several validation checks, verifying that the entity is an instance of `Restriction`, has a type corresponding to `OWL.qualifiedCardinality` or `OWL.cardinality`, and possesses a property of type `DataPropertyClass`. If valid, it queries the graph for the `onDataRange` to define the data type and converts the associated property. The method employs a caching mechanism, storing the generated object in `self.data_exact_cardinality` to avoid redundant processing for the same entity. It returns `None` if any validation fails or if necessary components like the data range or converted property are missing.

      :param entity: The restriction object to convert into an OWL data exact cardinality expression. It must have a type of qualifiedCardinality or cardinality and a property of type DataPropertyClass.
      :type entity: Restriction

      :return: The OWLDataExactCardinality representation of the restriction, or None if the entity is invalid or not a data exact cardinality restriction.

      :rtype: typing.Optional[OWLDataExactCardinality]



   .. py:method:: to_owl_data_has_value(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_has_value.OWLDataHasValue]

      Converts a provided Restriction entity into its corresponding OWLDataHasValue representation, provided the entity meets specific structural criteria. The method validates that the input is a Restriction instance, has a type corresponding to OWL.hasValue, and possesses a property that is a DataPropertyClass. If these conditions are not met, the method returns None. When valid, it utilizes an internal cache to store and retrieve the constructed object, ensuring that repeated calls with the same entity return the same instance without redundant processing. The conversion involves transforming the entity's property into an OWL data property and wrapping its value in an OWLLiteral.

      :param entity: The restriction entity to convert into an OWLDataHasValue representation, which must be a hasValue restriction associated with a DataPropertyClass.
      :type entity: Restriction

      :return: The OWLDataHasValue representation of the restriction, or None if the entity is not a valid data property has-value restriction.

      :rtype: typing.Optional[OWLDataHasValue]



   .. py:method:: to_owl_data_intersection_of(entity: owlready2.And) -> Optional[pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf]

      Converts a logical `And` entity into its corresponding OWL data intersection representation, validating that the input is an `And` instance and that all contained classes are valid data ranges, such as data properties, datatypes, or constrained datatypes. The method recursively converts each component into an OWL data range and constructs an `OWLDataIntersectionOf` object if all conversions succeed. To optimize performance, the result is cached internally for subsequent calls, and the method returns `None` if the input is invalid, contains unsupported component types, or if any component fails to convert.

      :param entity: The `And` entity representing a logical intersection of data types or data ranges to be converted into an OWL data intersection.
      :type entity: And

      :return: An OWLDataIntersectionOf object representing the intersection of data ranges defined by the And entity, or None if the entity is invalid or its components cannot be converted to data ranges.

      :rtype: typing.Optional[OWLDataIntersectionOf]



   .. py:method:: to_owl_data_max_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality]

      Attempts to convert a Restriction entity into an OWLDataMaxCardinality object by validating its type and associated property. The method specifically targets restrictions defined with `maxCardinality` or `maxQualifiedCardinality` and requires the property to be a DataPropertyClass. It retrieves the data range from the graph and constructs the cardinality object, utilizing an internal cache to store and return previously processed instances. If the entity is invalid, does not meet the type criteria, or lacks the necessary data range or property conversion, the method returns None.

      :param entity: An instance of Restriction representing a maximum cardinality constraint on a data property. The entity must be of type maxCardinality or maxQualifiedCardinality and have a property of type DataPropertyClass.
      :type entity: Restriction

      :return: The OWLDataMaxCardinality representation of the restriction, or None if the entity is invalid or does not represent a data max cardinality restriction.

      :rtype: typing.Optional[OWLDataMaxCardinality]



   .. py:method:: to_owl_data_min_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality]

      This method attempts to construct an OWLDataMinCardinality object from a given Restriction entity, strictly validating the entity's type and property characteristics. It requires the restriction to be defined as either an OWL.minCardinality or OWL.minQualifiedCardinality and ensures the restricted property is a DataPropertyClass. Upon successful validation, the method queries the underlying graph for the specific data range and recursively converts the property using the instance's data property converter. To improve performance, the method caches the generated object in an internal dictionary, returning the cached instance on subsequent calls. If the input entity is invalid, missing required data, or fails conversion steps, the method returns None.

      :param entity: The entity to be converted into an OWLDataMinCardinality representation. It must be a Restriction of type minCardinality or minQualifiedCardinality with a DataPropertyClass property.
      :type entity: Restriction

      :return: The OWLDataMinCardinality representation of the restriction, or None if the entity is invalid or does not define a data minimum cardinality.

      :rtype: typing.Optional[OWLDataMinCardinality]



   .. py:method:: to_owl_data_one_of(entity: owlready2.OneOf) -> Optional[pyowl2.data_range.data_one_of.OWLDataOneOf]

      Converts a provided `OneOf` entity into its corresponding `OWLDataOneOf` representation, ensuring that the entity is valid and contains only literal or base datatype instances. If the input is not a `OneOf` instance, is empty, or contains non-literal values, the method returns `None`. The method implements a caching mechanism by storing the generated `OWLDataOneOf` object in `self.data_ones_of`, returning the cached instance on subsequent calls for the same entity to avoid redundant processing.

      :param entity: The OneOf entity to convert. It must contain a non-empty set of instances, all of which must be literals or valid base data types.
      :type entity: OneOf

      :return: The OWLDataOneOf representation of the entity, or None if the entity is invalid, empty, or contains non-literal instances.

      :rtype: typing.Optional[OWLDataOneOf]



   .. py:method:: to_owl_data_property(property: owlready2.DataPropertyClass) -> Optional[pyowl2.expressions.data_property.OWLDataProperty]

      Retrieves or creates an OWL data property representation corresponding to the provided input property. The method first validates the input, ensuring it is a non-null instance of DataPropertyClass, and returns None if this check fails. It then consults an internal cache to determine if the property has already been processed; if not, a new OWLDataProperty is instantiated using the current namespace and the property's name and stored in the cache. Finally, the method returns the cached or newly created OWLDataProperty instance.

      :param property: The DataPropertyClass instance to be converted into an OWLDataProperty.
      :type property: DataPropertyClass

      :return: The corresponding OWLDataProperty instance for the given property, or None if the input is invalid.

      :rtype: typing.Optional[OWLDataProperty]



   .. py:method:: to_owl_data_property_assertion(individual_source: owlready2.NamedIndividual, property: owlready2.DataPropertyClass, target: rdflib.Literal, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion]

      Constructs an OWL data property assertion axiom linking a named individual to a literal value via a specific data property. The method performs strict validation on the inputs, ensuring the source is a named individual, the property is a data property, and the target is a literal, returning None if these conditions are not met. It maintains an internal cache of assertions to prevent duplication; if the specific combination does not already exist, it attempts to resolve the corresponding OWL expressions for the individual and property. During creation, it attaches annotations either from the provided argument or by retrieving them automatically based on the source and property. The method returns the cached or newly created assertion, or None if the underlying expressions cannot be resolved.

      :param individual_source: The named individual acting as the subject of the data property assertion.
      :type individual_source: NamedIndividual
      :param property: The data property linking the source individual to the target literal value.
      :type property: DataPropertyClass
      :param target: The literal value assigned to the source individual via the data property.
      :type target: Literal
      :param annotations: Optional list of OWLAnnotation objects to attach to the axiom. If not provided, default annotations are retrieved automatically.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLDataPropertyAssertion axiom representing the relationship between the source individual, data property, and target literal, or None if the inputs are invalid or the conversion fails.

      :rtype: typing.Optional[OWLDataPropertyAssertion]



   .. py:method:: to_owl_data_property_declaration(property: owlready2.DataPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]

      Converts a given DataPropertyClass instance into its corresponding OWLDeclaration representation. The method validates the input type and checks an internal cache to avoid redundant processing. If the declaration has not yet been generated, it attempts to retrieve the OWL data property expression via the `to_owl_data_property` method. Upon successful retrieval, it constructs a new OWLDeclaration, applying either the provided annotations or automatically fetching default ones if none are supplied. The resulting declaration is cached within the instance and returned, while invalid inputs or conversion failures result in a None return value.

      :param property: The data property to be converted into an OWL declaration.
      :type property: DataPropertyClass
      :param annotations: Optional list of annotations to attach to the OWL declaration. If provided, these override the default annotations.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLDeclaration instance corresponding to the specified data property, or None if the property is invalid or cannot be converted.

      :rtype: typing.Optional[OWLDeclaration]



   .. py:method:: to_owl_data_property_domain(property: owlready2.DataPropertyClass, domain: owlready2.ThingClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain]

      Generates an OWL axiom defining the domain of a data property by converting a `DataPropertyClass` and a `ThingClass` into an `OWLDataPropertyDomain` instance. The method performs validation to ensure the property is of the correct type and that both arguments are present, returning `None` if these checks fail or if the underlying OWL expressions cannot be resolved. It utilizes an internal cache to store generated axioms; if the property has already been processed, the cached instance is returned immediately. Otherwise, it resolves the OWL expressions for the property and domain using helper methods, determines the appropriate annotations—either from the input arguments or by retrieving them automatically—and constructs the new axiom before storing it in the cache.

      :param property: An instance representing the data property whose domain is being specified.
      :type property: DataPropertyClass
      :param domain: The class that serves as the domain for the data property.
      :type domain: ThingClass
      :param annotations: Optional list of annotations to attach to the resulting axiom. If provided, these override any automatically retrieved annotations.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLDataPropertyDomain axiom representing the domain relationship between the provided property and class, or None if the inputs are invalid or the conversion fails.

      :rtype: typing.Optional[OWLDataPropertyDomain]



   .. py:method:: to_owl_data_property_range(property: owlready2.DataPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange]

      Converts a `DataPropertyClass` instance into an `OWLDataPropertyRange` axiom, defining the specific data type range for the property. The method validates the input type and checks an internal cache to return a previously generated instance if available. If the instance is not cached, it attempts to resolve the OWL data property expression and the OWL data range from the property's definition; if either component cannot be resolved, the method returns `None`. Otherwise, it constructs the `OWLDataPropertyRange` object, attaching either the explicitly provided annotations or those retrieved from the underlying graph, stores the result in the cache, and returns the new axiom.

      :param property: The data property to convert into an OWL data property range axiom.
      :type property: DataPropertyClass
      :param annotations: Optional list of OWL annotations to attach to the axiom. If omitted, annotations are automatically retrieved from the source property.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWL data property range axiom corresponding to the specified property, or None if the property is invalid or the range cannot be resolved.

      :rtype: typing.Optional[OWLDataPropertyRange]



   .. py:method:: to_owl_data_some_values_from(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom]

      Converts a Restriction entity into an OWLDataSomeValuesFrom object, representing an existential restriction on a data property. The method performs validation to ensure the input entity is a Restriction with the specific OWL type 'someValuesFrom' and that its property is a DataPropertyClass. If these conditions are not met, or if the required data range cannot be retrieved from the underlying graph, the method returns None. Additionally, it utilizes an internal cache to store and retrieve converted instances, preventing redundant processing of the same entity.

      :param entity: The Restriction instance to convert into an OWLDataSomeValuesFrom representation. It must be of type OWL.someValuesFrom and have a property of type DataPropertyClass to be considered valid.
      :type entity: Restriction

      :return: Returns the OWLDataSomeValuesFrom object corresponding to the provided Restriction entity, or None if the entity is not a valid data property someValuesFrom restriction.

      :rtype: typing.Optional[OWLDataSomeValuesFrom]



   .. py:method:: to_owl_data_union_of(entity: owlready2.Or) -> Optional[pyowl2.class_expression.object_union_of.OWLObjectUnionOf]

      Converts a logical 'Or' entity into its corresponding OWL data union representation, ensuring that all operands are valid data ranges or base datatypes. The method performs strict validation to confirm that the input is an instance of 'Or' and that its constituent classes are either data properties, datatypes, or constrained datatypes. If the validation passes, it recursively retrieves the OWL data range for each operand and constructs an OWLDataUnionOf object, caching the result to optimize subsequent lookups. The method returns None if the input entity is invalid, contains unsupported class types, or if any operand fails to convert to a valid data range.

      :param entity: The Or entity representing a union of data types to be converted into an OWLDataUnionOf.
      :type entity: Or

      :return: An OWLDataUnionOf object representing the provided Or entity, or None if the entity is invalid or its components cannot be converted to valid data ranges.

      :rtype: typing.Optional[OWLObjectUnionOf]



   .. py:method:: to_owl_datatype(entity: Union[owlready2.DatatypeClass, type]) -> Optional[Union[pyowl2.base.datatype.OWLDatatype, set[pyowl2.base.datatype.OWLDatatype]]]

      Retrieves or creates an OWL datatype representation for a specified entity, which may be a DatatypeClass instance or a standard Python type. The method validates the input, returning None if the entity is invalid or unsupported. For Python built-in types like integers or strings, it maps them to their corresponding XML Schema Definition (XSD) datatypes, while custom DatatypeClass instances are mapped to IRIs based on the getter's namespace. As a side effect, the method caches newly created OWLDatatype instances in an internal dictionary to ensure object identity across multiple calls.

      :param entity: The Python built-in type or DatatypeClass instance to be mapped to its corresponding OWLDatatype.
      :type entity: typing.Union[DatatypeClass, type]

      :return: The OWLDatatype instance representing the input entity, mapping Python built-ins to XSD types or handling DatatypeClass instances. Returns None if the entity is invalid or unsupported.

      :rtype: typing.Optional[typing.Union[OWLDatatype, set[OWLDatatype]]]



   .. py:method:: to_owl_datatype_declaration(entity: owlready2.DatatypeClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]

      Generates and caches an OWL declaration axiom for a specific datatype entity. The method validates the input to ensure it is a `DatatypeClass` instance, returning None if the entity is invalid or if the underlying OWL datatype expression cannot be retrieved. If the declaration does not already exist in the internal cache, it creates a new `OWLDeclaration` instance, incorporating either the provided annotations or default annotations derived from the entity. The resulting declaration is stored in the internal `declarations` dictionary to prevent redundant processing and is then returned.

      :param entity: The DatatypeClass instance to be converted into an OWL declaration axiom.
      :type entity: DatatypeClass
      :param annotations: Optional list of OWL annotations to attach to the declaration axiom. If provided, these override the default annotations.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLDeclaration axiom representing the declaration of the specified DatatypeClass, including any provided or derived annotations. Returns None if the entity is invalid or the OWL datatype conversion fails; otherwise, returns the existing declaration instance if it has already been generated.

      :rtype: typing.Optional[OWLDeclaration]



   .. py:method:: to_owl_datatype_restriction(entity: owlready2.ConstrainedDatatype) -> Optional[pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction]

      Converts a ConstrainedDatatype entity into its corresponding OWLDatatypeRestriction representation, handling validation and caching internally. The method first verifies that the input is a valid ConstrainedDatatype instance. If the entity has not been processed before, it queries the underlying graph to determine the base datatype via the OWL.onDatatype property; if this lookup fails, the method returns None. Upon successfully retrieving the base datatype, the method constructs a new restriction by mapping specific attributes of the entity—such as minimum and maximum inclusive or exclusive values—to their corresponding OWL facets. The resulting object is cached for future use and returned.

      :param entity: The constrained datatype instance to be converted into an OWL datatype restriction.
      :type entity: ConstrainedDatatype

      :return: The OWLDatatypeRestriction representation of the ConstrainedDatatype, or None if the entity is invalid or the base datatype cannot be determined.

      :rtype: typing.Optional[OWLDatatypeRestriction]



   .. py:method:: to_owl_different_individuals(individuals: Union[tuple[owlready2.NamedIndividual, Ellipsis], owlready2.AllDifferent]) -> Optional[pyowl2.axioms.assertion.OWLDifferentIndividuals]

      Converts a tuple of `NamedIndividual` instances or an `AllDifferent` container into an `OWLDifferentIndividuals` axiom, ensuring that all specified entities are distinct. The method performs rigorous validation, rejecting empty inputs, tuples with fewer than two elements, or any collection containing entities that are not named individuals. It utilizes an internal cache to store generated axioms, returning a cached instance if the specific combination of individuals has already been processed to avoid redundant creation. During the conversion process, the method recursively maps each individual to its corresponding OWL expression and attempts to retrieve relevant annotations, using different strategies for tuples versus `AllDifferent` instances. If the input is invalid, contains non-convertible individuals, or fails validation, the method returns None; otherwise, it returns the constructed or cached axiom.

      :param individuals: A tuple of NamedIndividual objects or an AllDifferent instance representing the entities to be asserted as pairwise distinct.
      :type individuals: typing.Union[tuple[NamedIndividual, ...], AllDifferent]

      :return: An OWLDifferentIndividuals axiom representing the difference relationship between the provided individuals, or None if the input is invalid, contains fewer than two individuals, or if any individual expression cannot be retrieved.

      :rtype: typing.Optional[OWLDifferentIndividuals]



   .. py:method:: to_owl_disjoint_classes(classes: Union[tuple[owlready2.ThingClass], owlready2.AllDifferent]) -> Optional[pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses]

      Retrieves or constructs an OWL axiom representing a disjointness relationship between classes, accepting either a tuple of exactly two `ThingClass` instances or an `AllDifferent` instance. The method validates the input and attempts to resolve the corresponding OWL class expressions for the entities involved; if any expression cannot be retrieved, it returns None. Upon successful resolution, it creates an `OWLDisjointClasses` instance, automatically attaching relevant annotations derived from the source data, and stores the result in an internal cache. Subsequent calls with the same input will return the cached object, while invalid inputs or those failing expression resolution result in a None value.

      :param classes: A tuple of ThingClass instances or an AllDifferent instance representing the classes to be defined as disjoint.
      :type classes: typing.Union[tuple[ThingClass], AllDifferent]

      :return: The OWLDisjointClasses axiom corresponding to the provided classes, or None if the input is invalid or conversion fails.

      :rtype: typing.Optional[OWLDisjointClasses]



   .. py:method:: to_owl_disjoint_data_properties(classes: Union[tuple[owlready2.DataPropertyClass, Ellipsis], owlready2.AllDifferent]) -> Optional[pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties]

      Converts a representation of disjoint data properties into a formal OWL axiom, accepting either a tuple of exactly two data property classes or an AllDifferent instance. The function strictly validates the input, returning None if the tuple does not contain exactly two elements, if any element is not a DataPropertyClass, or if the provided AllDifferent instance contains invalid entities. It attempts to translate the internal property representations into OWL data property expressions, returning None if any translation fails. Additionally, the method automatically retrieves and attaches relevant annotations based on the input structure, distinguishing between binary disjointness and general AllDifferent declarations. As a side effect, the successfully created OWLDisjointDataProperties instance is cached in the instance's disjoint_data_properties dictionary to ensure reuse.

      :param classes: A tuple of DataPropertyClass instances or an AllDifferent instance representing the data properties that are mutually disjoint.
      :type classes: typing.Union[tuple[DataPropertyClass, ...], AllDifferent]

      :return: An OWLDisjointDataProperties instance representing the disjointness relationship between the provided data properties, or None if the input is invalid or conversion fails.

      :rtype: typing.Optional[OWLDisjointDataProperties]



   .. py:method:: to_owl_disjoint_object_properties(properties: Union[tuple[owlready2.ObjectPropertyClass], owlready2.AllDifferent]) -> Optional[pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties]

      This method retrieves or constructs an OWL axiom representing a disjointness relationship between object properties, accepting either a tuple of exactly two `ObjectPropertyClass` instances or an `AllDifferent` instance. It validates the input structure and types, returning `None` if the input is empty, contains invalid entities, or if the underlying properties cannot be converted to OWL expressions. The method employs an internal cache to store generated axioms, populating it with new instances that include annotations derived from the source data. If the input is already cached, the cached instance is returned; otherwise, a new `OWLDisjointObjectProperties` object is created and stored.

      :param properties: The object properties to be defined as disjoint, provided as a tuple of ObjectPropertyClass instances or an AllDifferent instance.
      :type properties: typing.Union[tuple[ObjectPropertyClass], AllDifferent]

      :return: An OWLDisjointObjectProperties axiom representing the disjointness of the provided object properties, or None if the input is invalid or conversion fails.

      :rtype: typing.Optional[OWLDisjointObjectProperties]



   .. py:method:: to_owl_disjoint_union(main_class: owlready2.EntityClass, classes: tuple[owlready2.EntityClass]) -> Optional[pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion]

      Constructs and retrieves an OWLDisjointUnion axiom that defines a main class as the disjoint union of a tuple of constituent classes. The method performs validation to ensure the inputs are non-empty and that the tuple contains at least three classes; otherwise, it returns None. It checks an internal cache to return previously generated axioms, and if the combination is new, it attempts to resolve the OWL class expressions for the main class and all constituent classes. If any class expression cannot be resolved, the method returns None. Successfully created axioms are stored in the cache along with any applicable annotations retrieved for the main class before being returned.

      :param main_class: The class equivalent to the disjoint union of the provided classes.
      :type main_class: EntityClass
      :param classes: A tuple of disjoint entity classes whose union is equivalent to the main class. The tuple must contain at least three elements to be considered valid.
      :type classes: tuple[EntityClass]

      :return: An OWLDisjointUnion axiom representing the main class as the disjoint union of the provided classes, or None if the inputs are invalid or fewer than three classes are provided.

      :rtype: typing.Optional[OWLDisjointUnion]



   .. py:method:: to_owl_equivalent_classes(classes: tuple[owlready2.EntityClass], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses]

      Retrieves or constructs an OWL axiom representing the equivalence relationship among a tuple of entity classes. The method validates that the input tuple contains at least two elements, as an equivalence relationship requires multiple participants. It utilizes an internal cache to store generated axioms, ensuring that subsequent calls with the same tuple return the existing instance rather than creating a duplicate. For uncached tuples, it attempts to resolve each class to its corresponding OWL class expression; if this resolution fails for any member, the method returns None. Optionally, a list of OWL annotations can be attached to the resulting axiom.

      :param classes: A tuple of EntityClass instances representing the classes to be defined as equivalent. The tuple must contain at least two elements to form a valid equivalence relationship.
      :type classes: tuple[EntityClass]
      :param annotations: Optional list of annotations to include in the OWLEquivalentClasses axiom.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLEquivalentClasses axiom representing the equivalence relationship between the provided classes, or None if the input contains fewer than two classes or if any class expression cannot be retrieved.

      :rtype: typing.Optional[OWLEquivalentClasses]



   .. py:method:: to_owl_equivalent_data_properties(classes: tuple[owlready2.DataPropertyClass, Ellipsis], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties]

      This method constructs an OWL axiom representing the equivalence relationship between a set of data properties, provided as a tuple of DataPropertyClass instances. It performs strict validation to ensure the input is a non-empty tuple containing only valid data property classes, returning None if these conditions are not met. If the specific combination of properties has not yet been processed, it converts each property into its corresponding OWL data property expression; if any conversion fails, the method returns None. Upon successful conversion, it creates an OWLEquivalentDataProperties instance, optionally attaching the provided annotations, and caches the result within the instance's dictionary to prevent redundant processing. The method returns the resulting axiom or None if the input is invalid or conversion is unsuccessful.

      :param classes: A tuple of DataPropertyClass instances representing the data properties that are equivalent to each other.
      :type classes: tuple[DataPropertyClass, ...]
      :param annotations: Optional list of annotations to attach to the resulting OWL equivalence axiom.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLEquivalentDataProperties axiom representing the equivalence of the input data properties, optionally annotated. Returns None if the input is invalid, contains non-data property instances, or if any property conversion fails.

      :rtype: typing.Optional[OWLEquivalentDataProperties]



   .. py:method:: to_owl_equivalent_object_properties(properties: tuple[owlready2.ObjectPropertyClass], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties]

      Converts a tuple of internal object property representations into an OWL axiom asserting that the properties are equivalent. The method validates the input by ensuring the tuple is non-empty and consists exclusively of ObjectPropertyClass instances, returning None if the input is invalid. It employs an internal caching mechanism to store generated axioms, checking the cache before performing any conversions. If the tuple is not cached, the method attempts to translate each property into its corresponding OWL expression; if any property fails to translate, the method returns None. Upon successful translation, it constructs a new OWLEquivalentObjectProperties instance, optionally attaches the provided annotations, stores the result in the cache, and returns the axiom.

      :param properties: A tuple of ObjectPropertyClass instances representing the properties to be declared equivalent. The tuple must contain at least two properties to form a valid equivalence relationship.
      :type properties: tuple[ObjectPropertyClass]
      :param annotations: Optional list of OWL annotations to attach to the equivalent object properties axiom.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLEquivalentObjectProperties instance representing the equivalence relationship between the provided properties, or None if the input is invalid or any property expression cannot be retrieved.

      :rtype: typing.Optional[OWLEquivalentObjectProperties]



   .. py:method:: to_owl_functional_data_property(property: owlready2.DataPropertyClass) -> Optional[pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty]

      Converts a `DataPropertyClass` instance into an `OWLFunctionalDataProperty` axiom, provided the property is defined as functional. The method validates the input by checking its type and ensuring `FunctionalProperty` is listed among its characteristics; it returns `None` if these conditions are not met or if the underlying OWL data property expression cannot be generated. To optimize performance, the method caches generated axioms in an internal dictionary, retrieving them from the cache on subsequent calls for the same property. When creating a new axiom, it relies on helper methods to generate the base data property expression and extract relevant annotations associated with the functional characteristic.

      :param property: The data property to be converted into an OWL functional data property axiom.
      :type property: DataPropertyClass

      :return: The OWLFunctionalDataProperty axiom for the provided data property, or None if the property is invalid, not functional, or conversion fails.

      :rtype: typing.Optional[OWLFunctionalDataProperty]



   .. py:method:: to_owl_functional_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.functional_object_property.OWLFunctionalObjectProperty]

      This method attempts to convert a provided ObjectPropertyClass into an OWLFunctionalObjectProperty, representing the functional characteristic of the property within an OWL ontology. It validates the input to ensure it is a valid ObjectPropertyClass and explicitly checks for the presence of the FunctionalProperty characteristic in its inheritance chain; if either check fails, the method returns None. To avoid redundant processing, the method maintains an internal cache of previously converted properties. If the property is not cached, it relies on the `to_owl_object_property` method to generate the base property expression, returning None if that conversion fails. Upon successful generation, the method constructs the OWLFunctionalObjectProperty with associated annotations and stores it in the cache before returning the instance.

      :param property: The object property class instance to be converted into an OWL functional object property. The property must possess the FunctionalProperty characteristic to be successfully processed.
      :type property: ObjectPropertyClass

      :return: An OWLFunctionalObjectProperty instance representing the functional characteristic of the provided property, or None if the property is invalid, lacks the FunctionalProperty characteristic, or the underlying object property expression cannot be retrieved.

      :rtype: typing.Optional[OWLFunctionalObjectProperty]



   .. py:method:: to_owl_general_class_axiom(left: Union[owlready2.And, owlready2.Or, owlready2.Not, owlready2.Restriction], property: rdflib.URIRef, right: owlready2.EntityClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.general.OWLGeneralClassAxiom]

      Constructs an OWL general class axiom linking a left-hand side class expression, a specific property, and a right-hand side class. The method validates the input types, ensuring the left side is a complex expression (And, Or, Not, or Restriction) and the property is a URI reference. It then converts the class expressions into their OWL equivalents and creates the axiom, optionally including any provided annotations. To prevent duplication, the implementation caches created axioms internally, returning the existing instance if the specific combination of inputs has been processed before. If any input is invalid or the conversion process fails, the method returns None.

      :param left: The left-hand side class expression, which must be a boolean combination (And, Or, Not) or a Restriction.
      :type left: typing.Union[And, Or, Not, Restriction]
      :param property: The IRI representing the property that links the left-hand side class expression to the right-hand side class.
      :type property: URIRef
      :param right: The right-hand side class expression used to form the general class axiom.
      :type right: EntityClass
      :param annotations: Optional list of annotations to attach to the resulting axiom.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLGeneralClassAxiom corresponding to the provided left-hand side expression, property, and right-hand side class, or None if the inputs are invalid or the expressions cannot be retrieved.

      :rtype: typing.Optional[OWLGeneralClassAxiom]



   .. py:method:: to_owl_individual(individual: owlready2.NamedIndividual) -> Optional[pyowl2.abstracts.individual.OWLIndividual]

      Converts a `NamedIndividual` object into an `OWLIndividual` instance, utilizing an internal cache to manage object identity. The method validates the input, returning `None` if the provided individual is invalid or not of the correct type. If the individual has not been processed previously, it constructs a new `OWLIndividual`—choosing between `OWLAnonymousIndividual` and `OWLNamedIndividual` based on the input's IRI type—using the configured namespace and the individual's name. The resulting object is stored in the internal cache and returned, ensuring that subsequent calls with the same individual return the same instance.

      :param individual: The source instance to be converted into its corresponding OWLIndividual representation.
      :type individual: NamedIndividual

      :return: The OWLIndividual instance corresponding to the provided NamedIndividual, created with the current namespace if necessary, or None if the input is invalid.

      :rtype: typing.Optional[OWLIndividual]



   .. py:method:: to_owl_individual_declaration(individual: owlready2.NamedIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]

      Converts a provided NamedIndividual instance into an OWLDeclaration axiom, utilizing an internal cache to avoid redundant processing. The method validates the input type and attempts to retrieve the corresponding OWL individual expression; if the input is invalid or conversion fails, it returns None. When generating the declaration, it prioritizes explicitly provided annotations, but defaults to fetching them automatically if none are supplied. The resulting OWLDeclaration is stored in the instance's declarations dictionary before being returned, ensuring that subsequent calls with the same individual return the cached object.

      :param individual: The named individual entity to be converted into an OWL declaration axiom.
      :type individual: NamedIndividual
      :param annotations: Optional list of OWL annotations to attach to the declaration. If provided, these override the default annotations; otherwise, default annotations are retrieved.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLDeclaration instance representing the declaration of the specified NamedIndividual, or None if the individual is invalid or the conversion fails.

      :rtype: typing.Optional[OWLDeclaration]



   .. py:method:: to_owl_inverse_functional_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty]

      Retrieves or creates an OWL representation of an inverse functional object property from a given RDF object property class. The method validates the input to ensure it is an instance of ObjectPropertyClass and explicitly possesses the InverseFunctionalProperty characteristic; if these conditions are not met, it returns None. To optimize performance, the implementation caches results in an internal dictionary, checking this cache before generating new instances. When a new instance is required, it delegates to `to_owl_object_property` to obtain the underlying property expression and retrieves associated annotations to construct the final OWLInverseFunctionalObjectProperty.

      :param property: The object property class instance to be converted into an OWL inverse functional object property. The property must possess the InverseFunctionalProperty characteristic.
      :type property: ObjectPropertyClass

      :return: The OWLInverseFunctionalObjectProperty instance for the given property, or None if the property is invalid, not inverse functional, or conversion fails.

      :rtype: typing.Optional[OWLInverseFunctionalObjectProperty]



   .. py:method:: to_owl_inverse_object_properties(property: Union[owlready2.Inverse, owlready2.ObjectPropertyClass, int], inv_property: Union[owlready2.Inverse, owlready2.ObjectPropertyClass]) -> Optional[Union[pyowl2.expressions.inverse_object_property.OWLInverseObjectProperty, pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties]]

      Converts a property and its inverse into the corresponding OWL axiom representation, either `OWLInverseObjectProperty` or `OWLInverseObjectProperties`. The method validates the input types, accepting integers representing blank nodes, `Inverse` objects, or `ObjectPropertyClass` instances, and returns None if the inputs are invalid or conversion fails. It utilizes an internal cache to store and retrieve previously processed relationships, normalizing the order of property pairs to ensure consistency. When the property is a blank node, the method retrieves the node from the graph and constructs a singular inverse property axiom; for standard object properties, it resolves the OWL expressions for both sides and constructs a plural inverse properties axiom, including any associated annotations found in the graph.

      :param property: The object property involved in the inverse relationship, specified as an ObjectPropertyClass, an Inverse wrapper, or an integer representing a blank node ID.
      :type property: typing.Union[Inverse, ObjectPropertyClass, int]
      :param inv_property: The inverse property corresponding to the `property` argument, provided as an Inverse instance or an ObjectPropertyClass.
      :type inv_property: typing.Union[Inverse, ObjectPropertyClass]

      :return: An OWLInverseObjectProperty or OWLInverseObjectProperties instance representing the inverse relationship between the provided properties, or None if the inputs are invalid or conversion fails.

      :rtype: typing.Optional[typing.Union[OWLInverseObjectProperty, OWLInverseObjectProperties]]



   .. py:method:: to_owl_irreflexive_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty]

      Attempts to convert a source object property into an OWL irreflexive object property representation, provided the input is valid and explicitly marked with the IrreflexiveProperty characteristic. If the input is not an ObjectPropertyClass or lacks the required characteristic, the method returns None. The process utilizes an internal cache to store and retrieve previously created instances, ensuring that duplicate conversions are avoided. When a new instance is required, the method retrieves the underlying object property expression and associated annotations to construct the final OWL entity.

      :param property: The object property instance to be converted into an OWL irreflexive object property.
      :type property: ObjectPropertyClass

      :return: The OWLIrreflexiveObjectProperty representation of the provided property if it is valid and marked as irreflexive, or None if the property is invalid, not irreflexive, or the conversion fails.

      :rtype: typing.Optional[OWLIrreflexiveObjectProperty]



   .. py:method:: to_owl_negative_data_property_assertion(individual_source: owlready2.NamedIndividual, property: owlready2.DataPropertyClass, target: rdflib.Literal) -> Optional[pyowl2.axioms.assertion.OWLNegativeDataPropertyAssertion]

      Constructs an OWL negative data property assertion representing the relationship where a specific individual does not have a particular data property value. The method validates the input types, ensuring the source is a named individual, the property is a data property, and the target is a literal. If the inputs are valid, it resolves the corresponding OWL property and individual expressions and retrieves any associated annotations. To ensure consistency and performance, it caches the resulting assertion instance based on the combination of inputs, returning the cached instance on subsequent calls. Returns None if any input is invalid, of the wrong type, or if the required OWL expressions cannot be resolved.

      :param individual_source: The named individual acting as the subject of the negative data property assertion.
      :type individual_source: NamedIndividual
      :param property: The data property that the source individual is asserted not to possess with the given literal value.
      :type property: DataPropertyClass
      :param target: The literal value that the source individual is asserted not to possess for the specified data property.
      :type target: Literal

      :return: An OWLNegativeDataPropertyAssertion instance representing the negative data property assertion for the given source individual, property, and target literal, or None if the inputs are invalid or conversion fails.

      :rtype: typing.Optional[OWLNegativeDataPropertyAssertion]



   .. py:method:: to_owl_negative_object_property_assertion(individual_source: owlready2.NamedIndividual, property: owlready2.ObjectPropertyClass, individual_target: owlready2.NamedIndividual) -> Optional[pyowl2.axioms.assertion.OWLNegativeObjectPropertyAssertion]

      Constructs an OWL negative object property assertion from a source individual, an object property, and a target individual. It validates the input types and existence, returning None if any argument is invalid or if the conversion of the property or individuals to OWL expressions fails. To ensure consistency and prevent redundancy, the method normalizes the internal storage key by handling inverse properties, preferring the lexicographically smaller property name when applicable. The resulting assertion is cached within the instance's dictionary of negative object property assertions, and any associated annotations are included during creation.

      :param individual_source: The source individual for the assertion, representing the entity from which the object property relationship is explicitly denied.
      :type individual_source: NamedIndividual
      :param property: The object property that is asserted not to relate the source individual to the target individual.
      :type property: ObjectPropertyClass
      :param individual_target: The individual representing the target of the negative object property assertion.
      :type individual_target: NamedIndividual

      :return: An OWLNegativeObjectPropertyAssertion representing the negative relationship between the source individual, property, and target individual, or None if the inputs are invalid or the conversion to OWL entities fails.

      :rtype: typing.Optional[OWLNegativeObjectPropertyAssertion]



   .. py:method:: to_owl_object_all_values_from(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom]

      Converts a provided RDF/XML Restriction entity into an OWLObjectAllValuesFrom object, which represents a universal quantification restriction in the OWL API. The method validates that the input entity is a Restriction with the specific type `OWL.allValuesFrom` and that its property is an ObjectPropertyClass; if these conditions are not met, or if the conversion of the nested property or value fails, it returns None. To optimize performance and maintain object identity, the method caches the resulting OWLObjectAllValuesFrom instance in an internal dictionary, returning the cached version if the entity has already been processed.

      :param entity: An instance of Restriction to be converted to an OWLObjectAllValuesFrom representation. The entity must be of type OWL.allValuesFrom and its property must be an ObjectPropertyClass.
      :type entity: Restriction

      :return: An OWLObjectAllValuesFrom instance representing the provided Restriction entity, or None if the entity is invalid, not an 'allValuesFrom' restriction, or if the property is not an ObjectPropertyClass.

      :rtype: typing.Optional[OWLObjectAllValuesFrom]



   .. py:method:: to_owl_object_complement_of(entity: owlready2.Not, expression: owlready2.ThingClass) -> Optional[pyowl2.class_expression.object_complement_of.OWLObjectComplementOf]

      Converts a logical negation entity into its corresponding OWL object complement representation by processing the provided class expression. It validates that the input entity is an instance of `Not` and recursively resolves the inner expression into an OWL class expression. The method utilizes an internal cache to store generated objects, ensuring that repeated calls with the same entity return the existing instance rather than creating a new one. If the entity is invalid, not of the correct type, or if the inner expression cannot be processed, the method returns `None`.

      :param entity: The 'Not' entity to be transformed into an OWL object complement representation.
      :type entity: Not
      :param expression: The class expression to be negated to form the complement.
      :type expression: ThingClass

      :return: An OWLObjectComplementOf instance representing the complement of the provided class expression, or None if the entity is invalid or the expression cannot be processed.

      :rtype: typing.Optional[OWLObjectComplementOf]



   .. py:method:: to_owl_object_exact_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality]

      This method attempts to construct an OWLObjectExactCardinality object from a given Restriction entity, serving as a specific converter within the RDF/XML parsing context. It performs strict validation to ensure the entity represents a qualified cardinality restriction involving an object property. Upon successful validation, it recursively converts the associated property and filler value into their OWL representations and caches the resulting object to optimize performance. The method returns None if the entity is invalid, does not match the required type, or if the conversion of its internal components fails.

      :param entity: The Restriction entity to convert into an OWLObjectExactCardinality representation. It must be a qualified cardinality restriction with a property of type ObjectPropertyClass.
      :type entity: Restriction

      :return: The OWLObjectExactCardinality representation of the entity, or None if the entity is invalid or does not represent an object property exact cardinality restriction.

      :rtype: typing.Optional[OWLObjectExactCardinality]



   .. py:method:: to_owl_object_has_self(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_has_self.OWLObjectHasSelf]

      Converts a provided `Restriction` entity into its corresponding `OWLObjectHasSelf` representation, performing strict validation on the entity's type and associated property. The method verifies that the restriction type corresponds to `OWL.hasSelf` and that the property is an instance of `ObjectPropertyClass`. If validation passes, it recursively converts the property, instantiates the `OWLObjectHasSelf` object, and caches the result in the `objects_has_self` dictionary to prevent redundant processing. Returns `None` if the input is invalid, the restriction type is incorrect, the property is not an object property, or if the nested property conversion fails.

      :param entity: The entity to convert into an OWLObjectHasSelf representation. It must be of type OWL.hasSelf and have a property of type ObjectPropertyClass.
      :type entity: Restriction

      :return: The OWLObjectHasSelf instance corresponding to the restriction, or None if the entity is invalid, not a has-self restriction, or the property conversion fails.

      :rtype: typing.Optional[OWLObjectHasSelf]



   .. py:method:: to_owl_object_has_value(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_has_value.OWLObjectHasValue]

      This method attempts to transform a Restriction entity into an OWLObjectHasValue object, representing a specific type of class restriction in OWL. It validates that the input entity is a Restriction with a type corresponding to 'hasValue' and that its property is an ObjectPropertyClass. Upon successful validation, the method delegates the conversion of the property and the value to internal helper methods before constructing the final OWLObjectHasValue instance. To prevent redundant processing, the method caches the resulting object within the instance's `objects_has_value` dictionary. If the input entity fails any validation check or if the conversion of its components is unsuccessful, the method returns None.

      :param entity: A Restriction entity representing a has-value constraint on an object property, intended for conversion into an OWLObjectHasValue object.
      :type entity: Restriction

      :return: The OWLObjectHasValue representation of the given Restriction, or None if the entity is invalid, not a hasValue restriction, or if the property or value cannot be converted.

      :rtype: typing.Optional[OWLObjectHasValue]



   .. py:method:: to_owl_object_intersection_of(entity: owlready2.And) -> Optional[pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf]

      Converts a logical `And` entity into its corresponding `OWLObjectIntersectionOf` representation, recursively processing the entity's constituent classes. The method first verifies that the input is a valid `And` instance and checks an internal cache to prevent redundant object creation. For each class contained within the entity, it attempts to retrieve the OWL class expression; if any component cannot be resolved, the method returns `None`. If all components are successfully converted, the resulting intersection object is stored in the cache and returned.

      :param entity: An instance representing a logical conjunction of classes to be transformed into its OWL intersection representation.
      :type entity: And

      :return: An OWLObjectIntersectionOf instance representing the logical intersection of the classes in the And entity, or None if the entity is invalid or conversion fails.

      :rtype: typing.Optional[OWLObjectIntersectionOf]



   .. py:method:: to_owl_object_max_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality]

      Converts a provided RDF/XML Restriction entity into its corresponding OWLObjectMaxCardinality representation, provided the entity meets specific structural criteria. The method validates that the restriction type is either `OWL.maxCardinality` or `OWL.maxQualifiedCardinality` and that the associated property is an `ObjectPropertyClass`. If the validation passes, it recursively resolves the object property and class expression components using helper methods before constructing the final object. To optimize performance, the result is cached within the instance's `objects_max_cardinality` dictionary for subsequent access. The method returns None if the input entity is invalid, does not match the required types, or if the conversion of nested components fails.

      :param entity: The Restriction entity to convert into an OWLObjectMaxCardinality representation. It must be of type OWL.maxCardinality or OWL.maxQualifiedCardinality and possess an ObjectPropertyClass property.
      :type entity: Restriction

      :return: The OWLObjectMaxCardinality representation of the provided Restriction entity, or None if the entity is not a valid object property max cardinality restriction.

      :rtype: typing.Optional[OWLObjectMaxCardinality]



   .. py:method:: to_owl_object_min_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality]

      Converts a Restriction entity into an OWLObjectMinCardinality object, validating that the entity represents a minimum cardinality constraint involving an object property. The method ensures the input is a Restriction instance with a type of OWL.minCardinality or OWL.minQualifiedCardinality and that its property is an ObjectPropertyClass; if these conditions are not met, or if the conversion of the property or value fails, it returns None. This method utilizes an internal cache to store generated instances, preventing redundant processing of the same entity. When a valid entity is not found in the cache, it constructs the OWLObjectMinCardinality by converting the associated property and value into their OWL representations and stores the result for future access.

      :param entity: The Restriction entity to convert. It must represent a minimum cardinality constraint (OWL.minCardinality or OWL.minQualifiedCardinality) involving an ObjectPropertyClass.
      :type entity: Restriction

      :return: The OWLObjectMinCardinality object representing the restriction, or None if the entity is invalid, not of the correct type, or if the property is not an object property.

      :rtype: typing.Optional[OWLObjectMinCardinality]



   .. py:method:: to_owl_object_one_of(entity: owlready2.OneOf) -> Optional[pyowl2.class_expression.object_one_of.OWLObjectOneOf]

      Converts a `OneOf` entity into its corresponding `OWLObjectOneOf` representation, ensuring the input is a valid, non-empty collection of named individuals. The method recursively transforms the contained instances into OWL individuals and caches the resulting object within the instance to prevent redundant processing of the same entity. It returns `None` if the input is invalid, empty, contains non-named individuals, or if the recursive conversion of any instance fails.

      :param entity: An instance representing a specific enumeration of named individuals to be converted into an OWL object one-of construct.
      :type entity: OneOf

      :return: The OWLObjectOneOf representation of the input entity, or None if the entity is invalid, empty, contains non-named individuals, or if instance conversion fails.

      :rtype: typing.Optional[OWLObjectOneOf]



   .. py:method:: to_owl_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.expressions.object_property.OWLObjectProperty]

      Converts a given `ObjectPropertyClass` instance into its corresponding `OWLObjectProperty` representation, utilizing an internal cache to manage object creation. The method first validates the input, returning `None` if the argument is missing or not an instance of `ObjectPropertyClass`. If the property is valid and not already stored in the `object_properties` dictionary, a new `OWLObjectProperty` is constructed using the instance's namespace and the property's name, then added to the cache. The method returns the cached or newly created property object, ensuring that repeated conversions of the same property yield the same instance.

      :param property: The ObjectPropertyClass instance to be converted into an OWLObjectProperty.
      :type property: ObjectPropertyClass

      :return: The OWLObjectProperty instance corresponding to the provided ObjectPropertyClass, retrieved from an internal cache or created anew. Returns None if the input is invalid or not an ObjectPropertyClass.

      :rtype: typing.Optional[OWLObjectProperty]



   .. py:method:: to_owl_object_property_assertion(individual_source: owlready2.NamedIndividual, property: owlready2.ObjectPropertyClass, individual_target: owlready2.NamedIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion]

      This method constructs and caches an OWL object property assertion representing a relationship between a source individual and a target individual. It performs strict validation to ensure the inputs are valid named individuals and an object property class, returning None if these checks fail. A key feature is the normalization of inverse properties: if the property has an inverse and its name is lexicographically greater than or equal to the inverse's name, the method swaps the arguments to use the inverse property, preventing duplicate assertions for inverse relationships. If the assertion is not already cached, it converts the inputs into their respective OWL expressions and instantiates the assertion, attaching either the provided annotations or automatically retrieving them from the context if the annotation list is omitted.

      :param individual_source: The individual acting as the subject of the object property assertion.
      :type individual_source: NamedIndividual
      :param property: The object property class representing the relationship to be asserted between the source and target individuals.
      :type property: ObjectPropertyClass
      :param individual_target: The target individual in the object property assertion relationship.
      :type individual_target: NamedIndividual
      :param annotations: Optional list of OWLAnnotation instances to attach to the axiom. If not provided, annotations are retrieved automatically.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLObjectPropertyAssertion axiom representing the relationship between the source individual, object property, and target individual, or None if the inputs are invalid or conversion fails.

      :rtype: typing.Optional[OWLObjectPropertyAssertion]



   .. py:method:: to_owl_object_property_declaration(property: owlready2.ObjectPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]

      Converts an ObjectPropertyClass instance into an OWLDeclaration axiom, handling validation and caching internally. The method first verifies that the input is a valid object property before attempting to retrieve its corresponding OWL expression. If the property has not been previously processed, it constructs a new declaration, optionally attaching either user-provided annotations or automatically generated ones based on the property's metadata. The result is cached in the internal declarations dictionary to ensure that subsequent calls for the same property return the same instance. Returns None if the input is invalid or if the underlying OWL object property expression cannot be generated.

      :param property: The object property to be converted into an OWL declaration axiom.
      :type property: ObjectPropertyClass
      :param annotations: Optional list of OWLAnnotation instances to include in the declaration axiom. If provided, these override the default annotations.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLDeclaration instance corresponding to the provided object property, or None if the property is invalid or cannot be converted.

      :rtype: typing.Optional[OWLDeclaration]



   .. py:method:: to_owl_object_property_domain(property: owlready2.ObjectPropertyClass, cls: owlready2.ThingClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain]

      Constructs an OWLObjectPropertyDomain axiom defining the domain of a given object property. The method validates the input property type and attempts to resolve the corresponding OWL expressions for both the property and the class. It utilizes an internal cache to return existing instances for previously processed properties, ensuring efficiency. If the optional `annotations` parameter is not provided, the method automatically retrieves annotations associated with the RDFS domain relationship. The operation returns None if the property is invalid, the class is missing, or if the conversion to OWL expressions fails.

      :param property: The object property for which the domain axiom is being created or retrieved.
      :type property: ObjectPropertyClass
      :param annotations: Optional list of OWLAnnotation instances to attach to the resulting axiom. If provided, these override automatically inferred annotations.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLObjectPropertyDomain axiom representing the domain relationship between the provided property and class, or None if the inputs are invalid or the conversion fails.

      :rtype: typing.Optional[OWLObjectPropertyDomain]



   .. py:method:: to_owl_object_property_range(property: owlready2.ObjectPropertyClass, cls: owlready2.ThingClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange]

      This method constructs an OWL object property range axiom that defines the valid class range for a given object property. It validates the inputs, ensuring the property is an instance of ObjectPropertyClass and the class is not null, returning None if these conditions are not met. The implementation utilizes an internal cache to store and retrieve previously generated axioms, avoiding redundant processing for the same property and class pair. If the axiom is not cached, the method attempts to convert the property and class into their corresponding OWL expressions; if either conversion fails, it returns None. Annotations for the axiom are either taken directly from the optional argument or automatically retrieved based on the RDF context. The resulting axiom is stored in the cache and returned to the caller.

      :param property: The ObjectPropertyClass instance representing the property for which the range is being defined.
      :type property: ObjectPropertyClass
      :param annotations: Optional list of OWLAnnotation instances to attach to the resulting object property range axiom. If provided, these override any automatically retrieved annotations.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLObjectPropertyRange instance representing the range relationship between the provided property and class, or None if the inputs are invalid or conversion fails.

      :rtype: typing.Optional[OWLObjectPropertyRange]



   .. py:method:: to_owl_object_some_values_from(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom]

      Converts a specific Restriction entity into an OWLObjectSomeValuesFrom object, ensuring the entity represents an existential restriction on an object property. The method performs strict validation to confirm the input is a Restriction with the type OWL.someValuesFrom and an ObjectPropertyClass property; it returns None if these conditions are not met. To optimize performance, the implementation caches generated instances in `self.objects_some_values_from`, returning the cached object if available. When creating a new instance, the method delegates to `to_owl_object_property` and `get_owl_class_expression` to transform the restriction's property and value, returning None if these dependent conversions fail.

      :param entity: The restriction entity to convert into an OWLObjectSomeValuesFrom representation. It must be of type OWL.someValuesFrom and have a property of type ObjectPropertyClass.
      :type entity: Restriction

      :return: The OWLObjectSomeValuesFrom representation of the provided restriction, or None if the entity is invalid, not a someValuesFrom restriction, or if the property or value cannot be converted.

      :rtype: typing.Optional[OWLObjectSomeValuesFrom]



   .. py:method:: to_owl_object_union_of(entity: owlready2.Or) -> Optional[pyowl2.class_expression.object_union_of.OWLObjectUnionOf]

      Converts a logical `Or` entity into an `OWLObjectUnionOf` instance by recursively translating its constituent class expressions. The method validates that the input is an instance of `Or` and utilizes an internal cache to memoize results, preventing redundant object creation for the same entity. If the entity is not cached, the method attempts to convert each class within the union using `get_owl_class_expression`; if any conversion fails, the method returns `None`. Upon successful conversion, the resulting `OWLObjectUnionOf` is stored in the cache and returned.

      :param entity: The `Or` object representing a logical disjunction of classes to be converted into an OWL union expression.
      :type entity: Or

      :return: The OWLObjectUnionOf object corresponding to the input entity, or None if the entity is invalid, empty, or contains classes that cannot be converted.

      :rtype: typing.Optional[OWLObjectUnionOf]



   .. py:method:: to_owl_reflexive_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.reflexive_object_property.OWLReflexiveObjectProperty]

      This method converts an `ObjectPropertyClass` instance into an `OWLReflexiveObjectProperty` representation, provided the input is valid and explicitly defined as reflexive. It performs validation to ensure the argument is an instance of `ObjectPropertyClass` and that `ReflexiveProperty` is listed among its characteristics; if these conditions are not met, the method returns None. To optimize performance, the method utilizes an internal cache, storing generated instances so that subsequent calls for the same property return the cached object immediately. When a new instance is required, the method retrieves the base object property expression via `to_owl_object_property` and gathers relevant annotations associated with the reflexive characteristic. If the base property expression cannot be resolved, the method returns None; otherwise, it constructs, caches, and returns the `OWLReflexiveObjectProperty` instance.

      :param property: The object property to convert into an OWL reflexive object property. The property must be an instance of ObjectPropertyClass and possess the ReflexiveProperty characteristic.
      :type property: ObjectPropertyClass

      :return: An OWLReflexiveObjectProperty instance representing the provided property if it is valid and has the ReflexiveProperty characteristic; otherwise, None.

      :rtype: typing.Optional[OWLReflexiveObjectProperty]



   .. py:method:: to_owl_same_individual(individuals: tuple[owlready2.NamedIndividual, Ellipsis], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.assertion.OWLSameIndividual]

      Converts a tuple of `NamedIndividual` instances into an `OWLSameIndividual` axiom, representing the equivalence of the provided individuals. The method validates the input to ensure it is a non-empty tuple consisting solely of `NamedIndividual` objects, returning `None` if the input is invalid. It leverages an internal cache to return existing axioms for known combinations of individuals. If the combination is not cached, the method attempts to translate each individual into its OWL representation; if any translation fails, it returns `None`. Upon successful translation, it constructs the `OWLSameIndividual` instance with optional annotations, updates the cache, and returns the resulting axiom.

      :param individuals: A tuple of NamedIndividual instances that are asserted to be identical.
      :type individuals: tuple[NamedIndividual, ...]
      :param annotations: Optional list of OWLAnnotation instances to attach to the generated OWLSameIndividual axiom.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLSameIndividual axiom representing the sameness of the provided individuals, or None if the input is invalid or conversion fails.

      :rtype: typing.Optional[OWLSameIndividual]



   .. py:method:: to_owl_sub_annotation_property_of(sub_property: owlready2.AnnotationPropertyClass, super_property: owlready2.AnnotationPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.annotations.OWLSubAnnotationPropertyOf]

      Constructs an OWL sub-annotation property of axiom representing a hierarchical relationship between two annotation properties. The method validates that both the sub-property and super-property arguments are valid instances of AnnotationPropertyClass, returning None if either is invalid. It employs an internal cache to store and retrieve axioms based on the property pair; if the pair is not already cached, the method attempts to resolve the corresponding OWL annotation property expressions. If this resolution fails, the method returns None. Upon success, it creates a new OWLSubAnnotationPropertyOf instance, optionally attaches the provided annotations, updates the cache, and returns the resulting axiom.

      :param sub_property: The annotation property instance representing the sub-property in the sub-property relationship.
      :type sub_property: AnnotationPropertyClass
      :param super_property: The annotation property representing the super-property in the sub-property relationship.
      :type super_property: AnnotationPropertyClass
      :param annotations: Optional list of annotations to be attached to the sub-property axiom.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLSubAnnotationPropertyOf axiom representing the sub-property relationship between the provided properties, or None if the inputs are invalid or conversion fails.

      :rtype: typing.Optional[OWLSubAnnotationPropertyOf]



   .. py:method:: to_owl_sub_data_property_of(sub_property: owlready2.DataPropertyClass, super_property: owlready2.DataPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf]

      Converts a pair of data properties into an OWL sub-property axiom, caching the result to ensure that repeated calls with the same arguments return the same instance. The method validates that both the sub-property and super-property are non-null instances of DataPropertyClass, returning None if validation fails. If the relationship is not already cached, it attempts to retrieve the corresponding OWL data property expressions; if this conversion fails, the method returns None. Annotations for the axiom are either taken directly from the optional input argument or retrieved dynamically from the underlying RDF structure if no explicit annotations are provided.

      :param sub_property: The data property instance representing the sub-property in the relationship, which is validated and converted into the subject of the OWLSubDataPropertyOf axiom.
      :type sub_property: DataPropertyClass
      :param super_property: The data property acting as the super-property (parent) in the sub-property relationship.
      :type super_property: DataPropertyClass
      :param annotations: Optional list of annotations to attach to the axiom. If provided, these are used directly; otherwise, annotations are retrieved automatically from the source properties.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: An OWLSubDataPropertyOf axiom representing the sub-property relationship between the provided properties, or None if the inputs are invalid or conversion fails.

      :rtype: typing.Optional[OWLSubDataPropertyOf]



   .. py:method:: to_owl_sub_object_property_of(sub_property: Union[tuple[owlready2.ObjectPropertyClass], owlready2.ObjectPropertyClass], super_property: owlready2.ObjectPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]

      Constructs an OWL axiom representing a sub-object-property relationship, accommodating both direct sub-property hierarchies and complex property chains. The method validates the input types, ensuring the super-property is an `ObjectPropertyClass` and the sub-property is either a single instance or a tuple of instances. It converts these properties into OWL expressions, returning `None` if the inputs are invalid or if the conversion process fails. A side effect of this method is the caching of generated axioms within an internal dictionary to prevent redundant creation. If annotations are not explicitly supplied, the method automatically retrieves them from the source properties, utilizing specific logic for property chains versus standard sub-property relationships.

      :param sub_property: The sub-property in the relationship, which can be a single ObjectPropertyClass or a tuple of ObjectPropertyClass instances representing an object property chain.
      :type sub_property: typing.Union[tuple[ObjectPropertyClass], ObjectPropertyClass]
      :param super_property: The parent object property that the sub-property is a specialization of.
      :type super_property: ObjectPropertyClass
      :param annotations: Optional list of annotations to attach to the axiom. If provided, these override any automatically retrieved annotations.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLSubObjectPropertyOf axiom representing the sub-property relationship between the provided properties, or None if the inputs are invalid or the expressions cannot be retrieved.

      :rtype: typing.Optional[OWLSubObjectPropertyOf]



   .. py:method:: to_owl_subclass_of(sub_class: owlready2.EntityClass, super_class: owlready2.EntityClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf]

      Constructs and retrieves an `OWLSubClassOf` axiom representing the relationship between a specified subclass and superclass. The method validates the input classes and checks an internal cache to prevent redundant creation of axioms for the same pair. If the pair is not cached, it attempts to resolve the OWL class expressions for both entities; if either expression cannot be retrieved, the method returns None. When generating the axiom, it applies the provided annotations or, if none are given, automatically retrieves them based on the relationship. The resulting axiom is stored in the cache and returned.

      :param sub_class: The instance representing the subclass in the subclass relationship.
      :type sub_class: EntityClass
      :param super_class: The EntityClass instance representing the superclass in the subclass relationship.
      :type super_class: EntityClass
      :param annotations: Optional list of OWL annotations to attach to the subclass axiom. If provided, these override the default annotations.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The OWLSubClassOf axiom representing the subclass relationship between the provided classes, or None if the inputs are invalid or their OWL expressions cannot be retrieved.

      :rtype: typing.Optional[OWLSubClassOf]



   .. py:method:: to_owl_symmetric_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.symmetric_object_property.OWLSymmetricObjectProperty]

      This method converts a provided `ObjectPropertyClass` into an `OWLSymmetricObjectProperty` instance, representing the symmetric characteristic of the property within the OWL ontology. It validates the input to ensure it is a valid object property and explicitly checks for the presence of the `SymmetricProperty` type in its definition, returning None if these conditions are not met. The method relies on `to_owl_object_property` to obtain the underlying property expression and attaches any relevant annotations found for the symmetric property axiom. As a side effect, it caches the generated instance in an internal dictionary to prevent redundant processing for the same property in subsequent calls.

      :param property: The object property to convert into an OWL symmetric object property. It must be a valid instance possessing the SymmetricProperty characteristic.
      :type property: ObjectPropertyClass

      :return: The OWLSymmetricObjectProperty instance corresponding to the input property, or None if the property is not symmetric or conversion fails.

      :rtype: typing.Optional[OWLSymmetricObjectProperty]



   .. py:method:: to_owl_transitive_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty]

      Attempts to convert a given object property into an OWL transitive object property axiom, provided the property is explicitly defined as transitive. The method first validates the input type and checks for the presence of the TransitiveProperty characteristic; if these conditions are not met, it returns None. Upon successful validation, it retrieves the base object property expression and constructs the transitive property instance, attaching any relevant annotations associated with the transitive characteristic. To optimize performance, the method caches the resulting instances within the class, returning the cached object on subsequent calls for the same property.

      :param property: The transitive property to be converted into an OWL transitive object property representation.
      :type property: ObjectPropertyClass

      :return: An OWLTransitiveObjectProperty instance representing the transitive property characteristic of the input, or None if the input is invalid, not transitive, or conversion fails.

      :rtype: typing.Optional[OWLTransitiveObjectProperty]



   .. py:attribute:: STANDARD_ANNOTATIONS
      :type:  dict[int, owlready2.AnnotationPropertyClass]


   .. py:attribute:: _annotation_assertions
      :type:  dict[tuple[Union[owlready2.NamedIndividual, rdflib.URIRef, str], owlready2.AnnotationPropertyClass, Union[owlready2.NamedIndividual, rdflib.URIRef, rdflib.Literal]], pyowl2.axioms.annotations.OWLAnnotationAssertion]


   .. py:attribute:: _annotation_properties
      :type:  dict[owlready2.AnnotationPropertyClass, pyowl2.base.annotation_property.OWLAnnotationProperty]


   .. py:attribute:: _annotation_property_domains
      :type:  dict[owlready2.AnnotationPropertyClass, pyowl2.axioms.annotations.OWLAnnotationPropertyDomain]


   .. py:attribute:: _annotation_property_ranges
      :type:  dict[owlready2.AnnotationPropertyClass, pyowl2.axioms.annotations.OWLAnnotationPropertyRange]


   .. py:attribute:: _annotations
      :type:  dict[owlready2.EntityClass, tuple[rdflib.URIRef, pyowl2.base.annotation.OWLAnnotation]]


   .. py:attribute:: _asymmetric_object_properties
      :type:  dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.asymmetric_object_property.OWLAsymmetricObjectProperty]


   .. py:attribute:: _class_assertions
      :type:  dict[tuple[owlready2.ThingClass, owlready2.NamedIndividual], pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]


   .. py:attribute:: _class_expressions
      :type:  dict[owlready2.EntityClass, pyowl2.abstracts.class_expression.OWLClassExpression]


   .. py:attribute:: _classes
      :type:  dict[owlready2.ThingClass, pyowl2.base.owl_class.OWLClass]


   .. py:attribute:: _data_all_values_from
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom]


   .. py:attribute:: _data_complements_of
      :type:  dict[tuple[owlready2.Not], pyowl2.data_range.data_complement_of.OWLDataComplementOf]


   .. py:attribute:: _data_exact_cardinality
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality]


   .. py:attribute:: _data_has_value
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.data_has_value.OWLDataHasValue]


   .. py:attribute:: _data_intersections_of
      :type:  dict[tuple[owlready2.And], pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf]


   .. py:attribute:: _data_max_cardinality
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality]


   .. py:attribute:: _data_min_cardinality
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality]


   .. py:attribute:: _data_ones_of
      :type:  dict[tuple[owlready2.OneOf], pyowl2.data_range.data_one_of.OWLDataOneOf]


   .. py:attribute:: _data_properties
      :type:  dict[owlready2.DataPropertyClass, pyowl2.expressions.data_property.OWLDataProperty]


   .. py:attribute:: _data_property_assertions
      :type:  dict[tuple[owlready2.DataPropertyClass, owlready2.NamedIndividual, rdflib.Literal], pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion]


   .. py:attribute:: _data_property_domains
      :type:  dict[owlready2.DataPropertyClass, pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain]


   .. py:attribute:: _data_property_ranges
      :type:  dict[owlready2.DataPropertyClass, pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange]


   .. py:attribute:: _data_some_values_from
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom]


   .. py:attribute:: _data_unions_of
      :type:  dict[tuple[owlready2.Or], pyowl2.data_range.data_union_of.OWLDataUnionOf]


   .. py:attribute:: _datatype_definitions
      :type:  dict[owlready2.DatatypeClass, pyowl2.axioms.datatype_definition.OWLDatatypeDefinition]


   .. py:attribute:: _datatype_restrictions
      :type:  dict[owlready2.ConstrainedDatatype, pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction]


   .. py:attribute:: _datatypes
      :type:  dict[owlready2.DatatypeClass, pyowl2.base.datatype.OWLDatatype]


   .. py:attribute:: _declarations
      :type:  dict[owlready2.EntityClass, owlready2.EntityClass]


   .. py:attribute:: _different_individuals
      :type:  dict[Union[tuple[owlready2.NamedIndividual, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.assertion.OWLDifferentIndividuals]


   .. py:attribute:: _disjoint_classes
      :type:  dict[Union[tuple[owlready2.ThingClass, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses]


   .. py:attribute:: _disjoint_data_properties
      :type:  dict[Union[tuple[owlready2.DataPropertyClass, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties]


   .. py:attribute:: _disjoint_object_properties
      :type:  dict[Union[tuple[owlready2.ObjectPropertyClass, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties]


   .. py:attribute:: _disjoint_unions
      :type:  dict[tuple[owlready2.ThingClass, Ellipsis], pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion]


   .. py:attribute:: _equivalent_classes
      :type:  dict[tuple[owlready2.ThingClass, Ellipsis], pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses]


   .. py:attribute:: _equivalent_data_properties
      :type:  dict[tuple[owlready2.DataPropertyClass, Ellipsis], pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties]


   .. py:attribute:: _equivalent_object_properties
      :type:  dict[tuple[owlready2.ObjectPropertyClass, Ellipsis], pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties]


   .. py:attribute:: _functional_data_properties
      :type:  dict[owlready2.DataPropertyClass, pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty]


   .. py:attribute:: _functional_object_properties
      :type:  dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.functional_object_property.OWLFunctionalObjectProperty]


   .. py:attribute:: _general_axioms
      :type:  dict[owlready2.EntityClass, pyowl2.axioms.annotations.OWLAnnotationAssertion]


   .. py:attribute:: _graph
      :type:  rdflib.Graph


   .. py:attribute:: _has_keys
      :type:  dict[owlready2.ThingClass, pyowl2.axioms.has_key.OWLHasKey]


   .. py:attribute:: _individuals
      :type:  dict[owlready2.NamedIndividual, pyowl2.abstracts.individual.OWLIndividual]


   .. py:attribute:: _inverse_functional_object_properties
      :type:  dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty]


   .. py:attribute:: _inverse_object_properties
      :type:  dict[tuple[owlready2.ObjectPropertyClass, Ellipsis], pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties]


   .. py:attribute:: _irreflexive_object_properties
      :type:  dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty]


   .. py:attribute:: _negative_data_property_assertions
      :type:  dict[tuple[owlready2.DataPropertyClass, owlready2.NamedIndividual, rdflib.Literal], pyowl2.axioms.assertion.OWLNegativeDataPropertyAssertion]


   .. py:attribute:: _negative_object_property_assertions
      :type:  dict[tuple[owlready2.ObjectPropertyClass, owlready2.NamedIndividual, owlready2.NamedIndividual], pyowl2.axioms.assertion.OWLNegativeObjectPropertyAssertion]


   .. py:attribute:: _object_complements_of
      :type:  dict[tuple[owlready2.Not], pyowl2.class_expression.object_complement_of.OWLObjectComplementOf]


   .. py:attribute:: _object_intersections_of
      :type:  dict[tuple[owlready2.And], pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf]


   .. py:attribute:: _object_ones_of
      :type:  dict[tuple[owlready2.OneOf], pyowl2.class_expression.object_one_of.OWLObjectOneOf]


   .. py:attribute:: _object_properties
      :type:  dict[owlready2.ObjectPropertyClass, pyowl2.expressions.object_property.OWLObjectProperty]


   .. py:attribute:: _object_property_assertions
      :type:  dict[tuple[owlready2.ObjectPropertyClass, owlready2.NamedIndividual, owlready2.NamedIndividual], pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion]


   .. py:attribute:: _object_property_domains
      :type:  dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain]


   .. py:attribute:: _object_property_ranges
      :type:  dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange]


   .. py:attribute:: _object_unions_of
      :type:  dict[tuple[owlready2.Or], pyowl2.class_expression.object_union_of.OWLObjectUnionOf]


   .. py:attribute:: _objects_all_values_from
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom]


   .. py:attribute:: _objects_exact_cardinality
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality]


   .. py:attribute:: _objects_has_self
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.object_has_self.OWLObjectHasSelf]


   .. py:attribute:: _objects_has_value
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.object_has_value.OWLObjectHasValue]


   .. py:attribute:: _objects_max_cardinality
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality]


   .. py:attribute:: _objects_min_cardinality
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality]


   .. py:attribute:: _objects_some_values_from
      :type:  dict[owlready2.Restriction, pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom]


   .. py:attribute:: _ontology
      :type:  owlready2.Ontology


   .. py:attribute:: _reflexive_object_properties
      :type:  dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.reflexive_object_property.OWLReflexiveObjectProperty]


   .. py:attribute:: _same_individuals
      :type:  dict[tuple[owlready2.NamedIndividual, Ellipsis], pyowl2.axioms.assertion.OWLSameIndividual]


   .. py:attribute:: _subannotation_properties_of
      :type:  dict[tuple[owlready2.AnnotationPropertyClass, owlready2.AnnotationPropertyClass], pyowl2.axioms.annotations.OWLSubAnnotationPropertyOf]


   .. py:attribute:: _subclasses_of
      :type:  dict[tuple[owlready2.ThingClass, owlready2.ThingClass], pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf]


   .. py:attribute:: _subdata_properties_of
      :type:  dict[tuple[owlready2.DataPropertyClass, owlready2.DataPropertyClass], pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf]


   .. py:attribute:: _subobject_properties_of
      :type:  dict[tuple[owlready2.ObjectPropertyClass, owlready2.ObjectPropertyClass], pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]


   .. py:attribute:: _symmetric_object_properties
      :type:  dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.symmetric_object_property.OWLSymmetricObjectProperty]


   .. py:attribute:: _transitive_object_properties
      :type:  dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty]


   .. py:attribute:: _world
      :type:  owlready2.World


   .. py:property:: annotation_assertions
      :type: dict[tuple[Union[owlready2.NamedIndividual, rdflib.URIRef, str], owlready2.AnnotationPropertyClass, Union[owlready2.NamedIndividual, rdflib.URIRef, rdflib.Literal]], pyowl2.axioms.annotations.OWLAnnotationAssertion]


      Returns a dictionary mapping annotation triples to their corresponding `OWLAnnotationAssertion` objects. The dictionary keys are tuples consisting of the subject (a NamedIndividual, URIRef, or string), the AnnotationPropertyClass, and the annotation value (a NamedIndividual, URIRef, or Literal). This property provides direct access to the internal collection of annotation assertions without performing any computation or causing side effects.

      :return: A dictionary mapping tuples of (subject, annotation property, value) to the corresponding `OWLAnnotationAssertion` objects.

      :rtype: dict[tuple[typing.Union[NamedIndividual, URIRef, str], AnnotationPropertyClass, typing.Union[NamedIndividual, URIRef, Literal]], OWLAnnotationAssertion]


   .. py:property:: annotation_properties
      :type: dict[owlready2.AnnotationPropertyClass, pyowl2.base.annotation_property.OWLAnnotationProperty]


      Returns a dictionary mapping internal annotation property class representations to their corresponding OWL annotation property objects. This property provides read-only access to the collection of annotation properties parsed or managed by the RDF/XML getter. The keys are instances of `AnnotationPropertyClass`, while the values are instances of `OWLAnnotationProperty`.

      :return: A dictionary mapping annotation property classes to their corresponding OWL annotation property objects.

      :rtype: dict[AnnotationPropertyClass, OWLAnnotationProperty]


   .. py:property:: annotation_property_domains
      :type: dict[owlready2.AnnotationPropertyClass, pyowl2.axioms.annotations.OWLAnnotationPropertyDomain]


      Returns a dictionary mapping annotation property classes to their corresponding OWL annotation property domain axioms. This property provides access to the collection of domain restrictions defined for annotation properties within the parsed RDF/XML data. The keys are instances of `AnnotationPropertyClass`, while the values are `OWLAnnotationPropertyDomain` objects representing the specific domain constraints.

      :return: A dictionary mapping annotation property classes to their corresponding OWL annotation property domains.

      :rtype: dict[AnnotationPropertyClass, OWLAnnotationPropertyDomain]


   .. py:property:: annotation_property_ranges
      :type: dict[owlready2.AnnotationPropertyClass, pyowl2.axioms.annotations.OWLAnnotationPropertyRange]


      Provides access to the collection of range constraints defined for annotation properties. This property returns a dictionary mapping AnnotationPropertyClass instances to their respective OWLAnnotationPropertyRange objects. Since it returns the internal dictionary directly, any modifications made to the returned object will be reflected in the underlying data structure.

      :return: A dictionary mapping AnnotationPropertyClass objects to their corresponding OWLAnnotationPropertyRange objects.

      :rtype: dict[AnnotationPropertyClass, OWLAnnotationPropertyRange]


   .. py:property:: annotations
      :type: dict[owlready2.EntityClass, tuple[rdflib.URIRef, pyowl2.base.annotation.OWLAnnotation]]


      Returns the internal dictionary mapping entity classes to their associated annotations. Each entry in the dictionary pairs an `EntityClass` with a tuple containing a `URIRef` and an `OWLAnnotation` object. Note that this property returns a direct reference to the internal storage, so modifying the returned dictionary will affect the state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping entity classes to tuples containing a URI reference and the corresponding OWL annotation.

      :rtype: dict[EntityClass, tuple[URIRef, OWLAnnotation]]


   .. py:property:: asymmetric_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.asymmetric_object_property.OWLAsymmetricObjectProperty]


      Returns a dictionary mapping object property classes to their corresponding OWL asymmetric object property axioms. This property provides read access to the internal collection of asymmetric properties identified during the parsing process. Since it returns a direct reference to the internal dictionary, modifications to the returned object may affect the state of the `RDFXMLGetter` instance, though the method itself performs no computation or state mutation. If the internal collection is empty, an empty dictionary is returned.

      :return: A dictionary mapping object property classes to their corresponding asymmetric object property axioms.

      :rtype: dict[ObjectPropertyClass, OWLAsymmetricObjectProperty]


   .. py:property:: axioms
      :type: list[dict]


      This property aggregates and returns a comprehensive collection of all axioms defined in the ontology, encompassing a wide variety of OWL 2 constructs such as class declarations, property characteristics, individual assertions, and logical restrictions. It consolidates data from numerous specific sub-properties into a single list, grouping the results by axiom type to provide a unified view of the ontology's structure. Accessing this property triggers the materialization of all underlying axiom data, ensuring a complete representation is available, though this may result in a performance impact for large ontologies due to the breadth of data retrieved.

      :return: A list of dictionaries representing all axioms and entities within the ontology, aggregating classes, properties, individuals, and their logical relationships into a single collection.

      :rtype: list[dict]


   .. py:property:: class_assertions
      :type: dict[tuple[owlready2.ThingClass, owlready2.NamedIndividual], pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]


      Retrieves the dictionary of OWL class assertions managed by the instance, mapping a composite key of a class and an individual to the assertion object itself. The keys in the dictionary are tuples consisting of a `ThingClass` and a `NamedIndividual`, while the values are `OWLClassAssertion` instances representing the specific type membership. As this property returns a direct reference to the internal storage, any modifications made to the returned dictionary will directly affect the state of the object.

      :return: A dictionary mapping (ThingClass, NamedIndividual) tuples to their corresponding OWLClassAssertion objects.

      :rtype: dict[tuple[ThingClass, NamedIndividual], OWLClassAssertion]


   .. py:property:: classes
      :type: dict[owlready2.ThingClass, pyowl2.base.owl_class.OWLClass]


      Returns the internal dictionary mapping specific `ThingClass` instances to their corresponding `OWLClass` representations. This property provides read-only access to the collection of class definitions that have been parsed or retrieved by the `RDFXMLGetter`. The dictionary serves as a bridge between the application's internal class model and the standard OWL ontology classes, allowing consumers of this object to inspect the relationships and definitions established during the RDF/XML processing. Since this is a property accessor, it has no side effects and simply exposes the state of the `_classes` attribute.

      :return: A dictionary mapping `ThingClass` objects to their corresponding `OWLClass` objects.

      :rtype: dict[ThingClass, OWLClass]


   .. py:property:: data_all_values_from
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom]


      Returns a dictionary mapping Restriction instances to OWLDataAllValuesFrom axioms. This property provides access to the internal collection of data property restrictions parsed from the RDF/XML source, where each key represents a restriction context and the corresponding value defines the constraint that all values of a specific data property must belong to a particular data range. As a read-only property, it exposes the stored data without causing any side effects or modifications to the object's state.

      :return: A dictionary mapping restrictions to their corresponding OWL data all-values-from expressions.

      :rtype: dict[Restriction, OWLDataAllValuesFrom]


   .. py:property:: data_complements_of
      :type: dict[tuple[owlready2.Not], pyowl2.data_range.data_complement_of.OWLDataComplementOf]


      This property provides access to the internal collection of OWL data complement axioms parsed from the RDF/XML structure. It returns a dictionary where the keys are tuples representing specific negation constraints and the values are the corresponding `OWLDataComplementOf` objects. Since this returns a direct reference to the internal storage, modifying the returned dictionary will affect the state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping tuples of `Not` components to the `OWLDataComplementOf` axioms associated with this entity.

      :rtype: dict[tuple[Not], OWLDataComplementOf]


   .. py:property:: data_exact_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality]


      Provides access to the collection of OWL data exact cardinality restrictions parsed from the RDF/XML source, mapping each restriction node to its corresponding axiom object. This dictionary represents constraints where a data property must have exactly a specific number of values for a given class. Because the property returns a direct reference to the internal storage, any modifications made to the dictionary will directly affect the state of the object.

      :return: A dictionary mapping `Restriction` objects to `OWLDataExactCardinality` instances.

      :rtype: dict[Restriction, OWLDataExactCardinality]


   .. py:property:: data_has_value
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_has_value.OWLDataHasValue]


      Retrieves the mapping of OWL restrictions to specific data value constraints identified during the parsing process. The returned dictionary uses `Restriction` objects as keys and `OWLDataHasValue` objects as values, representing restrictions where a property must have a specific literal value. This property serves as a read-only accessor to the internal storage of these specific OWL constructs without modifying the underlying data.

      :return: A dictionary mapping `Restriction` objects to `OWLDataHasValue` instances representing the data-has-value restrictions.

      :rtype: dict[Restriction, OWLDataHasValue]


   .. py:property:: data_intersections_of
      :type: dict[tuple[owlready2.And], pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf]


      Returns the dictionary mapping tuples of operands to their corresponding `OWLDataIntersectionOf` instances. This property provides direct access to the internal collection of data intersections parsed or retrieved by the object. Because it returns a reference to the mutable internal dictionary, modifications to the returned object will affect the state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping tuples of operands to the corresponding `OWLDataIntersectionOf` instances.

      :rtype: dict[tuple[And], OWLDataIntersectionOf]


   .. py:property:: data_max_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality]


      Retrieves the mapping of restriction definitions to their specific data maximum cardinality constraints. This property returns a dictionary where keys are `Restriction` objects and values are `OWLDataMaxCardinality` instances, representing the parsed ontology's limitations on the number of data property values an entity can possess. As a property getter, accessing this attribute has no side effects and simply exposes the internal state populated during the parsing process.

      :return: A dictionary mapping restrictions to their corresponding OWL data max cardinality restrictions.

      :rtype: dict[Restriction, OWLDataMaxCardinality]


   .. py:property:: data_min_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality]


      Returns the internal dictionary mapping parsed restrictions to their corresponding OWL minimum data cardinality constraints. The keys are instances of `Restriction` and the values are `OWLDataMinCardinality` objects, representing the specific constraints extracted from the RDF/XML source. Because this property returns a direct reference to the underlying mutable dictionary, modifications to the returned object will directly affect the internal state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping restrictions to their corresponding OWL data minimum cardinality restrictions.

      :rtype: dict[Restriction, OWLDataMinCardinality]


   .. py:property:: data_ones_of
      :type: dict[tuple[owlready2.OneOf], pyowl2.data_range.data_one_of.OWLDataOneOf]


      Retrieves the collection of OWL data one-of restrictions identified during the parsing process. The returned dictionary maps tuples of `OneOf` elements to their corresponding `OWLDataOneOf` object representations. This property acts as a direct accessor to the internal state and does not modify the underlying data or trigger any side effects.

      :return: A dictionary mapping tuples of OneOf instances to their corresponding OWLDataOneOf objects.

      :rtype: dict[tuple[OneOf], OWLDataOneOf]


   .. py:property:: data_properties
      :type: dict[owlready2.DataPropertyClass, pyowl2.expressions.data_property.OWLDataProperty]


      Returns a dictionary mapping data property classes to their corresponding OWL data property instances. This property provides direct access to the internal collection of data properties managed by the RDF/XML getter, allowing retrieval of the parsed data structure. Because the underlying attribute is returned directly, modifications to the dictionary will affect the internal state of the object.

      :return: A dictionary mapping data property classes to their corresponding OWL data property instances.

      :rtype: dict[DataPropertyClass, OWLDataProperty]


   .. py:property:: data_property_assertions
      :type: dict[tuple[owlready2.DataPropertyClass, owlready2.NamedIndividual, rdflib.Literal], pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion]


      Retrieves the internal mapping of data property assertions parsed from the RDF/XML source. The dictionary keys are tuples comprising the data property class, the named individual subject, and the literal value, while the values are the corresponding OWLDataPropertyAssertion objects. This property provides direct access to the underlying storage without performing any computation or modification.

      :return: A dictionary mapping tuples of (data property, named individual, literal) to the corresponding `OWLDataPropertyAssertion` objects.

      :rtype: dict[tuple[DataPropertyClass, NamedIndividual, Literal], OWLDataPropertyAssertion]


   .. py:property:: data_property_domains
      :type: dict[owlready2.DataPropertyClass, pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain]


      Retrieves the mapping of data property classes to their respective domain restrictions defined in the ontology. The returned dictionary uses `DataPropertyClass` instances as keys and `OWLDataPropertyDomain` instances as values, representing the specific classes to which each data property applies. This property acts as a direct accessor to the internal collection of domain information parsed by the RDF/XML getter.

      :return: A dictionary mapping data property classes to their corresponding OWL data property domains.

      :rtype: dict[DataPropertyClass, OWLDataPropertyDomain]


   .. py:property:: data_property_ranges
      :type: dict[owlready2.DataPropertyClass, pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange]


      Returns a dictionary mapping data property classes to their defined ranges within the ontology. This property provides direct access to the internal collection of range restrictions, where each key is a `DataPropertyClass` instance and the corresponding value is an `OWLDataPropertyRange` instance. The method performs no computation or side effects, simply returning the pre-populated mapping stored during the parsing process.

      :return: A dictionary mapping data property classes to their corresponding OWL data property ranges.

      :rtype: dict[DataPropertyClass, OWLDataPropertyRange]


   .. py:property:: data_some_values_from
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom]


      Retrieves the dictionary mapping parsed restrictions to their corresponding OWL data some values from representations. This property provides access to the internal collection where keys are Restriction objects and values are OWLDataSomeValuesFrom objects, representing data property restrictions that require at least one value from a specific data range. Since this is a direct getter, it returns the stored mapping without modification or computation, potentially returning an empty dictionary if no such restrictions were identified during parsing.

      :return: A dictionary mapping `Restriction` objects to their corresponding `OWLDataSomeValuesFrom` instances.

      :rtype: dict[Restriction, OWLDataSomeValuesFrom]


   .. py:property:: data_unions_of
      :type: dict[tuple[owlready2.Or], pyowl2.data_range.data_union_of.OWLDataUnionOf]


      Returns a dictionary mapping tuples of `Or` logical operands to their corresponding `OWLDataUnionOf` instances. This property provides direct access to the internal registry of data union expressions, which is typically populated during the parsing of RDF/XML structures to represent data range unions. Because the method returns a reference to the underlying mutable dictionary, any modifications made to the returned object will directly alter the internal state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping tuples of operands to the corresponding `OWLDataUnionOf` instances.

      :rtype: dict[tuple[Or], OWLDataUnionOf]


   .. py:property:: datatype_definitions
      :type: dict[owlready2.DatatypeClass, pyowl2.axioms.datatype_definition.OWLDatatypeDefinition]


      Returns a dictionary mapping specific datatype classes to their corresponding OWL datatype definitions. This property provides direct access to the internal collection of definitions managed by the RDF/XML getter. Because the internal dictionary reference is returned directly, any modifications made to the dictionary by the caller will affect the state of the getter instance.

      :return: A dictionary mapping datatype classes to their corresponding OWL datatype definitions.

      :rtype: dict[DatatypeClass, OWLDatatypeDefinition]


   .. py:property:: datatype_restrictions
      :type: dict[owlready2.ConstrainedDatatype, pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction]


      Returns a dictionary mapping constrained datatypes to their corresponding OWL datatype restrictions. This property provides access to the internal collection of restrictions identified during the parsing process, linking specific data types to the constraints defined upon them. Because the method returns a direct reference to the internal dictionary, any modifications made to the returned object will directly alter the state of the RDFXMLGetter instance.

      :return: A mapping of constrained datatypes to their associated OWL datatype restrictions.

      :rtype: dict[ConstrainedDatatype, OWLDatatypeRestriction]


   .. py:property:: datatypes
      :type: dict[owlready2.DatatypeClass, pyowl2.base.datatype.OWLDatatype]


      Returns the internal dictionary mapping datatype classes to their corresponding OWL datatype representations. This property provides read-only access to the collection of datatypes managed by the RDF/XML getter, where keys are instances of `DatatypeClass` and values are `OWLDatatype` objects.

      :return: A dictionary mapping DatatypeClass objects to OWLDatatype instances.

      :rtype: dict[DatatypeClass, OWLDatatype]


   .. py:property:: declarations
      :type: dict[owlready2.EntityClass, owlready2.EntityClass]


      Retrieves the dictionary mapping entity class declarations encountered during the RDF/XML parsing process. This property provides direct access to the internal mapping between entity classes, which typically represents type definitions or class relationships defined within the RDF source. Because the method returns a reference to the internal dictionary rather than a copy, any modifications made to the returned object will directly alter the state of the `RDFXMLGetter` instance.

      :return: A dictionary of entity class declarations.

      :rtype: dict[EntityClass, EntityClass]


   .. py:property:: different_individuals
      :type: dict[Union[tuple[owlready2.NamedIndividual, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.assertion.OWLDifferentIndividuals]


      Retrieves the internal dictionary mapping groups of individuals to the axioms that declare them distinct. The keys are either tuples of `NamedIndividual` instances or `AllDifferent` objects, and the values are `OWLDifferentIndividuals` axioms. This property provides direct access to the stored data structure without performing any validation or modification.

      :return: A dictionary mapping either tuples of NamedIndividuals or AllDifferent instances to the corresponding OWLDifferentIndividuals axioms.

      :rtype: dict[typing.Union[tuple[NamedIndividual, ...], AllDifferent], OWLDifferentIndividuals]


   .. py:property:: disjoint_classes
      :type: dict[Union[tuple[owlready2.ThingClass, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses]


      Returns a dictionary mapping sets of classes or `AllDifferent` axioms to their corresponding `OWLDisjointClasses` representations. The keys of the dictionary can be either a tuple of `ThingClass` instances or an `AllDifferent` object, while the values are the specific `OWLDisjointClasses` axioms. This property acts as a direct getter for the internal storage of disjointness relationships, returning the stored dictionary without performing any computation or modification.

      :return: A dictionary mapping tuples of ThingClass instances or AllDifferent objects to their corresponding OWLDisjointClasses axioms.

      :rtype: dict[typing.Union[tuple[ThingClass, ...], AllDifferent], OWLDisjointClasses]


   .. py:property:: disjoint_data_properties
      :type: dict[Union[tuple[owlready2.DataPropertyClass, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties]


      Returns a dictionary mapping groups of data properties to their corresponding OWL disjointness axioms. The keys of the dictionary are either tuples of DataPropertyClass instances or AllDifferent objects, representing the properties that are mutually exclusive, while the values are OWLDisjointDataProperties objects encapsulating the axiom details. This property provides direct access to the internal storage of parsed disjoint data properties without performing any computation or validation upon access, though the returned dictionary is mutable and modifications will affect the underlying state.

      :return: A dictionary mapping tuples of data properties or AllDifferent objects to the corresponding OWL disjoint data properties axioms.

      :rtype: dict[typing.Union[tuple[DataPropertyClass, ...], AllDifferent], OWLDisjointDataProperties]


   .. py:property:: disjoint_object_properties
      :type: dict[Union[tuple[owlready2.ObjectPropertyClass, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties]


      Returns a dictionary mapping sets of object properties to their corresponding disjointness axioms. The keys of the dictionary are either tuples of `ObjectPropertyClass` instances, representing a group of mutually disjoint properties, or an `AllDifferent` marker, while the values are `OWLDisjointObjectProperties` objects containing the axiom details. This property provides direct access to the internal storage of these relationships without performing any computation or modification.

      :return: A dictionary mapping tuples of object properties or AllDifferent instances to the corresponding OWL disjoint object properties axioms.

      :rtype: dict[typing.Union[tuple[ObjectPropertyClass, ...], AllDifferent], OWLDisjointObjectProperties]


   .. py:property:: disjoint_unions
      :type: dict[tuple[owlready2.ThingClass, Ellipsis], pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion]


      Returns a dictionary containing the OWL Disjoint Union axioms identified during the parsing process. The dictionary keys are tuples of `ThingClass` objects representing the classes involved in the union, while the values are the corresponding `OWLDisjointUnion` instances. This property provides direct access to the internal storage, meaning modifications to the returned dictionary will affect the state of the `RDFXMLGetter` instance. If no disjoint unions are present, an empty dictionary is returned.

      :return: A dictionary mapping tuples of `ThingClass` instances to their corresponding `OWLDisjointUnion` axioms.

      :rtype: dict[tuple[ThingClass, ...], OWLDisjointUnion]


   .. py:property:: equivalent_classes
      :type: dict[tuple[owlready2.ThingClass, Ellipsis], pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses]


      Returns a dictionary mapping tuples of `ThingClass` instances to their corresponding `OWLEquivalentClasses` axioms. This property provides access to the equivalence relationships discovered during the RDF/XML parsing process, where the keys represent the specific classes involved in the equivalence and the values encapsulate the axiom structure. Since this is a read-only property, accessing it does not modify the underlying state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping tuples of `ThingClass` instances to their corresponding `OWLEquivalentClasses` axioms.

      :rtype: dict[tuple[ThingClass, ...], OWLEquivalentClasses]


   .. py:property:: equivalent_data_properties
      :type: dict[tuple[owlready2.DataPropertyClass, Ellipsis], pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties]


      This property returns a dictionary that maps tuples of `DataPropertyClass` instances to `OWLEquivalentDataProperties` axioms. It serves as a getter for the internal collection of data properties that have been defined as equivalent to one another in the ontology. Since the method returns a direct reference to the internal dictionary, modifying the returned object may alter the state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping tuples of data properties to the axioms declaring them equivalent.

      :rtype: dict[tuple[DataPropertyClass, ...], OWLEquivalentDataProperties]


   .. py:property:: equivalent_object_properties
      :type: dict[tuple[owlready2.ObjectPropertyClass, Ellipsis], pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties]


      Retrieves the collection of equivalent object property axioms managed by this instance. The method returns a dictionary where each key is a tuple of `ObjectPropertyClass` instances representing a set of properties considered equivalent, and the corresponding value is the `OWLEquivalentObjectProperties` axiom object. Note that this property returns a direct reference to the internal storage dictionary; therefore, modifying the returned dictionary in-place will alter the state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping tuples of object properties to the corresponding axioms asserting their equivalence.

      :rtype: dict[tuple[ObjectPropertyClass, ...], OWLEquivalentObjectProperties]


   .. py:property:: functional_data_properties
      :type: dict[owlready2.DataPropertyClass, pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty]


      Returns the dictionary mapping data property classes to their corresponding OWL functional data property representations. This property provides access to the internal collection of functional data properties parsed or managed by the RDF/XML getter. Note that because the method returns a direct reference to the underlying dictionary, modifications to the returned object will affect the internal state of the instance.

      :return: A dictionary mapping data property classes to their corresponding OWL functional data property instances.

      :rtype: dict[DataPropertyClass, OWLFunctionalDataProperty]


   .. py:property:: functional_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.functional_object_property.OWLFunctionalObjectProperty]


      Returns a dictionary mapping object property classes to their corresponding OWL functional object property axioms. This property provides access to the internal collection of functional constraints parsed from the RDF/XML source, where each key represents an object property and the value represents the axiom asserting that the property is functional (i.e., has a unique value for any given subject).

      :return: A dictionary mapping object properties to their corresponding functional object property axioms.

      :rtype: dict[ObjectPropertyClass, OWLFunctionalObjectProperty]


   .. py:property:: general_axioms
      :type: dict[owlready2.EntityClass, pyowl2.axioms.annotations.OWLAnnotationAssertion]


      Provides access to the collection of general axioms parsed from the RDF/XML source. This property returns a dictionary where each key is an `EntityClass` and the corresponding value is an `OWLAnnotationAssertion` associated with that class. Since the method returns a direct reference to the internal storage, modifications to the returned dictionary may affect the internal state of the object.

      :return: A dictionary mapping entity classes to their general OWL annotation assertions.

      :rtype: dict[EntityClass, OWLAnnotationAssertion]


   .. py:property:: graph
      :type: rdflib.Graph


      Returns the RDF graph object associated with the data retrieved by this instance. This property provides direct access to the internal graph representation, meaning that modifications made to the returned object will affect the state of the `RDFXMLGetter` instance. It does not perform any computation or parsing upon access, simply retrieving the stored graph reference.

      :return: The underlying Graph instance associated with this object.

      :rtype: Graph


   .. py:property:: has_keys
      :type: dict[owlready2.ThingClass, pyowl2.axioms.has_key.OWLHasKey]


      Returns a dictionary mapping ontology classes to their corresponding unique key constraints. This property provides access to the internal collection of `HasKey` axioms parsed from the source, where the keys are instances of `ThingClass` and the values are `OWLHasKey` objects defining the properties that uniquely identify individuals of that class.

      :return: A dictionary mapping ThingClass instances to their corresponding OWLHasKey axioms.

      :rtype: dict[ThingClass, OWLHasKey]


   .. py:property:: individuals
      :type: dict[owlready2.NamedIndividual, pyowl2.abstracts.individual.OWLIndividual]


      Returns a dictionary mapping `NamedIndividual` keys to `OWLIndividual` values, representing the entities parsed from the RDF/XML source. This property provides direct access to the internal collection of individuals established during the data retrieval process. If the source data contains no individuals, an empty dictionary is returned. Note that because this returns a reference to the internal dictionary, modifications to the returned object may affect the state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping named individuals to their corresponding OWL individual objects.

      :rtype: dict[NamedIndividual, OWLIndividual]


   .. py:property:: inverse_functional_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty]


      Retrieves the mapping of inverse functional object properties parsed from the RDF/XML source. The return value is a dictionary where keys are instances of `ObjectPropertyClass` and values are `OWLInverseFunctionalObjectProperty` objects representing the specific OWL constraints. As this is a direct property getter, it returns the internal dictionary reference; therefore, modifications to the returned dictionary will directly affect the internal state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping object property classes to their inverse functional object property axioms.

      :rtype: dict[ObjectPropertyClass, OWLInverseFunctionalObjectProperty]


   .. py:property:: inverse_object_properties
      :type: dict[tuple[owlready2.ObjectPropertyClass, Ellipsis], pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties]


      Returns the collection of inverse object properties parsed from the RDF/XML source, structured as a dictionary. The keys are tuples of `ObjectPropertyClass` instances, and the values are `OWLInverseObjectProperties` objects representing the specific inverse relationship axioms. This property exposes the underlying data structure directly, allowing for lookup of inverse definitions based on the involved properties.

      :return: A dictionary mapping tuples of object property classes to their corresponding inverse object properties axioms.

      :rtype: dict[tuple[ObjectPropertyClass, ...], OWLInverseObjectProperties]


   .. py:property:: irreflexive_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty]


      Retrieves the internal mapping of object property classes to their corresponding OWL irreflexive object property axioms. This property provides access to the collection of properties defined as irreflexive within the parsed RDF/XML structure, where the dictionary keys are the property classes and the values are the specific axioms enforcing the irreflexive constraint. As this method returns a direct reference to the underlying dictionary, modifications to the returned object will affect the internal state of the instance.

      :return: A dictionary mapping object property classes to their corresponding OWL irreflexive object property axioms.

      :rtype: dict[ObjectPropertyClass, OWLIrreflexiveObjectProperty]


   .. py:property:: namespace
      :type: rdflib.Namespace


      Retrieves the namespace associated with the ontology by deriving it from the ontology's base IRI. It utilizes the underlying ontology's `get_namespace` method to resolve the namespace and subsequently wraps the resulting base IRI in a `Namespace` object to facilitate convenient access to the ontology's entities. This property performs a read-only operation and assumes that the internal ontology object is properly initialized with a valid base IRI; failure to meet these conditions may result in an AttributeError or an exception from the underlying namespace resolution logic.

      :return: A Namespace object representing the ontology's namespace, derived from its base IRI to facilitate convenient access to its entities.

      :rtype: Namespace


   .. py:property:: negative_data_property_assertions
      :type: dict[tuple[owlready2.DataPropertyClass, owlready2.NamedIndividual, rdflib.Literal], pyowl2.axioms.assertion.OWLNegativeDataPropertyAssertion]


      Retrieves the collection of negative data property assertions parsed from the RDF/XML source. The returned dictionary uses a composite key consisting of a data property class, a named individual, and a literal value to uniquely identify each assertion, mapping these keys to the corresponding `OWLNegativeDataPropertyAssertion` objects. This property provides read-only access to the internal state, representing explicit statements that a specific individual does not possess a particular data property value.

      :return: A dictionary mapping a tuple of a data property, a named individual, and a literal to the corresponding negative data property assertion axiom.

      :rtype: dict[tuple[DataPropertyClass, NamedIndividual, Literal], OWLNegativeDataPropertyAssertion]


   .. py:property:: negative_object_property_assertions
      :type: dict[tuple[owlready2.ObjectPropertyClass, owlready2.NamedIndividual, owlready2.NamedIndividual], pyowl2.axioms.assertion.OWLNegativeObjectPropertyAssertion]


      Retrieves the dictionary mapping negative object property assertions to their defining components. Each key in the dictionary is a tuple containing the object property class, the subject individual, and the object individual involved in the assertion, while the corresponding value is the `OWLNegativeObjectPropertyAssertion` object representing the constraint that the specific relationship does not hold between the two individuals. This property provides direct access to the internal storage of these constraints without performing any computation or modification.

      :return: A dictionary mapping tuples of an object property and two named individuals to their corresponding negative object property assertions.

      :rtype: dict[tuple[ObjectPropertyClass, NamedIndividual, NamedIndividual], OWLNegativeObjectPropertyAssertion]


   .. py:property:: object_complements_of
      :type: dict[tuple[owlready2.Not], pyowl2.class_expression.object_complement_of.OWLObjectComplementOf]


      Provides access to the collection of parsed object complement axioms, mapping specific negation nodes to their OWL representations. The return value is a dictionary where keys are tuples of `Not` instances and values are `OWLObjectComplementOf` objects. Note that this returns a direct reference to the internal storage, so modifying the returned dictionary will alter the state of the instance.

      :return: A dictionary mapping tuples of 'Not' expressions to their corresponding OWLObjectComplementOf objects.

      :rtype: dict[tuple[Not], OWLObjectComplementOf]


   .. py:property:: object_intersections_of
      :type: dict[tuple[owlready2.And], pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf]


      Returns the dictionary mapping tuples of operands to their corresponding OWL object intersection instances. This property provides access to the internal collection of `OWLObjectIntersectionOf` objects, where the keys are tuples of `And` components representing the operands of the intersection. It acts as a read-only accessor to the data structure populated during the retrieval process.

      :return: A dictionary mapping tuples of operands to the corresponding `OWLObjectIntersectionOf` instances.

      :rtype: dict[tuple[And], OWLObjectIntersectionOf]


   .. py:property:: object_ones_of
      :type: dict[tuple[owlready2.OneOf], pyowl2.class_expression.object_one_of.OWLObjectOneOf]


      Returns the dictionary mapping tuples of `OneOf` components to their corresponding `OWLObjectOneOf` representations. This property provides direct access to the internal cache of object one-of constructs parsed from the RDF/XML source. Since the method returns a reference to the internal dictionary rather than a copy, modifying the returned object will directly affect the state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping tuples of `OneOf` components to the corresponding `OWLObjectOneOf` instances.

      :rtype: dict[tuple[OneOf], OWLObjectOneOf]


   .. py:property:: object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.expressions.object_property.OWLObjectProperty]


      Retrieves the mapping of object property classes to their corresponding OWL object properties stored within the instance. This property returns a dictionary where the keys are instances of ObjectPropertyClass and the values are instances of OWLObjectProperty. Because the method returns a direct reference to the internal dictionary, any modifications made to the returned dictionary will directly affect the internal state of the object.

      :return: A dictionary mapping ObjectPropertyClass instances to their corresponding OWLObjectProperty instances.

      :rtype: dict[ObjectPropertyClass, OWLObjectProperty]


   .. py:property:: object_property_assertions
      :type: dict[tuple[owlready2.ObjectPropertyClass, owlready2.NamedIndividual, owlready2.NamedIndividual], pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion]


      Retrieves the dictionary mapping object property assertion components to their corresponding `OWLObjectPropertyAssertion` instances. The keys are tuples consisting of an `ObjectPropertyClass` and two `NamedIndividual` objects, representing the property, subject, and object of the assertion. This property provides direct access to the internal collection of assertions, allowing for lookups or iteration over the parsed object property relationships.

      :return: A dictionary mapping tuples of (ObjectPropertyClass, NamedIndividual, NamedIndividual) to the corresponding OWLObjectPropertyAssertion instances.

      :rtype: dict[tuple[ObjectPropertyClass, NamedIndividual, NamedIndividual], OWLObjectPropertyAssertion]


   .. py:property:: object_property_domains
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain]


      Provides access to the collection of domain restrictions associated with object properties extracted from the RDF/XML data. This property returns a dictionary where each key is an ObjectPropertyClass and the corresponding value is an OWLObjectPropertyDomain instance defining the valid class for the subject of that property. Because the method returns a direct reference to the internal storage, any modifications made to the dictionary will directly alter the state of the RDFXMLGetter instance.

      :return: A dictionary mapping object properties to their corresponding domains.

      :rtype: dict[ObjectPropertyClass, OWLObjectPropertyDomain]


   .. py:property:: object_property_ranges
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange]


      Retrieves the mapping of object property classes to their specific ranges defined in the ontology. This property returns a dictionary where each key is an `ObjectPropertyClass` and the corresponding value is an `OWLObjectPropertyRange`. Since the method returns a direct reference to the internal dictionary, modifying the returned collection will alter the state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping object property classes to their corresponding OWL object property ranges.

      :rtype: dict[ObjectPropertyClass, OWLObjectPropertyRange]


   .. py:property:: object_unions_of
      :type: dict[tuple[owlready2.And], pyowl2.class_expression.object_union_of.OWLObjectUnionOf]


      Returns a dictionary mapping tuples of `And` components to their corresponding `OWLObjectUnionOf` instances. This property provides access to the internal collection of object unions identified during the RDF/XML parsing process, allowing for the retrieval of specific union expressions based on their constituent elements. As a direct getter, it exposes the `_object_unions_of` attribute without performing any computation or modification.

      :return: A dictionary mapping tuples of `And` objects to their corresponding `OWLObjectUnionOf` instances.

      :rtype: dict[tuple[And], OWLObjectUnionOf]


   .. py:property:: objects_all_values_from
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom]


      Returns a dictionary mapping `Restriction` instances to their corresponding `OWLObjectAllValuesFrom` constraints. This property provides access to the internal collection of object property restrictions that define universal quantification (all values from) parsed from the RDF/XML structure. As a read-only getter, it exposes the underlying `_objects_all_values_from` attribute without modifying the object's state.

      :return: A dictionary mapping `Restriction` instances to their corresponding `OWLObjectAllValuesFrom` objects.

      :rtype: dict[Restriction, OWLObjectAllValuesFrom]


   .. py:property:: objects_exact_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality]


      Returns a dictionary mapping parsed ontology restrictions to their corresponding exact cardinality constraints. The keys are instances of `Restriction`, while the values are `OWLObjectExactCardinality` objects that define the precise number of relationships required for object properties. This property provides direct access to the internal collection populated during the RDF/XML parsing process, allowing consumers to inspect specific cardinality restrictions defined in the ontology.

      :return: A dictionary mapping `Restriction` objects to their corresponding `OWLObjectExactCardinality` instances.

      :rtype: dict[Restriction, OWLObjectExactCardinality]


   .. py:property:: objects_has_self
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_has_self.OWLObjectHasSelf]


      Returns a dictionary mapping parsed `Restriction` instances to their corresponding `OWLObjectHasSelf` objects, representing OWL restrictions where a property must have the individual itself as a value. This property provides direct access to the internal collection of object-has-self restrictions identified during the RDF/XML parsing process. Because it returns a reference to the underlying dictionary, modifying the returned object will alter the internal state of the getter.

      :return: A dictionary mapping `Restriction` objects to `OWLObjectHasSelf` instances.

      :rtype: dict[Restriction, OWLObjectHasSelf]


   .. py:property:: objects_has_value
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_has_value.OWLObjectHasValue]


      Returns a dictionary mapping parsed OWL restrictions to their corresponding object-has-value constraints. This property provides access to the internal collection of `Restriction` objects associated with `OWLObjectHasValue` instances, which are typically extracted during the parsing of RDF/XML data. The operation is a direct pass-through to the underlying private attribute, implying no side effects or data transformation occurs upon access.

      :return: A dictionary mapping `Restriction` objects to their corresponding `OWLObjectHasValue` objects.

      :rtype: dict[Restriction, OWLObjectHasValue]


   .. py:property:: objects_max_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality]


      Returns a dictionary mapping parsed OWL restrictions to their corresponding object max cardinality constraints. This property provides direct access to the internal collection of `Restriction` keys and `OWLObjectMaxCardinality` values that were extracted from the RDF/XML source. As a simple getter, it does not modify the underlying data or perform additional calculations during access.

      :return: A dictionary mapping `Restriction` objects to their corresponding `OWLObjectMaxCardinality` objects.

      :rtype: dict[Restriction, OWLObjectMaxCardinality]


   .. py:property:: objects_min_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality]


      Returns a dictionary mapping `Restriction` instances to their corresponding `OWLObjectMinCardinality` constraints. This property provides access to the internal collection of minimum cardinality restrictions that have been parsed or retrieved. Note that because the internal dictionary is returned directly, modifying the returned object will alter the state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping restrictions to their corresponding object minimum cardinality constraints.

      :rtype: dict[Restriction, OWLObjectMinCardinality]


   .. py:property:: objects_some_values_from
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom]


      Returns a dictionary mapping parsed restriction nodes to their corresponding OWL object some values from representations. This property provides direct access to the internal collection where keys are `Restriction` objects and values are `OWLObjectSomeValuesFrom` objects, typically populated during the RDF/XML parsing process. Because the reference to the internal dictionary is returned directly, modifications to the returned dictionary will affect the state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping Restriction objects to their corresponding OWLObjectSomeValuesFrom objects.

      :rtype: dict[Restriction, OWLObjectSomeValuesFrom]


   .. py:property:: ontology
      :type: owlready2.Ontology


      Returns the `Ontology` instance currently held by the `RDFXMLGetter`. This property provides read access to the internal `_ontology` attribute, which represents the structured data parsed from the RDF/XML source. It exposes the object directly, meaning changes to the returned instance may affect the internal state of the getter.

      :return: The Ontology instance associated with the current object.

      :rtype: Ontology


   .. py:property:: reflexive_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.reflexive_object_property.OWLReflexiveObjectProperty]


      Returns a dictionary mapping object property classes to their corresponding OWL reflexive object property instances. This property provides access to the internal collection of reflexive properties identified during the RDF/XML parsing process, where the keys represent the property definitions and the values represent the specific reflexive characteristics applied to them.

      :return: A dictionary mapping object property classes to their corresponding reflexive object property instances.

      :rtype: dict[ObjectPropertyClass, OWLReflexiveObjectProperty]


   .. py:property:: same_individuals
      :type: dict[tuple[owlready2.NamedIndividual, Ellipsis], pyowl2.axioms.assertion.OWLSameIndividual]


      Retrieves the collection of `SameIndividual` axioms parsed from the RDF/XML source. The returned dictionary maps tuples of `NamedIndividual` objects to their corresponding `OWLSameIndividual` axiom representations, effectively grouping individuals that are declared to be identical. Since this property returns a reference to the internal storage, modifications to the dictionary will affect the state of the `RDFXMLGetter` instance. If no same-individual axioms are present, an empty dictionary is returned.

      :return: A dictionary mapping tuples of named individuals to the corresponding OWLSameIndividual axioms.

      :rtype: dict[tuple[NamedIndividual, ...], OWLSameIndividual]


   .. py:property:: subannotation_properties_of
      :type: dict[tuple[owlready2.AnnotationPropertyClass, owlready2.AnnotationPropertyClass], pyowl2.axioms.annotations.OWLSubAnnotationPropertyOf]


      Retrieves the dictionary mapping sub-annotation property relationships to their corresponding axioms. The keys of the dictionary are tuples containing the sub-property and super-property `AnnotationPropertyClass` instances, and the values are `OWLSubAnnotationPropertyOf` objects representing the specific axioms. This property returns a direct reference to the internal storage, so modifications to the returned dictionary will affect the state of the object.

      :return: A dictionary mapping pairs of annotation properties to the corresponding `OWLSubAnnotationPropertyOf` axioms.

      :rtype: dict[tuple[AnnotationPropertyClass, AnnotationPropertyClass], OWLSubAnnotationPropertyOf]


   .. py:property:: subclasses_of
      :type: dict[tuple[owlready2.ThingClass, owlready2.ThingClass], pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf]


      This property provides access to the collection of subclass relationships identified during the RDF/XML parsing process. It returns a dictionary where each key is a tuple of two `ThingClass` objects representing the subclass and superclass pair, and the corresponding value is the `OWLSubClassOf` axiom object that defines this relationship. Because the property returns a direct reference to the internal dictionary, modifying the returned object will alter the state of the `RDFXMLGetter` instance.

      :return: A dictionary mapping pairs of classes to the corresponding OWL subclass axioms.

      :rtype: dict[tuple[ThingClass, ThingClass], OWLSubClassOf]


   .. py:property:: subdata_properties_of
      :type: dict[tuple[owlready2.DataPropertyClass, owlready2.DataPropertyClass], pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf]


      Returns a dictionary mapping pairs of data properties to the corresponding sub-data-property axioms defined in the ontology. The keys are tuples where the first element is the sub-property and the second is the super-property, while the values are instances of `OWLSubDataPropertyOf` representing the specific relationship. This property provides read-only access to the internal collection of these axioms, which is typically populated during the parsing of the RDF/XML structure.

      :return: A dictionary mapping pairs of data properties to the corresponding OWLSubDataPropertyOf axioms.

      :rtype: dict[tuple[DataPropertyClass, DataPropertyClass], OWLSubDataPropertyOf]


   .. py:property:: subobject_properties_of
      :type: dict[tuple[owlready2.ObjectPropertyClass, owlready2.ObjectPropertyClass], pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]


      Provides access to the internal collection of axioms defining sub-object property relationships within the parsed ontology. The returned dictionary maps tuples of `ObjectPropertyClass` instances—representing the sub-property and super-property pair—to their corresponding `OWLSubObjectPropertyOf` axiom objects. This property serves as a direct accessor to the underlying data structure populated during the RDF/XML parsing process, offering a view of the hierarchy between object properties without performing any computation or state modification.

      :return: A dictionary mapping pairs of object properties to the corresponding sub-object property axioms.

      :rtype: dict[tuple[ObjectPropertyClass, ObjectPropertyClass], OWLSubObjectPropertyOf]


   .. py:property:: symmetric_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.symmetric_object_property.OWLSymmetricObjectProperty]


      Returns a dictionary mapping object property classes to their corresponding OWL symmetric object property instances. The keys are `ObjectPropertyClass` objects, while the values are `OWLSymmetricObjectProperty` objects, representing the symmetric relationships identified within the RDF/XML data. This property provides read-only access to the internal collection of symmetric properties without modifying the underlying state.

      :return: A dictionary mapping object property classes to their corresponding symmetric object property definitions.

      :rtype: dict[ObjectPropertyClass, OWLSymmetricObjectProperty]


   .. py:property:: transitive_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty]


      Retrieves the mapping of object properties identified as transitive within the parsed ontology. The returned dictionary uses `ObjectPropertyClass` instances as keys and their corresponding `OWLTransitiveObjectProperty` representations as values. This property provides direct access to the internal collection of transitive properties without performing any computation or causing side effects.

      :return: A dictionary mapping object property classes to their corresponding transitive object property axioms.

      :rtype: dict[ObjectPropertyClass, OWLTransitiveObjectProperty]


   .. py:property:: world
      :type: owlready2.World


      This property retrieves the `World` object associated with the current `RDFXMLGetter` instance. It acts as a read-only accessor for the internal `_world` attribute, which typically holds the context or graph environment for RDF/XML data retrieval. The method has no side effects on the instance itself, but note that it returns a direct reference to the internal object, meaning modifications to the returned `World` instance may affect the state of the getter.

      :return: The World instance associated with this object.

      :rtype: World


.. py:function:: get_abbreviation(iri: rdflib.URIRef) -> int

   Retrieves the internal integer abbreviation for a specified IRI by first checking a global mapping of known IRIs. If the IRI exists in the mapping, the corresponding integer is returned directly; otherwise, the function computes the abbreviation by applying a universal abbreviation function to the string representation of the IRI. This function relies on module-level state for lookups and computation but does not modify the input IRI.

   :param iri: The IRI to look up in the universal mapping or generate an abbreviation for.
   :type iri: URIRef

   :return: The internal integer abbreviation for the IRI, retrieved from the universal mapping or generated if not present.

   :rtype: int


.. py:function:: is_named_individual(obj: object) -> bool

   Determines whether the provided object represents a named individual within the OWL ontology, distinguishing specific instances from class definitions. The function returns True only if the object is an instance of the base `Thing` class while explicitly excluding instances of `ThingClass`, which represent the classes themselves. This logic ensures that abstract types are filtered out, leaving only concrete entities. The operation is a read-only type check that produces no side effects on the object or the ontology.

   :param obj: The object to check for named individual status.
   :type obj: object

   :return: True if the object is a named individual (a concrete instance) in the OWL ontology, and False if it is a class definition or other type.

   :rtype: bool


.. py:data:: BASE_DATATYPES
