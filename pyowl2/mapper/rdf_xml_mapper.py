import typing

import owlready2
from rdflib import XSD, BNode, Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection
from rdflib.namespace import OWL, RDF, RDFS

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.entity import OWLEntity
from pyowl2.abstracts.object import OWLObject
from pyowl2.axioms.annotations import (
    OWLAnnotationAssertion,
    OWLAnnotationPropertyDomain,
    OWLAnnotationPropertyRange,
    OWLSubAnnotationPropertyOf,
)
from pyowl2.axioms.assertion import (
    OWLDifferentIndividuals,
    OWLNegativeDataPropertyAssertion,
    OWLNegativeObjectPropertyAssertion,
    OWLSameIndividual,
)
from pyowl2.axioms.assertion.class_assertion import OWLClassAssertion
from pyowl2.axioms.assertion.data_property_assertion import OWLDataPropertyAssertion
from pyowl2.axioms.assertion.object_property_assertion import OWLObjectPropertyAssertion
from pyowl2.axioms.class_axiom.disjoint_classes import OWLDisjointClasses
from pyowl2.axioms.class_axiom.disjoint_union import OWLDisjointUnion
from pyowl2.axioms.class_axiom.equivalent_classes import OWLEquivalentClasses
from pyowl2.axioms.class_axiom.sub_class_of import OWLSubClassOf
from pyowl2.axioms.data_property_axiom.data_property_domain import OWLDataPropertyDomain
from pyowl2.axioms.data_property_axiom.data_property_range import OWLDataPropertyRange
from pyowl2.axioms.data_property_axiom.disjoint_data_properties import (
    OWLDisjointDataProperties,
)
from pyowl2.axioms.data_property_axiom.equivalent_data_properties import (
    OWLEquivalentDataProperties,
)
from pyowl2.axioms.data_property_axiom.functional_data_property import (
    OWLFunctionalDataProperty,
)
from pyowl2.axioms.data_property_axiom.sub_data_property_of import OWLSubDataPropertyOf
from pyowl2.axioms.datatype_definition import OWLDatatypeDefinition
from pyowl2.axioms.declaration import OWLDeclaration
from pyowl2.axioms.general import OWLGeneralClassAxiom
from pyowl2.axioms.has_key import OWLHasKey
from pyowl2.axioms.object_property_axiom.asymmetric_object_property import (
    OWLAsymmetricObjectProperty,
)
from pyowl2.axioms.object_property_axiom.disjoint_object_properties import (
    OWLDisjointObjectProperties,
)
from pyowl2.axioms.object_property_axiom.equivalent_object_properties import (
    OWLEquivalentObjectProperties,
)
from pyowl2.axioms.object_property_axiom.functional_object_property import (
    OWLFunctionalObjectProperty,
)
from pyowl2.axioms.object_property_axiom.inverse_functional_object_property import (
    OWLInverseFunctionalObjectProperty,
)
from pyowl2.axioms.object_property_axiom.inverse_object_properties import (
    OWLInverseObjectProperties,
)
from pyowl2.axioms.object_property_axiom.irreflexive_object_property import (
    OWLIrreflexiveObjectProperty,
)
from pyowl2.axioms.object_property_axiom.object_property_chain import (
    OWLObjectPropertyChain,
)
from pyowl2.axioms.object_property_axiom.object_property_domain import (
    OWLObjectPropertyDomain,
)
from pyowl2.axioms.object_property_axiom.object_property_range import (
    OWLObjectPropertyRange,
)
from pyowl2.axioms.object_property_axiom.reflexive_object_property import (
    OWLReflexiveObjectProperty,
)
from pyowl2.axioms.object_property_axiom.sub_object_property_of import (
    OWLSubObjectPropertyOf,
)
from pyowl2.axioms.object_property_axiom.symmetric_object_property import (
    OWLSymmetricObjectProperty,
)
from pyowl2.axioms.object_property_axiom.transitive_object_property import (
    OWLTransitiveObjectProperty,
)
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.annotation_property import OWLAnnotationProperty
from pyowl2.base.datatype import OWLDatatype
from pyowl2.base.iri import IRI
from pyowl2.base.owl_class import OWLClass
from pyowl2.class_expression.data_all_values_from import OWLDataAllValuesFrom
from pyowl2.class_expression.data_exact_cardinality import OWLDataExactCardinality
from pyowl2.class_expression.data_has_value import OWLDataHasValue
from pyowl2.class_expression.data_max_cardinality import OWLDataMaxCardinality
from pyowl2.class_expression.data_min_cardinality import OWLDataMinCardinality
from pyowl2.class_expression.data_some_values_from import OWLDataSomeValuesFrom
from pyowl2.class_expression.object_all_values_from import OWLObjectAllValuesFrom
from pyowl2.class_expression.object_complement_of import OWLObjectComplementOf
from pyowl2.class_expression.object_exact_cardinality import OWLObjectExactCardinality
from pyowl2.class_expression.object_has_self import OWLObjectHasSelf
from pyowl2.class_expression.object_has_value import OWLObjectHasValue
from pyowl2.class_expression.object_intersection_of import OWLObjectIntersectionOf
from pyowl2.class_expression.object_max_cardinality import OWLObjectMaxCardinality
from pyowl2.class_expression.object_min_cardinality import OWLObjectMinCardinality
from pyowl2.class_expression.object_one_of import OWLObjectOneOf
from pyowl2.class_expression.object_some_values_from import OWLObjectSomeValuesFrom
from pyowl2.class_expression.object_union_of import OWLObjectUnionOf
from pyowl2.data_range.data_complement_of import OWLDataComplementOf
from pyowl2.data_range.data_intersection_of import OWLDataIntersectionOf
from pyowl2.data_range.data_one_of import OWLDataOneOf
from pyowl2.data_range.data_union_of import OWLDataUnionOf
from pyowl2.data_range.datatype_restriction import OWLDatatypeRestriction, OWLFacet
from pyowl2.expressions import OWLInverseObjectProperty
from pyowl2.expressions.data_property import OWLDataProperty
from pyowl2.expressions.object_property import OWLObjectProperty
from pyowl2.individual.anonymous_individual import OWLAnonymousIndividual
from pyowl2.individual.named_individual import OWLNamedIndividual
from pyowl2.literal.literal import OWLLiteral
from pyowl2.utils import utils


