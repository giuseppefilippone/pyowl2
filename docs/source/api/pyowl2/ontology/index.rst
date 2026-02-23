pyowl2.ontology
===============

.. py:module:: pyowl2.ontology



.. ── LLM-GENERATED DESCRIPTION START ──

A comprehensive interface for creating, loading, and manipulating OWL ontologies by wrapping the Owlready2 library to manage entities, axioms, and annotations.


Description
-----------


The software serves as a high-level abstraction over the Owlready2 library, enabling the creation, loading, and modification of Web Ontology Language (OWL) structures. It manages the lifecycle of an ontology by initializing a specific "World" context, which can either generate a new knowledge base from a base IRI or load an existing structure from a file path. To facilitate the manipulation of logical entities, the implementation delegates the translation of high-level objects—such as classes, properties, and individuals—into RDF triples using an internal mapping component. This mapping process includes specialized logic to decompose complex entities into their constituent declarations, domains, ranges, and nested axioms, ensuring that the underlying graph accurately reflects the intended semantic relationships. Beyond logical axioms, the system supports the attachment of metadata annotations to the ontology itself, specific elements, or individual relations, thereby enriching the knowledge base with descriptive details. Finally, the interface provides mechanisms for querying specific axiom types and serializing the complete graph to various file formats, ensuring that the data can be persisted and shared.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.ontology.OWLOntology


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_ontology_OWLOntology.png
       :alt: UML Class Diagram for OWLOntology
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLOntology**

.. only:: latex

    .. figure:: /_uml/pyowl2_ontology_OWLOntology.pdf
       :alt: UML Class Diagram for OWLOntology
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLOntology**

