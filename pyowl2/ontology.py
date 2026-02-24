import typing

from owlready2 import Ontology, World
from rdflib import Namespace, URIRef

from pyowl2.abstracts.axiom import OWLAxiom
from pyowl2.abstracts.object import OWLObject
from pyowl2.axioms.declaration import OWLDeclaration
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.iri import IRI
from pyowl2.getter.rdf_xml_clear import RDFXMLClear
from pyowl2.getter.rdf_xml_getter import AxiomsType, RDFXMLGetter
from pyowl2.mapper.rdf_xml_mapper import RDFXMLMapper
from pyowl2.utils.data_property import OWLFullDataProperty
from pyowl2.utils.datatype import OWLFullDataRange
from pyowl2.utils.individual import OWLFullIndividual
from pyowl2.utils.object_property import OWLFullObjectProperty
from pyowl2.utils.thing import OWLFullClass


class OWLOntology:
    """
    This class provides a comprehensive interface for creating, manipulating, and persisting OWL (Web Ontology Language) ontologies. It acts as a central container for knowledge representation, managing entities such as classes, properties, individuals, and the axioms that define their logical relationships. Users can initialize the instance with a base IRI to create a new ontology or provide a file path to load an existing one. The class facilitates the addition of complex logical structures through methods that handle declarations, domains, ranges, and nested axioms, while also offering robust capabilities for attaching metadata annotations to the ontology itself, specific elements, or individual relations. Internally, it utilizes mapping and retrieval components to translate high-level objects into RDF/XML and query the underlying graph, ultimately supporting the export of the ontology to various file formats.

    :param ontology_iri: The Internationalized Resource Identifier (IRI) that uniquely identifies the ontology. It serves as the base IRI for the namespace and is used to retrieve or create the ontology instance within the underlying world.
    :type ontology_iri: typing.Optional[URIRef]
    :param axioms: A list of axioms that define the logical statements and relationships within the ontology.
    :type axioms: list[OWLAxiom]
    :param ontology_annotations: Internal storage for the list of annotations providing metadata about the ontology itself, such as creator, version, or other descriptive details.
    :type ontology_annotations: typing.Optional[list[OWLAnnotation]]
    :param world: The World instance that manages the ontology's context and provides access to the underlying RDF graph.
    :type world: World
    :param ontology: The underlying ontology instance managed by the World object, serving as the core data structure for storing, loading, and persisting the ontology's contents.
    :type ontology: Ontology
    :param clear: An instance used to clear the ontology's content during initialization, ensuring a clean state for newly created ontologies.
    :type clear: RDFXMLClear
    :param mapper: Internal component that maps OWL axioms and annotations to the underlying RDF graph, enabling the translation of high-level ontology constructs into a storable format.
    :type mapper: RDFXMLMapper
    :param getter: Responsible for retrieving axioms and annotations from the ontology, providing methods to query and extract specific elements based on various criteria.
    :type getter: RDFXMLGetter
    """

    def __init__(
        self,
        base_iri: typing.Union[IRI, URIRef],
        ontology_path: typing.Optional[str] = None,
        OWL1_annotations: bool = False,
    ) -> None:
        """
        This constructor initializes an OWL ontology instance, capable of either creating a new ontology or loading an existing one from a specified file path. It requires a base IRI to serve as the namespace and unique identifier, which is stored internally regardless of whether the ontology is loaded from a file or created anew. If a file path is provided, the ontology is loaded from that location; otherwise, a new ontology is generated using the base IRI, its base IRI is set with entity renaming enabled, and the graph is cleared to ensure a clean state. Additionally, the method sets up an internal Owlready2 World object and initializes helper components for mapping and retrieving RDF/XML data, configuring the mapper to use OWL 1 annotations if the corresponding flag is enabled.

        :param base_iri: The unique identifier and namespace for the ontology, used to instantiate or reference the ontology and define the base URI for its entities.
        :type base_iri: typing.Union[IRI, URIRef]
        :param ontology_path: Optional file path to an existing ontology file. If provided, the ontology is loaded from this file; otherwise, a new ontology is created using the base IRI.
        :type ontology_path: typing.Optional[str]
        :param OWL1_annotations: If True, configures the RDF/XML mapper to use OWL 1 annotation properties for compatibility with legacy tools or ontologies; otherwise, defaults to OWL 2.
        :type OWL1_annotations: bool
        """

        self._ontology_iri: typing.Optional[URIRef] = (
            base_iri if isinstance(base_iri, URIRef) else str(base_iri.to_uriref())
        )
        self._axioms: list[OWLAxiom] = None
        self._ontology_annotations: typing.Optional[list[OWLAnnotation]] = None
        self._world: World = World()  # default_world
        if ontology_path is None:
            self._ontology: Ontology = self._world.get_ontology(self._ontology_iri)
            try:
                self._ontology.set_base_iri(self.ontology_iri, rename_entities=True)
            except Exception as e:
                print(e)
            self._clear: RDFXMLClear = RDFXMLClear(self._ontology)
            self._clear.clear()
        else:
            self._ontology: Ontology = self._world.get_ontology(ontology_path).load()

        self._mapper: RDFXMLMapper = RDFXMLMapper(
            self._world.as_rdflib_graph(), OWL1_annotations
        )
        self._getter: RDFXMLGetter = RDFXMLGetter(self._ontology)

    @property
    def namespace(self) -> Namespace:
        """
        Retrieves the `Namespace` object corresponding to the ontology's IRI. This property provides access to the namespace context by delegating to the underlying ontology handler, allowing for the generation and management of identifiers relative to the ontology's base IRI.

        :return: The Namespace object associated with the ontology IRI.

        :rtype: Namespace
        """

        return self._ontology.get_namespace(self._ontology_iri)

    @property
    def ontology_iri(self) -> typing.Optional[URIRef]:
        """
        Sets the Internationalized Resource Identifier (IRI) for the ontology, effectively updating its primary identifier. This method accepts a `URIRef` object or `None`, assigning the value to the internal `_ontology_iri` attribute. If `None` is provided, the ontology IRI is cleared; otherwise, it is replaced with the specified URI reference.

        :param value: The Internationalized Resource Identifier (IRI) to assign to the ontology.
        :type value: typing.Optional[URIRef]
        """

        return self._ontology_iri

    @ontology_iri.setter
    def ontology_iri(self, value: typing.Optional[URIRef]) -> None:
        """Setter for ontology_iri."""
        self._ontology_iri = value

    @property
    def axioms(self) -> list[OWLAxiom]:
        """
        Replaces the current collection of axioms associated with this ontology with the provided list of OWLAxiom instances. This setter performs a direct assignment to the internal storage, effectively discarding any previously held axioms without performing validation or deep copying. Consequently, the ontology's state is immediately updated to reflect the new set of axioms.

        :param value: The axioms to assign to the object.
        :type value: list[OWLAxiom]
        """

        return self._axioms

    @axioms.setter
    def axioms(self, value: list[OWLAxiom]) -> None:
        """Setter for axioms."""
        self._axioms = value

    @property
    def ontology_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        """
        Replaces the current collection of annotations associated with the ontology with the provided list. This method acts as the setter for the `ontology_annotations` property, allowing direct assignment of a list of `OWLAnnotation` objects to the underlying private attribute. Note that this operation overwrites any existing annotations rather than appending to them.

        :param value: A list of OWL annotations to assign to the ontology.
        :type value: list[OWLAnnotation]
        """

        return self._ontology_annotations

    @ontology_annotations.setter
    def ontology_annotations(self, value: list[OWLAnnotation]) -> None:
        """Setter for ontology_annotations."""
        self._ontology_annotations = value

    @property
    def mapper(self) -> RDFXMLMapper:
        """
        Returns the RDFXMLMapper instance associated with this ontology. This mapper is responsible for handling the conversion between the ontology's internal object representation and the RDF/XML serialization format. Accessing this property has no side effects and simply retrieves the pre-configured mapper object.

        :return: The RDFXMLMapper instance associated with this object.

        :rtype: RDFXMLMapper
        """

        return self._mapper

    @property
    def getter(self) -> RDFXMLGetter:
        """
        Returns the `RDFXMLGetter` instance associated with this ontology. This property provides access to the internal component responsible for handling RDF/XML data retrieval or parsing. It exposes the value of the private `_getter` attribute without modifying the state of the ontology.

        :return: The `RDFXMLGetter` instance associated with this object.

        :rtype: RDFXMLGetter
        """

        return self._getter

    def add_axiom(self, axiom: typing.Any) -> bool:
        """
        Adds a logical axiom to the ontology by delegating the mapping process to the internal mapper object. This operation is performed within a context manager to ensure the underlying ontology resource is managed correctly during the modification. The method returns True to indicate the completion of the operation, but if the mapper fails to process the axiom, an exception will be raised, as the implementation does not include explicit error handling to return False.

        :param axiom: The logical construct or statement to be added to the ontology, such as a class or property assertion.
        :type axiom: typing.Any

        :return: True, indicating that the axiom was successfully added to the ontology.

        :rtype: bool
        """

        with self._ontology:
            self.mapper.map(axiom)
        return True
        # try:
        #     with self._ontology:
        #         self.mapper.map(axiom)
        #     return True
        # except Exception as e:
        #     print(e)
        #     return False

    def add_axioms(self, axioms: list[OWLObject]) -> bool:
        """
        Adds a list of axioms to the ontology by iterating through the provided collection and mapping each logical statement to the underlying structure. The method performs specialized processing for complex entity types—specifically object properties, data properties, classes, data ranges, and individuals—by decomposing them into their constituent parts, including declarations, annotations, domains, ranges, and any associated inner axioms. Axioms that do not match these specific types are mapped directly without decomposition. Each addition operation is wrapped in a context manager to ensure the ontology is properly managed during the modification process. The method returns True upon successfully processing the entire list, though it does not currently handle exceptions internally and will propagate errors if mapping fails.

        :param axioms: A list of OWLObject instances representing logical statements to be added to the ontology. The method processes specific types—including object properties, data properties, classes, data ranges, and individuals—by mapping their declarations, domains, ranges, and inner axioms, while mapping other types directly.
        :type axioms: list[OWLObject]

        :return: True if all axioms were successfully added to the ontology.

        :rtype: bool
        """

        # try:
        for axiom in axioms:
            with self._ontology:
                if isinstance(axiom, OWLFullObjectProperty):
                    # If the axiom is an OWLFullObjectProperty, we need to map the declaration of the object property, its domain, its range, and any inner axioms that may be associated with it. The declaration is mapped using the OWLDeclaration class, which takes the object property and any annotations associated with it. The domain and range are mapped directly using the mapper's map method. Finally, any inner axioms that are part of the OWLFullObjectProperty are also mapped to ensure that all relevant information about the object property is included in the ontology. This process ensures that the OWLFullObjectProperty is fully represented in the ontology with all necessary components and relationships properly defined.
                    self.mapper.map(
                        OWLDeclaration(
                            axiom.object_property, annotations=axiom.annotations
                        )
                    )
                    self.mapper.map(axiom.domain)
                    self.mapper.map(axiom.range)
                    for inner_axiom in axiom.axioms:
                        self.mapper.map(inner_axiom)
                elif isinstance(axiom, OWLFullDataProperty):
                    # If the axiom is an OWLFullDataProperty, we need to map the declaration of the data property, its domain, its range, and any inner axioms that may be associated with it. The declaration is mapped using the OWLDeclaration class, which takes the data property and any annotations associated with it. The domain and range are mapped directly using the mapper's map method. Finally, any inner axioms that are part of the OWLFullDataProperty are also mapped to ensure that all relevant information about the data property is included in the ontology. This process ensures that the OWLFullDataProperty is fully represented in the ontology with all necessary components and relationships properly defined.
                    self.mapper.map(
                        OWLDeclaration(
                            axiom.data_property, annotations=axiom.annotations
                        )
                    )
                    self.mapper.map(axiom.domain)
                    self.mapper.map(axiom.range)
                    for inner_axiom in axiom.axioms:
                        self.mapper.map(inner_axiom)
                elif isinstance(axiom, OWLFullClass):
                    # If the axiom is an OWLFullClass, we need to map the declaration of the class and any inner axioms that may be associated with it. The declaration is mapped using the OWLDeclaration class, which takes the class and any annotations associated with it. Finally, any inner axioms that are part of the OWLFullClass are also mapped to ensure that all relevant information about the class is included in the ontology. This process ensures that the OWLFullClass is fully represented in the ontology with all necessary components and relationships properly defined.
                    self.mapper.map(
                        OWLDeclaration(axiom.class_, annotations=axiom.annotations)
                    )
                    for inner_axiom in axiom.axioms:
                        self.mapper.map(inner_axiom)
                elif isinstance(axiom, OWLFullDataRange):
                    # If the axiom is an OWLFullDataRange, we need to map the declaration of the data range and any inner axioms that may be associated with it. The declaration is mapped using the OWLDeclaration class, which takes the data range and any annotations associated with it. Finally, any inner axioms that are part of the OWLFullDataRange are also mapped to ensure that all relevant information about the data range is included in the ontology. This process ensures that the OWLFullDataRange is fully represented in the ontology with all necessary components and relationships properly defined.
                    self.mapper.map(
                        OWLDeclaration(axiom.data_range, annotations=axiom.annotations)
                    )
                    for inner_axiom in axiom.axioms:
                        self.mapper.map(inner_axiom)
                elif isinstance(axiom, OWLFullIndividual):
                    # If the axiom is an OWLFullIndividual, we need to map the declaration of the individual and any inner axioms that may be associated with it. The declaration is mapped using the OWLDeclaration class, which takes the individual and any annotations associated with it. Finally, any inner axioms that are part of the OWLFullIndividual are also mapped to ensure that all relevant information about the individual is included in the ontology. This process ensures that the OWLFullIndividual is fully represented in the ontology with all necessary components and relationships properly defined.
                    self.mapper.map(
                        OWLDeclaration(axiom.individual, annotations=axiom.annotations)
                    )
                    for inner_axiom in axiom.axioms:
                        self.mapper.map(inner_axiom)
                else:
                    # If the axiom does not match any of the specific types (OWLFullObjectProperty, OWLFullDataProperty, OWLFullClass, OWLFullDataRange, OWLFullIndividual), it will be mapped directly to the ontology without additional processing. This allows for the inclusion of axioms that may not require special handling or that do not fit into the predefined categories, ensuring that a wide range of axioms can be added to the ontology as needed.
                    self.mapper.map(axiom)
        return True
        # except Exception as e:
        #     print(e)
        #     return False

    def add_annotation(self, annotation: OWLAnnotation) -> bool:
        """
        Associates a single metadata annotation with the ontology by wrapping the bulk addition method. It accepts an `OWLAnnotation` object representing the metadata to be attached and attempts to persist it within the ontology structure. The operation returns a boolean value indicating success; it yields True if the annotation is successfully integrated, and False if the underlying process encounters an exception or mapping error. This method modifies the ontology's state by adding the specified annotation to its collection of annotations.

        :param annotation: Metadata to be added to the ontology.
        :type annotation: OWLAnnotation

        :return: True if the annotation was successfully added to the ontology, False if an error occurred.

        :rtype: bool
        """

        return self.add_annotations([annotation])

    def add_annotations(
        self, annotations: typing.Optional[list[OWLAnnotation]]
    ) -> bool:
        """
        Associates a collection of metadata annotations with the ontology by delegating the mapping process to an internal mapper object. The operation is performed within a context manager to ensure proper resource handling during the modification. Upon successful completion, the method returns True; conversely, if any exception is raised during the mapping process, the error is printed to standard output and the method returns False.

        :param annotations: A list of OWLAnnotation objects representing metadata to be added to the ontology. Can be None.
        :type annotations: typing.Optional[list[OWLAnnotation]]

        :return: True if the annotations were successfully added to the ontology, False if an error occurred during the process.

        :rtype: bool
        """

        try:
            with self._ontology:
                self.mapper.map_owl_annotations(self._ontology_iri, annotations)
            return True
        except Exception as e:
            print(e)
            return False

    def add_annotations_to_relation(
        self,
        a: typing.Any,
        property: typing.Any,
        b: typing.Any,
        annotations: typing.Optional[list[OWLAnnotation]],
    ) -> bool:
        """
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
        """

        try:
            with self._ontology:
                self.mapper.map_owl_annotations_entities(a, property, b, annotations)
            return True
        except Exception as e:
            print(e)
            return False

    def add_annotation_to_element(
        self,
        element: OWLObject,
        annotations: typing.Optional[list[OWLAnnotation]],
    ):
        """
        This method attaches a list of metadata annotations to a specific ontology element, such as a class, property, or individual, thereby enriching the element's documentation. The operation is performed within a managed context to ensure the integrity of the underlying ontology structure while the internal mapper applies the changes. It returns True if the annotations are successfully added; if an exception occurs during the mapping or attachment process, the error is printed to standard output and the method returns False.

        :param element: The target ontology entity or axiom to which the annotations will be attached.
        :type element: OWLObject
        :param annotations: A list of OWLAnnotation objects representing the metadata to associate with the element, or None.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        try:
            with self._ontology:
                node = self.mapper.map(element)
                self.mapper.map_owl_annotations(node, annotations)
            return True
        except Exception as e:
            print(e)
            return False

    def get_axioms(self, axiom: AxiomsType) -> list[OWLObject]:
        """
        Retrieves a list of axioms from the ontology that match the specified type, enabling targeted queries of the ontology's logical content. The method accepts an `AxiomsType` enumeration value to filter the results, returning a collection of `OWLObject` instances representing the requested axioms. Internally, the retrieval logic is delegated to the ontology's underlying getter, and the method returns an empty list if no matching axioms are found or if an error occurs during the operation.

        :param axiom: Specifies the category of axiom to retrieve from the ontology, acting as a filter to return only OWL objects matching the selected logical construct type.
        :type axiom: AxiomsType

        :return: A list of OWL objects representing the axioms of the specified type retrieved from the ontology. Returns an empty list if no matching axioms are found or if an error occurs during retrieval.

        :rtype: list[OWLObject]
        """

        return self.getter.get(axiom)

    def print_all(self) -> None:
        """Iterates through every axiom type defined in the `AxiomsType` enumeration, retrieves the corresponding axioms from the ontology, and prints them to the console. The method uses a context manager to ensure the ontology resource is properly managed while accessing the data. For each axiom category, it prints the type name followed by the specific results retrieved via the internal getter, providing a comprehensive text-based overview of the ontology's structure and contents. This operation produces side effects by writing to standard output and depends on the successful retrieval of data for each enumerated type."""

        with self._ontology:
            for axiom in list(AxiomsType):
                print(f"\n{axiom}")
                results = self.getter.get(axiom)
                print(results)

    def save(self, filepath: str, format: str = "rdfxml") -> bool:
        """
        Persists the current state of the ontology to a file at the specified path, serializing the data according to the given format (defaulting to RDF/XML). This method delegates the actual file writing operation to the underlying ontology object. Upon success, it returns True; if an error occurs—such as an invalid path, insufficient write permissions, or an unsupported format—the exception is caught, the error message is printed to standard output, and the method returns False without propagating the exception.

        :param filepath: The destination file system path where the ontology will be written.
        :type filepath: str
        :param format: The serialization format for the ontology file (e.g., "rdfxml", "turtle").
        :type format: str

        :return: True if the ontology was successfully saved to the specified file, False if an error occurred during the operation.

        :rtype: bool
        """

        try:
            # print(self.mapper.graph.serialize(format="turtle"))
            self._ontology.save(filepath, format=format)
            return True
        except Exception as e:
            print(e)
            return False
