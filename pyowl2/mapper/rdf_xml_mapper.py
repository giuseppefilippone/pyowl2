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


# @utils.timer_decorator
class RDFXMLMapper:
    """
    This class serves as a utility for translating OWL ontology constructs into RDF triples within an RDFLib Graph instance. It is designed to handle a wide array of OWL elements, including classes, properties, individuals, and complex axioms such as restrictions, intersections, and unions. By initializing the mapper with a target graph and an optional flag to enforce OWL 1 annotation compatibility, users can populate the graph by passing OWL objects to the `map` method, which intelligently dispatches to specific handlers based on the input type. The process involves generating appropriate URI references or blank nodes for entities and adding the corresponding triples to the graph, thereby enabling the serialization or manipulation of OWL data in a standard RDF format.

    :param graph: The RDFLib Graph instance that stores the RDF triples generated from OWL concepts.
    :type graph: Graph
    :param owl1_annotations: A boolean flag indicating whether to use OWL 1 annotation structures. When True, the mapper uses `owl:Axiom` for annotated axioms; otherwise, it uses the OWL 2 `owl:Annotation` class.
    :type owl1_annotations: bool

    :raises TypeError: Raised when the input value is not a recognized OWL entity, expression, or RDFLib type, preventing it from being mapped to an RDF triple.
    """

    def __init__(self, graph: Graph, OWL1_annotations: bool = False) -> None:
        """
        Sets up the mapper instance by storing the provided RDFLib Graph object as the target for RDF triple generation and mapping operations. It configures the internal behavior regarding annotations based on the optional boolean flag, which determines whether to utilize OWL 1 annotation syntax or default to a different standard. This initialization ensures that all subsequent processing performed by the instance is directed toward the specified graph and adheres to the chosen annotation compatibility level.

        :param graph: The RDFLib Graph instance to which OWL concepts are mapped as RDF triples.
        :type graph: Graph
        :param OWL1_annotations: Determines whether to use OWL 1 annotation syntax during the mapping process.
        :type OWL1_annotations: bool
        """

        self._graph: Graph = graph
        self._owl1_annotations: bool = OWL1_annotations

    @property
    def graph(self) -> Graph:
        """
        Returns the underlying RDF graph instance associated with the mapper. This property provides direct access to the internal `_graph` attribute, which serves as the primary data structure for storing and manipulating RDF triples. Because the actual graph object is returned rather than a copy, any modifications made to the returned instance will directly alter the state of the mapper.

        :return: The Graph object associated with this instance.

        :rtype: Graph
        """

        return self._graph

    @property
    def owl1_annotations(self) -> bool:
        """
        This property indicates whether the RDF/XML mapper is configured to handle annotations according to the OWL 1 specification. It acts as a read-only accessor for the internal `_owl1_annotations` flag, returning a boolean value that determines the specific annotation semantics used during mapping operations. Since this is a property getter, it does not modify the state of the mapper.

        :return: True if OWL 1 annotations are enabled, False otherwise.

        :rtype: bool
        """

        return self._owl1_annotations

    def map(
        self,
        value: typing.Optional[
            typing.Union[BNode, IRI, str, URIRef, Literal, OWLObject]
        ],
    ) -> typing.Optional[URIRef]:
        """
        Converts a diverse range of input types—including OWL entities, axioms, expressions, and basic RDF primitives—into corresponding RDFLib nodes suitable for graph construction. When the input is `None` or falsy, the method generates and returns a new blank node. For standard RDF types like `IRI`, `URIRef`, `BNode`, and `Literal`, it performs necessary conversions or returns the value directly. The method serves as a dispatcher for complex OWL constructs, inspecting the type of the input object and delegating the mapping logic to specialized helper methods tailored to specific axioms or expressions (such as intersections, unions, or restrictions). If the input is a string, it is cast to a `URIRef`, and if it is an iterable, it is processed as a sequence. Finally, if the input type is unsupported or invalid, a `TypeError` is raised.

        :param value: The OWL entity, expression, or RDF term to be mapped. Accepts a wide range of types including IRIs, strings, literals, blank nodes, and complex OWL axioms. If the value is None or falsy, a new blank node is generated.
        :type value: typing.Optional[typing.Union[BNode, IRI, str, URIRef, Literal, OWLObject]]

        :raises TypeError: Raised when the input value is not a recognized OWL entity, expression, or supported primitive type, or if an object's 'iri' attribute is not an IRI or URIRef.

        :return: The RDFLib node (URIRef, BNode, or Literal) representing the input value in the RDF graph, suitable for use as a subject or object in RDF triples.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method processes an iterable of OWL entities or expressions, converting each element into its corresponding RDF representation by delegating to the `map` method. The specific return value depends on the size of the input sequence: if the sequence is empty or None, the method returns `RDF.nil` to represent an empty RDF collection. If the sequence contains exactly one element, the method returns the mapped result of that element directly, rather than wrapping it in a list. For sequences containing multiple elements, the method returns a list of mapped results, preserving the order of the original input.

        :param sequence: An iterable of OWL entities or expressions to be mapped to RDFLib URIRefs. An empty or None input results in RDF.nil.
        :type sequence: typing.Iterable[typing.Any]

        :return: A list of mapped RDFLib URIRefs corresponding to the input OWL entities or expressions. Returns RDF.nil if the input sequence is empty, or the mapped element directly if the sequence contains a single item.

        :rtype: list[tuple[URIRef, ...]]
        """

        if not sequence or len(sequence) == 0:
            return RDF.nil
        if len(sequence) == 1:
            return self.map(sequence[0])
        return [self.map(x) for x in sequence]

    def map_owl_declaration(
        self, declaration: OWLDeclaration
    ) -> typing.Optional[URIRef]:
        """
        Processes an OWL declaration by inspecting the type of the entity being declared and delegating to the appropriate specific mapping method, such as those for classes, datatypes, or properties. After obtaining the RDF node representing the entity, the method ensures that any annotations associated with the declaration axiom are added to the graph. It returns the URI reference of the mapped entity, but raises a TypeError if the entity type is not recognized or supported.

        :param declaration: The OWL declaration to be mapped, encapsulating the entity to be declared and any associated annotations.
        :type declaration: OWLDeclaration

        :raises TypeError: Raised when the entity contained in the declaration is not a recognized OWL type supported for mapping.

        :return: The RDFLib URIRef representing the OWL entity being declared. This node serves as the subject of the declaration and is used to attach any associated annotations in the RDF graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method serializes a collection of OWL annotations into the underlying RDF graph by attaching them to a specified subject element. It accepts an OWL entity, IRI, or URIRef as the subject and an optional list of OWLAnnotation instances. If the annotation list is None or empty, the method performs no action and returns immediately. When annotations are present, the method iterates through the list and invokes `map_owl_annotation` for each item to generate the corresponding RDF triples. The operation relies on side effects to modify the graph and always returns None.

        :param element: The OWL entity, IRI, or URIRef serving as the subject to which the annotations are attached in the RDF graph.
        :type element: typing.Union[OWLEntity, IRI, URIRef]
        :param annotations: The OWL annotations to be mapped to RDF triples and attached to the element.
        :type annotations: typing.Optional[list[OWLAnnotation]]

        :return: None, as the method performs side effects on the graph without returning a value.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method converts an OWL annotation into RDF triples within the graph, attaching it to the specified element. It resolves the element, annotation property, and annotation value to their RDF representations and adds a triple to the graph. If the annotation contains nested annotations, the method reifies the statement to create a dedicated node and recursively processes the nested annotations, attaching them to this new node. The method modifies the graph as a side effect and returns None, performing no operation if the provided annotation is None.

        :param element: The OWL entity, IRI, or URIRef to which the annotation is attached, serving as the subject of the generated RDF triples.
        :type element: typing.Union[OWLEntity, IRI, URIRef]
        :param annotation: The OWL annotation to be mapped to RDF triples. It provides the property-value pair attached to the element and may contain nested annotations that are processed recursively.
        :type annotation: OWLAnnotation

        :return: None, as the method modifies the graph in place by adding the annotation triples.

        :rtype: typing.Optional[URIRef]
        """

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
        """
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
        """

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
        """
        This method maps an OWL general class axiom into the RDF graph by creating a reified axiom structure using a blank node. It adds triples to the graph that define this node as an `owl:Axiom`, linking it to the mapped representations of the axiom's left expression, property IRI, and right expression via `owl:annotatedSource`, `owl:annotatedProperty`, and `owl:annotatedTarget` predicates. Furthermore, the method ensures that any annotations attached to the axiom are processed and associated with the generated axiom node. Finally, it returns the blank node that serves as the identifier for this axiom in the graph.

        :param axiom: The OWL general class axiom to be mapped, containing a left expression, a property IRI, a right expression, and any associated annotations.
        :type axiom: OWLGeneralClassAxiom

        :return: The blank node identifier representing the reified OWL general class axiom in the RDF graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL data intersection expression into its corresponding RDF representation within the mapper's graph. The method creates a blank node to represent the intersection, asserts it as an `rdfs:Datatype`, and links it to an RDF collection of the constituent data ranges using the `owl:intersectionOf` property. This operation has the side effect of adding these triples directly to the graph. The blank node identifier representing the intersection is returned to facilitate further mapping operations.

        :param prop: The OWL data intersection axiom containing the sequence of data ranges to be mapped to the RDF graph.
        :type prop: OWLDataIntersectionOf

        :return: The RDFLib URIRef (a blank node) representing the data intersection class expression added to the graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL data union expression into its corresponding RDF representation within the mapper's graph. The method instantiates a blank node to serve as the subject of the union, types it as `rdfs:Datatype`, and links it to an RDF collection containing the mapped data ranges via the `owl:unionOf` property. This process involves recursively mapping the constituent data ranges to ensure the complete structure is serialized. As a side effect, the method directly mutates the internal graph by adding these triples. It returns the blank node identifier representing the union structure, which can be used to reference this data range definition elsewhere in the graph.

        :param prop: The OWL data union expression to be mapped, consisting of a sequence of data ranges that define the union.
        :type prop: OWLDataUnionOf

        :return: A blank node (BNode) representing the data union axiom in the RDF graph. This node serves as the subject for the triples defining the union of the input data ranges.

        :rtype: typing.Optional[URIRef]
        """

        union = BNode()
        iris = self.map_sequence(prop.data_ranges)
        self.graph.add((union, RDF.type, RDFS.Datatype))
        self.graph.add((union, OWL.unionOf, Collection(self.graph, BNode(), iris).uri))
        return union

    def map_owl_data_complement_of(
        self,
        prop: OWLDataComplementOf,
    ) -> typing.Optional[URIRef]:
        """
        Maps an OWL data complement expression to an RDF representation by creating a blank node and adding triples to the graph. The method recursively resolves the nested data range to its corresponding IRI, then asserts that the blank node is an `rdfs:Datatype` linked to that IRI via the `owl:datatypeComplementOf` property. This operation modifies the internal graph and returns the blank node identifier representing the complement structure. The method relies on the successful mapping of the nested data range to generate valid triples.

        :param prop: The OWL data complement expression to be mapped. It encapsulates the data range that is being complemented, which is used to generate the corresponding RDF triples.
        :type prop: OWLDataComplementOf

        :return: Returns the blank node identifier representing the OWL data complement data range in the RDF graph, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
        """

        complement = BNode()
        iri = self.map(prop.data_range)
        self.graph.add((complement, RDF.type, RDFS.Datatype))
        self.graph.add((complement, OWL.datatypeComplementOf, iri))
        return complement

    def map_owl_data_one_of(
        self,
        prop: OWLDataOneOf,
    ) -> typing.Optional[URIRef]:
        """
        This method maps an OWL `DataOneOf` axiom, which defines a datatype restricted to a specific set of literal values, into the RDF graph managed by the mapper. It creates a new blank node to represent the datatype and asserts that it is an instance of `rdfs:Datatype`. The literals contained within the axiom are converted into an RDF collection (list) via an internal sequence mapping, and this collection is linked to the blank node using the `owl:oneOf` predicate. This process modifies the graph by adding the necessary triples to define the enumerated datatype. The method returns the blank node identifier representing the axiom, which can be used as a reference for further mapping operations.

        :param prop: The OWL data one-of expression to be mapped, consisting of a set of literals that define an enumerated data range.
        :type prop: OWLDataOneOf

        :return: The blank node representing the data range in the RDF graph corresponding to the OWL data one-of axiom.

        :rtype: typing.Optional[URIRef]
        """

        one_of = BNode()
        iris = self.map_sequence(prop.literals)
        self.graph.add((one_of, RDF.type, RDFS.Datatype))
        self.graph.add((one_of, OWL.oneOf, Collection(self.graph, BNode(), iris).uri))
        return one_of

    def map_owl_object_intersection_of(
        self,
        prop: OWLObjectIntersectionOf,
    ) -> typing.Optional[URIRef]:
        """
        This method maps an OWL object intersection-of axiom to an RDF representation by creating a blank node to represent the intersection class. It processes the constituent class expressions by mapping them into a sequence and linking this sequence to the blank node via the `owl:intersectionOf` property, utilizing an RDF Collection to store the operands. The operation modifies the internal RDF graph by adding the necessary triples to define the class and its structure. Finally, the method returns the blank node identifier for the intersection class, which serves as the reference for this complex class definition.

        :param prop: The OWL class expression representing an intersection of a set of class expressions to be mapped to RDF triples.
        :type prop: OWLObjectIntersectionOf

        :return: The blank node identifier representing the OWL object intersection class in the RDF graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL object union-of axiom into an RDF representation by generating a blank node to represent the anonymous class defined by the union. The method processes the constituent class expressions into an RDF collection and adds triples to the graph to establish the blank node as an `owl:Class` linked to this collection via the `owl:unionOf` property. This operation directly modifies the underlying graph structure and returns the blank node identifier that serves as the subject for the union class.

        :param prop: The OWL object union-of class expression containing the set of class expressions to be mapped to RDF.
        :type prop: OWLObjectUnionOf

        :return: The blank node (BNode) representing the OWL union class in the RDF graph, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
        """

        union = BNode()
        iris = self.map_sequence(prop.classes_expressions)
        self.graph.add((union, RDF.type, OWL.Class))
        self.graph.add((union, OWL.unionOf, Collection(self.graph, BNode(), iris).uri))
        return union

    def map_owl_object_complement_of(
        self,
        prop: OWLObjectComplementOf,
    ) -> typing.Optional[URIRef]:
        """
        This method maps an OWL object complement-of axiom to RDF triples by creating a blank node to represent the complement class. It recursively processes the nested class expression to obtain its IRI and then adds triples to the graph, defining the blank node as an `owl:Class` and linking it to the nested expression via the `owl:complementOf` property. As a side effect, this method mutates the internal graph with these new triples and returns the blank node identifier representing the complement class.

        :param prop: The OWL object complement-of class expression to be serialized into the RDF graph. It encapsulates the operand class expression that defines the complement.
        :type prop: OWLObjectComplementOf

        :return: The blank node identifier representing the complement class added to the RDF graph.

        :rtype: typing.Optional[URIRef]
        """

        complement = BNode()
        iri = self.map(prop.expression)
        self.graph.add((complement, RDF.type, OWL.Class))
        self.graph.add((complement, OWL.complementOf, iri))
        return complement

    def map_owl_object_one_of(
        self,
        prop: OWLObjectOneOf,
    ) -> typing.Optional[URIRef]:
        """
        Converts an OWL ObjectOneOf axiom into an equivalent RDF structure by creating a blank node to represent the enumerated class. It processes the set of individuals associated with the axiom, mapping them into an RDF collection sequence, and adds triples to the graph to define the blank node as an `owl:Class` linked to this collection via the `owl:oneOf` property. This operation modifies the underlying graph as a side effect and returns the URI reference of the generated blank node, which serves as the subject for the newly created class definition.

        :param prop: The class expression representing an enumeration of individuals to be mapped to an RDF collection.
        :type prop: OWLObjectOneOf

        :return: The blank node representing the anonymous OWL class defined by the object one-of axiom.

        :rtype: typing.Optional[URIRef]
        """

        one_of = BNode()
        iris = self.map_sequence(prop.individuals)
        self.graph.add((one_of, RDF.type, OWL.Class))
        self.graph.add((one_of, OWL.oneOf, Collection(self.graph, BNode(), iris).uri))
        return one_of

    def map_owl_object_some_values_from(
        self,
        prop: OWLObjectSomeValuesFrom,
    ) -> typing.Optional[URIRef]:
        """
        This method translates an OWL object some-values-from restriction into an RDF representation by creating a blank node to represent the anonymous restriction class. It adds triples to the graph to define this node as an `owl:Restriction`, linking it to the mapped object property via `owl:onProperty` and the mapped class expression via `owl:someValuesFrom`. The method modifies the internal graph state as a side effect and returns the blank node identifier for the restriction.

        :param prop: Represents an OWL existential restriction consisting of an object property expression and a class expression, defining a class of individuals that have at least one relationship via the property to an instance of the specified class.
        :type prop: OWLObjectSomeValuesFrom

        :return: The blank node identifier representing the `owl:Restriction` created in the graph, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method maps an OWL object all-values-from restriction to its RDF representation by generating a blank node and populating the graph with the necessary triples. It recursively resolves the object property expression and class expression contained within the input axiom to obtain their RDF identifiers. These identifiers are then used to assert that the blank node is an `owl:Restriction` with a specific `owl:onProperty` and `owl:allValuesFrom` constraint. The method returns the blank node identifier, serving as the subject for the newly created restriction structure.

        :param prop: An OWL class expression representing an ObjectAllValuesFrom restriction, which defines that all values of a specific object property must belong to a given class expression.
        :type prop: OWLObjectAllValuesFrom

        :return: The Blank Node identifier of the OWL restriction created in the graph representing the all-values-from axiom.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method translates an OWL object has-value restriction into RDF triples within the graph. It creates a blank node to serve as the subject of the restriction, then maps the constituent object property expression and individual to their RDF equivalents. The resulting triples assert that this blank node is an `owl:Restriction` defined by a specific `owl:onProperty` and `owl:hasValue`. As a side effect, these triples are added directly to the graph, and the blank node identifier is returned to reference the newly created restriction.

        :param prop: The OWL object has-value restriction to be mapped, consisting of an object property expression and a specific individual filler.
        :type prop: OWLObjectHasValue

        :return: The subject node (URIRef or BNode) of the OWL restriction added to the graph, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL object has-self axiom into an RDF representation by creating a blank node representing an `owl:Restriction`. It retrieves the IRI of the associated object property expression and adds triples to the graph defining the restriction's type, the property it applies to via `owl:onProperty`, and the `owl:hasSelf` condition set to a literal boolean true. This method modifies the underlying graph directly and returns the blank node identifier for the newly created restriction.

        :param prop: The has-self axiom to be mapped, containing the object property expression required to generate the RDF restriction.
        :type prop: OWLObjectHasSelf

        :return: The blank node identifier representing the OWL restriction created in the graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method translates an OWL object minimum cardinality restriction into an RDF representation by adding triples to the internal graph. It creates a blank node to serve as the subject of the restriction and maps the provided object property expression to define the property being constrained. If the input includes a specific class expression, the method uses `owl:minQualifiedCardinality` and links the restriction to that class via `owl:onClass`; otherwise, it uses the standard `owl:minCardinality`. The cardinality value is added as a typed literal, and the blank node identifier is returned to reference the newly created restriction structure.

        :param prop: The OWL object min cardinality expression to be mapped to RDF triples, containing the object property, minimum cardinality value, and an optional class expression.
        :type prop: OWLObjectMinCardinality

        :return: The blank node representing the OWL restriction added to the graph to encode the minimum cardinality constraint.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method translates an OWL object max cardinality restriction into RDF triples within the graph. It creates a blank node to represent the restriction and asserts it is an instance of `owl:Restriction`. The method maps the associated object property expression and links it using `owl:onProperty`, then sets the cardinality limit using `owl:maxCardinality` or `owl:maxQualifiedCardinality` depending on whether a class expression is present. If a class expression is provided, it is mapped and linked via `owl:onClass` to define a qualified restriction. The method returns the blank node identifier for the newly created restriction.

        :param prop: The OWL object max cardinality restriction to be mapped to the RDF graph, encapsulating the object property, the maximum cardinality value, and an optional class expression.
        :type prop: OWLObjectMaxCardinality

        :return: The blank node identifier of the restriction node created in the graph to represent the max cardinality axiom.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Maps an OWL object exact cardinality restriction to an equivalent set of RDF triples within the graph. The method instantiates a blank node to represent the restriction and adds triples declaring it as an `owl:Restriction` linked to the specified object property via `owl:onProperty`. It handles both qualified and unqualified restrictions by using `owl:qualifiedCardinality` and `owl:onClass` when a class expression is present, or `owl:cardinality` when it is absent. The process modifies the graph directly and returns the blank node identifier for the created restriction.

        :param prop: The OWL exact cardinality restriction to be mapped to RDF triples, specifying the object property, the exact number of relationships, and an optional class expression.
        :type prop: OWLObjectExactCardinality

        :return: The URIRef (specifically a blank node) identifying the restriction node created in the graph to represent the exact cardinality axiom.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method converts an OWL data some values from restriction into a corresponding RDF structure within the graph. It generates a blank node to represent the restriction and asserts its type as `owl:Restriction`. The method processes the input's data property expressions and data range, adding triples to link the restriction to the specific data range via `owl:someValuesFrom`. Depending on the number of data property expressions provided, it either assigns the property directly using `owl:onProperty` for a single expression or creates an RDF collection and uses `owl:onProperties` for multiple expressions. As a side effect, this method modifies the internal graph by adding these triples and returns the blank node identifier for the newly created restriction.

        :param prop: The OWL data some values from restriction to be mapped to RDF triples, containing data property expressions and a data range.
        :type prop: OWLDataSomeValuesFrom

        :return: The Blank Node representing the OWL Restriction created in the graph for the specified data some values from axiom.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL data all-values-from restriction into its corresponding RDF representation within the graph. The method creates a blank node to represent the restriction and adds triples asserting its type as `owl:Restriction`. It handles the mapping of the data property expressions by using `owl:onProperty` for a single expression or `owl:onProperties` (via an RDF collection) for multiple expressions. Finally, it links the restriction to the mapped data range using the `owl:allValuesFrom` predicate, modifying the graph state and returning the identifier of the restriction node.

        :param prop: The OWL data all-values-from restriction to be mapped to RDF triples, consisting of one or more data property expressions and a data range.
        :type prop: OWLDataAllValuesFrom

        :return: The RDFLib URIRef (specifically a Blank Node) identifying the `owl:Restriction` node created in the graph to represent the axiom.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL data has value restriction into its corresponding RDF representation within the graph. The method instantiates a new blank node to serve as the subject of the restriction and recursively maps the associated data property expression and literal value to RDF terms. It then populates the graph with triples defining the blank node as an `owl:Restriction`, linking it to the property via `owl:onProperty` and to the literal via `owl:hasValue`. As a side effect, this method mutates the internal graph by adding these triples. The identifier of the newly created blank node representing the restriction is returned.

        :param prop: The OWL data has value axiom to map, consisting of a data property expression and a specific literal value.
        :type prop: OWLDataHasValue

        :return: The blank node identifier representing the OWL restriction in the graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Translates an OWL data minimum cardinality restriction into RDF triples and inserts them into the graph. The method creates a blank node representing the restriction and establishes its type as `owl:Restriction`. It links this node to the specified data property and sets the minimum cardinality value, using `owl:minCardinality` for unqualified restrictions or `owl:minQualifiedCardinality` if a specific data range is defined. When a data range is present, the method also adds a triple linking the restriction to that range. This process modifies the internal graph state and returns the blank node identifier for the newly created restriction.

        :param prop: The OWL data min cardinality restriction to be mapped to RDF triples, comprising the data property, the minimum cardinality value, and an optional data range.
        :type prop: OWLDataMinCardinality

        :return: The blank node identifier of the restriction node created in the graph to represent the OWL data min cardinality axiom.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Maps an OWL data maximum cardinality restriction to an RDF representation by creating a blank node and populating the internal graph with the necessary triples. The method determines whether to use a qualified or unqualified restriction based on the presence of a data range; if a data range is provided, it utilizes `owl:maxQualifiedCardinality` and `owl:onDataRange`, otherwise it defaults to `owl:maxCardinality`. It recursively resolves the IRI for the data property expression and the optional data range. The function returns the blank node representing the restriction, having modified the graph as a side effect.

        :param prop: The OWL data max cardinality axiom to be mapped to RDF triples. It encapsulates the data property expression, the maximum cardinality value, and an optional data range.
        :type prop: OWLDataMaxCardinality

        :return: The blank node identifier representing the restriction created in the graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method maps an OWL data exact cardinality restriction to RDF triples within the graph. It creates a blank node to represent the restriction and adds triples defining it as an `owl:Restriction` linked to the specific data property. The mapping logic adapts based on the presence of a data range: if a data range is provided, it uses `owl:qualifiedCardinality` and includes an `owl:onDataRange` triple; otherwise, it uses `owl:cardinality`. The method modifies the graph by adding these triples and returns the blank node identifier for the restriction.

        :param prop: The OWL data exact cardinality axiom to map, consisting of a data property expression, a specific cardinality value, and an optional data range.
        :type prop: OWLDataExactCardinality

        :return: The blank node identifier representing the restriction added to the graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Translates an OWL subclass axiom into RDF triples and adds them to the internal graph. The method resolves the subclass and superclass expressions into their corresponding IRIs and asserts a relationship using the `rdfs:subClassOf` predicate. It also processes any annotations associated with the axiom, linking them to the generated triple structure. This operation modifies the graph directly as a side effect and returns None.

        :param subclass: The OWL subclass axiom to be mapped to the RDF graph, containing the sub-class and super-class expressions that define the relationship along with any associated annotations.
        :type subclass: OWLSubClassOf

        :return: None, as the method modifies the graph in place and does not return a reference to the created axiom.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Maps an OWL disjoint union axiom to the internal RDF graph by generating the necessary triples to represent the relationship between a union class and its disjoint components. The method creates an RDF collection to hold the mapped IRIs of the disjoint class expressions and asserts an `owl:disjointUnionOf` property linking the union class to this collection. It also processes and attaches any annotations associated with the axiom to the graph. This operation mutates the graph state as a side effect and returns None.

        :param disjoints: The OWL disjoint union axiom to map, consisting of a union class and a set of mutually disjoint class expressions.
        :type disjoints: OWLDisjointUnion

        :return: None, as the method modifies the graph in place.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method maps an OWL sub-object property axiom to RDF triples within the graph, handling both standard sub-property relationships and property chains. When the sub-property is a chain, it generates an RDF collection representing the sequence and connects the super-property via `owl:propertyChainAxiom`; for simple properties, it creates a direct `rdfs:subPropertyOf` assertion. The method also serializes any axiom annotations, resulting in direct modifications to the graph state.

        :param subclass: An OWL axiom asserting that one object property is a subproperty of another, containing the sub-property and super-property expressions along with any annotations to be mapped to the RDF graph.
        :type subclass: OWLSubObjectPropertyOf

        :return: None, as the method modifies the graph in place to add the subobject property axiom.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method processes an OWL equivalent object properties axiom by generating RDF triples that represent the equivalence relationships between the specified object properties. It iterates through the list of property expressions, creating an `owl:equivalentProperty` link between each adjacent pair to ensure a complete chain of equivalence. Any annotations associated with the axiom are also mapped and attached to the generated triples. The operation directly modifies the underlying RDF graph and returns None; if the input contains fewer than two properties, no triples are generated.

        :param eq: An OWL axiom asserting the equivalence of a set of object properties. The method extracts the property expressions and annotations from this axiom to generate the corresponding RDF triples.
        :type eq: OWLEquivalentObjectProperties

        :return: None, as the method modifies the graph in place.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Maps an OWL disjoint object properties axiom to the RDF graph by generating triples that represent the mutual exclusivity of the specified object properties. The method distinguishes between binary and N-ary disjointness: if exactly two properties are provided, it establishes a direct relationship using the `owl:propertyDisjointWith` predicate; otherwise, it creates an `owl:AllDisjointProperties` blank node containing the properties as members. In both scenarios, any associated axiom annotations are mapped to the graph, attached either to the specific relationship or the axiom node. The method returns the blank node identifier for N-ary axioms or None for binary axioms.

        :param disjoints: Represents an OWL axiom asserting that a collection of object properties are mutually disjoint. The method extracts the property expressions from this axiom to generate the appropriate RDF structure, handling both binary and n-ary disjointness.
        :type disjoints: OWLDisjointObjectProperties

        :return: The identifier of the axiom node created in the graph, or None if the disjointness is represented as a binary relationship between exactly two properties.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Maps an OWL subdata property axiom to the internal RDF graph by establishing a hierarchical relationship between data properties. The method resolves the sub-property and super-property expressions to their corresponding IRIs and adds a triple using the `rdfs:subPropertyOf` predicate to represent the axiom. It also processes and attaches any annotations associated with the axiom to the graph. This operation modifies the graph as a side effect and returns None.

        :param subdata: The OWL axiom defining a subdata property relationship, containing the sub-property, super-property, and associated annotations. It is used to generate the corresponding `rdfs:subPropertyOf` triple and map annotations to the graph.
        :type subdata: OWLSubDataPropertyOf

        :return: Returns None, as the mapping is performed by adding triples directly to the graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Maps an OWL equivalent data properties axiom to RDF triples by creating a chain of `owl:equivalentProperty` relationships between the data properties involved. The method iterates through the list of data property expressions provided in the axiom, adding a triple to the graph for each consecutive pair to signify their equivalence. It also handles the mapping of any annotations associated with the axiom, attaching them to the generated triples. This operation modifies the internal graph directly and returns None, performing no action if the list of properties contains fewer than two elements.

        :param eq: The OWL axiom containing the data property expressions that are mutually equivalent.
        :type eq: OWLEquivalentDataProperties

        :return: None, as the method modifies the graph in place to represent the axiom.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method maps an OWL disjoint data properties axiom to RDF triples, handling both binary and n-ary cases to conform to OWL 2 RDF serialization standards. When the axiom contains exactly two data property expressions, it creates a direct `owl:propertyDisjointWith` relationship between the two mapped property nodes and returns None. For axioms involving a different number of properties, it generates a blank node of type `owl:AllDisjointProperties`, populates an RDF collection with the mapped property expressions, and links the collection to the blank node using the `owl:members` predicate. The method also processes and attaches any axiom annotations to the relevant subject node, returning the blank node identifier for the n-ary representation.

        :param disjoints: The OWL axiom representing a set of mutually disjoint data properties. It contains the list of data property expressions to be mapped to RDF triples, handling both binary and n-ary disjointness.
        :type disjoints: OWLDisjointDataProperties

        :return: The identifier of the `AllDisjointProperties` axiom node if the list of properties does not contain exactly two items; otherwise returns `None` because the disjointness is asserted directly between the two properties.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL datatype definition axiom into RDF triples within the mapper's graph. The method resolves the datatype and data range components of the axiom to their corresponding IRIs and asserts an equivalence relationship between them using the `owl:equivalentClass` predicate. It also handles the mapping of any annotations associated with the axiom. This method modifies the graph as a side effect and returns None, despite the type hint indicating an optional URIRef.

        :param datatype_def: The OWL datatype definition axiom to be mapped, representing an equivalence between a datatype and a data range.
        :type datatype_def: OWLDatatypeDefinition

        :return: Returns None, as the method performs the mapping by adding triples directly to the graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Translates an OWL `HasKey` axiom into corresponding RDF triples within the graph. The method processes the class expression and the associated object and data property expressions, converting them into IRIs and organizing the properties into an RDF collection. It then asserts a triple linking the class to the `owl:hasKey` property with the collection as the object, and handles any associated axiom annotations. As a side effect, the graph is modified, and the method returns None.

        :param has_key: The OWLHasKey axiom to be mapped to RDF, defining a key for a class expression via a set of object and data property expressions.
        :type has_key: OWLHasKey

        :return: None, as the method modifies the graph in-place and does not return a reference to the created axiom.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL same individual axiom into a series of RDF triples within the graph. The method processes the set of individual expressions contained in the axiom, mapping them to their corresponding RDF IRIs. It then establishes a chain of equivalence relationships by adding `owl:sameAs` triples between consecutive individuals in the sequence. Additionally, any annotations associated with the axiom are attached to these generated triples. This operation directly modifies the internal graph structure and returns None.

        :param same: The OWL same individual axiom to be mapped, consisting of a set of individual expressions that will be linked via `owl:sameAs` relationships in the graph, including any associated annotations.
        :type same: OWLSameIndividual

        :return: None, as the method modifies the graph in place by adding the same individual triples.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Maps an OWL DifferentIndividuals axiom to the underlying RDF graph by generating triples that represent the distinctness of the specified individuals. If the axiom contains exactly two individuals, the method creates a direct triple using the `owl:differentFrom` predicate and returns None. For axioms involving three or more individuals, it instantiates a blank node typed as `owl:AllDifferent` and links it to an RDF collection of the individuals via the `owl:members` property, returning the blank node identifier. In both scenarios, the method adds the generated triples to the graph and processes any associated axiom annotations.

        :param different: Represents the OWL axiom specifying a set of individuals that are all distinct. The mapping process handles pairs of individuals using `owl:differentFrom` and larger sets using `owl:AllDifferent`.
        :type different: OWLDifferentIndividuals

        :return: The blank node representing the `owl:AllDifferent` axiom in the graph, or None if the axiom was mapped as a binary `owl:differentFrom` relationship.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Maps an OWL class assertion axiom to an RDF triple within the internal graph. The method resolves the individual and class expression components of the assertion to their corresponding IRIs and adds a triple asserting that the individual is an instance of the class using the `rdf:type` predicate. It also handles the mapping of any annotations attached to the axiom. This operation modifies the graph in place and returns None.

        :param assertion: The OWL class assertion axiom to be mapped, defining an individual as an instance of a specific class expression.
        :type assertion: OWLClassAssertion

        :return: None, as the method performs the mapping by adding triples directly to the graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL object property assertion axiom into RDF triples and adds them to the internal graph. The method resolves the source individual, object property expression, and target individual to their corresponding IRIs. It specifically handles inverse object properties by swapping the subject and object positions in the generated triple to ensure correct semantic representation. Additionally, any annotations associated with the axiom are processed and linked to the newly created triple. This operation modifies the graph directly and returns None.

        :param assertion: The OWL axiom representing a relationship between a source individual and a target individual via an object property expression, to be converted into RDF triples.
        :type assertion: OWLObjectPropertyAssertion

        :return: None, as the assertion is added directly to the graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method transforms an OWL negative object property assertion axiom into a corresponding RDF structure within the graph. It creates a blank node to represent the assertion and populates the graph with triples linking this node to the source individual, the object property expression, and the target individual using the standard OWL vocabulary. Furthermore, the method handles any annotations attached to the axiom by mapping them to the blank node. As a side effect, it modifies the internal graph by adding these triples and returns the blank node identifier for the assertion.

        :param assertion: The negative object property assertion axiom to be mapped, consisting of a source individual, an object property expression, and a target individual.
        :type assertion: OWLNegativeObjectPropertyAssertion

        :return: The blank node identifier representing the negative object property assertion axiom in the RDF graph.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL data property assertion axiom into an RDF triple and adds it to the internal graph. The method resolves the RDF representations for the source individual, the data property expression, and the target literal value, then inserts the triple into the graph. It also processes and adds any annotations associated with the axiom. This operation modifies the graph state as a side effect and returns None.

        :param assertion: The OWL data property assertion axiom to be mapped, comprising a source individual, a data property, a target literal value, and any associated annotations.
        :type assertion: OWLDataPropertyAssertion

        :return: None, as the method performs side effects by adding triples to the graph in place.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method transforms an OWL negative data property assertion axiom into a reified RDF structure within the graph. It extracts the source individual, data property expression, and target literal value from the input assertion, mapping them to their corresponding RDF representations. A blank node is created to serve as the subject of the reified statement, typed as `owl:NegativePropertyAssertion`, and connected to the mapped components via `owl:sourceIndividual`, `owl:assertionProperty`, and `owl:targetValue` predicates. Any annotations attached to the axiom are also applied to this node. The process modifies the graph by adding these triples and returns the blank node identifier for the newly created assertion.

        :param assertion: The negative data property assertion axiom to be mapped to the RDF graph, consisting of a source individual, a data property expression, and a target literal value that the individual does not possess.
        :type assertion: OWLNegativeDataPropertyAssertion

        :return:

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method processes an OWL annotation assertion axiom by converting it into an RDF triple and adding it to the underlying graph. It resolves the annotation's subject, property, and value into their corresponding RDF representations and inserts the resulting triple into the graph structure. Additionally, the method handles any annotations associated with the axiom itself by delegating to the entity annotation mapping logic. The operation modifies the graph as a side effect and always returns None.

        :param assertion: The OWL annotation assertion axiom to be converted into an RDF triple, containing a subject, property, and value.
        :type assertion: OWLAnnotationAssertion

        :return: None, as the method modifies the graph in place to add the corresponding RDF triples.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Maps an OWL sub-annotation property axiom to RDF triples by asserting a hierarchical relationship between two annotation properties. It extracts the sub-property and super-property from the input axiom, converts them to IRIs, and adds a triple to the graph using the `rdfs:subPropertyOf` predicate. The method also processes and adds any annotations associated with the axiom itself. This process modifies the internal graph structure as a side effect and returns None.

        :param prop: The OWL sub-annotation property axiom to be mapped to RDF triples, defining a relationship where one annotation property is a subproperty of another.
        :type prop: OWLSubAnnotationPropertyOf

        :return: None, as the method modifies the graph in place.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL annotation property domain axiom into RDF triples within the internal graph. The method resolves the IRI of the annotation property and the specified domain, creating a triple that links them using the `rdfs:domain` predicate. It also processes and adds any annotations associated with the axiom itself. This operation modifies the graph's state and returns the URI reference of the annotation property, or None if the mapping cannot be performed.

        :param prop: The OWL axiom specifying the domain of an annotation property, containing the property, the domain class, and any associated annotations to be mapped to RDF.
        :type prop: OWLAnnotationPropertyDomain

        :return: The IRI of the annotation property for which the domain axiom was mapped.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method maps an OWL annotation property range axiom to an RDF triple within the internal graph. It resolves the annotation property and the range to their respective URI references and establishes a relationship between them using the `rdfs:range` predicate. The method also handles any annotations attached to the axiom, ensuring they are properly represented in the graph. It returns the URI reference of the annotation property, or None if the mapping fails. As a side effect, the internal graph is mutated to include the new range assertion and any associated annotations.

        :param prop: The OWL annotation property range axiom to be mapped to RDF triples, consisting of an annotation property and its range.
        :type prop: OWLAnnotationPropertyRange

        :return: The IRI of the annotation property that was mapped to the graph, or None if the mapping failed.

        :rtype: typing.Optional[URIRef]
        """

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
        Maps an OWL class entity to its corresponding RDF representation within the internal graph. It resolves the IRI of the provided `OWLClass` into a `URIRef` and adds a triple asserting that the resource is of type `owl:Class`. This operation modifies the graph by registering the class declaration, though it does not handle complex axioms such as subclass relationships or restrictions. The method returns the generated `URIRef`, which can be used to reference the class in further mapping operations.

        :param class_: The OWL class instance to be converted into RDF triples. It represents a class in the ontology identified by an IRI and will be added to the graph as an `owl:Class`.
        :type class_: OWLClass

        :return: The RDFLib URIRef representing the IRI of the mapped OWL class, or None if the class cannot be mapped.

        :rtype: typing.Optional[URIRef]
        """

        iri_node = self.map(class_)
        self.graph.add((iri_node, RDF.type, OWL.Class))
        return iri_node

    def map_owl_named_individual(
        self,
        individual: OWLNamedIndividual,
    ) -> typing.Optional[URIRef]:
        """
        Maps an OWL named individual to the RDF graph by converting its IRI into a URIRef and asserting its type. The method retrieves the individual's IRI, transforms it into an RDFLib URIRef, and adds a triple to the internal graph stating that the node is an instance of `owl:NamedIndividual`. This process modifies the graph state as a side effect. The function returns the generated URIRef, which serves as the concrete identifier for the individual within the RDF structure, or None if the IRI mapping fails.

        :param individual: The OWL named individual to be mapped to the RDF graph. It represents a specific instance in the ontology identified by an IRI.
        :type individual: OWLNamedIndividual

        :return: The RDFLib URIRef representing the mapped individual, or None if the individual's IRI cannot be mapped.

        :rtype: typing.Optional[URIRef]
        """

        iri_node = self.map(individual.iri)
        self.graph.add((iri_node, RDF.type, OWL.NamedIndividual))
        return iri_node

    def map_owl_anonymous_individual(
        self,
        individual: OWLAnonymousIndividual,
    ) -> typing.Optional[URIRef]:
        """
        Maps an OWL anonymous individual to an RDF node by converting its node ID into a URI reference and adding a type assertion to the graph. The method generates a triple stating that the resulting node is an `owl:NamedIndividual` and returns the URIRef. This process modifies the internal graph structure, and the return value may be None if the node ID cannot be successfully mapped.

        :param individual: The OWL anonymous individual to be mapped to RDF triples. The method uses the individual's node ID to generate the corresponding RDF node and adds it to the graph as a NamedIndividual.
        :type individual: OWLAnonymousIndividual

        :return: The RDFLib URIRef representing the mapped anonymous individual, or None if the mapping cannot be performed.

        :rtype: typing.Optional[URIRef]
        """

        iri_node = self.map(individual.node_id)
        self.graph.add((iri_node, RDF.type, OWL.NamedIndividual))
        return iri_node

    def map_owl_object_property_domain(
        self,
        domain: OWLObjectPropertyDomain,
    ) -> typing.Optional[URIRef]:
        """
        Translates an OWL Object Property Domain axiom into an RDF triple representation within the mapper's internal graph. The method resolves the object property expression and the class expression from the input axiom into RDF nodes, then establishes a relationship between them using the `RDFS.domain` predicate. Additionally, it processes and maps any annotations associated with the axiom to the graph. As a side effect, this method mutates the graph by adding the domain assertion and any annotation triples. It returns the URI reference corresponding to the object property, or None if the property expression cannot be successfully mapped.

        :param domain: The OWL axiom specifying the class expression that constitutes the domain of an object property expression.
        :type domain: OWLObjectPropertyDomain

        :return: The URI reference of the object property expression that serves as the subject of the domain restriction triple, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method maps an OWL Object Property Range axiom to an RDF triple within the internal graph. It resolves the object property expression and the class expression from the input, creating a triple that asserts the property has the specified class as its range using the `rdfs:range` predicate. The method also handles the mapping of any annotations attached to the axiom. It returns the URI reference of the object property node, or None if the mapping of the property expression fails.

        :param range: The OWL object property range axiom to be mapped, containing the object property expression and the class expression that defines its range.
        :type range: OWLObjectPropertyRange

        :return: The URI reference of the object property expression that serves as the subject of the range assertion.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        This method processes an OWL Data Property Domain axiom by converting it into an RDF triple within the mapper's graph. It resolves the constituent data property expression and class expression into RDF nodes and establishes a relationship between them using the `rdfs:domain` predicate. Additionally, the method handles any annotations associated with the axiom, integrating them into the graph structure. The function returns the URI reference of the data property node that serves as the subject of the domain assertion.

        :param domain: The OWL data property domain axiom to be mapped to RDF triples. This object contains the data property expression, the class expression defining its domain, and any associated annotations.
        :type domain: OWLDataPropertyDomain

        :return: The URIRef of the data property expression, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts an OWL data property range axiom into RDF triples by linking a data property expression to a specific data range. The method maps both the property and the range to their corresponding RDF nodes and adds a triple to the internal graph using the `rdfs:range` predicate to define the constraint. It also processes any annotations attached to the axiom, adding them to the graph to preserve metadata. This process modifies the internal graph as a side effect and returns the URI reference of the data property node that serves as the subject of the range assertion.

        :param range: The OWL axiom defining the valid data range for a data property expression. It encapsulates the property and the range constraint to be serialized as an `rdfs:range` triple in the RDF graph.
        :type range: OWLDataPropertyRange

        :return: The URI reference of the mapped data property expression, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
        """

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
        """
        Converts a list of OWL facet objects into the constituent elements required to construct RDF triples. For each facet in the input list, the method generates a unique blank node to act as the subject, resolves the facet's constraint to a URI reference, and converts the facet's value to a URI reference. The function returns a tuple containing three parallel lists: the generated blank nodes, the constraint URIs, and the value URIs, which correspond to the subjects, predicates, and objects of the intended triples. This method does not modify any external state but relies on the `constraint_to_uriref` and `value.to_uriref` methods of the input objects to perform the conversion, potentially raising exceptions if those methods fail.

        :param facets: A list of OWL facet instances representing data range restrictions, each containing a constraint and a value to be mapped to RDF.
        :type facets: list[OWLFacet]

        :return: A tuple containing three lists of URIRefs corresponding to the input facets: blank node identifiers, constraint URIs, and value URIs.

        :rtype: tuple[list[URIRef], list[URIRef], list[URIRef]]
        """

        nodes: list[URIRef] = [BNode() for _ in facets]
        uris: list[URIRef] = [f.constraint_to_uriref() for f in facets]
        values: list[URIRef] = [f.value.to_uriref() for f in facets]
        return nodes, uris, values

    def map_owl_datatype_restriction(
        self,
        restriction_type: OWLDatatypeRestriction,
    ) -> typing.Optional[URIRef]:
        """
        Converts an OWL datatype restriction into its corresponding RDF representation within the graph. The method instantiates a blank node to serve as the subject of the restriction, asserting it as an `rdfs:Datatype` and linking it to the constrained datatype via the `owl:onDatatype` property. It then processes the specific facet constraints, such as minimum or maximum values, organizing them into an RDF collection attached through the `owl:withRestrictions` predicate. This process directly mutates the internal graph by adding the necessary triples and returns the identifier of the generated restriction node.

        :param restriction_type: The OWL datatype restriction instance to be mapped, consisting of a base datatype and a set of facet constraints.
        :type restriction_type: OWLDatatypeRestriction

        :return: The blank node identifier representing the OWL datatype restriction in the RDF graph.

        :rtype: typing.Optional[URIRef]
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
        Converts an OWL equivalent classes axiom into a set of RDF triples by establishing pairwise equivalence relationships between the class expressions involved. The method iterates through the list of class expressions, mapping each to a node and linking adjacent nodes with the `owl:equivalentClass` property to form a chain of equivalences. It also processes and attaches any annotations associated with the axiom to these triples. This operation modifies the internal RDF graph directly and returns None, effectively handling cases with fewer than two class expressions by performing no action.

        :param eq: The OWL equivalent classes axiom containing the class expressions to be mapped as mutually equivalent in the RDF graph.
        :type eq: OWLEquivalentClasses

        :return: None, as the method modifies the graph in place.

        :rtype: typing.Optional[URIRef]
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
        Converts an OWL disjoint classes axiom into corresponding RDF triples within the mapper's graph, distinguishing between binary and n-ary relationships to produce the appropriate RDF structure. If the axiom involves exactly two class expressions, the method establishes a direct `owl:disjointWith` relationship between the mapped class nodes and returns None. For axioms involving three or more class expressions, it creates a blank node typed as `owl:AllDisjointClasses`, links the class expressions to this node using an `owl:members` collection, and returns the URI of the blank node. In both scenarios, any associated axiom annotations are processed and added to the graph.

        :param disjoints: The OWL axiom containing the class expressions declared to be mutually exclusive, which will be mapped to RDF triples.
        :type disjoints: OWLDisjointClasses

        :return: The identifier of the RDF node representing the disjoint classes collection, or None if the axiom involves exactly two class expressions.

        :rtype: typing.Optional[URIRef]
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
        """
        Converts an OWL annotation property into its RDF representation by asserting its type within the graph. The method resolves the IRI of the provided annotation property and adds a triple to the underlying graph stating that the corresponding node is an instance of `owl:AnnotationProperty`. This process modifies the graph as a side effect. It returns the URI reference representing the property, or None if the IRI cannot be mapped.

        :param annotation: The specific annotation property to be mapped to the RDF graph.
        :type annotation: OWLAnnotationProperty

        :return: The RDFLib URIRef representing the IRI of the mapped OWL annotation property, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
        """

        iri_node = self.map(annotation)
        self.graph.add((iri_node, RDF.type, OWL.AnnotationProperty))
        return iri_node

    def map_owl_object_inverse_of(
        self,
        prop: OWLInverseObjectProperty,
    ) -> typing.Optional[URIRef]:
        """
        Maps an OWL inverse object property axiom to its corresponding RDF representation within the graph. The method generates a blank node to serve as the subject of the inverse relationship and recursively maps the underlying object property to an RDF node. It then adds a triple to the graph using the `owl:inverseOf` predicate to link the blank node to the mapped property. The function returns the blank node representing the inverse property expression, modifying the graph as a side effect.

        :param prop: The OWL inverse object property axiom to be mapped to RDF triples.
        :type prop: OWLInverseObjectProperty

        :return: The blank node representing the inverse property axiom in the RDF graph, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
        """

        inverse = BNode()
        iri_node = self.map(prop.object_property)
        self.graph.add((inverse, OWL.inverseOf, iri_node))
        return inverse

    def map_owl_inverse_object_properties(
        self,
        prop: OWLInverseObjectProperties,
    ) -> typing.Optional[URIRef]:
        """
        Maps an OWL Inverse Object Properties axiom to the RDF graph by asserting that two object properties are inverses of one another. The method resolves the property expressions from the axiom into IRIs and adds a triple to the graph using the `owl:inverseOf` predicate to link them. This process modifies the internal graph state and returns a blank node identifier.

        :param prop: The OWL axiom representing the inverse relationship between two object property expressions, which will be mapped to RDF triples.
        :type prop: OWLInverseObjectProperties

        :return: A Blank Node (BNode) representing the OWL inverse object properties axiom.

        :rtype: typing.Optional[URIRef]
        """

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
        Processes an OWL object property to generate its RDF representation within the graph. It delegates the creation of the property's URI reference to the generic mapping logic and then explicitly adds a triple asserting that this node is of type `owl:ObjectProperty`. This method modifies the internal graph by adding this type declaration and returns the URI reference associated with the property.

        :param prop: The OWL object property to be mapped to RDF triples. It represents a property relationship in the ontology and provides the IRI used to identify the property in the graph.
        :type prop: OWLObjectProperty

        :return: The RDFLib URIRef representing the mapped OWL object property in the graph, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
        """

        iri_node = self.map(prop)
        self.graph.add((iri_node, RDF.type, OWL.ObjectProperty))
        return iri_node

    def map_owl_datatype(self, datatype: OWLDatatype) -> typing.Optional[URIRef]:
        """
        Converts an OWL datatype into its corresponding RDF representation by asserting its type within the mapper's internal graph. The method retrieves the IRI node associated with the datatype and adds a triple defining it as an instance of `rdfs:Datatype`. It returns the URI reference for the datatype, which serves as the subject for these assertions and can be used for further mapping operations.

        :param datatype: The OWL datatype instance to be mapped to RDF triples. It represents a datatype in the ontology identified by an IRI.
        :type datatype: OWLDatatype

        :return: The RDFLib URIRef representing the IRI of the mapped OWL datatype, or None if the datatype cannot be mapped.

        :rtype: typing.Optional[URIRef]
        """

        iri_node = self.map(datatype)
        self.graph.add((iri_node, RDF.type, RDFS.Datatype))
        return iri_node

    def map_owl_data_property(self, prop: OWLDataProperty) -> typing.Optional[URIRef]:
        """
        Transforms an OWL data property into an RDF representation by generating a URI reference and asserting its type within the graph. The method utilizes the generic mapping logic to resolve the property's IRI, then adds a triple to the internal graph stating that this node is an instance of `owl:DatatypeProperty`. It returns the resulting URI reference, or None if the property cannot be successfully mapped to a valid identifier.

        :param prop: The OWL datatype property instance to be mapped to the RDF graph. It represents a property associated with literal values and provides the IRI used to generate the corresponding RDF triples.
        :type prop: OWLDataProperty

        :return: The RDFLib URIRef representing the IRI of the mapped OWL datatype property, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
        """

        iri_node = self.map(prop)
        self.graph.add((iri_node, RDF.type, OWL.DatatypeProperty))
        return iri_node

    def map_owl_symmetric_property(
        self,
        prop: OWLSymmetricObjectProperty,
    ) -> typing.Optional[URIRef]:
        """
        Converts an OWL symmetric object property axiom into its corresponding RDF representation within the mapper's graph. It resolves the IRI of the underlying object property expression and adds a triple declaring it as an instance of `owl:SymmetricProperty`. Any annotations associated with the axiom are also processed and linked to the property. The function returns the URI reference of the property, or None if the underlying expression mapping fails.

        :param prop: The OWL symmetric object property to be mapped to RDF triples, containing the property expression and annotations to be serialized.
        :type prop: OWLSymmetricObjectProperty

        :return: The IRI of the symmetric property in the RDF graph, or None if the property expression cannot be mapped.

        :rtype: typing.Optional[URIRef]
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
        Converts an OWL transitive object property axiom into its corresponding RDF representation within the mapper's graph. It first resolves the IRI of the underlying object property expression and then asserts that this property is an instance of `owl:TransitiveProperty` by adding a specific triple to the graph. Additionally, the method processes and maps any annotations associated with the axiom. It returns the IRI of the mapped property, or None if the underlying property expression cannot be successfully mapped.

        :param prop: The OWL transitive object property to be mapped, including its object property expression and axiom annotations.
        :type prop: OWLTransitiveObjectProperty

        :return: The IRI of the transitive property as a URIRef, or None if the property expression cannot be mapped.

        :rtype: typing.Optional[URIRef]
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
        This method converts an OWL asymmetric object property axiom into corresponding RDF triples within the mapper's graph. It retrieves the IRI of the property by recursively mapping the underlying object property expression, then asserts that this IRI is an instance of `owl:AsymmetricProperty`. The method also processes and adds any annotations associated with the axiom. It returns the URI reference of the mapped property, or None if the property expression cannot be successfully resolved.

        :param prop: The OWL asymmetric object property to be mapped to RDF triples, containing the property expression and any associated annotations.
        :type prop: OWLAsymmetricObjectProperty

        :return: The IRI of the object property that was mapped as an asymmetric property, or None if the mapping was unsuccessful.

        :rtype: typing.Optional[URIRef]
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
        This method maps an OWL reflexive object property axiom to the underlying RDF graph by generating the necessary triples. It first resolves the IRI of the underlying object property expression and then asserts that this property is an instance of `owl:ReflexiveProperty`. The method also handles any annotations associated with the axiom, mapping them to the graph. It returns the IRI of the mapped property, or None if the underlying property expression fails to map.

        :param prop: The OWL reflexive object property axiom to be mapped to RDF triples, containing the property expression and associated annotations.
        :type prop: OWLReflexiveObjectProperty

        :return: The IRI of the object property mapped as a reflexive property, or None if the mapping fails.

        :rtype: typing.Optional[URIRef]
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
        This method maps an OWL Irreflexive Object Property axiom to its corresponding RDF representation within the graph. It resolves the IRI of the underlying object property expression and adds a triple asserting that this property is an instance of `owl:IrreflexiveProperty`. Additionally, the method processes and attaches any annotations associated with the axiom to the graph. As a side effect, the internal RDF graph is modified with these new triples. The method returns the IRI of the mapped property, or None if the underlying property expression cannot be successfully mapped.

        :param prop: The OWL irreflexive object property axiom to be mapped to RDF, containing the property expression and associated annotations.
        :type prop: OWLIrreflexiveObjectProperty

        :return: The IRI of the object property that was mapped and asserted as an irreflexive property in the RDF graph.

        :rtype: typing.Optional[URIRef]
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
        Maps an OWL functional property, either a data or object property, to RDF triples by asserting its functional characteristic in the graph. The method recursively resolves the IRI of the underlying property expression and adds a triple defining it as an instance of `owl:FunctionalProperty`. It also processes and attaches any annotations associated with the property axiom to the graph. This process directly modifies the internal RDF graph as a side effect. The method returns the IRI of the mapped property, or None if the underlying property expression cannot be resolved.

        :param prop: The OWL functional property instance (data or object) to be converted into RDF triples, containing the property expression and annotations required for the mapping.
        :type prop: typing.Union[OWLFunctionalDataProperty, OWLFunctionalObjectProperty]

        :return: The RDFLib URIRef representing the IRI of the mapped functional property, or None if the property expression cannot be mapped.

        :rtype: typing.Optional[URIRef]
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
        This method converts an OWL inverse functional property axiom into RDF triples by asserting the specific property type in the graph. It first resolves the IRI of the underlying object property expression and then adds a triple declaring that this property is an instance of `owl:InverseFunctionalProperty`. Any annotations attached to the axiom are also mapped and added to the graph. The function returns the IRI of the property, which may be None if the mapping of the underlying object property expression fails.

        :param prop: The OWL inverse functional object property to be mapped to RDF triples, containing the property expression and annotations.
        :type prop: OWLInverseFunctionalObjectProperty

        :return: The IRI of the object property that was asserted to be an inverse functional property in the RDF graph, or None if the property expression could not be mapped.

        :rtype: typing.Optional[URIRef]
        """

        iri = self.map(prop.object_property_expression)
        self.graph.add((iri, RDF.type, OWL.InverseFunctionalProperty))
        self.map_owl_annotations(iri, prop.axiom_annotations)
        return iri


# Example usage
def example_usage():
    """Provides a comprehensive demonstration of the `RDFXMLMapper` class by constructing a sample OWL ontology and serializing it into RDF triples. The function initializes an `owlready2` environment, defines a custom namespace, and instantiates various OWL entities such as classes, named individuals, object properties, and annotations. These entities are then mapped to an RDF graph using the mapper's methods. As a side effect, the function prints the resulting graph to standard output in Turtle format and writes the ontology to a local file named 'test.owl' in RDF/XML format."""

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