.. py:class:: OWLOntology(base_iri: Union[pyowl2.base.iri.IRI, rdflib.URIRef], ontology_path: Optional[str] = None, OWL1_annotations: bool = False)

   This class provides a comprehensive interface for creating, manipulating, and persisting OWL (Web Ontology Language) ontologies. It acts as a central container for knowledge representation, managing entities such as classes, properties, individuals, and the axioms that define their logical relationships. Users can initialize the instance with a base IRI to create a new ontology or provide a file path to load an existing one. The class facilitates the addition of complex logical structures through methods that handle declarations, domains, ranges, and nested axioms, while also offering robust capabilities for attaching metadata annotations to the ontology itself, specific elements, or individual relations. Internally, it utilizes mapping and retrieval components to translate high-level objects into RDF/XML and query the underlying graph, ultimately supporting the export of the ontology to various file formats.

   :parm ontology_iri: The Internationalized Resource Identifier (IRI) that uniquely identifies the ontology. It serves as the base IRI for the namespace and is used to retrieve or create the ontology instance within the underlying world.
   :type ontology_iri: typing.Optional[URIRef]
   :parm axioms: A list of axioms that define the logical statements and relationships within the ontology.
   :type axioms: list[OWLAxiom]
   :parm ontology_annotations: Internal storage for the list of annotations providing metadata about the ontology itself, such as creator, version, or other descriptive details.
   :type ontology_annotations: typing.Optional[list[OWLAnnotation]]
   :parm world: The World instance that manages the ontology's context and provides access to the underlying RDF graph.
   :type world: World
   :parm ontology: The underlying ontology instance managed by the World object, serving as the core data structure for storing, loading, and persisting the ontology's contents.
   :type ontology: Ontology
   :parm clear: An instance used to clear the ontology's content during initialization, ensuring a clean state for newly created ontologies.
   :type clear: RDFXMLClear
   :parm mapper: Internal component that maps OWL axioms and annotations to the underlying RDF graph, enabling the translation of high-level ontology constructs into a storable format.
   :type mapper: RDFXMLMapper
   :parm getter: Responsible for retrieving axioms and annotations from the ontology, providing methods to query and extract specific elements based on various criteria.
   :type getter: RDFXMLGetter


   .. py:method:: add_annotation(annotation: pyowl2.base.annotation.OWLAnnotation) -> bool

      Associates a single metadata annotation with the ontology by wrapping the bulk addition method. It accepts an `OWLAnnotation` object representing the metadata to be attached and attempts to persist it within the ontology structure. The operation returns a boolean value indicating success; it yields True if the annotation is successfully integrated, and False if the underlying process encounters an exception or mapping error. This method modifies the ontology's state by adding the specified annotation to its collection of annotations.

      :param annotation: Metadata to be added to the ontology.
      :type annotation: OWLAnnotation

      :return: True if the annotation was successfully added to the ontology, False if an error occurred.

      :rtype: bool



   .. py:method:: add_annotation_to_element(element: pyowl2.abstracts.object.OWLObject, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]])

      This method attaches a list of metadata annotations to a specific ontology element, such as a class, property, or individual, thereby enriching the element's documentation. The operation is performed within a managed context to ensure the integrity of the underlying ontology structure while the internal mapper applies the changes. It returns True if the annotations are successfully added; if an exception occurs during the mapping or attachment process, the error is printed to standard output and the method returns False.

      :param element: The target ontology entity or axiom to which the annotations will be attached.
      :type element: OWLObject
      :param annotations: A list of OWLAnnotation objects representing the metadata to associate with the element, or None.
      :type annotations: typing.Optional[list[OWLAnnotation]]



   .. py:method:: add_annotations(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]]) -> bool

      Associates a collection of metadata annotations with the ontology by delegating the mapping process to an internal mapper object. The operation is performed within a context manager to ensure proper resource handling during the modification. Upon successful completion, the method returns True; conversely, if any exception is raised during the mapping process, the error is printed to standard output and the method returns False.

      :param annotations: A list of OWLAnnotation objects representing metadata to be added to the ontology. Can be None.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: True if the annotations were successfully added to the ontology, False if an error occurred during the process.

      :rtype: bool



   .. py:method:: add_annotations_to_relation(a: Any, property: Any, b: Any, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]]) -> bool

      This method attaches a list of OWLAnnotation objects to a specific relation defined by the subject `a`, predicate `property`, and object `b` within the ontology. It delegates the actual mapping to the ontology's mapper, operating within a context manager to ensure safe modification of the ontology state. The function returns a boolean indicating success; if an exception occurs during the process, the error is printed to standard output and the method returns False.

      :param a: The subject of the relation to be annotated. Used in conjunction with the property and object to identify the specific relation within the ontology.
      :type a: typing.Any
      :param property: The predicate of the relation, acting as the property that links the subject to the object to identify the specific triple for annotation.
      :type property: typing.Any
      :param b: The object of the relation to which the annotations should be added, used to identify the specific relation alongside the subject and predicate.
      :type b: typing.Any
      :param annotations: A list of OWLAnnotation objects representing the metadata to be attached to the specified relation.
      :type annotations: typing.Optional[list[OWLAnnotation]]

      :return: True if the annotations were successfully added to the relation, False if an error occurred during the process.

      :rtype: bool



   .. py:method:: add_axiom(axiom: Any) -> bool

      Adds a logical axiom to the ontology by delegating the mapping process to the internal mapper object. This operation is performed within a context manager to ensure the underlying ontology resource is managed correctly during the modification. The method returns True to indicate the completion of the operation, but if the mapper fails to process the axiom, an exception will be raised, as the implementation does not include explicit error handling to return False.

      :param axiom: The logical construct or statement to be added to the ontology, such as a class or property assertion.
      :type axiom: typing.Any

      :return: True, indicating that the axiom was successfully added to the ontology.

      :rtype: bool



   .. py:method:: add_axioms(axioms: list[pyowl2.abstracts.object.OWLObject]) -> bool

      Adds a list of axioms to the ontology by iterating through the provided collection and mapping each logical statement to the underlying structure. The method performs specialized processing for complex entity types—specifically object properties, data properties, classes, data ranges, and individuals—by decomposing them into their constituent parts, including declarations, annotations, domains, ranges, and any associated inner axioms. Axioms that do not match these specific types are mapped directly without decomposition. Each addition operation is wrapped in a context manager to ensure the ontology is properly managed during the modification process. The method returns True upon successfully processing the entire list, though it does not currently handle exceptions internally and will propagate errors if mapping fails.

      :param axioms: A list of OWLObject instances representing logical statements to be added to the ontology. The method processes specific types—including object properties, data properties, classes, data ranges, and individuals—by mapping their declarations, domains, ranges, and inner axioms, while mapping other types directly.
      :type axioms: list[OWLObject]

      :return: True if all axioms were successfully added to the ontology.

      :rtype: bool



   .. py:method:: get_axioms(axiom: pyowl2.getter.rdf_xml_getter.AxiomsType) -> list[pyowl2.abstracts.object.OWLObject]

      Retrieves a list of axioms from the ontology that match the specified type, enabling targeted queries of the ontology's logical content. The method accepts an `AxiomsType` enumeration value to filter the results, returning a collection of `OWLObject` instances representing the requested axioms. Internally, the retrieval logic is delegated to the ontology's underlying getter, and the method returns an empty list if no matching axioms are found or if an error occurs during the operation.

      :param axiom: Specifies the category of axiom to retrieve from the ontology, acting as a filter to return only OWL objects matching the selected logical construct type.
      :type axiom: AxiomsType

      :return: A list of OWL objects representing the axioms of the specified type retrieved from the ontology. Returns an empty list if no matching axioms are found or if an error occurs during retrieval.

      :rtype: list[OWLObject]



   .. py:method:: print_all() -> None

      Iterates through every axiom type defined in the `AxiomsType` enumeration, retrieves the corresponding axioms from the ontology, and prints them to the console. The method uses a context manager to ensure the ontology resource is properly managed while accessing the data. For each axiom category, it prints the type name followed by the specific results retrieved via the internal getter, providing a comprehensive text-based overview of the ontology's structure and contents. This operation produces side effects by writing to standard output and depends on the successful retrieval of data for each enumerated type.



   .. py:method:: save(filepath: str, format: str = 'rdfxml') -> bool

      Persists the current state of the ontology to a file at the specified path, serializing the data according to the given format (defaulting to RDF/XML). This method delegates the actual file writing operation to the underlying ontology object. Upon success, it returns True; if an error occurs—such as an invalid path, insufficient write permissions, or an unsupported format—the exception is caught, the error message is printed to standard output, and the method returns False without propagating the exception.

      :param filepath: The destination file system path where the ontology will be written.
      :type filepath: str
      :param format: The serialization format for the ontology file (e.g., "rdfxml", "turtle").
      :type format: str

      :return: True if the ontology was successfully saved to the specified file, False if an error occurred during the operation.

      :rtype: bool



   .. py:attribute:: _axioms
      :type:  list[pyowl2.abstracts.axiom.OWLAxiom]
      :value: None



   .. py:attribute:: _getter
      :type:  pyowl2.getter.rdf_xml_getter.RDFXMLGetter


   .. py:attribute:: _mapper
      :type:  pyowl2.mapper.rdf_xml_mapper.RDFXMLMapper


   .. py:attribute:: _ontology_annotations
      :type:  Optional[list[pyowl2.base.annotation.OWLAnnotation]]
      :value: None



   .. py:attribute:: _ontology_iri
      :type:  Optional[rdflib.URIRef]


   .. py:attribute:: _world
      :type:  owlready2.World


   .. py:property:: axioms
      :type: list[pyowl2.abstracts.axiom.OWLAxiom]


      Replaces the current collection of axioms associated with this ontology with the provided list of OWLAxiom instances. This setter performs a direct assignment to the internal storage, effectively discarding any previously held axioms without performing validation or deep copying. Consequently, the ontology's state is immediately updated to reflect the new set of axioms.

      :param value: The axioms to assign to the object.
      :type value: list[OWLAxiom]


   .. py:property:: getter
      :type: pyowl2.getter.rdf_xml_getter.RDFXMLGetter


      Returns the `RDFXMLGetter` instance associated with this ontology. This property provides access to the internal component responsible for handling RDF/XML data retrieval or parsing. It exposes the value of the private `_getter` attribute without modifying the state of the ontology.

      :return: The `RDFXMLGetter` instance associated with this object.

      :rtype: RDFXMLGetter


   .. py:property:: mapper
      :type: pyowl2.mapper.rdf_xml_mapper.RDFXMLMapper


      Returns the RDFXMLMapper instance associated with this ontology. This mapper is responsible for handling the conversion between the ontology's internal object representation and the RDF/XML serialization format. Accessing this property has no side effects and simply retrieves the pre-configured mapper object.

      :return: The RDFXMLMapper instance associated with this object.

      :rtype: RDFXMLMapper


   .. py:property:: namespace
      :type: rdflib.Namespace


      Retrieves the `Namespace` object corresponding to the ontology's IRI. This property provides access to the namespace context by delegating to the underlying ontology handler, allowing for the generation and management of identifiers relative to the ontology's base IRI.

      :return: The Namespace object associated with the ontology IRI.

      :rtype: Namespace


   .. py:property:: ontology_annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]


      Replaces the current collection of annotations associated with the ontology with the provided list. This method acts as the setter for the `ontology_annotations` property, allowing direct assignment of a list of `OWLAnnotation` objects to the underlying private attribute. Note that this operation overwrites any existing annotations rather than appending to them.

      :param value: A list of OWL annotations to assign to the ontology.
      :type value: list[OWLAnnotation]


   .. py:property:: ontology_iri
      :type: Optional[rdflib.URIRef]


      Sets the Internationalized Resource Identifier (IRI) for the ontology, effectively updating its primary identifier. This method accepts a `URIRef` object or `None`, assigning the value to the internal `_ontology_iri` attribute. If `None` is provided, the ontology IRI is cleared; otherwise, it is replaced with the specified URI reference.

      :param value: The Internationalized Resource Identifier (IRI) to assign to the ontology.
      :type value: typing.Optional[URIRef]

