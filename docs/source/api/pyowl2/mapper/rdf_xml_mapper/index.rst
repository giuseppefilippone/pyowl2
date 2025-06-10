pyowl2.mapper.rdf_xml_mapper
============================

.. py:module:: pyowl2.mapper.rdf_xml_mapper


Classes
-------

.. autoapisummary::

   pyowl2.mapper.rdf_xml_mapper.RDFXMLMapper


Functions
---------

.. autoapisummary::

   pyowl2.mapper.rdf_xml_mapper.example_usage


Module Contents
---------------

.. py:class:: RDFXMLMapper(graph: rdflib.Graph, OWL1_annotations: bool = False)

   A utility class for mapping OWL concepts to RDF triples using RDFLib.
   Each static method handles a specific OWL mapping transformation.


   .. py:method:: map(value: Optional[Union[rdflib.BNode, pyowl2.base.iri.IRI, str, rdflib.URIRef, rdflib.Literal, pyowl2.abstracts.object.OWLObject]]) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_annotation(element: Union[pyowl2.abstracts.entity.OWLEntity, pyowl2.base.iri.IRI, rdflib.URIRef], annotation: pyowl2.base.annotation.OWLAnnotation) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_annotation_assertion(assertion: pyowl2.axioms.annotations.OWLAnnotationAssertion) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_annotation_property(annotation: pyowl2.base.annotation_property.OWLAnnotationProperty) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_annotation_property_domain(prop: pyowl2.axioms.annotations.OWLAnnotationPropertyDomain) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_annotation_property_range(prop: pyowl2.axioms.annotations.OWLAnnotationPropertyRange) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_annotations(element: Union[pyowl2.abstracts.entity.OWLEntity, pyowl2.base.iri.IRI, rdflib.URIRef], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_annotations_entities(element1: Union[pyowl2.abstracts.entity.OWLEntity, pyowl2.base.iri.IRI, rdflib.URIRef], property: Union[pyowl2.base.iri.IRI, rdflib.URIRef], element2: Union[pyowl2.abstracts.entity.OWLEntity, pyowl2.base.iri.IRI, rdflib.URIRef], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_anonymous_individual(individual: pyowl2.individual.anonymous_individual.OWLAnonymousIndividual) -> Optional[rdflib.URIRef]

      Map an OWL Individual to RDF triples.

      :param individual_iri: iri of the OWL Individual
      :return: tuple of (triples list, individual node)



   .. py:method:: map_owl_asymmetric_property(prop: pyowl2.axioms.object_property_axiom.asymmetric_object_property.OWLAsymmetricObjectProperty) -> Optional[rdflib.URIRef]

      Map an OWL Asymmetric Property to RDF triples.

      :param property_iri: iri of the Transitive Property
      :return: tuple of (triples list, property node)



   .. py:method:: map_owl_class(class_: pyowl2.base.owl_class.OWLClass) -> Optional[rdflib.URIRef]

      Map an OWL Class to RDF triples.

      :param class_iri: iri of the OWL Class
      :return: tuple of (triples list, class node)



   .. py:method:: map_owl_class_assertion(assertion: pyowl2.axioms.assertion.class_assertion.OWLClassAssertion) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_all_values_from(prop: pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_complement_of(prop: pyowl2.data_range.data_complement_of.OWLDataComplementOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_exact_cardinality(prop: pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_has_value(prop: pyowl2.class_expression.data_has_value.OWLDataHasValue) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_intersection_of(prop: pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_max_cardinality(prop: pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_min_cardinality(prop: pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_one_of(prop: pyowl2.data_range.data_one_of.OWLDataOneOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_property(prop: pyowl2.expressions.data_property.OWLDataProperty) -> Optional[rdflib.URIRef]

      Map an OWL Datatype Property to RDF triples.

      :param property_iri: iri of the OWL Datatype Property
      :return: tuple of (triples list, property node)



   .. py:method:: map_owl_data_property_assertion(assertion: pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_property_domain(domain: pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_property_range(range: pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_some_values_from(prop: pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_data_union_of(prop: pyowl2.data_range.data_union_of.OWLDataUnionOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_datatype(datatype: pyowl2.base.datatype.OWLDatatype) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_datatype_definition(datatype_def: pyowl2.axioms.datatype_definition.OWLDatatypeDefinition) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_datatype_restriction(restriction_type: pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction) -> rdflib.URIRef

      Map an OWL Restriction to RDF triples.

      :param restriction_type: Type of restriction (e.g., OWL.someValuesFrom, OWL.allValuesFrom)
      :return: tuple of (triples list, restriction node)



   .. py:method:: map_owl_declaration(declaration: pyowl2.axioms.declaration.OWLDeclaration) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_different_individuals(different: pyowl2.axioms.assertion.OWLDifferentIndividuals) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_disjoint_classes(disjoints: pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses) -> Optional[rdflib.URIRef]

      Map OWL Disjoint Classes to RDF triples.

      :param classes: list of OWL Classes to be declared disjoint
      :return: tuple of (triples list, list of classes)



   .. py:method:: map_owl_disjoint_data_properties(disjoints: pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_disjoint_object_properties(disjoints: pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_disjoint_union(disjoints: pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_equivalent_classes(eq: pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses) -> Optional[rdflib.URIRef]

      Map OWL Equivalent Classes to RDF triples.

      :param eq: First OWL Class
      :return: tuple of (triples list, list of classes)



   .. py:method:: map_owl_equivalent_data_properties(eq: pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_equivalent_object_properties(eq: pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_facets(facets: list[pyowl2.data_range.datatype_restriction.OWLFacet]) -> tuple[list[rdflib.URIRef], list[rdflib.URIRef], list[rdflib.URIRef]]


   .. py:method:: map_owl_functional_property(prop: Union[pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty, pyowl2.axioms.object_property_axiom.functional_object_property.OWLFunctionalObjectProperty]) -> Optional[rdflib.URIRef]

      Map an OWL Functional Property to RDF triples.

      :param property_iri: iri of the Transitive Property
      :return: tuple of (triples list, property node)



   .. py:method:: map_owl_general_class_axiom(axiom: pyowl2.axioms.general.OWLGeneralClassAxiom) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_has_key(has_key: pyowl2.axioms.has_key.OWLHasKey) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_inverse_functional_property(prop: pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty) -> Optional[rdflib.URIRef]

      Map an OWL Inverse Functional Property to RDF triples.

      :param property_iri: iri of the Transitive Property
      :return: tuple of (triples list, property node)



   .. py:method:: map_owl_inverse_object_properties(prop: pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_irreflexive_property(prop: pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty) -> Optional[rdflib.URIRef]

      Map an OWL Irreflexive Property to RDF triples.

      :param property_iri: iri of the Transitive Property
      :return: tuple of (triples list, property node)



   .. py:method:: map_owl_named_individual(individual: pyowl2.individual.named_individual.OWLNamedIndividual) -> Optional[rdflib.URIRef]

      Map an OWL Individual to RDF triples.

      :param individual_iri: iri of the OWL Individual
      :return: tuple of (triples list, individual node)



   .. py:method:: map_owl_negative_data_property_assertion(assertion: pyowl2.axioms.assertion.OWLNegativeDataPropertyAssertion) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_negative_object_property_assertion(assertion: pyowl2.axioms.assertion.OWLNegativeObjectPropertyAssertion) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_all_values_from(prop: pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_complement_of(prop: pyowl2.class_expression.object_complement_of.OWLObjectComplementOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_exact_cardinality(prop: pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_has_self(prop: pyowl2.class_expression.object_has_self.OWLObjectHasSelf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_has_value(prop: pyowl2.class_expression.object_has_value.OWLObjectHasValue) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_intersection_of(prop: pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_inverse_of(prop: pyowl2.expressions.OWLInverseObjectProperty) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_max_cardinality(prop: pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_min_cardinality(prop: pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_one_of(prop: pyowl2.class_expression.object_one_of.OWLObjectOneOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_property(prop: pyowl2.expressions.object_property.OWLObjectProperty) -> Optional[rdflib.URIRef]

      Map an OWL Object Property to RDF triples.



   .. py:method:: map_owl_object_property_assertion(assertion: pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_property_domain(domain: pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_property_range(range: pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_some_values_from(prop: pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_object_union_of(prop: pyowl2.class_expression.object_union_of.OWLObjectUnionOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_reflexive_property(prop: pyowl2.axioms.object_property_axiom.reflexive_object_property.OWLReflexiveObjectProperty) -> Optional[rdflib.URIRef]

      Map an OWL Reflexive Property to RDF triples.

      :param property_iri: iri of the Transitive Property
      :return: tuple of (triples list, property node)



   .. py:method:: map_owl_same_individual(same: pyowl2.axioms.assertion.OWLSameIndividual) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_sub_annotation_property_of(prop: pyowl2.axioms.annotations.OWLSubAnnotationPropertyOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_subclass_of(subclass: pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_subdata_property_of(subdata: pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_subobject_property_of(subclass: pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf) -> Optional[rdflib.URIRef]


   .. py:method:: map_owl_symmetric_property(prop: pyowl2.axioms.object_property_axiom.symmetric_object_property.OWLSymmetricObjectProperty) -> Optional[rdflib.URIRef]

      Map an OWL Symmetric Property to RDF triples.

      :param property_iri: iri of the Symmetric Property
      :return: tuple of (triples list, property node)



   .. py:method:: map_owl_transitive_property(prop: pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty) -> Optional[rdflib.URIRef]

      Map an OWL Transitive Property to RDF triples.

      :param property_iri: iri of the Transitive Property
      :return: tuple of (triples list, property node)



   .. py:method:: map_sequence(sequence: Iterable[Any]) -> list[tuple[rdflib.URIRef, Ellipsis]]


   .. py:property:: graph
      :type: rdflib.Graph



   .. py:property:: owl1_annotations
      :type: bool



.. py:function:: example_usage()

