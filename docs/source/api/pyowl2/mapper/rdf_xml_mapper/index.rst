pyowl2.mapper.rdf_xml_mapper
============================

.. py:module:: pyowl2.mapper.rdf_xml_mapper



.. ── LLM-GENERATED DESCRIPTION START ──

A utility class that translates high-level OWL ontology constructs into standard RDF triples within an RDFLib graph.


Description
-----------


The software provides a comprehensive mechanism for serializing a wide variety of OWL 2 entities, axioms, and class expressions into their corresponding RDF representations. By accepting an RDFLib graph instance during initialization, the mapper populates it with triples generated from complex structures such as class intersections, unions, restrictions, and property characteristics. A central dispatch method inspects the type of the input object and delegates the transformation to specialized helper methods, ensuring that anonymous classes are represented as blank nodes and collections are handled correctly using RDF lists. Furthermore, the implementation supports both OWL 1 and OWL 2 annotation styles, utilizing reification to attach metadata to axioms when necessary, thereby facilitating the conversion of abstract ontology models into concrete graph data.

.. ── LLM-GENERATED DESCRIPTION END ──

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

.. only:: html

    .. figure:: /_uml/class_pyowl2_mapper_rdf_xml_mapper_RDFXMLMapper.png
       :alt: UML Class Diagram for RDFXMLMapper
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RDFXMLMapper**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_mapper_rdf_xml_mapper_RDFXMLMapper.pdf
       :alt: UML Class Diagram for RDFXMLMapper
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RDFXMLMapper**

