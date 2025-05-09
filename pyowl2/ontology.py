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
    """A formal representation of knowledge that includes classes, properties, individuals, and axioms."""

    def __init__(
        self,
        base_iri: typing.Union[IRI, URIRef],
        ontology_path: typing.Optional[str] = None,
        OWL1_annotations: bool = False,
    ) -> None:
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
        """Getter for namespace."""
        return self._ontology.get_namespace(self._ontology_iri)

    @property
    def ontology_iri(self) -> typing.Optional[URIRef]:
        """Getter for ontology_iri."""
        return self._ontology_iri

    @ontology_iri.setter
    def ontology_iri(self, value: typing.Optional[URIRef]) -> None:
        """Setter for ontology_iri."""
        self._ontology_iri = value

    @property
    def axioms(self) -> list[OWLAxiom]:
        """Getter for axioms."""
        return self._axioms

    @axioms.setter
    def axioms(self, value: list[OWLAxiom]) -> None:
        """Setter for axioms."""
        self._axioms = value

    @property
    def ontology_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        """Getter for ontology_annotations."""
        return self._ontology_annotations

    @ontology_annotations.setter
    def ontology_annotations(self, value: list[OWLAnnotation]) -> None:
        """Setter for ontology_annotations."""
        self._ontology_annotations = value

    @property
    def mapper(self) -> RDFXMLMapper:
        return self._mapper

    @property
    def getter(self) -> RDFXMLGetter:
        return self._getter

    def add_axiom(self, axiom: typing.Any) -> bool:
        """Adds an axiom to the ontology."""
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
        """Adds a list of axioms to the ontology."""
        # try:
        for axiom in axioms:
            with self._ontology:
                if isinstance(axiom, OWLFullObjectProperty):
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
                    self.mapper.map(
                        OWLDeclaration(axiom.class_, annotations=axiom.annotations)
                    )
                    for inner_axiom in axiom.axioms:
                        self.mapper.map(inner_axiom)
                elif isinstance(axiom, OWLFullDataRange):
                    self.mapper.map(
                        OWLDeclaration(axiom.data_range, annotations=axiom.annotations)
                    )
                    for inner_axiom in axiom.axioms:
                        self.mapper.map(inner_axiom)
                elif isinstance(axiom, OWLFullIndividual):
                    self.mapper.map(
                        OWLDeclaration(axiom.individual, annotations=axiom.annotations)
                    )
                    for inner_axiom in axiom.axioms:
                        self.mapper.map(inner_axiom)
                else:
                    self.mapper.map(axiom)
        return True
        # except Exception as e:
        #     print(e)
        #     return False

    def add_annotation(self, annotation: OWLAnnotation) -> bool:
        """Adds an annotation to the ontology."""
        return self.add_annotations([annotation])

    def add_annotations(
        self, annotations: typing.Optional[list[OWLAnnotation]]
    ) -> bool:
        """Adds annotations to the ontology."""
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
        """Adds annotations to a relation in the ontology."""
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
        """Adds annotations to an element in the ontology."""
        try:
            with self._ontology:
                node = self.mapper.map(element)
                self.mapper.map_owl_annotations(node, annotations)
            return True
        except Exception as e:
            print(e)
            return False

    def get_axioms(self, axiom: AxiomsType) -> list[OWLObject]:
        """Retrieves an axiom from the ontology."""
        return self.getter.get(axiom)

    def print_all(self) -> None:
        """Retrieves all axioms from the ontology."""
        with self._ontology:
            for axiom in list(AxiomsType):
                print(f"\n{axiom}")
                results = self.getter.get(axiom)
                print(results)

    def save(self, filepath: str, format: str = "rdfxml") -> bool:
        """Saves the ontology to a file."""
        try:
            # print(self.mapper.graph.serialize(format="turtle"))
            self._ontology.save(filepath, format=format)
            return True
        except Exception as e:
            print(e)
            return False
