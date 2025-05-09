import typing

from owlready2 import Ontology, Thing, ThingClass, World
from owlready2.base import _universal_abbrev, _universal_iri_2_abbrev
from rdflib import OWL, RDF, RDFS, Graph, Namespace, URIRef


def get_abbreviation(iri: URIRef) -> int:
    if str(iri) in _universal_iri_2_abbrev:
        return _universal_iri_2_abbrev[str(iri)]
    else:
        return _universal_abbrev(str(iri))


def is_named_individual(obj):
    return isinstance(obj, Thing) and not isinstance(obj, ThingClass)


class RDFXMLClear:

    def __init__(self, ontology: Ontology) -> None:
        assert ontology is not None
        self._ontology: Ontology = ontology
        self._world: World = typing.cast(World, ontology.world)
        self._graph: Graph = self._world.as_rdflib_graph()

    @property
    def graph(self) -> Graph:
        return self._graph

    @property
    def ontology(self) -> Ontology:
        return self._ontology

    @property
    def world(self) -> World:
        return self._world

    @property
    def namespace(self) -> Namespace:
        return self.ontology.get_namespace(self.ontology.base_iri)

    def _clear_ontology(self) -> None:
        for s, p, o in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(OWL.Ontology)
        ):
            self.ontology._del_obj_triple_spo(s, p, o)

    def _clear_class(self) -> None:
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
        for sj, pj, oj in self.world.get_triples(
            None, get_abbreviation(RDF.type), get_abbreviation(RDF.List)
        ):
            for _ in self.world.get_triples(sj, RDF.first, None):
                for _ in self.world.get_triples(sj, RDF.rest, None):
                    self.ontology._del_obj_triple_spo(sj, pj, oj)

    def _replace_declarations(self) -> None:
        for sj, pj, oj in self.world.get_triples(
            None,
            get_abbreviation(RDF.type),
            get_abbreviation(OWL.OntologyProperty),
        ):
            obj = self.world._get_by_storid(sj)
            if not hasattr(obj, "iri"): continue
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
        # self._clear_ontology()
        self._clear_class()
        self._clear_list()
        self._clear_property()
        self._replace_declarations()