.. py:class:: RDFXMLMapper(graph: rdflib.Graph, OWL1_annotations: bool = False)

   This class serves as a utility for translating OWL ontology constructs into RDF triples within an RDFLib Graph instance. It is designed to handle a wide array of OWL elements, including classes, properties, individuals, and complex axioms such as restrictions, intersections, and unions. By initializing the mapper with a target graph and an optional flag to enforce OWL 1 annotation compatibility, users can populate the graph by passing OWL objects to the `map` method, which intelligently dispatches to specific handlers based on the input type. The process involves generating appropriate URI references or blank nodes for entities and adding the corresponding triples to the graph, thereby enabling the serialization or manipulation of OWL data in a standard RDF format.

   :parm graph: The RDFLib Graph instance that stores the RDF triples generated from OWL concepts.
   :type graph: Graph
   :parm owl1_annotations: A boolean flag indicating whether to use OWL 1 annotation structures. When True, the mapper uses `owl:Axiom` for annotated axioms; otherwise, it uses the OWL 2 `owl:Annotation` class.
   :type owl1_annotations: bool

   :raises TypeError: Raised when the input value is not a recognized OWL entity, expression, or RDFLib type, preventing it from being mapped to an RDF triple.


   .. py:method:: map(value: Optional[Union[rdflib.BNode, pyowl2.base.iri.IRI, str, rdflib.URIRef, rdflib.Literal, pyowl2.abstracts.object.OWLObject]]) -> Optional[rdflib.URIRef]

      Converts a diverse range of input types—including OWL entities, axioms, expressions, and basic RDF primitives—into corresponding RDFLib nodes suitable for graph construction. When the input is `None` or falsy, the method generates and returns a new blank node. For standard RDF types like `IRI`, `URIRef`, `BNode`, and `Literal`, it performs necessary conversions or returns the value directly. The method serves as a dispatcher for complex OWL constructs, inspecting the type of the input object and delegating the mapping logic to specialized helper methods tailored to specific axioms or expressions (such as intersections, unions, or restrictions). If the input is a string, it is cast to a `URIRef`, and if it is an iterable, it is processed as a sequence. Finally, if the input type is unsupported or invalid, a `TypeError` is raised.

      :param value: The OWL entity, expression, or RDF term to be mapped. Accepts a wide range of types including IRIs, strings, literals, blank nodes, and complex OWL axioms. If the value is None or falsy, a new blank node is generated.
      :type value: typing.Optional[typing.Union[BNode, IRI, str, URIRef, Literal, OWLObject]]

      :raises TypeError: Raised when the input value is not a recognized OWL entity, expression, or supported primitive type, or if an object's 'iri' attribute is not an IRI or URIRef.

      :return: The RDFLib node (URIRef, BNode, or Literal) representing the input value in the RDF graph, suitable for use as a subject or object in RDF triples.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_annotation(element: Union[pyowl2.abstracts.entity.OWLEntity, pyowl2.base.iri.IRI, rdflib.URIRef], annotation: pyowl2.base.annotation.OWLAnnotation) -> Optional[rdflib.URIRef]

      This method converts an OWL annotation into RDF triples within the graph, attaching it to the specified element. It resolves the element, annotation property, and annotation value to their RDF representations and adds a triple to the graph. If the annotation contains nested annotations, the method reifies the statement to create a dedicated node and recursively processes the nested annotations, attaching them to this new node. The method modifies the graph as a side effect and returns None, performing no operation if the provided annotation is None.

      :param element: The OWL entity, IRI, or URIRef to which the annotation is attached, serving as the subject of the generated RDF triples.
      :type element: typing.Union[OWLEntity, IRI, URIRef]
      :param annotation: The OWL annotation to be mapped to RDF triples. It provides the property-value pair attached to the element and may contain nested annotations that are processed recursively.
      :type annotation: OWLAnnotation

      :return: None, as the method modifies the graph in place by adding the annotation triples.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_annotation_assertion(assertion: pyowl2.axioms.annotations.OWLAnnotationAssertion) -> Optional[rdflib.URIRef]

      This method processes an OWL annotation assertion axiom by converting it into an RDF triple and adding it to the underlying graph. It resolves the annotation's subject, property, and value into their corresponding RDF representations and inserts the resulting triple into the graph structure. Additionally, the method handles any annotations associated with the axiom itself by delegating to the entity annotation mapping logic. The operation modifies the graph as a side effect and always returns None.

      :param assertion: The OWL annotation assertion axiom to be converted into an RDF triple, containing a subject, property, and value.
      :type assertion: OWLAnnotationAssertion

      :return: None, as the method modifies the graph in place to add the corresponding RDF triples.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_annotation_property(annotation: pyowl2.base.annotation_property.OWLAnnotationProperty) -> Optional[rdflib.URIRef]

      Converts an OWL annotation property into its RDF representation by asserting its type within the graph. The method resolves the IRI of the provided annotation property and adds a triple to the underlying graph stating that the corresponding node is an instance of `owl:AnnotationProperty`. This process modifies the graph as a side effect. It returns the URI reference representing the property, or None if the IRI cannot be mapped.

      :param annotation: The specific annotation property to be mapped to the RDF graph.
      :type annotation: OWLAnnotationProperty

      :return: The RDFLib URIRef representing the IRI of the mapped OWL annotation property, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_annotation_property_domain(prop: pyowl2.axioms.annotations.OWLAnnotationPropertyDomain) -> Optional[rdflib.URIRef]

      Converts an OWL annotation property domain axiom into RDF triples within the internal graph. The method resolves the IRI of the annotation property and the specified domain, creating a triple that links them using the `rdfs:domain` predicate. It also processes and adds any annotations associated with the axiom itself. This operation modifies the graph's state and returns the URI reference of the annotation property, or None if the mapping cannot be performed.

      :param prop: The OWL axiom specifying the domain of an annotation property, containing the property, the domain class, and any associated annotations to be mapped to RDF.
      :type prop: OWLAnnotationPropertyDomain

      :return: The IRI of the annotation property for which the domain axiom was mapped.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_annotation_property_range(prop: pyowl2.axioms.annotations.OWLAnnotationPropertyRange) -> Optional[rdflib.URIRef]

      This method maps an OWL annotation property range axiom to an RDF triple within the internal graph. It resolves the annotation property and the range to their respective URI references and establishes a relationship between them using the `rdfs:range` predicate. The method also handles any annotations attached to the axiom, ensuring they are properly represented in the graph. It returns the URI reference of the annotation property, or None if the mapping fails. As a side effect, the internal graph is mutated to include the new range assertion and any associated annotations.

      :param prop: The OWL annotation property range axiom to be mapped to RDF triples, consisting of an annotation property and its range.
      :type prop: OWLAnnotationPropertyRange

      :return: The IRI of the annotation property that was mapped to the graph, or None if the mapping failed.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_annotations(element: Union[pyowl2.abstracts.entity.OWLEntity, pyowl2.base.iri.IRI, rdflib.URIRef], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[rdflib.URIRef]

      This method serializes a collection of OWL annotations into the underlying RDF graph by attaching them to a specified subject element. It accepts an OWL entity, IRI, or URIRef as the subject and an optional list of OWLAnnotation instances. If the annotation list is None or empty, the method performs no action and returns immediately. When annotations are present, the method iterates through the list and invokes `map_owl_annotation` for each item to generate the corresponding RDF triples. The operation relies on side effects to modify the graph and always returns None.

      :param element: The OWL entity, IRI, or URIRef serving as the subject to which the annotations are attached in the RDF graph.
      :type element: typing.Union[OWLEntity, IRI, URIRef]
      :param annotations: The OWL annotations to be mapped to RDF triples and attached to the element.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: None, as the method performs side effects on the graph without returning a value.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_annotations_entities(element1: Union[pyowl2.abstracts.entity.OWLEntity, pyowl2.base.iri.IRI, rdflib.URIRef], property: Union[pyowl2.base.iri.IRI, rdflib.URIRef], element2: Union[pyowl2.abstracts.entity.OWLEntity, pyowl2.base.iri.IRI, rdflib.URIRef], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> Optional[rdflib.URIRef]

      This method creates a reified OWL Axiom or Annotation node within the RDF graph to associate a list of annotations with a specific subject-predicate-object triple. It maps the provided elements to their corresponding IRIs and generates a blank node to serve as the axiom container, adding triples to define its type and its relationships to the annotated source, property, and target. The method then attaches the provided annotations to this blank node, effectively reifying the triple to support annotation. If the input list of annotations is empty or None, the method returns None without modifying the graph; otherwise, it returns the blank node identifier representing the annotated axiom.

      :param element1: The subject of the statement being annotated. It is converted to an IRI and used as the `owl:annotatedSource` in the generated annotation axiom.
      :type element1: typing.Union[OWLEntity, IRI, URIRef]
      :param property: The IRI or URIRef representing the property (predicate) of the statement being annotated, used as the object for the `owl:annotatedProperty` triple.
      :type property: typing.Union[IRI, URIRef]
      :param element2: The object or target of the annotation assertion, which is mapped to the `owl:annotatedTarget` property of the generated RDF reification node.
      :type element2: typing.Union[OWLEntity, IRI, URIRef]
      :param annotations: Optional list of OWLAnnotation instances to be attached to the generated RDF axiom or annotation node. These provide metadata about the relationship defined by the source, property, and target elements. If None or empty, the method returns None without creating the axiom node.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: The blank node identifier of the reified OWL Axiom or Annotation, or None if no annotations are provided.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_anonymous_individual(individual: pyowl2.individual.anonymous_individual.OWLAnonymousIndividual) -> Optional[rdflib.URIRef]

      Maps an OWL anonymous individual to an RDF node by converting its node ID into a URI reference and adding a type assertion to the graph. The method generates a triple stating that the resulting node is an `owl:NamedIndividual` and returns the URIRef. This process modifies the internal graph structure, and the return value may be None if the node ID cannot be successfully mapped.

      :param individual: The OWL anonymous individual to be mapped to RDF triples. The method uses the individual's node ID to generate the corresponding RDF node and adds it to the graph as a NamedIndividual.
      :type individual: OWLAnonymousIndividual

      :return: The RDFLib URIRef representing the mapped anonymous individual, or None if the mapping cannot be performed.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_asymmetric_property(prop: pyowl2.axioms.object_property_axiom.asymmetric_object_property.OWLAsymmetricObjectProperty) -> Optional[rdflib.URIRef]

      This method converts an OWL asymmetric object property axiom into corresponding RDF triples within the mapper's graph. It retrieves the IRI of the property by recursively mapping the underlying object property expression, then asserts that this IRI is an instance of `owl:AsymmetricProperty`. The method also processes and adds any annotations associated with the axiom. It returns the URI reference of the mapped property, or None if the property expression cannot be successfully resolved.

      :param prop: The OWL asymmetric object property to be mapped to RDF triples, containing the property expression and any associated annotations.
      :type prop: OWLAsymmetricObjectProperty

      :return: The IRI of the object property that was mapped as an asymmetric property, or None if the mapping was unsuccessful.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_class(class_: pyowl2.base.owl_class.OWLClass) -> Optional[rdflib.URIRef]

      Maps an OWL class entity to its corresponding RDF representation within the internal graph. It resolves the IRI of the provided `OWLClass` into a `URIRef` and adds a triple asserting that the resource is of type `owl:Class`. This operation modifies the graph by registering the class declaration, though it does not handle complex axioms such as subclass relationships or restrictions. The method returns the generated `URIRef`, which can be used to reference the class in further mapping operations.

      :param class_: The OWL class instance to be converted into RDF triples. It represents a class in the ontology identified by an IRI and will be added to the graph as an `owl:Class`.
      :type class_: OWLClass

      :return: The RDFLib URIRef representing the IRI of the mapped OWL class, or None if the class cannot be mapped.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_class_assertion(assertion: pyowl2.axioms.assertion.class_assertion.OWLClassAssertion) -> Optional[rdflib.URIRef]

      Maps an OWL class assertion axiom to an RDF triple within the internal graph. The method resolves the individual and class expression components of the assertion to their corresponding IRIs and adds a triple asserting that the individual is an instance of the class using the `rdf:type` predicate. It also handles the mapping of any annotations attached to the axiom. This operation modifies the graph in place and returns None.

      :param assertion: The OWL class assertion axiom to be mapped, defining an individual as an instance of a specific class expression.
      :type assertion: OWLClassAssertion

      :return: None, as the method performs the mapping by adding triples directly to the graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_all_values_from(prop: pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom) -> Optional[rdflib.URIRef]

      Converts an OWL data all-values-from restriction into its corresponding RDF representation within the graph. The method creates a blank node to represent the restriction and adds triples asserting its type as `owl:Restriction`. It handles the mapping of the data property expressions by using `owl:onProperty` for a single expression or `owl:onProperties` (via an RDF collection) for multiple expressions. Finally, it links the restriction to the mapped data range using the `owl:allValuesFrom` predicate, modifying the graph state and returning the identifier of the restriction node.

      :param prop: The OWL data all-values-from restriction to be mapped to RDF triples, consisting of one or more data property expressions and a data range.
      :type prop: OWLDataAllValuesFrom

      :return: The RDFLib URIRef (specifically a Blank Node) identifying the `owl:Restriction` node created in the graph to represent the axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_complement_of(prop: pyowl2.data_range.data_complement_of.OWLDataComplementOf) -> Optional[rdflib.URIRef]

      Maps an OWL data complement expression to an RDF representation by creating a blank node and adding triples to the graph. The method recursively resolves the nested data range to its corresponding IRI, then asserts that the blank node is an `rdfs:Datatype` linked to that IRI via the `owl:datatypeComplementOf` property. This operation modifies the internal graph and returns the blank node identifier representing the complement structure. The method relies on the successful mapping of the nested data range to generate valid triples.

      :param prop: The OWL data complement expression to be mapped. It encapsulates the data range that is being complemented, which is used to generate the corresponding RDF triples.
      :type prop: OWLDataComplementOf

      :return: Returns the blank node identifier representing the OWL data complement data range in the RDF graph, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_exact_cardinality(prop: pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality) -> Optional[rdflib.URIRef]

      This method maps an OWL data exact cardinality restriction to RDF triples within the graph. It creates a blank node to represent the restriction and adds triples defining it as an `owl:Restriction` linked to the specific data property. The mapping logic adapts based on the presence of a data range: if a data range is provided, it uses `owl:qualifiedCardinality` and includes an `owl:onDataRange` triple; otherwise, it uses `owl:cardinality`. The method modifies the graph by adding these triples and returns the blank node identifier for the restriction.

      :param prop: The OWL data exact cardinality axiom to map, consisting of a data property expression, a specific cardinality value, and an optional data range.
      :type prop: OWLDataExactCardinality

      :return: The blank node identifier representing the restriction added to the graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_has_value(prop: pyowl2.class_expression.data_has_value.OWLDataHasValue) -> Optional[rdflib.URIRef]

      Converts an OWL data has value restriction into its corresponding RDF representation within the graph. The method instantiates a new blank node to serve as the subject of the restriction and recursively maps the associated data property expression and literal value to RDF terms. It then populates the graph with triples defining the blank node as an `owl:Restriction`, linking it to the property via `owl:onProperty` and to the literal via `owl:hasValue`. As a side effect, this method mutates the internal graph by adding these triples. The identifier of the newly created blank node representing the restriction is returned.

      :param prop: The OWL data has value axiom to map, consisting of a data property expression and a specific literal value.
      :type prop: OWLDataHasValue

      :return: The blank node identifier representing the OWL restriction in the graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_intersection_of(prop: pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf) -> Optional[rdflib.URIRef]

      Converts an OWL data intersection expression into its corresponding RDF representation within the mapper's graph. The method creates a blank node to represent the intersection, asserts it as an `rdfs:Datatype`, and links it to an RDF collection of the constituent data ranges using the `owl:intersectionOf` property. This operation has the side effect of adding these triples directly to the graph. The blank node identifier representing the intersection is returned to facilitate further mapping operations.

      :param prop: The OWL data intersection axiom containing the sequence of data ranges to be mapped to the RDF graph.
      :type prop: OWLDataIntersectionOf

      :return: The RDFLib URIRef (a blank node) representing the data intersection class expression added to the graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_max_cardinality(prop: pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality) -> Optional[rdflib.URIRef]

      Maps an OWL data maximum cardinality restriction to an RDF representation by creating a blank node and populating the internal graph with the necessary triples. The method determines whether to use a qualified or unqualified restriction based on the presence of a data range; if a data range is provided, it utilizes `owl:maxQualifiedCardinality` and `owl:onDataRange`, otherwise it defaults to `owl:maxCardinality`. It recursively resolves the IRI for the data property expression and the optional data range. The function returns the blank node representing the restriction, having modified the graph as a side effect.

      :param prop: The OWL data max cardinality axiom to be mapped to RDF triples. It encapsulates the data property expression, the maximum cardinality value, and an optional data range.
      :type prop: OWLDataMaxCardinality

      :return: The blank node identifier representing the restriction created in the graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_min_cardinality(prop: pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality) -> Optional[rdflib.URIRef]

      Translates an OWL data minimum cardinality restriction into RDF triples and inserts them into the graph. The method creates a blank node representing the restriction and establishes its type as `owl:Restriction`. It links this node to the specified data property and sets the minimum cardinality value, using `owl:minCardinality` for unqualified restrictions or `owl:minQualifiedCardinality` if a specific data range is defined. When a data range is present, the method also adds a triple linking the restriction to that range. This process modifies the internal graph state and returns the blank node identifier for the newly created restriction.

      :param prop: The OWL data min cardinality restriction to be mapped to RDF triples, comprising the data property, the minimum cardinality value, and an optional data range.
      :type prop: OWLDataMinCardinality

      :return: The blank node identifier of the restriction node created in the graph to represent the OWL data min cardinality axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_one_of(prop: pyowl2.data_range.data_one_of.OWLDataOneOf) -> Optional[rdflib.URIRef]

      This method maps an OWL `DataOneOf` axiom, which defines a datatype restricted to a specific set of literal values, into the RDF graph managed by the mapper. It creates a new blank node to represent the datatype and asserts that it is an instance of `rdfs:Datatype`. The literals contained within the axiom are converted into an RDF collection (list) via an internal sequence mapping, and this collection is linked to the blank node using the `owl:oneOf` predicate. This process modifies the graph by adding the necessary triples to define the enumerated datatype. The method returns the blank node identifier representing the axiom, which can be used as a reference for further mapping operations.

      :param prop: The OWL data one-of expression to be mapped, consisting of a set of literals that define an enumerated data range.
      :type prop: OWLDataOneOf

      :return: The blank node representing the data range in the RDF graph corresponding to the OWL data one-of axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_property(prop: pyowl2.expressions.data_property.OWLDataProperty) -> Optional[rdflib.URIRef]

      Transforms an OWL data property into an RDF representation by generating a URI reference and asserting its type within the graph. The method utilizes the generic mapping logic to resolve the property's IRI, then adds a triple to the internal graph stating that this node is an instance of `owl:DatatypeProperty`. It returns the resulting URI reference, or None if the property cannot be successfully mapped to a valid identifier.

      :param prop: The OWL datatype property instance to be mapped to the RDF graph. It represents a property associated with literal values and provides the IRI used to generate the corresponding RDF triples.
      :type prop: OWLDataProperty

      :return: The RDFLib URIRef representing the IRI of the mapped OWL datatype property, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_property_assertion(assertion: pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion) -> Optional[rdflib.URIRef]

      Converts an OWL data property assertion axiom into an RDF triple and adds it to the internal graph. The method resolves the RDF representations for the source individual, the data property expression, and the target literal value, then inserts the triple into the graph. It also processes and adds any annotations associated with the axiom. This operation modifies the graph state as a side effect and returns None.

      :param assertion: The OWL data property assertion axiom to be mapped, comprising a source individual, a data property, a target literal value, and any associated annotations.
      :type assertion: OWLDataPropertyAssertion

      :return: None, as the method performs side effects by adding triples to the graph in place.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_property_domain(domain: pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain) -> Optional[rdflib.URIRef]

      This method processes an OWL Data Property Domain axiom by converting it into an RDF triple within the mapper's graph. It resolves the constituent data property expression and class expression into RDF nodes and establishes a relationship between them using the `rdfs:domain` predicate. Additionally, the method handles any annotations associated with the axiom, integrating them into the graph structure. The function returns the URI reference of the data property node that serves as the subject of the domain assertion.

      :param domain: The OWL data property domain axiom to be mapped to RDF triples. This object contains the data property expression, the class expression defining its domain, and any associated annotations.
      :type domain: OWLDataPropertyDomain

      :return: The URIRef of the data property expression, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_property_range(range: pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange) -> Optional[rdflib.URIRef]

      Converts an OWL data property range axiom into RDF triples by linking a data property expression to a specific data range. The method maps both the property and the range to their corresponding RDF nodes and adds a triple to the internal graph using the `rdfs:range` predicate to define the constraint. It also processes any annotations attached to the axiom, adding them to the graph to preserve metadata. This process modifies the internal graph as a side effect and returns the URI reference of the data property node that serves as the subject of the range assertion.

      :param range: The OWL axiom defining the valid data range for a data property expression. It encapsulates the property and the range constraint to be serialized as an `rdfs:range` triple in the RDF graph.
      :type range: OWLDataPropertyRange

      :return: The URI reference of the mapped data property expression, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_some_values_from(prop: pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom) -> Optional[rdflib.URIRef]

      This method converts an OWL data some values from restriction into a corresponding RDF structure within the graph. It generates a blank node to represent the restriction and asserts its type as `owl:Restriction`. The method processes the input's data property expressions and data range, adding triples to link the restriction to the specific data range via `owl:someValuesFrom`. Depending on the number of data property expressions provided, it either assigns the property directly using `owl:onProperty` for a single expression or creates an RDF collection and uses `owl:onProperties` for multiple expressions. As a side effect, this method modifies the internal graph by adding these triples and returns the blank node identifier for the newly created restriction.

      :param prop: The OWL data some values from restriction to be mapped to RDF triples, containing data property expressions and a data range.
      :type prop: OWLDataSomeValuesFrom

      :return: The Blank Node representing the OWL Restriction created in the graph for the specified data some values from axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_data_union_of(prop: pyowl2.data_range.data_union_of.OWLDataUnionOf) -> Optional[rdflib.URIRef]

      Converts an OWL data union expression into its corresponding RDF representation within the mapper's graph. The method instantiates a blank node to serve as the subject of the union, types it as `rdfs:Datatype`, and links it to an RDF collection containing the mapped data ranges via the `owl:unionOf` property. This process involves recursively mapping the constituent data ranges to ensure the complete structure is serialized. As a side effect, the method directly mutates the internal graph by adding these triples. It returns the blank node identifier representing the union structure, which can be used to reference this data range definition elsewhere in the graph.

      :param prop: The OWL data union expression to be mapped, consisting of a sequence of data ranges that define the union.
      :type prop: OWLDataUnionOf

      :return: A blank node (BNode) representing the data union axiom in the RDF graph. This node serves as the subject for the triples defining the union of the input data ranges.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_datatype(datatype: pyowl2.base.datatype.OWLDatatype) -> Optional[rdflib.URIRef]

      Converts an OWL datatype into its corresponding RDF representation by asserting its type within the mapper's internal graph. The method retrieves the IRI node associated with the datatype and adds a triple defining it as an instance of `rdfs:Datatype`. It returns the URI reference for the datatype, which serves as the subject for these assertions and can be used for further mapping operations.

      :param datatype: The OWL datatype instance to be mapped to RDF triples. It represents a datatype in the ontology identified by an IRI.
      :type datatype: OWLDatatype

      :return: The RDFLib URIRef representing the IRI of the mapped OWL datatype, or None if the datatype cannot be mapped.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_datatype_definition(datatype_def: pyowl2.axioms.datatype_definition.OWLDatatypeDefinition) -> Optional[rdflib.URIRef]

      Converts an OWL datatype definition axiom into RDF triples within the mapper's graph. The method resolves the datatype and data range components of the axiom to their corresponding IRIs and asserts an equivalence relationship between them using the `owl:equivalentClass` predicate. It also handles the mapping of any annotations associated with the axiom. This method modifies the graph as a side effect and returns None, despite the type hint indicating an optional URIRef.

      :param datatype_def: The OWL datatype definition axiom to be mapped, representing an equivalence between a datatype and a data range.
      :type datatype_def: OWLDatatypeDefinition

      :return: Returns None, as the method performs the mapping by adding triples directly to the graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_datatype_restriction(restriction_type: pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction) -> Optional[rdflib.URIRef]

      Converts an OWL datatype restriction into its corresponding RDF representation within the graph. The method instantiates a blank node to serve as the subject of the restriction, asserting it as an `rdfs:Datatype` and linking it to the constrained datatype via the `owl:onDatatype` property. It then processes the specific facet constraints, such as minimum or maximum values, organizing them into an RDF collection attached through the `owl:withRestrictions` predicate. This process directly mutates the internal graph by adding the necessary triples and returns the identifier of the generated restriction node.

      :param restriction_type: The OWL datatype restriction instance to be mapped, consisting of a base datatype and a set of facet constraints.
      :type restriction_type: OWLDatatypeRestriction

      :return: The blank node identifier representing the OWL datatype restriction in the RDF graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_declaration(declaration: pyowl2.axioms.declaration.OWLDeclaration) -> Optional[rdflib.URIRef]

      Processes an OWL declaration by inspecting the type of the entity being declared and delegating to the appropriate specific mapping method, such as those for classes, datatypes, or properties. After obtaining the RDF node representing the entity, the method ensures that any annotations associated with the declaration axiom are added to the graph. It returns the URI reference of the mapped entity, but raises a TypeError if the entity type is not recognized or supported.

      :param declaration: The OWL declaration to be mapped, encapsulating the entity to be declared and any associated annotations.
      :type declaration: OWLDeclaration

      :raises TypeError: Raised when the entity contained in the declaration is not a recognized OWL type supported for mapping.

      :return: The RDFLib URIRef representing the OWL entity being declared. This node serves as the subject of the declaration and is used to attach any associated annotations in the RDF graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_different_individuals(different: pyowl2.axioms.assertion.OWLDifferentIndividuals) -> Optional[rdflib.URIRef]

      Maps an OWL DifferentIndividuals axiom to the underlying RDF graph by generating triples that represent the distinctness of the specified individuals. If the axiom contains exactly two individuals, the method creates a direct triple using the `owl:differentFrom` predicate and returns None. For axioms involving three or more individuals, it instantiates a blank node typed as `owl:AllDifferent` and links it to an RDF collection of the individuals via the `owl:members` property, returning the blank node identifier. In both scenarios, the method adds the generated triples to the graph and processes any associated axiom annotations.

      :param different: Represents the OWL axiom specifying a set of individuals that are all distinct. The mapping process handles pairs of individuals using `owl:differentFrom` and larger sets using `owl:AllDifferent`.
      :type different: OWLDifferentIndividuals

      :return: The blank node representing the `owl:AllDifferent` axiom in the graph, or None if the axiom was mapped as a binary `owl:differentFrom` relationship.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_disjoint_classes(disjoints: pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses) -> Optional[rdflib.URIRef]

      Converts an OWL disjoint classes axiom into corresponding RDF triples within the mapper's graph, distinguishing between binary and n-ary relationships to produce the appropriate RDF structure. If the axiom involves exactly two class expressions, the method establishes a direct `owl:disjointWith` relationship between the mapped class nodes and returns None. For axioms involving three or more class expressions, it creates a blank node typed as `owl:AllDisjointClasses`, links the class expressions to this node using an `owl:members` collection, and returns the URI of the blank node. In both scenarios, any associated axiom annotations are processed and added to the graph.

      :param disjoints: The OWL axiom containing the class expressions declared to be mutually exclusive, which will be mapped to RDF triples.
      :type disjoints: OWLDisjointClasses

      :return: The identifier of the RDF node representing the disjoint classes collection, or None if the axiom involves exactly two class expressions.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_disjoint_data_properties(disjoints: pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties) -> Optional[rdflib.URIRef]

      This method maps an OWL disjoint data properties axiom to RDF triples, handling both binary and n-ary cases to conform to OWL 2 RDF serialization standards. When the axiom contains exactly two data property expressions, it creates a direct `owl:propertyDisjointWith` relationship between the two mapped property nodes and returns None. For axioms involving a different number of properties, it generates a blank node of type `owl:AllDisjointProperties`, populates an RDF collection with the mapped property expressions, and links the collection to the blank node using the `owl:members` predicate. The method also processes and attaches any axiom annotations to the relevant subject node, returning the blank node identifier for the n-ary representation.

      :param disjoints: The OWL axiom representing a set of mutually disjoint data properties. It contains the list of data property expressions to be mapped to RDF triples, handling both binary and n-ary disjointness.
      :type disjoints: OWLDisjointDataProperties

      :return: The identifier of the `AllDisjointProperties` axiom node if the list of properties does not contain exactly two items; otherwise returns `None` because the disjointness is asserted directly between the two properties.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_disjoint_object_properties(disjoints: pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties) -> Optional[rdflib.URIRef]

      Maps an OWL disjoint object properties axiom to the RDF graph by generating triples that represent the mutual exclusivity of the specified object properties. The method distinguishes between binary and N-ary disjointness: if exactly two properties are provided, it establishes a direct relationship using the `owl:propertyDisjointWith` predicate; otherwise, it creates an `owl:AllDisjointProperties` blank node containing the properties as members. In both scenarios, any associated axiom annotations are mapped to the graph, attached either to the specific relationship or the axiom node. The method returns the blank node identifier for N-ary axioms or None for binary axioms.

      :param disjoints: Represents an OWL axiom asserting that a collection of object properties are mutually disjoint. The method extracts the property expressions from this axiom to generate the appropriate RDF structure, handling both binary and n-ary disjointness.
      :type disjoints: OWLDisjointObjectProperties

      :return: The identifier of the axiom node created in the graph, or None if the disjointness is represented as a binary relationship between exactly two properties.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_disjoint_union(disjoints: pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion) -> Optional[rdflib.URIRef]

      Maps an OWL disjoint union axiom to the internal RDF graph by generating the necessary triples to represent the relationship between a union class and its disjoint components. The method creates an RDF collection to hold the mapped IRIs of the disjoint class expressions and asserts an `owl:disjointUnionOf` property linking the union class to this collection. It also processes and attaches any annotations associated with the axiom to the graph. This operation mutates the graph state as a side effect and returns None.

      :param disjoints: The OWL disjoint union axiom to map, consisting of a union class and a set of mutually disjoint class expressions.
      :type disjoints: OWLDisjointUnion

      :return: None, as the method modifies the graph in place.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_equivalent_classes(eq: pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses) -> Optional[rdflib.URIRef]

      Converts an OWL equivalent classes axiom into a set of RDF triples by establishing pairwise equivalence relationships between the class expressions involved. The method iterates through the list of class expressions, mapping each to a node and linking adjacent nodes with the `owl:equivalentClass` property to form a chain of equivalences. It also processes and attaches any annotations associated with the axiom to these triples. This operation modifies the internal RDF graph directly and returns None, effectively handling cases with fewer than two class expressions by performing no action.

      :param eq: The OWL equivalent classes axiom containing the class expressions to be mapped as mutually equivalent in the RDF graph.
      :type eq: OWLEquivalentClasses

      :return: None, as the method modifies the graph in place.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_equivalent_data_properties(eq: pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties) -> Optional[rdflib.URIRef]

      Maps an OWL equivalent data properties axiom to RDF triples by creating a chain of `owl:equivalentProperty` relationships between the data properties involved. The method iterates through the list of data property expressions provided in the axiom, adding a triple to the graph for each consecutive pair to signify their equivalence. It also handles the mapping of any annotations associated with the axiom, attaching them to the generated triples. This operation modifies the internal graph directly and returns None, performing no action if the list of properties contains fewer than two elements.

      :param eq: The OWL axiom containing the data property expressions that are mutually equivalent.
      :type eq: OWLEquivalentDataProperties

      :return: None, as the method modifies the graph in place to represent the axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_equivalent_object_properties(eq: pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties) -> Optional[rdflib.URIRef]

      This method processes an OWL equivalent object properties axiom by generating RDF triples that represent the equivalence relationships between the specified object properties. It iterates through the list of property expressions, creating an `owl:equivalentProperty` link between each adjacent pair to ensure a complete chain of equivalence. Any annotations associated with the axiom are also mapped and attached to the generated triples. The operation directly modifies the underlying RDF graph and returns None; if the input contains fewer than two properties, no triples are generated.

      :param eq: An OWL axiom asserting the equivalence of a set of object properties. The method extracts the property expressions and annotations from this axiom to generate the corresponding RDF triples.
      :type eq: OWLEquivalentObjectProperties

      :return: None, as the method modifies the graph in place.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_facets(facets: list[pyowl2.data_range.datatype_restriction.OWLFacet]) -> tuple[list[rdflib.URIRef], list[rdflib.URIRef], list[rdflib.URIRef]]

      Converts a list of OWL facet objects into the constituent elements required to construct RDF triples. For each facet in the input list, the method generates a unique blank node to act as the subject, resolves the facet's constraint to a URI reference, and converts the facet's value to a URI reference. The function returns a tuple containing three parallel lists: the generated blank nodes, the constraint URIs, and the value URIs, which correspond to the subjects, predicates, and objects of the intended triples. This method does not modify any external state but relies on the `constraint_to_uriref` and `value.to_uriref` methods of the input objects to perform the conversion, potentially raising exceptions if those methods fail.

      :param facets: A list of OWL facet instances representing data range restrictions, each containing a constraint and a value to be mapped to RDF.
      :type facets: list[OWLFacet]

      :return: A tuple containing three lists of URIRefs corresponding to the input facets: blank node identifiers, constraint URIs, and value URIs.

      :rtype: tuple[list[URIRef], list[URIRef], list[URIRef]]



   .. py:method:: map_owl_functional_property(prop: Union[pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty, pyowl2.axioms.object_property_axiom.functional_object_property.OWLFunctionalObjectProperty]) -> Optional[rdflib.URIRef]

      Maps an OWL functional property, either a data or object property, to RDF triples by asserting its functional characteristic in the graph. The method recursively resolves the IRI of the underlying property expression and adds a triple defining it as an instance of `owl:FunctionalProperty`. It also processes and attaches any annotations associated with the property axiom to the graph. This process directly modifies the internal RDF graph as a side effect. The method returns the IRI of the mapped property, or None if the underlying property expression cannot be resolved.

      :param prop: The OWL functional property instance (data or object) to be converted into RDF triples, containing the property expression and annotations required for the mapping.
      :type prop: typing.Union[OWLFunctionalDataProperty, OWLFunctionalObjectProperty]

      :return: The RDFLib URIRef representing the IRI of the mapped functional property, or None if the property expression cannot be mapped.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_general_class_axiom(axiom: pyowl2.axioms.general.OWLGeneralClassAxiom) -> Optional[rdflib.URIRef]

      This method maps an OWL general class axiom into the RDF graph by creating a reified axiom structure using a blank node. It adds triples to the graph that define this node as an `owl:Axiom`, linking it to the mapped representations of the axiom's left expression, property IRI, and right expression via `owl:annotatedSource`, `owl:annotatedProperty`, and `owl:annotatedTarget` predicates. Furthermore, the method ensures that any annotations attached to the axiom are processed and associated with the generated axiom node. Finally, it returns the blank node that serves as the identifier for this axiom in the graph.

      :param axiom: The OWL general class axiom to be mapped, containing a left expression, a property IRI, a right expression, and any associated annotations.
      :type axiom: OWLGeneralClassAxiom

      :return: The blank node identifier representing the reified OWL general class axiom in the RDF graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_has_key(has_key: pyowl2.axioms.has_key.OWLHasKey) -> Optional[rdflib.URIRef]

      Translates an OWL `HasKey` axiom into corresponding RDF triples within the graph. The method processes the class expression and the associated object and data property expressions, converting them into IRIs and organizing the properties into an RDF collection. It then asserts a triple linking the class to the `owl:hasKey` property with the collection as the object, and handles any associated axiom annotations. As a side effect, the graph is modified, and the method returns None.

      :param has_key: The OWLHasKey axiom to be mapped to RDF, defining a key for a class expression via a set of object and data property expressions.
      :type has_key: OWLHasKey

      :return: None, as the method modifies the graph in-place and does not return a reference to the created axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_inverse_functional_property(prop: pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty) -> Optional[rdflib.URIRef]

      This method converts an OWL inverse functional property axiom into RDF triples by asserting the specific property type in the graph. It first resolves the IRI of the underlying object property expression and then adds a triple declaring that this property is an instance of `owl:InverseFunctionalProperty`. Any annotations attached to the axiom are also mapped and added to the graph. The function returns the IRI of the property, which may be None if the mapping of the underlying object property expression fails.

      :param prop: The OWL inverse functional object property to be mapped to RDF triples, containing the property expression and annotations.
      :type prop: OWLInverseFunctionalObjectProperty

      :return: The IRI of the object property that was asserted to be an inverse functional property in the RDF graph, or None if the property expression could not be mapped.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_inverse_object_properties(prop: pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties) -> Optional[rdflib.URIRef]

      Maps an OWL Inverse Object Properties axiom to the RDF graph by asserting that two object properties are inverses of one another. The method resolves the property expressions from the axiom into IRIs and adds a triple to the graph using the `owl:inverseOf` predicate to link them. This process modifies the internal graph state and returns a blank node identifier.

      :param prop: The OWL axiom representing the inverse relationship between two object property expressions, which will be mapped to RDF triples.
      :type prop: OWLInverseObjectProperties

      :return: A Blank Node (BNode) representing the OWL inverse object properties axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_irreflexive_property(prop: pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty) -> Optional[rdflib.URIRef]

      This method maps an OWL Irreflexive Object Property axiom to its corresponding RDF representation within the graph. It resolves the IRI of the underlying object property expression and adds a triple asserting that this property is an instance of `owl:IrreflexiveProperty`. Additionally, the method processes and attaches any annotations associated with the axiom to the graph. As a side effect, the internal RDF graph is modified with these new triples. The method returns the IRI of the mapped property, or None if the underlying property expression cannot be successfully mapped.

      :param prop: The OWL irreflexive object property axiom to be mapped to RDF, containing the property expression and associated annotations.
      :type prop: OWLIrreflexiveObjectProperty

      :return: The IRI of the object property that was mapped and asserted as an irreflexive property in the RDF graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_named_individual(individual: pyowl2.individual.named_individual.OWLNamedIndividual) -> Optional[rdflib.URIRef]

      Maps an OWL named individual to the RDF graph by converting its IRI into a URIRef and asserting its type. The method retrieves the individual's IRI, transforms it into an RDFLib URIRef, and adds a triple to the internal graph stating that the node is an instance of `owl:NamedIndividual`. This process modifies the graph state as a side effect. The function returns the generated URIRef, which serves as the concrete identifier for the individual within the RDF structure, or None if the IRI mapping fails.

      :param individual: The OWL named individual to be mapped to the RDF graph. It represents a specific instance in the ontology identified by an IRI.
      :type individual: OWLNamedIndividual

      :return: The RDFLib URIRef representing the mapped individual, or None if the individual's IRI cannot be mapped.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_negative_data_property_assertion(assertion: pyowl2.axioms.assertion.OWLNegativeDataPropertyAssertion) -> Optional[rdflib.URIRef]

      This method transforms an OWL negative data property assertion axiom into a reified RDF structure within the graph. It extracts the source individual, data property expression, and target literal value from the input assertion, mapping them to their corresponding RDF representations. A blank node is created to serve as the subject of the reified statement, typed as `owl:NegativePropertyAssertion`, and connected to the mapped components via `owl:sourceIndividual`, `owl:assertionProperty`, and `owl:targetValue` predicates. Any annotations attached to the axiom are also applied to this node. The process modifies the graph by adding these triples and returns the blank node identifier for the newly created assertion.

      :param assertion: The negative data property assertion axiom to be mapped to the RDF graph, consisting of a source individual, a data property expression, and a target literal value that the individual does not possess.
      :type assertion: OWLNegativeDataPropertyAssertion

      :return:

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_negative_object_property_assertion(assertion: pyowl2.axioms.assertion.OWLNegativeObjectPropertyAssertion) -> Optional[rdflib.URIRef]

      This method transforms an OWL negative object property assertion axiom into a corresponding RDF structure within the graph. It creates a blank node to represent the assertion and populates the graph with triples linking this node to the source individual, the object property expression, and the target individual using the standard OWL vocabulary. Furthermore, the method handles any annotations attached to the axiom by mapping them to the blank node. As a side effect, it modifies the internal graph by adding these triples and returns the blank node identifier for the assertion.

      :param assertion: The negative object property assertion axiom to be mapped, consisting of a source individual, an object property expression, and a target individual.
      :type assertion: OWLNegativeObjectPropertyAssertion

      :return: The blank node identifier representing the negative object property assertion axiom in the RDF graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_all_values_from(prop: pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom) -> Optional[rdflib.URIRef]

      This method maps an OWL object all-values-from restriction to its RDF representation by generating a blank node and populating the graph with the necessary triples. It recursively resolves the object property expression and class expression contained within the input axiom to obtain their RDF identifiers. These identifiers are then used to assert that the blank node is an `owl:Restriction` with a specific `owl:onProperty` and `owl:allValuesFrom` constraint. The method returns the blank node identifier, serving as the subject for the newly created restriction structure.

      :param prop: An OWL class expression representing an ObjectAllValuesFrom restriction, which defines that all values of a specific object property must belong to a given class expression.
      :type prop: OWLObjectAllValuesFrom

      :return: The Blank Node identifier of the OWL restriction created in the graph representing the all-values-from axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_complement_of(prop: pyowl2.class_expression.object_complement_of.OWLObjectComplementOf) -> Optional[rdflib.URIRef]

      This method maps an OWL object complement-of axiom to RDF triples by creating a blank node to represent the complement class. It recursively processes the nested class expression to obtain its IRI and then adds triples to the graph, defining the blank node as an `owl:Class` and linking it to the nested expression via the `owl:complementOf` property. As a side effect, this method mutates the internal graph with these new triples and returns the blank node identifier representing the complement class.

      :param prop: The OWL object complement-of class expression to be serialized into the RDF graph. It encapsulates the operand class expression that defines the complement.
      :type prop: OWLObjectComplementOf

      :return: The blank node identifier representing the complement class added to the RDF graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_exact_cardinality(prop: pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality) -> Optional[rdflib.URIRef]

      Maps an OWL object exact cardinality restriction to an equivalent set of RDF triples within the graph. The method instantiates a blank node to represent the restriction and adds triples declaring it as an `owl:Restriction` linked to the specified object property via `owl:onProperty`. It handles both qualified and unqualified restrictions by using `owl:qualifiedCardinality` and `owl:onClass` when a class expression is present, or `owl:cardinality` when it is absent. The process modifies the graph directly and returns the blank node identifier for the created restriction.

      :param prop: The OWL exact cardinality restriction to be mapped to RDF triples, specifying the object property, the exact number of relationships, and an optional class expression.
      :type prop: OWLObjectExactCardinality

      :return: The URIRef (specifically a blank node) identifying the restriction node created in the graph to represent the exact cardinality axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_has_self(prop: pyowl2.class_expression.object_has_self.OWLObjectHasSelf) -> Optional[rdflib.URIRef]

      Converts an OWL object has-self axiom into an RDF representation by creating a blank node representing an `owl:Restriction`. It retrieves the IRI of the associated object property expression and adds triples to the graph defining the restriction's type, the property it applies to via `owl:onProperty`, and the `owl:hasSelf` condition set to a literal boolean true. This method modifies the underlying graph directly and returns the blank node identifier for the newly created restriction.

      :param prop: The has-self axiom to be mapped, containing the object property expression required to generate the RDF restriction.
      :type prop: OWLObjectHasSelf

      :return: The blank node identifier representing the OWL restriction created in the graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_has_value(prop: pyowl2.class_expression.object_has_value.OWLObjectHasValue) -> Optional[rdflib.URIRef]

      This method translates an OWL object has-value restriction into RDF triples within the graph. It creates a blank node to serve as the subject of the restriction, then maps the constituent object property expression and individual to their RDF equivalents. The resulting triples assert that this blank node is an `owl:Restriction` defined by a specific `owl:onProperty` and `owl:hasValue`. As a side effect, these triples are added directly to the graph, and the blank node identifier is returned to reference the newly created restriction.

      :param prop: The OWL object has-value restriction to be mapped, consisting of an object property expression and a specific individual filler.
      :type prop: OWLObjectHasValue

      :return: The subject node (URIRef or BNode) of the OWL restriction added to the graph, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_intersection_of(prop: pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf) -> Optional[rdflib.URIRef]

      This method maps an OWL object intersection-of axiom to an RDF representation by creating a blank node to represent the intersection class. It processes the constituent class expressions by mapping them into a sequence and linking this sequence to the blank node via the `owl:intersectionOf` property, utilizing an RDF Collection to store the operands. The operation modifies the internal RDF graph by adding the necessary triples to define the class and its structure. Finally, the method returns the blank node identifier for the intersection class, which serves as the reference for this complex class definition.

      :param prop: The OWL class expression representing an intersection of a set of class expressions to be mapped to RDF triples.
      :type prop: OWLObjectIntersectionOf

      :return: The blank node identifier representing the OWL object intersection class in the RDF graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_inverse_of(prop: pyowl2.expressions.OWLInverseObjectProperty) -> Optional[rdflib.URIRef]

      Maps an OWL inverse object property axiom to its corresponding RDF representation within the graph. The method generates a blank node to serve as the subject of the inverse relationship and recursively maps the underlying object property to an RDF node. It then adds a triple to the graph using the `owl:inverseOf` predicate to link the blank node to the mapped property. The function returns the blank node representing the inverse property expression, modifying the graph as a side effect.

      :param prop: The OWL inverse object property axiom to be mapped to RDF triples.
      :type prop: OWLInverseObjectProperty

      :return: The blank node representing the inverse property axiom in the RDF graph, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_max_cardinality(prop: pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality) -> Optional[rdflib.URIRef]

      This method translates an OWL object max cardinality restriction into RDF triples within the graph. It creates a blank node to represent the restriction and asserts it is an instance of `owl:Restriction`. The method maps the associated object property expression and links it using `owl:onProperty`, then sets the cardinality limit using `owl:maxCardinality` or `owl:maxQualifiedCardinality` depending on whether a class expression is present. If a class expression is provided, it is mapped and linked via `owl:onClass` to define a qualified restriction. The method returns the blank node identifier for the newly created restriction.

      :param prop: The OWL object max cardinality restriction to be mapped to the RDF graph, encapsulating the object property, the maximum cardinality value, and an optional class expression.
      :type prop: OWLObjectMaxCardinality

      :return: The blank node identifier of the restriction node created in the graph to represent the max cardinality axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_min_cardinality(prop: pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality) -> Optional[rdflib.URIRef]

      This method translates an OWL object minimum cardinality restriction into an RDF representation by adding triples to the internal graph. It creates a blank node to serve as the subject of the restriction and maps the provided object property expression to define the property being constrained. If the input includes a specific class expression, the method uses `owl:minQualifiedCardinality` and links the restriction to that class via `owl:onClass`; otherwise, it uses the standard `owl:minCardinality`. The cardinality value is added as a typed literal, and the blank node identifier is returned to reference the newly created restriction structure.

      :param prop: The OWL object min cardinality expression to be mapped to RDF triples, containing the object property, minimum cardinality value, and an optional class expression.
      :type prop: OWLObjectMinCardinality

      :return: The blank node representing the OWL restriction added to the graph to encode the minimum cardinality constraint.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_one_of(prop: pyowl2.class_expression.object_one_of.OWLObjectOneOf) -> Optional[rdflib.URIRef]

      Converts an OWL ObjectOneOf axiom into an equivalent RDF structure by creating a blank node to represent the enumerated class. It processes the set of individuals associated with the axiom, mapping them into an RDF collection sequence, and adds triples to the graph to define the blank node as an `owl:Class` linked to this collection via the `owl:oneOf` property. This operation modifies the underlying graph as a side effect and returns the URI reference of the generated blank node, which serves as the subject for the newly created class definition.

      :param prop: The class expression representing an enumeration of individuals to be mapped to an RDF collection.
      :type prop: OWLObjectOneOf

      :return: The blank node representing the anonymous OWL class defined by the object one-of axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_property(prop: pyowl2.expressions.object_property.OWLObjectProperty) -> Optional[rdflib.URIRef]

      Processes an OWL object property to generate its RDF representation within the graph. It delegates the creation of the property's URI reference to the generic mapping logic and then explicitly adds a triple asserting that this node is of type `owl:ObjectProperty`. This method modifies the internal graph by adding this type declaration and returns the URI reference associated with the property.

      :param prop: The OWL object property to be mapped to RDF triples. It represents a property relationship in the ontology and provides the IRI used to identify the property in the graph.
      :type prop: OWLObjectProperty

      :return: The RDFLib URIRef representing the mapped OWL object property in the graph, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_property_assertion(assertion: pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion) -> Optional[rdflib.URIRef]

      Converts an OWL object property assertion axiom into RDF triples and adds them to the internal graph. The method resolves the source individual, object property expression, and target individual to their corresponding IRIs. It specifically handles inverse object properties by swapping the subject and object positions in the generated triple to ensure correct semantic representation. Additionally, any annotations associated with the axiom are processed and linked to the newly created triple. This operation modifies the graph directly and returns None.

      :param assertion: The OWL axiom representing a relationship between a source individual and a target individual via an object property expression, to be converted into RDF triples.
      :type assertion: OWLObjectPropertyAssertion

      :return: None, as the assertion is added directly to the graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_property_domain(domain: pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain) -> Optional[rdflib.URIRef]

      Translates an OWL Object Property Domain axiom into an RDF triple representation within the mapper's internal graph. The method resolves the object property expression and the class expression from the input axiom into RDF nodes, then establishes a relationship between them using the `RDFS.domain` predicate. Additionally, it processes and maps any annotations associated with the axiom to the graph. As a side effect, this method mutates the graph by adding the domain assertion and any annotation triples. It returns the URI reference corresponding to the object property, or None if the property expression cannot be successfully mapped.

      :param domain: The OWL axiom specifying the class expression that constitutes the domain of an object property expression.
      :type domain: OWLObjectPropertyDomain

      :return: The URI reference of the object property expression that serves as the subject of the domain restriction triple, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_property_range(range: pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange) -> Optional[rdflib.URIRef]

      This method maps an OWL Object Property Range axiom to an RDF triple within the internal graph. It resolves the object property expression and the class expression from the input, creating a triple that asserts the property has the specified class as its range using the `rdfs:range` predicate. The method also handles the mapping of any annotations attached to the axiom. It returns the URI reference of the object property node, or None if the mapping of the property expression fails.

      :param range: The OWL object property range axiom to be mapped, containing the object property expression and the class expression that defines its range.
      :type range: OWLObjectPropertyRange

      :return: The URI reference of the object property expression that serves as the subject of the range assertion.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_some_values_from(prop: pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom) -> Optional[rdflib.URIRef]

      This method translates an OWL object some-values-from restriction into an RDF representation by creating a blank node to represent the anonymous restriction class. It adds triples to the graph to define this node as an `owl:Restriction`, linking it to the mapped object property via `owl:onProperty` and the mapped class expression via `owl:someValuesFrom`. The method modifies the internal graph state as a side effect and returns the blank node identifier for the restriction.

      :param prop: Represents an OWL existential restriction consisting of an object property expression and a class expression, defining a class of individuals that have at least one relationship via the property to an instance of the specified class.
      :type prop: OWLObjectSomeValuesFrom

      :return: The blank node identifier representing the `owl:Restriction` created in the graph, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_object_union_of(prop: pyowl2.class_expression.object_union_of.OWLObjectUnionOf) -> Optional[rdflib.URIRef]

      Converts an OWL object union-of axiom into an RDF representation by generating a blank node to represent the anonymous class defined by the union. The method processes the constituent class expressions into an RDF collection and adds triples to the graph to establish the blank node as an `owl:Class` linked to this collection via the `owl:unionOf` property. This operation directly modifies the underlying graph structure and returns the blank node identifier that serves as the subject for the union class.

      :param prop: The OWL object union-of class expression containing the set of class expressions to be mapped to RDF.
      :type prop: OWLObjectUnionOf

      :return: The blank node (BNode) representing the OWL union class in the RDF graph, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_reflexive_property(prop: pyowl2.axioms.object_property_axiom.reflexive_object_property.OWLReflexiveObjectProperty) -> Optional[rdflib.URIRef]

      This method maps an OWL reflexive object property axiom to the underlying RDF graph by generating the necessary triples. It first resolves the IRI of the underlying object property expression and then asserts that this property is an instance of `owl:ReflexiveProperty`. The method also handles any annotations associated with the axiom, mapping them to the graph. It returns the IRI of the mapped property, or None if the underlying property expression fails to map.

      :param prop: The OWL reflexive object property axiom to be mapped to RDF triples, containing the property expression and associated annotations.
      :type prop: OWLReflexiveObjectProperty

      :return: The IRI of the object property mapped as a reflexive property, or None if the mapping fails.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_same_individual(same: pyowl2.axioms.assertion.OWLSameIndividual) -> Optional[rdflib.URIRef]

      Converts an OWL same individual axiom into a series of RDF triples within the graph. The method processes the set of individual expressions contained in the axiom, mapping them to their corresponding RDF IRIs. It then establishes a chain of equivalence relationships by adding `owl:sameAs` triples between consecutive individuals in the sequence. Additionally, any annotations associated with the axiom are attached to these generated triples. This operation directly modifies the internal graph structure and returns None.

      :param same: The OWL same individual axiom to be mapped, consisting of a set of individual expressions that will be linked via `owl:sameAs` relationships in the graph, including any associated annotations.
      :type same: OWLSameIndividual

      :return: None, as the method modifies the graph in place by adding the same individual triples.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_sub_annotation_property_of(prop: pyowl2.axioms.annotations.OWLSubAnnotationPropertyOf) -> Optional[rdflib.URIRef]

      Maps an OWL sub-annotation property axiom to RDF triples by asserting a hierarchical relationship between two annotation properties. It extracts the sub-property and super-property from the input axiom, converts them to IRIs, and adds a triple to the graph using the `rdfs:subPropertyOf` predicate. The method also processes and adds any annotations associated with the axiom itself. This process modifies the internal graph structure as a side effect and returns None.

      :param prop: The OWL sub-annotation property axiom to be mapped to RDF triples, defining a relationship where one annotation property is a subproperty of another.
      :type prop: OWLSubAnnotationPropertyOf

      :return: None, as the method modifies the graph in place.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_subclass_of(subclass: pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf) -> Optional[rdflib.URIRef]

      Translates an OWL subclass axiom into RDF triples and adds them to the internal graph. The method resolves the subclass and superclass expressions into their corresponding IRIs and asserts a relationship using the `rdfs:subClassOf` predicate. It also processes any annotations associated with the axiom, linking them to the generated triple structure. This operation modifies the graph directly as a side effect and returns None.

      :param subclass: The OWL subclass axiom to be mapped to the RDF graph, containing the sub-class and super-class expressions that define the relationship along with any associated annotations.
      :type subclass: OWLSubClassOf

      :return: None, as the method modifies the graph in place and does not return a reference to the created axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_subdata_property_of(subdata: pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf) -> Optional[rdflib.URIRef]

      Maps an OWL subdata property axiom to the internal RDF graph by establishing a hierarchical relationship between data properties. The method resolves the sub-property and super-property expressions to their corresponding IRIs and adds a triple using the `rdfs:subPropertyOf` predicate to represent the axiom. It also processes and attaches any annotations associated with the axiom to the graph. This operation modifies the graph as a side effect and returns None.

      :param subdata: The OWL axiom defining a subdata property relationship, containing the sub-property, super-property, and associated annotations. It is used to generate the corresponding `rdfs:subPropertyOf` triple and map annotations to the graph.
      :type subdata: OWLSubDataPropertyOf

      :return: Returns None, as the mapping is performed by adding triples directly to the graph.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_subobject_property_of(subclass: pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf) -> Optional[rdflib.URIRef]

      This method maps an OWL sub-object property axiom to RDF triples within the graph, handling both standard sub-property relationships and property chains. When the sub-property is a chain, it generates an RDF collection representing the sequence and connects the super-property via `owl:propertyChainAxiom`; for simple properties, it creates a direct `rdfs:subPropertyOf` assertion. The method also serializes any axiom annotations, resulting in direct modifications to the graph state.

      :param subclass: An OWL axiom asserting that one object property is a subproperty of another, containing the sub-property and super-property expressions along with any annotations to be mapped to the RDF graph.
      :type subclass: OWLSubObjectPropertyOf

      :return: None, as the method modifies the graph in place to add the subobject property axiom.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_symmetric_property(prop: pyowl2.axioms.object_property_axiom.symmetric_object_property.OWLSymmetricObjectProperty) -> Optional[rdflib.URIRef]

      Converts an OWL symmetric object property axiom into its corresponding RDF representation within the mapper's graph. It resolves the IRI of the underlying object property expression and adds a triple declaring it as an instance of `owl:SymmetricProperty`. Any annotations associated with the axiom are also processed and linked to the property. The function returns the URI reference of the property, or None if the underlying expression mapping fails.

      :param prop: The OWL symmetric object property to be mapped to RDF triples, containing the property expression and annotations to be serialized.
      :type prop: OWLSymmetricObjectProperty

      :return: The IRI of the symmetric property in the RDF graph, or None if the property expression cannot be mapped.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_owl_transitive_property(prop: pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty) -> Optional[rdflib.URIRef]

      Converts an OWL transitive object property axiom into its corresponding RDF representation within the mapper's graph. It first resolves the IRI of the underlying object property expression and then asserts that this property is an instance of `owl:TransitiveProperty` by adding a specific triple to the graph. Additionally, the method processes and maps any annotations associated with the axiom. It returns the IRI of the mapped property, or None if the underlying property expression cannot be successfully mapped.

      :param prop: The OWL transitive object property to be mapped, including its object property expression and axiom annotations.
      :type prop: OWLTransitiveObjectProperty

      :return: The IRI of the transitive property as a URIRef, or None if the property expression cannot be mapped.

      :rtype: typing.Optional[URIRef]



   .. py:method:: map_sequence(sequence: Iterable[Any]) -> list[tuple[rdflib.URIRef, Ellipsis]]

      This method processes an iterable of OWL entities or expressions, converting each element into its corresponding RDF representation by delegating to the `map` method. The specific return value depends on the size of the input sequence: if the sequence is empty or None, the method returns `RDF.nil` to represent an empty RDF collection. If the sequence contains exactly one element, the method returns the mapped result of that element directly, rather than wrapping it in a list. For sequences containing multiple elements, the method returns a list of mapped results, preserving the order of the original input.

      :param sequence: An iterable of OWL entities or expressions to be mapped to RDFLib URIRefs. An empty or None input results in RDF.nil.
      :type sequence: typing.Iterable[typing.Any]

      :return: A list of mapped RDFLib URIRefs corresponding to the input OWL entities or expressions. Returns RDF.nil if the input sequence is empty, or the mapped element directly if the sequence contains a single item.

      :rtype: list[tuple[URIRef, ...]]



   .. py:attribute:: _graph
      :type:  rdflib.Graph


   .. py:attribute:: _owl1_annotations
      :type:  bool
      :value: False



   .. py:property:: graph
      :type: rdflib.Graph


      Returns the underlying RDF graph instance associated with the mapper. This property provides direct access to the internal `_graph` attribute, which serves as the primary data structure for storing and manipulating RDF triples. Because the actual graph object is returned rather than a copy, any modifications made to the returned instance will directly alter the state of the mapper.

      :return: The Graph object associated with this instance.

      :rtype: Graph


   .. py:property:: owl1_annotations
      :type: bool


      This property indicates whether the RDF/XML mapper is configured to handle annotations according to the OWL 1 specification. It acts as a read-only accessor for the internal `_owl1_annotations` flag, returning a boolean value that determines the specific annotation semantics used during mapping operations. Since this is a property getter, it does not modify the state of the mapper.

      :return: True if OWL 1 annotations are enabled, False otherwise.

      :rtype: bool


.. py:function:: example_usage()

   Provides a comprehensive demonstration of the `RDFXMLMapper` class by constructing a sample OWL ontology and serializing it into RDF triples. The function initializes an `owlready2` environment, defines a custom namespace, and instantiates various OWL entities such as classes, named individuals, object properties, and annotations. These entities are then mapped to an RDF graph using the mapper's methods. As a side effect, the function prints the resulting graph to standard output in Turtle format and writes the ontology to a local file named 'test.owl' in RDF/XML format.

