import typing

from owlready2 import Ontology, Thing, ThingClass, World
from owlready2.base import _universal_abbrev, _universal_iri_2_abbrev
from rdflib import OWL, RDF, RDFS, Graph, Namespace, URIRef


def get_abbreviation(iri: URIRef) -> int:
    """
    Retrieves the integer identifier associated with a given IRI from the module's global mapping. If the IRI has already been processed and exists within the `_universal_iri_2_abbrev` dictionary, the function returns the stored integer. Otherwise, it delegates to the `_universal_abbrev` function to generate a new abbreviation based on the string representation of the IRI, ensuring that all IRIs are consistently mapped to a compact integer format.

    :param iri: Internationalized Resource Identifier to look up in the universal mapping or generate a new abbreviation for.
    :type iri: URIRef

    :return: The integer abbreviation associated with the IRI. If the IRI is not already mapped, a new abbreviation is generated and returned.

    :rtype: int
    """

    if str(iri) in _universal_iri_2_abbrev:
        return _universal_iri_2_abbrev[str(iri)]
    else:
        return _universal_abbrev(str(iri))


def is_named_individual(obj: object) -> bool:
    """
    Determines whether the provided object represents a named individual by verifying that it is an instance of the base `Thing` class while explicitly excluding instances of `ThingClass`. This distinction is necessary to differentiate between concrete entities and their abstract class definitions within the ontology structure. The check relies solely on type inspection and does not modify the input object or cause any side effects.

    :param obj: The object to evaluate for named individual status.
    :type obj: object

    :return: True if the object is a named individual (an instance of Thing but not a ThingClass).

    :rtype: bool
    """

    return isinstance(obj, Thing) and not isinstance(obj, ThingClass)


