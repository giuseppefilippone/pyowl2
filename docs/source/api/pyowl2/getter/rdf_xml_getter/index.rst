pyowl2.getter.rdf_xml_getter
============================

.. py:module:: pyowl2.getter.rdf_xml_getter


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

.. py:class:: AxiomsType

   Bases: :py:obj:`enum.StrEnum`


   Enum where members are also (and must be) strings


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


.. py:class:: RDFXMLGetter(ontology: owlready2.Ontology)

   A utility class providing static methods to retrieve OWL concepts from RDF/XML
   using SPARQL queries or direct graph operations with rdflib and owlready2.

   This class implements the OWL 2 mapping to RDF as described in W3C specification:
   https://www.w3.org/TR/owl2-mapping-to-rdf/


   .. py:method:: exists_annotation_property(property: rdflib.URIRef) -> bool


   .. py:method:: exists_class(class_: rdflib.URIRef) -> bool


   .. py:method:: exists_data_property(data: rdflib.URIRef) -> bool


   .. py:method:: exists_data_range(data_range: rdflib.URIRef) -> bool


   .. py:method:: exists_datatype(datatype: rdflib.URIRef) -> bool


   .. py:method:: exists_element_by_iri_type(iri: rdflib.URIRef, type=URIRef) -> bool


   .. py:method:: exists_object_property(object: rdflib.URIRef) -> bool


   .. py:method:: get(element: AxiomsType) -> list[owlready2.EntityClass]


   .. py:method:: get_owl_annotation_axiom(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom


   .. py:method:: get_owl_annotation_properties() -> list[pyowl2.base.annotation_property.OWLAnnotationProperty]

      Get all annotation properties using SPARQL.

      :returns: List of annotation property URIs



   .. py:method:: get_owl_annotation_property_domains() -> list[pyowl2.axioms.annotations.OWLAnnotationPropertyDomain]

      Get all annotation properties using SPARQL.

      :returns: List of annotation property URIs



   .. py:method:: get_owl_annotation_property_ranges() -> list[pyowl2.axioms.annotations.OWLAnnotationPropertyRange]

      Get all annotation properties using SPARQL.

      :returns: List of annotation property URIs



   .. py:method:: get_owl_annotations() -> list[pyowl2.base.annotation.OWLAnnotation]

      Get all annotations for resources.

      :returns: Dictionary mapping resource URIs to lists of (property, value) tuples



   .. py:method:: get_owl_assertion(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.assertion.OWLAssertion


   .. py:method:: get_owl_asymmetric_object_properties() -> list[pyowl2.expressions.object_property.OWLObjectProperty]

      Get all asymmetric object properties.

      :returns: List of asymmetric object properties



   .. py:method:: get_owl_axiom(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.axiom.OWLAxiom


   .. py:method:: get_owl_axiom_annotations_for(source: owlready2.EntityClass, property: Optional[owlready2.EntityClass] = None, target: Optional[owlready2.EntityClass] = None) -> Optional[list[pyowl2.base.annotation.OWLAnnotation]]


   .. py:method:: get_owl_class_assertions() -> list[pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]

      Get all class assertions (individual type declarations).

      :returns: List of (individual, class) tuples



   .. py:method:: get_owl_class_axiom(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.class_axiom.OWLClassAxiom


   .. py:method:: get_owl_class_expression(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:method:: get_owl_classes() -> list[pyowl2.base.owl_class.OWLClass]

      Get all OWL classes using SPARQL.

      :returns: List of class URIs



   .. py:method:: get_owl_data_all_values_from() -> list[pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_data_complement_of() -> list[pyowl2.data_range.data_complement_of.OWLDataComplementOf]

      Get all datatype complements (owl:datatypeComplementOf).

      :returns: List of (complement_class, complemented_class) tuples



   .. py:method:: get_owl_data_exact_cardinality() -> list[pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_data_has_value() -> list[pyowl2.class_expression.data_has_value.OWLDataHasValue]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_data_intersection_of() -> list[pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf]

      Get all class intersections (owl:intersectionOf).

      :returns: List of (intersection_class, [component_classes]) tuples



   .. py:method:: get_owl_data_max_cardinality() -> list[pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_data_min_cardinality() -> list[pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_data_one_of() -> list[pyowl2.data_range.data_one_of.OWLDataOneOf]

      Get all enumerated classes (owl:oneOf).

      :returns: List of (enum_class, [individuals]) tuples



   .. py:method:: get_owl_data_property_assertions() -> list[pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion]

      Get all property assertions.

      :returns: List of property assertions.



   .. py:method:: get_owl_data_property_axiom(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom


   .. py:method:: get_owl_data_property_domains() -> list[pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain]

      Get all data property domains.

      :returns: List of data property domains



   .. py:method:: get_owl_data_property_ranges() -> list[pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange]

      Get all data property ranges.

      :returns: List of data property ranges



   .. py:method:: get_owl_data_range(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.data_range.OWLDataRange


   .. py:method:: get_owl_data_some_values_from() -> list[pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_data_union_of() -> list[pyowl2.data_range.data_union_of.OWLDataUnionOf]

      Get all class unions (owl:unionOf).

      :returns: List of (union_class, [component_classes]) tuples



   .. py:method:: get_owl_datatype_definition(datatype: Union[owlready2.DatatypeClass, owlready2.ConstrainedDatatype], data_range: Union[owlready2.DatatypeClass, owlready2.ConstrainedDatatype, owlready2.And]) -> Optional[pyowl2.axioms.datatype_definition.OWLDatatypeDefinition]


   .. py:method:: get_owl_datatype_definitions() -> list[pyowl2.axioms.datatype_definition.OWLDatatypeDefinition]

      Get all datatype definitions.

      :returns: List of datatype definitions



   .. py:method:: get_owl_datatype_properties() -> list[pyowl2.expressions.data_property.OWLDataProperty]

      Get all datatype properties using SPARQL.

      :returns: List of datatype property URIs



   .. py:method:: get_owl_datatype_restrictions() -> list[pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction]

      Get all datatype restrictions (owl:withRestrictions).

      :returns: List of OWLDatatypeRestriction



   .. py:method:: get_owl_datatypes() -> list[pyowl2.base.datatype.OWLDatatype]

      Get all defined datatypes.

      :returns: List of datatype URIs



   .. py:method:: get_owl_declaration(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.axioms.declaration.OWLDeclaration


   .. py:method:: get_owl_declaration_annotations_for(source: owlready2.EntityClass, target: owlready2.EntityClass = None) -> Optional[list[pyowl2.base.annotation.OWLAnnotation]]


   .. py:method:: get_owl_different_individuals() -> list[pyowl2.axioms.assertion.OWLDifferentIndividuals]

      Get all differentFrom assertions between individuals.

      :returns: List of (individual1, individual2) tuples



   .. py:method:: get_owl_disjoint_classes() -> list[pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses]

      Get all disjoint class relationships.

      :returns: List of (class1, class2) tuples



   .. py:method:: get_owl_disjoint_data_properties() -> list[pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties]

      Get all disjoint data property pairs.

      :returns: List of disjoint data properties



   .. py:method:: get_owl_disjoint_object_properties() -> list[pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties]

      Get all disjoint property pairs.

      :returns: List of (property1, property2) tuples



   .. py:method:: get_owl_disjoint_unions() -> list[pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion]

      Get all disjoint unions (owl:disjointUnionOf).

      :returns: List of (union_class, [component_classes]) tuples



   .. py:method:: get_owl_equivalent_classes() -> list[pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses]

      Get all equivalent class relationships.

      :returns: List of (class1, class2) tuples



   .. py:method:: get_owl_equivalent_data_properties() -> list[pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties]

      Get all equivalent data property relationships.

      :returns: List of (property1, property2) tuples



   .. py:method:: get_owl_equivalent_object_properties() -> list[pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties]

      Get all equivalent property relationships.

      :returns: List of (property1, property2) tuples



   .. py:method:: get_owl_functional_data_properties() -> list[pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty]

      Get all functional data properties.

      :returns: List of functional data properties



   .. py:method:: get_owl_functional_object_properties() -> list[pyowl2.axioms.object_property_axiom.functional_object_property.OWLFunctionalObjectProperty]

      Get all functional object properties.

      :returns: List of functional object properties



   .. py:method:: get_owl_general_axiom() -> list[owlready2.EntityClass]

      Get all OWL general axioms using SPARQL.

      :returns: List of class URIs



   .. py:method:: get_owl_has_key(entity: owlready2.EntityClass, objects: tuple[owlready2.ObjectPropertyClass, Ellipsis], data: tuple[owlready2.DataPropertyClass, Ellipsis]) -> Optional[pyowl2.axioms.has_key.OWLHasKey]


   .. py:method:: get_owl_has_keys() -> list[pyowl2.axioms.has_key.OWLHasKey]

      Get all key property sets (owl:hasKey).

      :returns: List of (class, [key_properties]) tuples



   .. py:method:: get_owl_individuals() -> list[pyowl2.abstracts.individual.OWLIndividual]

      Get all individuals using SPARQL.

      :returns: List of individual URIs



   .. py:method:: get_owl_inverse_functional_object_properties() -> list[pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty]

      Get all inverse functional object properties.

      :returns: List of inverse functional object properties



   .. py:method:: get_owl_inverse_object_properties() -> list[pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties]

      Get all inverse property pairs.

      :returns: List of (property1, property2) tuples



   .. py:method:: get_owl_irreflexive_object_properties() -> list[pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty]

      Get all irreflexive object properties.

      :returns: List of irreflexive object properties



   .. py:method:: get_owl_negative_data_property_assertions() -> list[pyowl2.axioms.assertion.OWLNegativeDataPropertyAssertion]

      Get all negative property assertions.

      :returns: List of dictionaries with assertion details



   .. py:method:: get_owl_negative_object_property_assertions() -> list[pyowl2.axioms.assertion.OWLNegativeObjectPropertyAssertion]

      Get all negative property assertions.

      :returns: List of dictionaries with assertion details



   .. py:method:: get_owl_object_all_values_from() -> list[pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_object_complement_of() -> list[pyowl2.class_expression.object_complement_of.OWLObjectComplementOf]

      Get all class complements (owl:complementOf).

      :returns: List of (complement_class, complemented_class) tuples



   .. py:method:: get_owl_object_exact_cardinality() -> list[pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_object_has_self() -> list[pyowl2.class_expression.object_has_self.OWLObjectHasSelf]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_object_has_value() -> list[pyowl2.class_expression.object_has_value.OWLObjectHasValue]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_object_intersection_of() -> list[pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf]

      Get all class intersections (owl:intersectionOf).

      :returns: List of (intersection_class, [component_classes]) tuples



   .. py:method:: get_owl_object_max_cardinality() -> list[pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_object_min_cardinality() -> list[pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_object_one_of() -> list[pyowl2.class_expression.object_one_of.OWLObjectOneOf]

      Get all enumerated classes (owl:oneOf).

      :returns: List of (enum_class, [individuals]) tuples



   .. py:method:: get_owl_object_properties() -> list[pyowl2.expressions.object_property.OWLObjectProperty]

      Get all object properties using SPARQL.

      :returns: List of object property URIs



   .. py:method:: get_owl_object_property_assertions() -> list[pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion]

      Get all property assertions.

      :returns: List of property assertions.



   .. py:method:: get_owl_object_property_axiom(*params: tuple[pyowl2.abstracts.object.OWLObject, Ellipsis]) -> pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom


   .. py:method:: get_owl_object_property_domains() -> list[pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain]

      Get all object property domains.

      :returns: List of object property domains



   .. py:method:: get_owl_object_property_ranges() -> list[pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange]

      Get all object property ranges.

      :returns: List of object property ranges



   .. py:method:: get_owl_object_some_values_from() -> list[pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom]

      Get all property restrictions.

      :returns: List of restriction dictionaries with details



   .. py:method:: get_owl_object_union_of() -> list[pyowl2.class_expression.object_union_of.OWLObjectUnionOf]

      Get all object unions of (owl:unionOf).

      :returns: List of (union_class, [component_classes]) tuples



   .. py:method:: get_owl_ontology_annotations() -> Optional[list[pyowl2.base.annotation.OWLAnnotation]]


   .. py:method:: get_owl_reflexive_object_properties() -> list[pyowl2.axioms.object_property_axiom.reflexive_object_property.OWLReflexiveObjectProperty]

      Get all reflexive object properties.

      :returns: List of reflexive object properties



   .. py:method:: get_owl_same_individuals() -> list[pyowl2.axioms.assertion.OWLSameIndividual]

      Get all sameAs assertions between individuals.

      :returns: List of (individual1, individual2) tuples



   .. py:method:: get_owl_sub_annotation_property_of() -> list[pyowl2.axioms.annotations.OWLSubAnnotationPropertyOf]

      Get all sub data property.

      :returns: List of OWLSubAnnotationPropertyOf



   .. py:method:: get_owl_sub_data_property_of() -> list[pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf]

      Get all sub data property.

      :returns: List of OWLSubDataPropertyOf



   .. py:method:: get_owl_sub_object_property_chain() -> list[pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]

      Get all subproperty relationships.

      :returns: List of (subproperty, superproperty) tuples



   .. py:method:: get_owl_sub_object_property_of() -> list[pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]

      Get all sub object property.

      :returns: List of OWLSubObjectPropertyOf



   .. py:method:: get_owl_subclass_relationships() -> list[pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf]

      Get all subclass relationships.

      :returns: List of (subclass, superclass) tuples



   .. py:method:: get_owl_symmetric_object_properties() -> list[pyowl2.axioms.object_property_axiom.symmetric_object_property.OWLSymmetricObjectProperty]

      Get all symmetric object properties.

      :returns: List of symmetric object properties



   .. py:method:: get_owl_transitive_object_properties() -> list[pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty]

      Get all transitive object properties.

      :returns: List of transitive object properties



   .. py:method:: nothing_to_owl_class() -> pyowl2.base.owl_class.OWLClass


   .. py:method:: nothing_to_owl_class_declaration(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]


   .. py:method:: thing_to_owl_class() -> pyowl2.base.owl_class.OWLClass


   .. py:method:: thing_to_owl_class_declaration(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]


   .. py:method:: to_owl_annotation_assertion(subject: Union[owlready2.NamedIndividual, rdflib.URIRef, str], property: owlready2.AnnotationPropertyClass, value: Union[owlready2.NamedIndividual, rdflib.URIRef, rdflib.Literal], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.annotations.OWLAnnotationAssertion]


   .. py:method:: to_owl_annotation_property(property: owlready2.AnnotationPropertyClass) -> Optional[pyowl2.base.annotation_property.OWLAnnotationProperty]


   .. py:method:: to_owl_annotation_property_declaration(property: owlready2.AnnotationPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]


   .. py:method:: to_owl_annotation_property_domain(property: owlready2.AnnotationPropertyClass, domain: rdflib.URIRef, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.annotations.OWLAnnotationPropertyDomain]


   .. py:method:: to_owl_annotation_property_range(property: owlready2.AnnotationPropertyClass, range: rdflib.URIRef, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.annotations.OWLAnnotationPropertyRange]


   .. py:method:: to_owl_asymmetric_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.asymmetric_object_property.OWLAsymmetricObjectProperty]


   .. py:method:: to_owl_class(entity: owlready2.ThingClass) -> Optional[pyowl2.base.owl_class.OWLClass]


   .. py:method:: to_owl_class_assertion(individual: owlready2.NamedIndividual, individual_class: owlready2.ThingClass) -> Optional[pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]


   .. py:method:: to_owl_class_declaration(entity: owlready2.EntityClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]


   .. py:method:: to_owl_data_all_values_from(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom]


   .. py:method:: to_owl_data_complement_of(entity: owlready2.Not, data_range: owlready2.EntityClass) -> Optional[pyowl2.data_range.data_complement_of.OWLDataComplementOf]


   .. py:method:: to_owl_data_exact_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality]


   .. py:method:: to_owl_data_has_value(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_has_value.OWLDataHasValue]


   .. py:method:: to_owl_data_intersection_of(entity: owlready2.And) -> Optional[pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf]


   .. py:method:: to_owl_data_max_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality]


   .. py:method:: to_owl_data_min_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality]


   .. py:method:: to_owl_data_one_of(entity: owlready2.OneOf) -> Optional[pyowl2.data_range.data_one_of.OWLDataOneOf]


   .. py:method:: to_owl_data_property(property: owlready2.DataPropertyClass) -> Optional[pyowl2.expressions.data_property.OWLDataProperty]


   .. py:method:: to_owl_data_property_assertion(individual_source: owlready2.NamedIndividual, property: owlready2.DataPropertyClass, target: rdflib.Literal, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion]


   .. py:method:: to_owl_data_property_declaration(property: owlready2.DataPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]


   .. py:method:: to_owl_data_property_domain(property: owlready2.DataPropertyClass, domain: owlready2.ThingClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain]


   .. py:method:: to_owl_data_property_range(property: owlready2.DataPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange]


   .. py:method:: to_owl_data_some_values_from(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom]


   .. py:method:: to_owl_data_union_of(entity: owlready2.Or) -> Optional[pyowl2.class_expression.object_union_of.OWLObjectUnionOf]


   .. py:method:: to_owl_datatype(entity: Union[owlready2.DatatypeClass, type]) -> Optional[Union[pyowl2.base.datatype.OWLDatatype, set[pyowl2.base.datatype.OWLDatatype]]]


   .. py:method:: to_owl_datatype_declaration(entity: owlready2.DatatypeClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]


   .. py:method:: to_owl_datatype_restriction(entity: owlready2.ConstrainedDatatype) -> Optional[pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction]


   .. py:method:: to_owl_different_individuals(individuals: Union[tuple[owlready2.NamedIndividual, Ellipsis], owlready2.AllDifferent]) -> Optional[pyowl2.axioms.assertion.OWLDifferentIndividuals]


   .. py:method:: to_owl_disjoint_classes(classes: Union[tuple[owlready2.ThingClass], owlready2.AllDifferent]) -> Optional[pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses]


   .. py:method:: to_owl_disjoint_data_properties(classes: Union[tuple[owlready2.DataPropertyClass, Ellipsis], owlready2.AllDifferent]) -> Optional[pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties]


   .. py:method:: to_owl_disjoint_object_properties(properties: Union[tuple[owlready2.ObjectPropertyClass], owlready2.AllDifferent]) -> Optional[pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties]


   .. py:method:: to_owl_disjoint_union(main_class: owlready2.EntityClass, classes: tuple[owlready2.EntityClass]) -> Optional[pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion]


   .. py:method:: to_owl_equivalent_classes(classes: tuple[owlready2.EntityClass], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses]


   .. py:method:: to_owl_equivalent_data_properties(classes: tuple[owlready2.DataPropertyClass, Ellipsis], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties]


   .. py:method:: to_owl_equivalent_object_properties(properties: tuple[owlready2.ObjectPropertyClass], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties]


   .. py:method:: to_owl_functional_data_property(property: owlready2.DataPropertyClass) -> Optional[pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty]


   .. py:method:: to_owl_functional_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.functional_object_property.OWLFunctionalObjectProperty]


   .. py:method:: to_owl_general_class_axiom(left: Union[owlready2.And, owlready2.Or, owlready2.Not, owlready2.Restriction], property: rdflib.URIRef, right: owlready2.EntityClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.general.OWLGeneralClassAxiom]


   .. py:method:: to_owl_individual(individual: owlready2.NamedIndividual) -> Optional[pyowl2.abstracts.individual.OWLIndividual]


   .. py:method:: to_owl_individual_declaration(individual: owlready2.NamedIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]


   .. py:method:: to_owl_inverse_functional_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty]


   .. py:method:: to_owl_inverse_object_properties(property: Union[owlready2.Inverse, owlready2.ObjectPropertyClass, int], inv_property: Union[owlready2.Inverse, owlready2.ObjectPropertyClass]) -> Optional[Union[pyowl2.expressions.inverse_object_property.OWLInverseObjectProperty, pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties]]


   .. py:method:: to_owl_irreflexive_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty]


   .. py:method:: to_owl_negative_data_property_assertion(individual_source: owlready2.NamedIndividual, property: owlready2.DataPropertyClass, target: rdflib.Literal) -> Optional[pyowl2.axioms.assertion.OWLNegativeDataPropertyAssertion]


   .. py:method:: to_owl_negative_object_property_assertion(individual_source: owlready2.NamedIndividual, property: owlready2.ObjectPropertyClass, individual_target: owlready2.NamedIndividual) -> Optional[pyowl2.axioms.assertion.OWLNegativeObjectPropertyAssertion]


   .. py:method:: to_owl_object_all_values_from(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom]


   .. py:method:: to_owl_object_complement_of(entity: owlready2.Not, expression: owlready2.ThingClass) -> Optional[pyowl2.class_expression.object_complement_of.OWLObjectComplementOf]


   .. py:method:: to_owl_object_exact_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality]


   .. py:method:: to_owl_object_has_self(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_has_self.OWLObjectHasSelf]


   .. py:method:: to_owl_object_has_value(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_has_value.OWLObjectHasValue]


   .. py:method:: to_owl_object_intersection_of(entity: owlready2.And) -> Optional[pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf]


   .. py:method:: to_owl_object_max_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality]


   .. py:method:: to_owl_object_min_cardinality(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality]


   .. py:method:: to_owl_object_one_of(entity: owlready2.OneOf) -> Optional[pyowl2.class_expression.object_one_of.OWLObjectOneOf]


   .. py:method:: to_owl_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.expressions.object_property.OWLObjectProperty]


   .. py:method:: to_owl_object_property_assertion(individual_source: owlready2.NamedIndividual, property: owlready2.ObjectPropertyClass, individual_target: owlready2.NamedIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion]


   .. py:method:: to_owl_object_property_declaration(property: owlready2.ObjectPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.declaration.OWLDeclaration]


   .. py:method:: to_owl_object_property_domain(property: owlready2.ObjectPropertyClass, cls: owlready2.ThingClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain]


   .. py:method:: to_owl_object_property_range(property: owlready2.ObjectPropertyClass, cls: owlready2.ThingClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange]


   .. py:method:: to_owl_object_some_values_from(entity: owlready2.Restriction) -> Optional[pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom]


   .. py:method:: to_owl_object_union_of(entity: owlready2.Or) -> Optional[pyowl2.class_expression.object_union_of.OWLObjectUnionOf]


   .. py:method:: to_owl_reflexive_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.reflexive_object_property.OWLReflexiveObjectProperty]


   .. py:method:: to_owl_same_individual(individuals: tuple[owlready2.NamedIndividual, Ellipsis], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.assertion.OWLSameIndividual]


   .. py:method:: to_owl_sub_annotation_property_of(sub_property: owlready2.AnnotationPropertyClass, super_property: owlready2.AnnotationPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.annotations.OWLSubAnnotationPropertyOf]


   .. py:method:: to_owl_sub_data_property_of(sub_property: owlready2.DataPropertyClass, super_property: owlready2.DataPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf]


   .. py:method:: to_owl_sub_object_property_of(sub_property: Union[tuple[owlready2.ObjectPropertyClass], owlready2.ObjectPropertyClass], super_property: owlready2.ObjectPropertyClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]


   .. py:method:: to_owl_subclass_of(sub_class: owlready2.EntityClass, super_class: owlready2.EntityClass, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf]


   .. py:method:: to_owl_symmetric_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.symmetric_object_property.OWLSymmetricObjectProperty]


   .. py:method:: to_owl_transitive_object_property(property: owlready2.ObjectPropertyClass) -> Optional[pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty]


   .. py:attribute:: STANDARD_ANNOTATIONS
      :type:  dict[int, owlready2.AnnotationPropertyClass]


   .. py:property:: annotation_assertions
      :type: dict[tuple[Union[owlready2.NamedIndividual, rdflib.URIRef, str], owlready2.AnnotationPropertyClass, Union[owlready2.NamedIndividual, rdflib.URIRef, rdflib.Literal]], pyowl2.axioms.annotations.OWLAnnotationAssertion]



   .. py:property:: annotation_properties
      :type: dict[owlready2.AnnotationPropertyClass, pyowl2.base.annotation_property.OWLAnnotationProperty]



   .. py:property:: annotation_property_domains
      :type: dict[owlready2.AnnotationPropertyClass, pyowl2.axioms.annotations.OWLAnnotationPropertyDomain]



   .. py:property:: annotation_property_ranges
      :type: dict[owlready2.AnnotationPropertyClass, pyowl2.axioms.annotations.OWLAnnotationPropertyRange]



   .. py:property:: annotations
      :type: dict[owlready2.EntityClass, tuple[rdflib.URIRef, pyowl2.base.annotation.OWLAnnotation]]



   .. py:property:: asymmetric_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.asymmetric_object_property.OWLAsymmetricObjectProperty]



   .. py:property:: axioms
      :type: list[dict]



   .. py:property:: class_assertions
      :type: dict[tuple[owlready2.ThingClass, owlready2.NamedIndividual], pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]



   .. py:property:: classes
      :type: dict[owlready2.ThingClass, pyowl2.base.owl_class.OWLClass]



   .. py:property:: data_all_values_from
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom]



   .. py:property:: data_complements_of
      :type: dict[tuple[owlready2.Not], pyowl2.data_range.data_complement_of.OWLDataComplementOf]



   .. py:property:: data_exact_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality]



   .. py:property:: data_has_value
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_has_value.OWLDataHasValue]



   .. py:property:: data_intersections_of
      :type: dict[tuple[owlready2.And], pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf]



   .. py:property:: data_max_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality]



   .. py:property:: data_min_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality]



   .. py:property:: data_ones_of
      :type: dict[tuple[owlready2.OneOf], pyowl2.data_range.data_one_of.OWLDataOneOf]



   .. py:property:: data_properties
      :type: dict[owlready2.DataPropertyClass, pyowl2.expressions.data_property.OWLDataProperty]



   .. py:property:: data_property_assertions
      :type: dict[tuple[owlready2.DataPropertyClass, owlready2.NamedIndividual, rdflib.Literal], pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion]



   .. py:property:: data_property_domains
      :type: dict[owlready2.DataPropertyClass, pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain]



   .. py:property:: data_property_ranges
      :type: dict[owlready2.DataPropertyClass, pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange]



   .. py:property:: data_some_values_from
      :type: dict[owlready2.Restriction, pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom]



   .. py:property:: data_unions_of
      :type: dict[tuple[owlready2.Or], pyowl2.data_range.data_union_of.OWLDataUnionOf]



   .. py:property:: datatype_definitions
      :type: dict[owlready2.DatatypeClass, pyowl2.axioms.datatype_definition.OWLDatatypeDefinition]



   .. py:property:: datatype_restrictions
      :type: dict[owlready2.ConstrainedDatatype, pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction]



   .. py:property:: datatypes
      :type: dict[owlready2.DatatypeClass, pyowl2.base.datatype.OWLDatatype]



   .. py:property:: declarations
      :type: dict[owlready2.EntityClass, owlready2.EntityClass]



   .. py:property:: different_individuals
      :type: dict[Union[tuple[owlready2.NamedIndividual, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.assertion.OWLDifferentIndividuals]



   .. py:property:: disjoint_classes
      :type: dict[Union[tuple[owlready2.ThingClass, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses]



   .. py:property:: disjoint_data_properties
      :type: dict[Union[tuple[owlready2.DataPropertyClass, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties]



   .. py:property:: disjoint_object_properties
      :type: dict[Union[tuple[owlready2.ObjectPropertyClass, Ellipsis], owlready2.AllDifferent], pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties]



   .. py:property:: disjoint_unions
      :type: dict[tuple[owlready2.ThingClass, Ellipsis], pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion]



   .. py:property:: equivalent_classes
      :type: dict[tuple[owlready2.ThingClass, Ellipsis], pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses]



   .. py:property:: equivalent_data_properties
      :type: dict[tuple[owlready2.DataPropertyClass, Ellipsis], pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties]



   .. py:property:: equivalent_object_properties
      :type: dict[tuple[owlready2.ObjectPropertyClass, Ellipsis], pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties]



   .. py:property:: functional_data_properties
      :type: dict[owlready2.DataPropertyClass, pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty]



   .. py:property:: functional_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.functional_object_property.OWLFunctionalObjectProperty]



   .. py:property:: general_axioms
      :type: dict[owlready2.EntityClass, pyowl2.axioms.annotations.OWLAnnotationAssertion]



   .. py:property:: graph
      :type: rdflib.Graph



   .. py:property:: has_keys
      :type: dict[owlready2.ThingClass, pyowl2.axioms.has_key.OWLHasKey]



   .. py:property:: individuals
      :type: dict[owlready2.NamedIndividual, pyowl2.abstracts.individual.OWLIndividual]



   .. py:property:: inverse_functional_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty]



   .. py:property:: inverse_object_properties
      :type: dict[tuple[owlready2.ObjectPropertyClass, Ellipsis], pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties]



   .. py:property:: irreflexive_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty]



   .. py:property:: namespace
      :type: rdflib.Namespace



   .. py:property:: negative_data_property_assertions
      :type: dict[tuple[owlready2.DataPropertyClass, owlready2.NamedIndividual, rdflib.Literal], pyowl2.axioms.assertion.OWLNegativeDataPropertyAssertion]



   .. py:property:: negative_object_property_assertions
      :type: dict[tuple[owlready2.ObjectPropertyClass, owlready2.NamedIndividual, owlready2.NamedIndividual], pyowl2.axioms.assertion.OWLNegativeObjectPropertyAssertion]



   .. py:property:: object_complements_of
      :type: dict[tuple[owlready2.Not], pyowl2.class_expression.object_complement_of.OWLObjectComplementOf]



   .. py:property:: object_intersections_of
      :type: dict[tuple[owlready2.And], pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf]



   .. py:property:: object_ones_of
      :type: dict[tuple[owlready2.OneOf], pyowl2.class_expression.object_one_of.OWLObjectOneOf]



   .. py:property:: object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.expressions.object_property.OWLObjectProperty]



   .. py:property:: object_property_assertions
      :type: dict[tuple[owlready2.ObjectPropertyClass, owlready2.NamedIndividual, owlready2.NamedIndividual], pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion]



   .. py:property:: object_property_domains
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain]



   .. py:property:: object_property_ranges
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange]



   .. py:property:: object_unions_of
      :type: dict[tuple[owlready2.And], pyowl2.class_expression.object_union_of.OWLObjectUnionOf]



   .. py:property:: objects_all_values_from
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom]



   .. py:property:: objects_exact_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality]



   .. py:property:: objects_has_self
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_has_self.OWLObjectHasSelf]



   .. py:property:: objects_has_value
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_has_value.OWLObjectHasValue]



   .. py:property:: objects_max_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality]



   .. py:property:: objects_min_cardinality
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality]



   .. py:property:: objects_some_values_from
      :type: dict[owlready2.Restriction, pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom]



   .. py:property:: ontology
      :type: owlready2.Ontology



   .. py:property:: reflexive_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.reflexive_object_property.OWLReflexiveObjectProperty]



   .. py:property:: same_individuals
      :type: dict[tuple[owlready2.NamedIndividual, Ellipsis], pyowl2.axioms.assertion.OWLSameIndividual]



   .. py:property:: subannotation_properties_of
      :type: dict[tuple[owlready2.AnnotationPropertyClass, owlready2.AnnotationPropertyClass], pyowl2.axioms.annotations.OWLSubAnnotationPropertyOf]



   .. py:property:: subclasses_of
      :type: dict[tuple[owlready2.ThingClass, owlready2.ThingClass], pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf]



   .. py:property:: subdata_properties_of
      :type: dict[tuple[owlready2.DataPropertyClass, owlready2.DataPropertyClass], pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf]



   .. py:property:: subobject_properties_of
      :type: dict[tuple[owlready2.ObjectPropertyClass, owlready2.ObjectPropertyClass], pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]



   .. py:property:: symmetric_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.symmetric_object_property.OWLSymmetricObjectProperty]



   .. py:property:: transitive_object_properties
      :type: dict[owlready2.ObjectPropertyClass, pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty]



   .. py:property:: world
      :type: owlready2.World



.. py:function:: get_abbreviation(iri: rdflib.URIRef) -> int

.. py:function:: is_named_individual(obj)

.. py:data:: BASE_DATATYPES