# @utils.timer_decorator
class RDFXMLMapper:
    """
    A utility class for mapping OWL concepts to RDF triples using RDFLib.
    Each static method handles a specific OWL mapping transformation.
    """

    def __init__(self, graph: Graph, OWL1_annotations: bool = False) -> None:
        self._graph: Graph = graph
        self._owl1_annotations: bool = OWL1_annotations

    @property
    def graph(self) -> Graph:
        return self._graph

    @property
    def owl1_annotations(self) -> bool:
        return self._owl1_annotations

    def map(
        self,
        value: typing.Optional[
            typing.Union[BNode, IRI, str, URIRef, Literal, OWLObject]
        ],
    ) -> typing.Optional[URIRef]:
        if not value:
            return BNode()
        if isinstance(value, IRI):
            return value.to_uriref()
        if isinstance(value, URIRef):
            return value
        if isinstance(value, BNode):
            return value
        if isinstance(value, Literal):
            return value
        if isinstance(value, OWLLiteral):
            return value.to_uriref()
        if hasattr(value, "iri"):
            if isinstance(value.iri, IRI):
                return value.iri.to_uriref()
            elif isinstance(value.iri, URIRef):
                return value.iri
            raise TypeError(
                f"Cannot map value of type {type(value.iri)}. "
                "Please provide a valid OWL entity or expression."
            )
        if isinstance(value, str):
            return URIRef(value)
        if isinstance(value, OWLDeclaration):
            return self.map_owl_declaration(value)
        if isinstance(value, typing.Iterable):
            return self.map_sequence(value)
        if isinstance(value, OWLDataIntersectionOf):
            return self.map_owl_data_intersection_of(value)
        if isinstance(value, OWLDataUnionOf):
            return self.map_owl_data_union_of(value)
        if isinstance(value, OWLDataComplementOf):
            return self.map_owl_data_complement_of(value)
        if isinstance(value, OWLDataOneOf):
            return self.map_owl_data_one_of(value)
        if isinstance(value, OWLObjectIntersectionOf):
            return self.map_owl_object_intersection_of(value)
        if isinstance(value, OWLObjectUnionOf):
            return self.map_owl_object_union_of(value)
        if isinstance(value, OWLObjectComplementOf):
            return self.map_owl_object_complement_of(value)
        if isinstance(value, OWLObjectOneOf):
            return self.map_owl_object_one_of(value)
        if isinstance(value, OWLObjectSomeValuesFrom):
            return self.map_owl_object_some_values_from(value)
        if isinstance(value, OWLObjectAllValuesFrom):
            return self.map_owl_object_all_values_from(value)
        if isinstance(value, OWLObjectHasValue):
            return self.map_owl_object_has_value(value)
        if isinstance(value, OWLObjectHasSelf):
            return self.map_owl_object_has_self(value)
        if isinstance(value, OWLObjectMinCardinality):
            return self.map_owl_object_min_cardinality(value)
        if isinstance(value, OWLObjectMaxCardinality):
            return self.map_owl_object_max_cardinality(value)
        if isinstance(value, OWLObjectExactCardinality):
            return self.map_owl_object_exact_cardinality(value)
        if isinstance(value, OWLDataSomeValuesFrom):
            return self.map_owl_data_some_values_from(value)
        if isinstance(value, OWLDataAllValuesFrom):
            return self.map_owl_data_all_values_from(value)
        if isinstance(value, OWLDataHasValue):
            return self.map_owl_data_has_value(value)
        if isinstance(value, OWLDataMinCardinality):
            return self.map_owl_data_min_cardinality(value)
        if isinstance(value, OWLDataMaxCardinality):
            return self.map_owl_data_max_cardinality(value)
        if isinstance(value, OWLDataExactCardinality):
            return self.map_owl_data_exact_cardinality(value)
        if isinstance(value, OWLSubClassOf):
            return self.map_owl_subclass_of(value)
        if isinstance(value, OWLDisjointUnion):
            return self.map_owl_disjoint_union(value)
        if isinstance(value, OWLSubObjectPropertyOf):
            return self.map_owl_subobject_property_of(value)
        if isinstance(value, OWLEquivalentObjectProperties):
            return self.map_owl_equivalent_object_properties(value)
        if isinstance(value, OWLDisjointObjectProperties):
            return self.map_owl_disjoint_object_properties(value)
        if isinstance(value, OWLSubDataPropertyOf):
            return self.map_owl_subdata_property_of(value)
        if isinstance(value, OWLEquivalentDataProperties):
            return self.map_owl_equivalent_data_properties(value)
        if isinstance(value, OWLDisjointDataProperties):
            return self.map_owl_disjoint_data_properties(value)
        if isinstance(value, OWLDatatypeDefinition):
            return self.map_owl_datatype_definition(value)
        if isinstance(value, OWLHasKey):
            return self.map_owl_has_key(value)
        if isinstance(value, OWLSameIndividual):
            return self.map_owl_same_individual(value)
        if isinstance(value, OWLDifferentIndividuals):
            return self.map_owl_different_individuals(value)
        if isinstance(value, OWLClassAssertion):
            return self.map_owl_class_assertion(value)
        if isinstance(value, OWLObjectPropertyAssertion):
            return self.map_owl_object_property_assertion(value)
        if isinstance(value, OWLNegativeObjectPropertyAssertion):
            return self.map_owl_negative_object_property_assertion(value)
        if isinstance(value, OWLDataPropertyAssertion):
            return self.map_owl_data_property_assertion(value)
        if isinstance(value, OWLNegativeDataPropertyAssertion):
            return self.map_owl_negative_data_property_assertion(value)
        if isinstance(value, OWLAnnotationAssertion):
            return self.map_owl_annotation_assertion(value)
        if isinstance(value, OWLSubAnnotationPropertyOf):
            return self.map_owl_sub_annotation_property_of(value)
        if isinstance(value, OWLAnnotationPropertyDomain):
            return self.map_owl_annotation_property_domain(value)
        if isinstance(value, OWLAnnotationPropertyRange):
            return self.map_owl_annotation_property_range(value)
        if isinstance(value, OWLClass):
            return self.map_owl_class(value)
        if isinstance(value, OWLNamedIndividual):
            return self.map_owl_named_individual(value)
        if isinstance(value, OWLAnonymousIndividual):
            return self.map_owl_anonymous_individual(value)
        if isinstance(value, OWLObjectPropertyDomain):
            return self.map_owl_object_property_domain(value)
        if isinstance(value, OWLObjectPropertyRange):
            return self.map_owl_object_property_range(value)
        if isinstance(value, OWLDataPropertyDomain):
            return self.map_owl_data_property_domain(value)
        if isinstance(value, OWLDataPropertyRange):
            return self.map_owl_data_property_range(value)
        if isinstance(value, OWLDatatypeRestriction):
            return self.map_owl_datatype_restriction(value)
        if isinstance(value, OWLEquivalentClasses):
            return self.map_owl_equivalent_classes(value)
        if isinstance(value, OWLDisjointClasses):
            return self.map_owl_disjoint_classes(value)
        if isinstance(value, OWLAnnotationProperty):
            return self.map_owl_annotation_property(value)
        if isinstance(value, OWLObjectProperty):
            return self.map_owl_object_property(value)
        if isinstance(value, OWLDataProperty):
            return self.map_owl_data_property(value)
        if isinstance(value, OWLDatatype):
            return self.map_owl_datatype(value)
        if isinstance(value, OWLInverseObjectProperty):
            return self.map_owl_object_inverse_of(value)
        if isinstance(value, OWLInverseObjectProperties):
            return self.map_owl_inverse_object_properties(value)
        if isinstance(value, (OWLFunctionalObjectProperty, OWLFunctionalDataProperty)):
            return self.map_owl_functional_property(value)
        if isinstance(value, OWLInverseFunctionalObjectProperty):
            return self.map_owl_inverse_functional_property(value)
        if isinstance(value, OWLSymmetricObjectProperty):
            return self.map_owl_symmetric_property(value)
        if isinstance(value, OWLAsymmetricObjectProperty):
            return self.map_owl_asymmetric_property(value)
        if isinstance(value, OWLTransitiveObjectProperty):
            return self.map_owl_transitive_property(value)
        if isinstance(value, OWLReflexiveObjectProperty):
            return self.map_owl_reflexive_property(value)
        if isinstance(value, OWLIrreflexiveObjectProperty):
            return self.map_owl_irreflexive_property(value)
        if isinstance(value, OWLGeneralClassAxiom):
            return self.map_owl_general_class_axiom(value)
        if isinstance(value, OWLClassExpression):
            return value
        raise TypeError(
            f"Cannot map value of type {type(value)}. "
            "Please provide a valid OWL entity or expression."
        )

    def map_sequence(
        self, sequence: typing.Iterable[typing.Any]
    ) -> list[tuple[URIRef, ...]]:
        if not sequence or len(sequence) == 0:
            return RDF.nil
        if len(sequence) == 1:
            return self.map(sequence[0])
        return [self.map(x) for x in sequence]

    def map_owl_declaration(
        self, declaration: OWLDeclaration
    ) -> typing.Optional[URIRef]:
        if isinstance(declaration.entity, OWLDatatype):
            node = self.map_owl_datatype(declaration.entity)
            self.map_owl_annotations(node, declaration.axiom_annotations)
            return node
        if isinstance(declaration.entity, OWLClass):
            node = self.map_owl_class(declaration.entity)
            self.map_owl_annotations(node, declaration.axiom_annotations)
            return node
        if isinstance(declaration.entity, OWLObjectProperty):
            node = self.map_owl_object_property(declaration.entity)
            self.map_owl_annotations(node, declaration.axiom_annotations)
            return node
        if isinstance(declaration.entity, OWLDataProperty):
            node = self.map_owl_data_property(declaration.entity)
            self.map_owl_annotations(node, declaration.axiom_annotations)
            return node
        if isinstance(declaration.entity, OWLAnnotationProperty):
            node = self.map_owl_annotation_property(declaration.entity)
            self.map_owl_annotations(node, declaration.axiom_annotations)
            return node
        if isinstance(declaration.entity, OWLNamedIndividual):
            node = self.map_owl_named_individual(declaration.entity)
            self.map_owl_annotations(node, declaration.axiom_annotations)
            return node
        if isinstance(declaration.entity, OWLAnonymousIndividual):
            node = self.map_owl_anonymous_individual(declaration.entity)
            self.map_owl_annotations(node, declaration.axiom_annotations)
            return node
        raise TypeError(f"Cannot map value of type {type(declaration.entity)}.")

    def map_owl_annotations(
        self,
        element: typing.Union[OWLEntity, IRI, URIRef],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[URIRef]:
        if not annotations or len(annotations) == 0:
            return None
        _ = [self.map_owl_annotation(element, ann) for ann in annotations]
        return None

    # def map_owl_nested_annotations(
    #     self,
    #     element: URIRef,
    #     annotations: typing.Optional[list[OWLAnnotation]] = None,
    # ) -> None:
    #     for ann in annotations:
    #         self.map_owl_nested_annotation(element, ann)

    # def map_owl_nested_annotation(
    #     self,
    #     element: URIRef,
    #     annotation: OWLAnnotation,
    # ) -> URIRef:
    #     node = BNode()
    #     entity_iri = self.map(element)
    #     prop_iri = self.map(annotation.annotation_property)
    #     value_iri = self.map(annotation.annotation_value)
    #     self.graph.add((entity_iri, prop_iri, value_iri))
    #     self.graph.add((node, RDF.type, OWL.Annotation))
    #     self.graph.add((node, OWL.annotatedSource, entity_iri))
    #     self.graph.add((node, OWL.annotatedProperty, prop_iri))
    #     self.graph.add((node, OWL.annotatedTarget, value_iri))
    #     if annotation.annotation_annotations:
    #         self.map_owl_nested_annotations(node, annotation.annotation_annotations)
    #     return node

    def map_owl_annotation(
        self, element: typing.Union[OWLEntity, IRI, URIRef], annotation: OWLAnnotation
    ) -> typing.Optional[URIRef]:

        if annotation is None:
            return None

        entity_iri = self.map(element)
        prop_iri = self.map(annotation.annotation_property)
        value_iri = self.map(annotation.annotation_value)

        self.graph.add((entity_iri, prop_iri, value_iri))
        if not annotation.annotation_annotations:
            return None

        node = self.map_owl_annotations_entities(element, prop_iri, value_iri)
        _ = self.map_owl_annotations(node, annotation.annotation_annotations)
        return None

    def map_owl_annotations_entities(
        self,
        element1: typing.Union[OWLEntity, IRI, URIRef],
        property: typing.Union[IRI, URIRef],
        element2: typing.Union[OWLEntity, IRI, URIRef],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[URIRef]:
        if not annotations:
            return None

        entity_iri = self.map(element1)
        prop_iri = self.map(property)
        value_iri = self.map(element2)

        node = BNode()
        self.graph.add(
            (node, RDF.type, OWL.Axiom if self.owl1_annotations else OWL.Annotation)
        )
        self.graph.add((node, OWL.annotatedSource, entity_iri))
        self.graph.add((node, OWL.annotatedProperty, prop_iri))
        self.graph.add((node, OWL.annotatedTarget, value_iri))
        _ = self.map_owl_annotations(node, annotations)
        return node

    def map_owl_general_class_axiom(
        self, axiom: OWLGeneralClassAxiom
    ) -> typing.Optional[URIRef]:
        axiom_node = BNode()
        left = self.map(axiom.left_expression)
        property = self.map(axiom.property_iri)
        right = self.map(axiom.right_expression)
        self.graph.add((axiom_node, RDF.type, OWL.Axiom))
        self.graph.add((axiom_node, OWL.annotatedSource, left))
        self.graph.add((axiom_node, OWL.annotatedProperty, property))
        self.graph.add((axiom_node, OWL.annotatedTarget, right))
        self.map_owl_annotations(axiom_node, axiom.axiom_annotations)
        return axiom_node

    def map_owl_data_intersection_of(
        self,
        prop: OWLDataIntersectionOf,
    ) -> typing.Optional[URIRef]:
        intersection = BNode()
        iris = self.map_sequence(prop.data_ranges)
        self.graph.add((intersection, RDF.type, RDFS.Datatype))
        self.graph.add(
            (
                intersection,
                OWL.intersectionOf,
                Collection(self.graph, BNode(), iris).uri,
            )
        )
        return intersection

    def map_owl_data_union_of(
        self,
        prop: OWLDataUnionOf,
    ) -> typing.Optional[URIRef]:
        union = BNode()
        iris = self.map_sequence(prop.data_ranges)
        self.graph.add((union, RDF.type, RDFS.Datatype))
        self.graph.add((union, OWL.unionOf, Collection(self.graph, BNode(), iris).uri))
        return union

    def map_owl_data_complement_of(
        self,
        prop: OWLDataComplementOf,
    ) -> typing.Optional[URIRef]:
        complement = BNode()
        iri = self.map(prop.data_range)
        self.graph.add((complement, RDF.type, RDFS.Datatype))
        self.graph.add((complement, OWL.datatypeComplementOf, iri))
        return complement

    def map_owl_data_one_of(
        self,
        prop: OWLDataOneOf,
    ) -> typing.Optional[URIRef]:
        one_of = BNode()
        iris = self.map_sequence(prop.literals)
        self.graph.add((one_of, RDF.type, RDFS.Datatype))
        self.graph.add((one_of, OWL.oneOf, Collection(self.graph, BNode(), iris).uri))
        return one_of

    def map_owl_object_intersection_of(
        self,
        prop: OWLObjectIntersectionOf,
    ) -> typing.Optional[URIRef]:
        intersection = BNode()
        iris = self.map_sequence(prop.classes_expressions)
        self.graph.add((intersection, RDF.type, OWL.Class))
        self.graph.add(
            (
                intersection,
                OWL.intersectionOf,
                Collection(self.graph, BNode(), iris).uri,
            )
        )
        return intersection

    def map_owl_object_union_of(
        self,
        prop: OWLObjectUnionOf,
    ) -> typing.Optional[URIRef]:
        union = BNode()
        iris = self.map_sequence(prop.classes_expressions)
        self.graph.add((union, RDF.type, OWL.Class))
        self.graph.add((union, OWL.unionOf, Collection(self.graph, BNode(), iris).uri))
        return union

    def map_owl_object_complement_of(
        self,
        prop: OWLObjectComplementOf,
    ) -> typing.Optional[URIRef]:
        complement = BNode()
        iri = self.map(prop.expression)
        self.graph.add((complement, RDF.type, OWL.Class))
        self.graph.add((complement, OWL.complementOf, iri))
        return complement

    def map_owl_object_one_of(
        self,
        prop: OWLObjectOneOf,
    ) -> typing.Optional[URIRef]:
        one_of = BNode()
        iris = self.map_sequence(prop.individuals)
        self.graph.add((one_of, RDF.type, OWL.Class))
        self.graph.add((one_of, OWL.oneOf, Collection(self.graph, BNode(), iris).uri))
        return one_of

    def map_owl_object_some_values_from(
        self,
        prop: OWLObjectSomeValuesFrom,
    ) -> typing.Optional[URIRef]:
        some = BNode()
        obj_iri = self.map(prop.object_property_expression)
        iri = self.map(prop.class_expression)
        self.graph.add((some, RDF.type, OWL.Restriction))
        self.graph.add((some, OWL.onProperty, obj_iri))
        self.graph.add(
            (
                some,
                OWL.someValuesFrom,
                iri,
            )
        )
        return some

    def map_owl_object_all_values_from(
        self,
        prop: OWLObjectAllValuesFrom,
    ) -> typing.Optional[URIRef]:
        all_values = BNode()
        obj_iri = self.map(prop.object_property_expression)
        iri = self.map(prop.class_expression)
        self.graph.add((all_values, RDF.type, OWL.Restriction))
        self.graph.add((all_values, OWL.onProperty, obj_iri))
        self.graph.add(
            (
                all_values,
                OWL.allValuesFrom,
                iri,
            )
        )
        return all_values

    def map_owl_object_has_value(
        self,
        prop: OWLObjectHasValue,
    ) -> typing.Optional[URIRef]:
        has_value = BNode()
        obj_iri = self.map(prop.object_property_expression)
        iri = self.map(prop.individual)
        self.graph.add((has_value, RDF.type, OWL.Restriction))
        self.graph.add((has_value, OWL.onProperty, obj_iri))
        self.graph.add((has_value, OWL.hasValue, iri))
        return has_value

    def map_owl_object_has_self(
        self,
        prop: OWLObjectHasSelf,
    ) -> typing.Optional[URIRef]:
        has_self = BNode()
        obj_iri = self.map(prop.object_property_expression)
        self.graph.add((has_self, RDF.type, OWL.Restriction))
        self.graph.add((has_self, OWL.onProperty, obj_iri))
        self.graph.add((has_self, OWL.hasSelf, Literal(True, datatype=XSD.boolean)))
        return has_self

    def map_owl_object_min_cardinality(
        self,
        prop: OWLObjectMinCardinality,
    ) -> typing.Optional[URIRef]:
        cardinality = BNode()
        obj_iri = self.map(prop.object_property_expression)
        class_iri = None
        if prop.class_expression:
            class_iri = self.map(prop.class_expression)
        self.graph.add((cardinality, RDF.type, OWL.Restriction))
        self.graph.add((cardinality, OWL.onProperty, obj_iri))
        self.graph.add(
            (
                cardinality,
                (
                    OWL.minCardinality
                    if class_iri is None
                    else OWL.minQualifiedCardinality
                ),
                Literal(prop.cardinality, datatype=XSD.nonNegativeInteger),
            )
        )
        if class_iri is not None:
            self.graph.add((cardinality, OWL.onClass, class_iri))
        return cardinality

    def map_owl_object_max_cardinality(
        self,
        prop: OWLObjectMaxCardinality,
    ) -> typing.Optional[URIRef]:
        cardinality = BNode()
        obj_iri = self.map(prop.object_property_expression)
        class_iri = None
        if prop.class_expression:
            class_iri = self.map(prop.class_expression)
        self.graph.add((cardinality, RDF.type, OWL.Restriction))
        self.graph.add((cardinality, OWL.onProperty, obj_iri))
        self.graph.add(
            (
                cardinality,
                (
                    OWL.maxCardinality
                    if class_iri is None
                    else OWL.maxQualifiedCardinality
                ),
                Literal(prop.cardinality, datatype=XSD.nonNegativeInteger),
            )
        )
        if class_iri is not None:
            self.graph.add((cardinality, OWL.onClass, class_iri))
        return cardinality

    def map_owl_object_exact_cardinality(
        self,
        prop: OWLObjectExactCardinality,
    ) -> typing.Optional[URIRef]:
        cardinality = BNode()
        obj_iri = self.map(prop.object_property_expression)
        class_iri = None
        if prop.class_expression:
            class_iri = self.map(prop.class_expression)
        self.graph.add((cardinality, RDF.type, OWL.Restriction))
        self.graph.add((cardinality, OWL.onProperty, obj_iri))
        self.graph.add(
            (
                cardinality,
                (OWL.cardinality if class_iri is None else OWL.qualifiedCardinality),
                Literal(prop.cardinality, datatype=XSD.nonNegativeInteger),
            )
        )
        if class_iri is not None:
            self.graph.add((cardinality, OWL.onClass, class_iri))
        return cardinality

    def map_owl_data_some_values_from(
        self,
        prop: OWLDataSomeValuesFrom,
    ) -> typing.Optional[URIRef]:
        some = BNode()
        obj_iris = self.map_sequence(prop.data_property_expressions)
        iri = self.map(prop.data_range)
        self.graph.add((some, RDF.type, OWL.Restriction))
        self.graph.add(
            (some, OWL.onProperty, obj_iris)
            if len(prop.data_property_expressions) == 1
            else (
                some,
                OWL.onProperties,
                Collection(self.graph, BNode(), obj_iris).uri,
            )
        )
        self.graph.add(
            (
                some,
                OWL.someValuesFrom,
                iri,
            )
        )
        return some

    def map_owl_data_all_values_from(
        self,
        prop: OWLDataAllValuesFrom,
    ) -> typing.Optional[URIRef]:
        all_values = BNode()
        obj_iris = self.map_sequence(prop.data_property_expressions)
        iri = self.map(prop.data_range)
        self.graph.add((all_values, RDF.type, OWL.Restriction))
        self.graph.add(
            (all_values, OWL.onProperty, obj_iris)
            if len(prop.data_property_expressions) == 1
            else (
                all_values,
                OWL.onProperties,
                Collection(self.graph, BNode(), obj_iris).uri,
            )
        )
        self.graph.add(
            (
                all_values,
                OWL.allValuesFrom,
                iri,
            )
        )
        return all_values

    def map_owl_data_has_value(
        self,
        prop: OWLDataHasValue,
    ) -> typing.Optional[URIRef]:
        has_value = BNode()
        obj_iri = self.map(prop.data_property_expression)
        iri = self.map(prop.literal)
        self.graph.add((has_value, RDF.type, OWL.Restriction))
        self.graph.add((has_value, OWL.onProperty, obj_iri))
        self.graph.add(
            (
                has_value,
                OWL.hasValue,
                iri,
            )
        )
        return has_value

    def map_owl_data_min_cardinality(
        self,
        prop: OWLDataMinCardinality,
    ) -> typing.Optional[URIRef]:
        cardinality = BNode()
        obj_iri = self.map(prop.data_property_expression)
        iri = None
        if prop.data_range:
            iri = self.map(prop.data_range)
        self.graph.add((cardinality, RDF.type, OWL.Restriction))
        self.graph.add((cardinality, OWL.onProperty, obj_iri))
        self.graph.add(
            (
                cardinality,
                (
                    OWL.minCardinality
                    if prop.data_range is None
                    else OWL.minQualifiedCardinality
                ),
                Literal(prop.cardinality, datatype=XSD.nonNegativeInteger),
            )
        )
        if iri is not None:
            self.graph.add((cardinality, OWL.onDataRange, iri))
        return cardinality

    def map_owl_data_max_cardinality(
        self,
        prop: OWLDataMaxCardinality,
    ) -> typing.Optional[URIRef]:
        cardinality = BNode()
        obj_iri = self.map(prop.data_property_expression)
        iri = None
        if prop.data_range:
            iri = self.map(prop.data_range)
        self.graph.add((cardinality, RDF.type, OWL.Restriction))
        self.graph.add((cardinality, OWL.onProperty, obj_iri))
        self.graph.add(
            (
                cardinality,
                (
                    OWL.maxCardinality
                    if prop.data_range is None
                    else OWL.maxQualifiedCardinality
                ),
                Literal(prop.cardinality, datatype=XSD.nonNegativeInteger),
            )
        )
        if iri is not None:
            self.graph.add((cardinality, OWL.onDataRange, iri))
        return cardinality

    def map_owl_data_exact_cardinality(
        self,
        prop: OWLDataExactCardinality,
    ) -> typing.Optional[URIRef]:
        cardinality = BNode()
        obj_iri: URIRef = self.map(prop.data_property_expression)
        iri: URIRef = None
        if prop.data_range:
            iri = self.map(prop.data_range)
        self.graph.add((cardinality, RDF.type, OWL.Restriction))
        self.graph.add((cardinality, OWL.onProperty, obj_iri))
        self.graph.add(
            (
                cardinality,
                (
                    OWL.cardinality
                    if prop.data_range is None
                    else OWL.qualifiedCardinality
                ),
                Literal(prop.cardinality, datatype=XSD.nonNegativeInteger),
            )
        )
        if iri is not None:
            self.graph.add((cardinality, OWL.onDataRange, iri))
        return cardinality

    def map_owl_subclass_of(self, subclass: OWLSubClassOf) -> typing.Optional[URIRef]:
        ce1_iri = self.map(subclass.sub_class_expression)
        ce2_iri = self.map(subclass.super_class_expression)
        self.graph.add((ce1_iri, RDFS.subClassOf, ce2_iri))
        self.map_owl_annotations_entities(
            ce1_iri, RDFS.subClassOf, ce2_iri, subclass.axiom_annotations
        )
        return None

    def map_owl_disjoint_union(
        self,
        disjoints: OWLDisjointUnion,
    ) -> typing.Optional[URIRef]:
        cls_iri = self.map(disjoints.union_class)
        iris = self.map_sequence(disjoints.disjoint_class_expressions)
        collect = Collection(self.graph, BNode(), iris)
        self.graph.add((cls_iri, OWL.disjointUnionOf, collect.uri))
        self.map_owl_annotations_entities(
            cls_iri, OWL.disjointUnionOf, collect.uri, disjoints.axiom_annotations
        )
        return None

    def map_owl_subobject_property_of(
        self,
        subclass: OWLSubObjectPropertyOf,
    ) -> typing.Optional[URIRef]:
        if isinstance(subclass.sub_object_property_expression, OWLObjectPropertyChain):
            ce1_iris = self.map_sequence(subclass.sub_object_property_expression.chain)
            ce2_iri = self.map(subclass.super_object_property_expression)
            collect = Collection(self.graph, BNode(), ce1_iris)
            self.graph.add(
                (
                    ce2_iri,
                    OWL.propertyChainAxiom,
                    collect.uri,
                )
            )
            self.map_owl_annotations_entities(
                ce2_iri, OWL.propertyChainAxiom, collect.uri, subclass.axiom_annotations
            )
            return None
        ce1_iri = self.map(subclass.sub_object_property_expression)
        ce2_iri = self.map(subclass.super_object_property_expression)
        self.graph.add((ce1_iri, RDFS.subPropertyOf, ce2_iri))
        self.map_owl_annotations_entities(
            ce1_iri, RDFS.subPropertyOf, ce2_iri, subclass.axiom_annotations
        )
        return None

    def map_owl_equivalent_object_properties(
        self,
        eq: OWLEquivalentObjectProperties,
    ) -> typing.Optional[URIRef]:
        for i in range(len(eq.object_property_expressions) - 1):
            cei_node = self.map(eq.object_property_expressions[i])
            ceii_node = self.map(eq.object_property_expressions[i + 1])
            self.graph.add((cei_node, OWL.equivalentProperty, ceii_node))
            self.map_owl_annotations_entities(
                cei_node, OWL.equivalentProperty, ceii_node, eq.axiom_annotations
            )
        return None

    def map_owl_disjoint_object_properties(
        self,
        disjoints: OWLDisjointObjectProperties,
    ) -> typing.Optional[URIRef]:
        if len(disjoints.object_property_expressions) == 2:
            ce1_node = self.map(disjoints.object_property_expressions[0])
            ce2_node = self.map(disjoints.object_property_expressions[1])
            self.graph.add((ce1_node, OWL.propertyDisjointWith, ce2_node))
            self.map_owl_annotations_entities(
                ce1_node,
                OWL.propertyDisjointWith,
                ce2_node,
                disjoints.axiom_annotations,
            )
            return None

        disjoint = BNode()
        iris = self.map_sequence(disjoints.object_property_expressions)
        self.graph.add((disjoint, RDF.type, OWL.AllDisjointProperties))
        self.graph.add(
            (disjoint, OWL.members, Collection(self.graph, BNode(), iris).uri)
        )
        self.map_owl_annotations(
            disjoint,
            disjoints.axiom_annotations,
        )
        return disjoint

    def map_owl_subdata_property_of(
        self,
        subdata: OWLSubDataPropertyOf,
    ) -> typing.Optional[URIRef]:
        ce1_iri = self.map(subdata.sub_data_property_expression)
        ce2_iri = self.map(subdata.super_data_property_expression)
        self.graph.add((ce1_iri, RDFS.subPropertyOf, ce2_iri))
        self.map_owl_annotations_entities(
            ce1_iri,
            RDFS.subPropertyOf,
            ce2_iri,
            subdata.axiom_annotations,
        )
        return None

    def map_owl_equivalent_data_properties(
        self,
        eq: OWLEquivalentDataProperties,
    ) -> typing.Optional[URIRef]:
        for i in range(len(eq.data_property_expressions) - 1):
            cei_node = self.map(eq.data_property_expressions[i])
            ceii_node = self.map(eq.data_property_expressions[i + 1])
            self.graph.add((cei_node, OWL.equivalentProperty, ceii_node))
            self.map_owl_annotations_entities(
                cei_node,
                OWL.equivalentProperty,
                ceii_node,
                eq.axiom_annotations,
            )
        return None

    def map_owl_disjoint_data_properties(
        self,
        disjoints: OWLDisjointDataProperties,
    ) -> typing.Optional[URIRef]:
        if len(disjoints.data_property_expressions) == 2:
            ce1_node = self.map(disjoints.data_property_expressions[0])
            ce2_node = self.map(disjoints.data_property_expressions[1])
            self.graph.add((ce1_node, OWL.propertyDisjointWith, ce2_node))
            self.map_owl_annotations_entities(
                ce1_node,
                OWL.propertyDisjointWith,
                ce2_node,
                disjoints.axiom_annotations,
            )
            return None

        disjoint_node = BNode()
        classes = self.map_sequence(disjoints.data_property_expressions)
        self.graph.add((disjoint_node, RDF.type, OWL.AllDisjointProperties))
        self.graph.add(
            (disjoint_node, OWL.members, Collection(self.graph, BNode(), classes).uri)
        )
        self.map_owl_annotations(disjoint_node, disjoints.axiom_annotations)
        return disjoint_node

    def map_owl_datatype_definition(
        self,
        datatype_def: OWLDatatypeDefinition,
    ) -> typing.Optional[URIRef]:
        dt_iri = self.map(datatype_def.datatype)
        dr_iri = self.map(datatype_def.data_range)
        self.graph.add((dt_iri, OWL.equivalentClass, dr_iri))
        self.map_owl_annotations_entities(
            dt_iri, OWL.equivalentClass, dr_iri, datatype_def.axiom_annotations
        )
        return None

    def map_owl_has_key(
        self,
        has_key: OWLHasKey,
    ) -> typing.Optional[URIRef]:
        cls_iri = self.map(has_key.class_expression)
        op_iris = self.map_sequence(has_key.object_property_expressions)
        dp_iris = self.map_sequence(has_key.data_property_expressions)
        collect = Collection(self.graph, BNode(), op_iris + dp_iris)
        self.graph.add(
            (
                cls_iri,
                OWL.hasKey,
                collect.uri,
            )
        )
        self.map_owl_annotations_entities(
            cls_iri, OWL.hasKey, collect.uri, has_key.axiom_annotations
        )
        return None

    def map_owl_same_individual(
        self,
        same: OWLSameIndividual,
    ) -> typing.Optional[URIRef]:
        iris = self.map_sequence(same.individuals)
        for i in range(len(iris) - 1):
            self.graph.add((iris[i], OWL.sameAs, iris[i + 1]))
            self.map_owl_annotations_entities(
                iris[i], OWL.sameAs, iris[i + 1], same.axiom_annotations
            )
        return None

    def map_owl_different_individuals(
        self,
        different: OWLDifferentIndividuals,
    ) -> typing.Optional[URIRef]:
        iris = self.map_sequence(different.individuals)
        if len(iris) == 2:
            self.graph.add((iris[0], OWL.differentFrom, iris[1]))
            self.map_owl_annotations_entities(
                iris[0], OWL.differentFrom, iris[1], different.axiom_annotations
            )
            return None
        node = BNode()
        self.graph.add((node, RDF.type, OWL.AllDifferent))
        self.graph.add((node, OWL.members, Collection(self.graph, BNode(), iris).uri))
        self.map_owl_annotations(node, different.axiom_annotations)
        return node

    def map_owl_class_assertion(
        self,
        assertion: OWLClassAssertion,
    ) -> typing.Optional[URIRef]:
        cls_iri = self.map(assertion.class_expression)
        ind_iri = self.map(assertion.individual)
        self.graph.add((ind_iri, RDF.type, cls_iri))
        self.map_owl_annotations_entities(
            ind_iri, RDF.type, cls_iri, assertion.axiom_annotations
        )
        return None

    def map_owl_object_property_assertion(
        self,
        assertion: OWLObjectPropertyAssertion,
    ) -> typing.Optional[URIRef]:
        source_iri = self.map(assertion.source_individual)
        op_iri = self.map(assertion.object_property_expression)
        target_iri = self.map(assertion.target_individual)
        if isinstance(assertion.object_property_expression, OWLInverseObjectProperty):
            self.graph.add((target_iri, op_iri, source_iri))
            self.map_owl_annotations_entities(
                target_iri, op_iri, source_iri, assertion.axiom_annotations
            )
        else:
            self.graph.add((source_iri, op_iri, target_iri))
            self.map_owl_annotations_entities(
                source_iri, op_iri, target_iri, assertion.axiom_annotations
            )
        return None

    def map_owl_negative_object_property_assertion(
        self,
        assertion: OWLNegativeObjectPropertyAssertion,
    ) -> typing.Optional[URIRef]:
        source_iri = self.map(assertion.source_individual)
        op_iri = self.map(assertion.object_property_expression)
        target_iri = self.map(assertion.target_individual)
        node = BNode()
        self.graph.add((node, RDF.type, OWL.NegativePropertyAssertion))
        self.graph.add((node, OWL.sourceIndividual, source_iri))
        self.graph.add((node, OWL.assertionProperty, op_iri))
        self.graph.add((node, OWL.targetIndividual, target_iri))
        self.map_owl_annotations(node, assertion.axiom_annotations)
        return node

    def map_owl_data_property_assertion(
        self,
        assertion: OWLDataPropertyAssertion,
    ) -> typing.Optional[URIRef]:
        dp_iri = self.map(assertion.data_property_expression)
        source_iri = self.map(assertion.source_individual)
        target_iri = self.map(assertion.target_value)
        self.graph.add((source_iri, dp_iri, target_iri))
        self.map_owl_annotations_entities(
            source_iri, dp_iri, target_iri, assertion.axiom_annotations
        )
        return None

    def map_owl_negative_data_property_assertion(
        self,
        assertion: OWLNegativeDataPropertyAssertion,
    ) -> typing.Optional[URIRef]:
        dp_iri = self.map(assertion.data_property_expression)
        source_iri = self.map(assertion.source_individual)
        target_iri = self.map(assertion.target_value)
        node = BNode()
        self.graph.add((node, RDF.type, OWL.NegativePropertyAssertion))
        self.graph.add((node, OWL.sourceIndividual, source_iri))
        self.graph.add((node, OWL.assertionProperty, dp_iri))
        self.graph.add((node, OWL.targetValue, target_iri))
        self.map_owl_annotations(node, assertion.axiom_annotations)
        return node

    def map_owl_annotation_assertion(
        self,
        assertion: OWLAnnotationAssertion,
    ) -> typing.Optional[URIRef]:
        source_iri = self.map(assertion.annotation_subject)
        iri = self.map(assertion.annotation_property)
        target_iri = self.map(assertion.annotation_value)
        self.graph.add((source_iri, iri, target_iri))
        self.map_owl_annotations_entities(
            source_iri, iri, target_iri, assertion.axiom_annotations
        )
        return None

    def map_owl_sub_annotation_property_of(
        self,
        prop: OWLSubAnnotationPropertyOf,
    ) -> typing.Optional[URIRef]:
        sub_iri = self.map(prop.sub_annotation_property)
        super_iri = self.map(prop.super_annotation_property)
        self.graph.add((sub_iri, RDFS.subPropertyOf, super_iri))
        self.map_owl_annotations_entities(
            sub_iri, RDFS.subPropertyOf, super_iri, prop.axiom_annotations
        )
        return None

    def map_owl_annotation_property_domain(
        self,
        prop: OWLAnnotationPropertyDomain,
    ) -> typing.Optional[URIRef]:
        prop_iri = self.map(prop.annotation_property)
        iri = self.map(prop.domain)
        self.graph.add((prop_iri, RDFS.domain, iri))
        self.map_owl_annotations_entities(
            prop_iri, RDFS.domain, iri, prop.axiom_annotations
        )
        return prop_iri

    def map_owl_annotation_property_range(
        self,
        prop: OWLAnnotationPropertyRange,
    ) -> typing.Optional[URIRef]:
        prop_iri = self.map(prop.annotation_property)
        iri = self.map(prop.range)
        self.graph.add((prop_iri, RDFS.range, iri))
        self.map_owl_annotations_entities(
            prop_iri, RDFS.range, iri, prop.axiom_annotations
        )
        return prop_iri

    def map_owl_class(
        self,
        class_: OWLClass,
    ) -> typing.Optional[URIRef]:
        """
        Map an OWL Class to RDF triples.

        :param class_iri: iri of the OWL Class
        :return: tuple of (triples list, class node)
        """
        iri_node = self.map(class_)
        self.graph.add((iri_node, RDF.type, OWL.Class))
        return iri_node

    def map_owl_named_individual(
        self,
        individual: OWLNamedIndividual,
    ) -> typing.Optional[URIRef]:
        """
        Map an OWL Individual to RDF triples.

        :param individual_iri: iri of the OWL Individual
        :return: tuple of (triples list, individual node)
        """
        iri_node = self.map(individual.iri)
        self.graph.add((iri_node, RDF.type, OWL.NamedIndividual))
        return iri_node

    def map_owl_anonymous_individual(
        self,
        individual: OWLAnonymousIndividual,
    ) -> typing.Optional[URIRef]:
        """
        Map an OWL Individual to RDF triples.

        :param individual_iri: iri of the OWL Individual
        :return: tuple of (triples list, individual node)
        """
        iri_node = self.map(individual.node_id)
        self.graph.add((iri_node, RDF.type, OWL.NamedIndividual))
        return iri_node

    def map_owl_object_property_domain(
        self,
        domain: OWLObjectPropertyDomain,
    ) -> typing.Optional[URIRef]:
        prop_iri_node = self.map(domain.object_property_expression)
        iri_node = self.map(domain.class_expression)
        self.graph.add(
            (
                prop_iri_node,
                RDFS.domain,
                iri_node,
            )
        )
        self.map_owl_annotations_entities(
            prop_iri_node, RDFS.domain, iri_node, domain.axiom_annotations
        )
        return prop_iri_node

    def map_owl_object_property_range(
        self,
        range: OWLObjectPropertyRange,
    ) -> typing.Optional[URIRef]:
        prop_iri_node = self.map(range.object_property_expression)
        iri_node = self.map(range.class_expression)
        self.graph.add(
            (
                prop_iri_node,
                RDFS.range,
                iri_node,
            )
        )
        self.map_owl_annotations_entities(
            prop_iri_node, RDFS.range, iri_node, range.axiom_annotations
        )
        return prop_iri_node

    def map_owl_data_property_domain(
        self,
        domain: OWLDataPropertyDomain,
    ) -> typing.Optional[URIRef]:
        prop_iri_node = self.map(domain.data_property_expression)
        iri_node = self.map(domain.class_expression)
        self.graph.add(
            (
                prop_iri_node,
                RDFS.domain,
                iri_node,
            )
        )
        self.map_owl_annotations_entities(
            prop_iri_node, RDFS.domain, iri_node, domain.axiom_annotations
        )
        return prop_iri_node

    def map_owl_data_property_range(
        self,
        range: OWLDataPropertyRange,
    ) -> typing.Optional[URIRef]:
        prop_iri_node = self.map(range.data_property_expression)
        iri_node = self.map(range.data_range)
        self.graph.add(
            (
                prop_iri_node,
                RDFS.range,
                iri_node,
            )
        )
        self.map_owl_annotations_entities(
            prop_iri_node, RDFS.range, iri_node, range.axiom_annotations
        )
        return prop_iri_node

    def map_owl_facets(
        self,
        facets: list[OWLFacet],
    ) -> tuple[list[URIRef], list[URIRef], list[URIRef]]:
        nodes: list[URIRef] = [BNode() for _ in facets]
        uris: list[URIRef] = [f.constraint_to_uriref() for f in facets]
        values: list[URIRef] = [f.value.to_uriref() for f in facets]
        return nodes, uris, values

    def map_owl_datatype_restriction(
        self,
        restriction_type: OWLDatatypeRestriction,
    ) -> URIRef:
        """
        Map an OWL Restriction to RDF triples.

        :param restriction_type: Type of restriction (e.g., OWL.someValuesFrom, OWL.allValuesFrom)
        :return: tuple of (triples list, restriction node)
        """
        restriction_node = BNode()

        datatype = self.map(restriction_type.datatype)
        self.graph.add((restriction_node, RDF.type, RDFS.Datatype))
        self.graph.add((restriction_node, OWL.onDatatype, datatype))
        nodes, uris, values = self.map_owl_facets(restriction_type.restrictions)
        self.graph.add(
            (
                restriction_node,
                OWL.withRestrictions,
                Collection(self.graph, BNode(), nodes).uri,
            )
        )
        for node, uri, value in zip(nodes, uris, values):
            self.graph.add((node, uri, value))
        return restriction_node

    def map_owl_equivalent_classes(
        self,
        eq: OWLEquivalentClasses,
    ) -> typing.Optional[URIRef]:
        """
        Map OWL Equivalent Classes to RDF triples.

        :param eq: First OWL Class
        :return: tuple of (triples list, list of classes)
        """
        for i in range(len(eq.class_expressions) - 1):
            cei_node = self.map(eq.class_expressions[i])
            ceii_node = self.map(eq.class_expressions[i + 1])
            self.graph.add((cei_node, OWL.equivalentClass, ceii_node))
            self.map_owl_annotations_entities(
                cei_node, OWL.equivalentClass, ceii_node, eq.axiom_annotations
            )
        return None

    def map_owl_disjoint_classes(
        self,
        disjoints: OWLDisjointClasses,
    ) -> typing.Optional[URIRef]:
        """
        Map OWL Disjoint Classes to RDF triples.

        :param classes: list of OWL Classes to be declared disjoint
        :return: tuple of (triples list, list of classes)
        """
        # Create a blank node to represent the disjoint classes collection

        if len(disjoints.class_expressions) == 2:
            ce1_node = self.map(disjoints.class_expressions[0])
            ce2_node = self.map(disjoints.class_expressions[1])
            self.graph.add((ce1_node, OWL.disjointWith, ce2_node))
            self.map_owl_annotations_entities(
                ce1_node, OWL.disjointWith, ce2_node, disjoints.axiom_annotations
            )
            return None

        disjoint_node = BNode()
        classes = self.map_sequence(disjoints.class_expressions)
        self.graph.add((disjoint_node, RDF.type, OWL.AllDisjointClasses))
        self.graph.add(
            (
                disjoint_node,
                OWL.members,
                Collection(self.graph, BNode(), classes).uri,
            )
        )
        self.map_owl_annotations(disjoint_node, disjoints.axiom_annotations)
        return disjoint_node

    def map_owl_annotation_property(
        self,
        annotation: OWLAnnotationProperty,
    ) -> typing.Optional[URIRef]:
        iri_node = self.map(annotation)
        self.graph.add((iri_node, RDF.type, OWL.AnnotationProperty))
        return iri_node

    def map_owl_object_inverse_of(
        self,
        prop: OWLInverseObjectProperty,
    ) -> typing.Optional[URIRef]:
        inverse = BNode()
        iri_node = self.map(prop.object_property)
        self.graph.add((inverse, OWL.inverseOf, iri_node))
        return inverse

    def map_owl_inverse_object_properties(
        self,
        prop: OWLInverseObjectProperties,
    ) -> typing.Optional[URIRef]:
        inverse = BNode()
        prop_iri = self.map(prop.object_property_expression)
        inv_prop_iri = self.map(prop.inverse_object_property_expression)
        self.graph.add((prop_iri, OWL.inverseOf, inv_prop_iri))
        return inverse

    def map_owl_object_property(
        self,
        prop: OWLObjectProperty,
    ) -> typing.Optional[URIRef]:
        """
        Map an OWL Object Property to RDF triples.
        """
        iri_node = self.map(prop)
        self.graph.add((iri_node, RDF.type, OWL.ObjectProperty))
        return iri_node

    def map_owl_datatype(self, datatype: OWLDatatype) -> typing.Optional[URIRef]:
        iri_node = self.map(datatype)
        self.graph.add((iri_node, RDF.type, RDFS.Datatype))
        return iri_node

    def map_owl_data_property(self, prop: OWLDataProperty) -> typing.Optional[URIRef]:
        """
        Map an OWL Datatype Property to RDF triples.

        :param property_iri: iri of the OWL Datatype Property
        :return: tuple of (triples list, property node)
        """
        iri_node = self.map(prop)
        self.graph.add((iri_node, RDF.type, OWL.DatatypeProperty))
        return iri_node

    def map_owl_symmetric_property(
        self,
        prop: OWLSymmetricObjectProperty,
    ) -> typing.Optional[URIRef]:
        """
        Map an OWL Symmetric Property to RDF triples.

        :param property_iri: iri of the Symmetric Property
        :return: tuple of (triples list, property node)
        """
        iri = self.map(prop.object_property_expression)
        self.graph.add((iri, RDF.type, OWL.SymmetricProperty))
        self.map_owl_annotations(iri, prop.axiom_annotations)
        return iri

    def map_owl_transitive_property(
        self,
        prop: OWLTransitiveObjectProperty,
    ) -> typing.Optional[URIRef]:
        """
        Map an OWL Transitive Property to RDF triples.

        :param property_iri: iri of the Transitive Property
        :return: tuple of (triples list, property node)
        """
        iri = self.map(prop.object_property_expression)
        self.graph.add((iri, RDF.type, OWL.TransitiveProperty))
        self.map_owl_annotations(iri, prop.axiom_annotations)
        return iri

    def map_owl_asymmetric_property(
        self,
        prop: OWLAsymmetricObjectProperty,
    ) -> typing.Optional[URIRef]:
        """
        Map an OWL Asymmetric Property to RDF triples.

        :param property_iri: iri of the Transitive Property
        :return: tuple of (triples list, property node)
        """
        iri = self.map(prop.object_property_expression)
        self.graph.add((iri, RDF.type, OWL.AsymmetricProperty))
        self.map_owl_annotations(iri, prop.axiom_annotations)
        return iri

    def map_owl_reflexive_property(
        self,
        prop: OWLReflexiveObjectProperty,
    ) -> typing.Optional[URIRef]:
        """
        Map an OWL Reflexive Property to RDF triples.

        :param property_iri: iri of the Transitive Property
        :return: tuple of (triples list, property node)
        """
        iri = self.map(prop.object_property_expression)
        self.graph.add((iri, RDF.type, OWL.ReflexiveProperty))
        self.map_owl_annotations(iri, prop.axiom_annotations)
        return iri

    def map_owl_irreflexive_property(
        self,
        prop: OWLIrreflexiveObjectProperty,
    ) -> typing.Optional[URIRef]:
        """
        Map an OWL Irreflexive Property to RDF triples.

        :param property_iri: iri of the Transitive Property
        :return: tuple of (triples list, property node)
        """
        iri = self.map(prop.object_property_expression)
        self.graph.add((iri, RDF.type, OWL.IrreflexiveProperty))
        self.map_owl_annotations(iri, prop.axiom_annotations)
        return iri

    def map_owl_functional_property(
        self,
        prop: typing.Union[OWLFunctionalDataProperty, OWLFunctionalObjectProperty],
    ) -> typing.Optional[URIRef]:
        """
        Map an OWL Functional Property to RDF triples.

        :param property_iri: iri of the Transitive Property
        :return: tuple of (triples list, property node)
        """
        iri = (
            self.map(prop.object_property_expression)
            if isinstance(prop, OWLFunctionalObjectProperty)
            else self.map(prop.data_property_expression)
        )
        self.graph.add((iri, RDF.type, OWL.FunctionalProperty))
        self.map_owl_annotations(iri, prop.axiom_annotations)
        return iri

    def map_owl_inverse_functional_property(
        self,
        prop: OWLInverseFunctionalObjectProperty,
    ) -> typing.Optional[URIRef]:
        """
        Map an OWL Inverse Functional Property to RDF triples.

        :param property_iri: iri of the Transitive Property
        :return: tuple of (triples list, property node)
        """
        iri = self.map(prop.object_property_expression)
        self.graph.add((iri, RDF.type, OWL.InverseFunctionalProperty))
        self.map_owl_annotations(iri, prop.axiom_annotations)
        return iri


# Example usage
def example_usage():
    # Create a graph

    # Define some example namespaces
    ex = Namespace("http://example.org/")
    world = owlready2.World()
    ontology = world.get_ontology(ex)
    with ontology:
        g = world.as_rdflib_graph()

        mapper = RDFXMLMapper(g)

        cls = OWLClass(IRI(ex, "Person"))
        ind = OWLNamedIndividual(IRI(ex, "John"))
        ind2 = OWLNamedIndividual(IRI(ex, "Alex"))
        cls_ind = OWLClassAssertion(cls, ind)
        cls_ind2 = OWLClassAssertion(cls, ind2)
        ann_prop = OWLAnnotationProperty(IRI(ex, "new_label"))
        prop = OWLObjectProperty(IRI(ex, "knows"))
        domain = OWLObjectPropertyDomain(prop, cls)
        range = OWLObjectPropertyRange(prop, cls)

        mapper.map_owl_annotation(
            URIRef("http://example.org/"), OWLAnnotation(ann_prop, Literal("Suca"))
        )

        mapper.map_owl_class(cls)
        mapper.map_owl_class_assertion(cls_ind)
        mapper.map_owl_class_assertion(cls_ind2)
        mapper.map_owl_object_property(prop)
        mapper.map_owl_object_property_domain(domain)
        mapper.map_owl_object_property_range(range)
        mapper.map_owl_annotation_property(ann_prop)
        mapper.map_owl_object_property_assertion(
            OWLObjectPropertyAssertion(
                prop, ind, ind2, [OWLAnnotation(ann_prop, Literal("I know"))]
            )
        )

    # Print the graph
    print(g.serialize(format="turtle"))

    ontology.save("./test.owl", format="rdfxml")


if __name__ == "__main__":
    example_usage()