class RDFXMLClear:
    """
    This utility class is designed to sanitize and restructure an ontology by removing specific RDF/XML definitions from its underlying graph. It is initialized with an ontology instance, which provides access to the associated world and RDF graph data structures. The primary functionality is exposed through a method that systematically removes type declarations for classes, properties, and lists, effectively stripping away structural definitions. Additionally, the logic performs a normalization step that replaces certain property declarations, such as inverse functional or transitive properties, with more general types like object properties. This process modifies the ontology in place, allowing for the selective clearing of semantic metadata without deleting the entire data model.

    :parm ontology: The target ontology instance from which RDF/XML data structures are removed.
    :type ontology: Ontology
    :parm world: The World instance associated with the ontology, used for accessing and querying RDF triples and the underlying graph.
    :type world: World
    :parm graph: The RDFLib graph representation of the ontology's world, providing a standard interface for querying and manipulating RDF triples.
    :type graph: Graph
    """

    def __init__(self, ontology: Ontology) -> None:
        """
        Constructs a new RDFXMLClear instance associated with the specified ontology, preparing the necessary context for clearing RDF/XML data. The method ensures the provided ontology is not None and stores it internally. Additionally, it extracts the underlying World object and converts it into an RDFLib Graph, which serves as the target for data removal operations.

        :param ontology: The ontology instance from which RDF/XML data will be cleared.
        :type ontology: Ontology
        """

        assert ontology is not None
        self._ontology: Ontology = ontology
        self._world: World = typing.cast(World, ontology.world)
        self._graph: Graph = self._world.as_rdflib_graph()

    @property
    def graph(self) -> Graph:
        """
        Returns the RDF Graph object associated with this instance. This property provides direct access to the internal graph storage, allowing retrieval of the triples managed by the object. Since it returns a reference to the actual graph rather than a copy, any modifications made to the returned graph will directly affect the state of the `RDFXMLClear` instance.

        :return: The underlying graph object.

        :rtype: Graph
        """

        return self._graph

    @property
    def ontology(self) -> Ontology:
        """
        Returns the Ontology instance associated with the current object. This property getter exposes the internal _ontology attribute, providing access to the ontology data managed by the RDFXMLClear instance. Since it returns a direct reference to the stored object rather than a copy, any modifications made to the returned Ontology will directly affect the internal state of the parent object.

        :return: The Ontology object associated with this instance.

        :rtype: Ontology
        """

        return self._ontology

    @property
    def world(self) -> World:
        """
        Retrieves the `World` instance associated with this `RDFXMLClear` object. This property acts as a getter for the internal `_world` attribute, providing access to the specific context or storage environment used by the RDF/XML parser or serializer. The method has no side effects and simply returns the reference to the stored `World` object.

        :return: The World instance associated with this object.

        :rtype: World
        """

        return self._world

    @property
    def namespace(self) -> Namespace:
        """
        Returns the `Namespace` object associated with the base IRI of the ontology linked to this instance. This property retrieves the namespace by invoking the `get_namespace` method on the `ontology` attribute, using the ontology's `base_iri` as the lookup key.

        :return: The Namespace object corresponding to the base IRI of the ontology.

        :rtype: Namespace
        """

        return self.ontology.get_namespace(self.ontology.base_iri)

    def _clear_ontology(self) -> None:
        """Removes all ontology declaration triples from the internal storage. It iterates through the RDF triples in the world to identify entries where the predicate is rdf:type and the object is owl:Ontology. Each matching triple is then deleted from the ontology's internal store, effectively clearing the ontology's declaration metadata."""

        for s, p, o in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(OWL.Ontology)
        ):
            self.ontology._del_obj_triple_spo(s, p, o)

    def _clear_class(self) -> None:
        """This method systematically removes class definitions from the ontology by targeting specific RDF type assertions. It iterates over entities identified as OWL classes, RDFS datatypes, or OWL data ranges and deletes any triples that classify them as RDFS classes. Furthermore, it locates OWL restrictions and removes their declarations as either OWL classes or RDFS classes. This process directly modifies the ontology's triple store, effectively stripping the class status from these entities while leaving other properties intact."""

        for sj, _, _ in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(OWL.Class)
        ):
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(RDFS.Class)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)
        for sj, _, _ in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(RDFS.Datatype)
        ):
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(RDFS.Class)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)
        for sj, _, _ in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(OWL.DataRange)
        ):
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(RDFS.Class)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)

        for sj, _, _ in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(OWL.Restriction)
        ):
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(OWL.Class)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(RDFS.Class)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)

    def _clear_property(self) -> None:
        """Removes all property definitions from the ontology by targeting specific OWL property types. It iterates through the world to identify subjects declared as `owl:ObjectProperty`, `owl:FunctionalProperty`, `owl:InverseFunctionalProperty`, `owl:TransitiveProperty`, `owl:DatatypeProperty`, `owl:AnnotationProperty`, or `owl:OntologyProperty`. For each identified subject, the method locates and deletes the triple asserting that the subject is an instance of `rdf:Property` within the ontology. This process results in the permanent removal of these property definitions from the ontology's data structure."""

        for sj, _, _ in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(OWL.ObjectProperty)
        ):
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(RDF.Property)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)
        for sj, _, _ in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(OWL.FunctionalProperty)
        ):
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(RDF.Property)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)
        for sj, _, _ in self.world.get_triples(
            None,
            get_abbreviation(RDF.type),
            get_abbreviation(OWL.InverseFunctionalProperty),
        ):
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(RDF.Property)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)
        for sj, _, _ in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(OWL.TransitiveProperty)
        ):
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(RDF.Property)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)
        for sj, _, _ in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(OWL.DatatypeProperty)
        ):
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(RDF.Property)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)
        for sj, _, _ in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(OWL.AnnotationProperty)
        ):
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(RDF.Property)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)
        for sj, _, _ in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(OWL.OntologyProperty)
        ):
            for si, pi, oi in self.world.get_triples(
                sj, get_abbreviation(RDF.type), get_abbreviation(RDF.Property)
            ):
                self.ontology._del_obj_triple_spo(si, pi, oi)

    def _clear_list(self) -> None:
        """This method iterates through the ontology to identify resources explicitly typed as `rdf:List` and removes the triple asserting that type. It performs this removal only if the resource possesses the structural characteristics of a list, specifically checking for the existence of both `rdf:first` and `rdf:rest` properties. By deleting the type assertion, the method effectively undefines these resources as lists within the ontology without removing the underlying structural triples."""

        for sj, pj, oj in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(RDF.List)
        ):
            for _ in self.world.get_triples(sj, RDF.first, None):
                for _ in self.world.get_triples(sj, RDF.rest, None):
                    self.ontology._del_obj_triple_spo(sj, pj, oj)

    def _replace_declarations(self) -> None:
        """This method refines OWL property declarations within the ontology by replacing or adding specific type assertions based on the property's characteristics. It iterates through triples in the world to identify properties declared as `owl:OntologyProperty`, `owl:InverseFunctionalProperty`, `owl:TransitiveProperty`, or `owl:SymmetricProperty`. For `owl:OntologyProperty`, the type is replaced with `owl:AnnotationProperty`, whereas for the inverse functional, transitive, and symmetric properties, `owl:ObjectProperty` is added as an additional type. Entities that do not possess an IRI attribute are skipped during this process. This operation results in direct modifications to the ontology's triple store to align property declarations with the intended schema."""

        for sj, pj, oj in self.world.get_triples(
            None,
            get_abbreviation(RDF.type),
            get_abbreviation(OWL.OntologyProperty),
        ):
            obj = self.world._get_by_storid(sj)
            if not hasattr(obj, "iri"):
                continue
            self.ontology._add_obj_triple_spo(
                sj, pj, get_abbreviation(OWL.AnnotationProperty)
            )
            self.ontology._del_obj_triple_spo(sj, pj, oj)
        for sj, pj, oj in self.world.get_triples(
            None,
            get_abbreviation(RDF.type),
            get_abbreviation(OWL.InverseFunctionalProperty),
        ):
            obj = self.world._get_by_storid(sj)
            if not hasattr(obj, "iri"):
                continue
            self.ontology._add_obj_triple_spo(
                sj, pj, get_abbreviation(OWL.ObjectProperty)
            )
        for sj, pj, oj in self.world.get_triples(
            None,
            get_abbreviation(RDF.type),
            get_abbreviation(OWL.TransitiveProperty),
        ):
            obj = self.world._get_by_storid(sj)
            if not hasattr(obj, "iri"):
                continue
            self.ontology._add_obj_triple_spo(
                sj, pj, get_abbreviation(OWL.ObjectProperty)
            )
        for sj, pj, oj in self.world.get_triples(
            None,
            get_abbreviation(RDF.type),
            get_abbreviation(OWL.SymmetricProperty),
        ):
            obj = self.world._get_by_storid(sj)
            if not hasattr(obj, "iri"):
                continue
            self.ontology._add_obj_triple_spo(
                sj, pj, get_abbreviation(OWL.ObjectProperty)
            )

    def clear(self) -> None:
        """Removes all structural definitions from the ontology by systematically deleting RDF triples associated with classes, lists, and properties. In addition to removal, this method transforms the remaining data by replacing certain OWL property declarations with more specific types. This operation directly mutates the underlying graph, resulting in the irreversible loss of the cleared definitions."""

        # self._clear_ontology()
        self._clear_class()
        self._clear_list()
        self._clear_property()
        self._replace_declarations()
