import enum
import inspect
import typing

from owlready2 import (
    AllDifferent,
    And,
    AnnotationPropertyClass,
    AsymmetricProperty,
    ConstrainedDatatype,
    DataPropertyClass,
    DatatypeClass,
    EntityClass,
    FunctionalProperty,
    Inverse,
    InverseFunctionalProperty,
    IrreflexiveProperty,
    NamedIndividual,
    Not,
    Nothing,
    ObjectPropertyClass,
    OneOf,
    Ontology,
    Or,
    ReflexiveProperty,
    Restriction,
    SymmetricProperty,
    Thing,
    ThingClass,
    TransitiveProperty,
    World,
)
from owlready2.annotation import (
    backwardCompatibleWith,
    comment,
    deprecated,
    incompatibleWith,
    isDefinedBy,
    label,
    priorVersion,
    seeAlso,
    versionInfo,
)
from owlready2.base import (
    _universal_abbrev,
    _universal_abbrev_2_iri,
    _universal_iri_2_abbrev,
)
from rdflib import RDFS, XSD, BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF

from pyowl2.abstracts.annotation_axiom import OWLAnnotationAxiom
from pyowl2.abstracts.assertion import OWLAssertion
from pyowl2.abstracts.axiom import OWLAxiom
from pyowl2.abstracts.class_axiom import OWLClassAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_axiom import OWLDataPropertyAxiom
from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.abstracts.object import OWLObject
from pyowl2.abstracts.object_property_axiom import OWLObjectPropertyAxiom
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
from pyowl2.expressions.data_property import OWLDataProperty
from pyowl2.expressions.inverse_object_property import OWLInverseObjectProperty
from pyowl2.expressions.object_property import OWLObjectProperty
from pyowl2.individual.anonymous_individual import OWLAnonymousIndividual
from pyowl2.individual.named_individual import OWLNamedIndividual
from pyowl2.literal.literal import OWLLiteral


def get_abbreviation(iri: URIRef) -> int:
    if str(iri) in _universal_iri_2_abbrev:
        return _universal_iri_2_abbrev[str(iri)]
    else:
        return _universal_abbrev(str(iri))


def is_named_individual(obj):
    return isinstance(obj, Thing) and not isinstance(obj, ThingClass)


BASE_DATATYPES = (str, int, float, bool, bytes)


class AxiomsType(enum.StrEnum):
    GENERAL_CLASS_AXIOMS = enum.auto()
    CLASSES = enum.auto()
    DECLARATIONS = enum.auto()
    OBJECT_PROPERTIES = enum.auto()
    DATA_PROPERTIES = enum.auto()
    ANNOTATION_PROPERTIES = enum.auto()
    INDIVIDUALS = enum.auto()
    SUBCLASSES = enum.auto()
    EQUIVALENT_CLASSES = enum.auto()
    DISJOINT_CLASSES = enum.auto()
    OBJECT_UNION_OF = enum.auto()
    DATA_UNION_OF = enum.auto()
    OBJECT_INTERSECTION_OF = enum.auto()
    DATA_INTERSECTION_OF = enum.auto()
    OBJECT_COMPLEMENT_OF = enum.auto()
    DATA_COMPLEMENT_OF = enum.auto()
    OBJECTS_ONE_OF = enum.auto()
    DATA_ONE_OF = enum.auto()
    DATATYPE_RESTRICTIONS = enum.auto()
    INVERSE_OBJECT_PROPERTIES = enum.auto()
    HAS_KEYS = enum.auto()
    DATATYPES = enum.auto()
    NEGATIVE_OBJECT_PROPERTY_ASSERTIONS = enum.auto()
    NEGATIVE_DATA_PROPERTY_ASSERTIONS = enum.auto()
    CLASS_ASSERTIONS = enum.auto()
    OBJECT_PROPERTY_ASSERTIONS = enum.auto()
    DATA_PROPERTY_ASSERTIONS = enum.auto()
    SAME_INDIVIDUALS = enum.auto()
    DIFFERENT_INDIVIDUALS = enum.auto()
    SUB_OBJECT_PROPERTIES = enum.auto()
    SUB_DATA_PROPERTIES = enum.auto()
    SUB_ANNOTATION_PROPERTIES = enum.auto()
    EQUIVALENT_OBJECT_PROPERTIES = enum.auto()
    DISJOINT_OBJECT_PROPERTIES = enum.auto()
    ANNOTATIONS = enum.auto()
    OBJECTS_SOME_VALUES_FROM = enum.auto()
    OBJECTS_ALL_VALUES_FROM = enum.auto()
    OBJECTS_HAS_VALUE = enum.auto()
    OBJECTS_HAS_SELF = enum.auto()
    OBJECTS_MIN_CARDINALITY = enum.auto()
    OBJECTS_MAX_CARDINALITY = enum.auto()
    OBJECTS_EXACT_CARDINALITY = enum.auto()
    DATA_SOME_VALUES_FROM = enum.auto()
    DATA_ALL_VALUES_FROM = enum.auto()
    DATAS_HAS_VALUE = enum.auto()
    DATA_MIN_CARDINALITY = enum.auto()
    DATA_MAX_CARDINALITY = enum.auto()
    DATA_EXACT_CARDINALITY = enum.auto()
    DISJOINT_UNIONS = enum.auto()
    FUNCIONAL_DATA_PROPERTIES = enum.auto()
    FUNCTIONAL_OBJECT_PROPERTIES = enum.auto()
    INVERSE_FUNCTIONAL_OBJECT_PROPERTIES = enum.auto()
    TRANSITIVE_OBJECT_PROPERTIES = enum.auto()
    SYMMETRIC_OBJECT_PROPERTIES = enum.auto()
    ASYMMETRIC_OBJECT_PROPERTIES = enum.auto()
    REFLEXIVE_OBJECT_PROPERTIES = enum.auto()
    IRREFLEXIVE_OBJECT_PROPERTIES = enum.auto()
    EQUIVALENT_DATA_PROPERTIES = enum.auto()
    DISJOINT_DATA_PROPERTIES = enum.auto()
    OBJECT_PROPERTY_DOMAIN = enum.auto()
    OBJECT_PROPERTY_RANGE = enum.auto()
    DATA_PROPERTY_DOMAIN = enum.auto()
    DATA_PROPERTY_RANGE = enum.auto()
    DATATYPE_DEFINITION = enum.auto()
    ANNOTATION_PROPERTY_DOMAINS = enum.auto()
    ANNOTATION_PROPERTY_RANGES = enum.auto()


# @utils.timer_decorator
class RDFXMLGetter:
    """
    A utility class providing static methods to retrieve OWL concepts from RDF/XML
    using SPARQL queries or direct graph operations with rdflib and owlready2.

    This class implements the OWL 2 mapping to RDF as described in W3C specification:
    https://www.w3.org/TR/owl2-mapping-to-rdf/
    """

    STANDARD_ANNOTATIONS: dict[int, AnnotationPropertyClass] = {
        comment.storid: comment,
        label.storid: label,
        backwardCompatibleWith.storid: backwardCompatibleWith,
        deprecated.storid: deprecated,
        incompatibleWith.storid: incompatibleWith,
        isDefinedBy.storid: isDefinedBy,
        priorVersion.storid: priorVersion,
        seeAlso.storid: seeAlso,
        versionInfo.storid: versionInfo,
    }

    def __init__(self, ontology: Ontology) -> None:
        assert ontology is not None
        self._ontology: Ontology = ontology
        self._world: World = typing.cast(World, ontology.world)
        self._graph: Graph = self._world.as_rdflib_graph()

        self._declarations: dict[EntityClass, EntityClass] = dict()
        self._classes: dict[ThingClass, OWLClass] = dict()
        self._class_expressions: dict[EntityClass, OWLClassExpression] = dict()
        self._object_properties: dict[ObjectPropertyClass, OWLObjectProperty] = dict()
        self._data_properties: dict[DataPropertyClass, OWLDataProperty] = dict()
        self._annotation_properties: dict[
            AnnotationPropertyClass, OWLAnnotationProperty
        ] = dict()
        self._individuals: dict[NamedIndividual, OWLIndividual] = dict()
        self._class_assertions: dict[
            tuple[ThingClass, NamedIndividual], OWLClassAssertion
        ] = dict()
        self._subclasses_of: dict[tuple[ThingClass, ThingClass], OWLSubClassOf] = dict()
        self._equivalent_classes: dict[tuple[ThingClass, ...], OWLEquivalentClasses] = (
            dict()
        )
        self._disjoint_classes: dict[
            typing.Union[tuple[ThingClass, ...], AllDifferent], OWLDisjointClasses
        ] = dict()
        self._data_unions_of: dict[tuple[Or], OWLDataUnionOf] = dict()
        self._object_unions_of: dict[tuple[Or], OWLObjectUnionOf] = dict()
        self._data_intersections_of: dict[tuple[And], OWLDataIntersectionOf] = dict()
        self._object_intersections_of: dict[tuple[And], OWLObjectIntersectionOf] = (
            dict()
        )
        self._data_complements_of: dict[tuple[Not], OWLDataComplementOf] = dict()
        self._object_complements_of: dict[tuple[Not], OWLObjectComplementOf] = dict()
        self._data_ones_of: dict[tuple[OneOf], OWLDataOneOf] = dict()
        self._object_ones_of: dict[tuple[OneOf], OWLObjectOneOf] = dict()
        self._datatypes: dict[DatatypeClass, OWLDatatype] = dict()
        self._datatype_restrictions: dict[
            ConstrainedDatatype, OWLDatatypeRestriction
        ] = dict()
        self._object_property_assertions: dict[
            tuple[ObjectPropertyClass, NamedIndividual, NamedIndividual],
            OWLObjectPropertyAssertion,
        ] = dict()
        self._data_property_assertions: dict[
            tuple[DataPropertyClass, NamedIndividual, Literal],
            OWLDataPropertyAssertion,
        ] = dict()
        self._same_individuals: dict[tuple[NamedIndividual, ...], OWLSameIndividual] = (
            dict()
        )
        self._different_individuals: dict[
            typing.Union[tuple[NamedIndividual, ...], AllDifferent],
            OWLDifferentIndividuals,
        ] = dict()
        self._subobject_properties_of: dict[
            tuple[ObjectPropertyClass, ObjectPropertyClass], OWLSubObjectPropertyOf
        ] = dict()
        self._subdata_properties_of: dict[
            tuple[DataPropertyClass, DataPropertyClass], OWLSubDataPropertyOf
        ] = dict()
        self._subannotation_properties_of: dict[
            tuple[AnnotationPropertyClass, AnnotationPropertyClass],
            OWLSubAnnotationPropertyOf,
        ] = dict()
        self._annotations: dict[
            EntityClass,
            tuple[URIRef, OWLAnnotation],
        ] = dict()
        self._general_axioms: dict[EntityClass, OWLAnnotationAssertion] = dict()
        self._objects_some_values_from: dict[Restriction, OWLObjectSomeValuesFrom] = (
            dict()
        )
        self._objects_all_values_from: dict[Restriction, OWLObjectAllValuesFrom] = (
            dict()
        )
        self._objects_has_value: dict[Restriction, OWLObjectHasValue] = dict()
        self._objects_has_self: dict[Restriction, OWLObjectHasSelf] = dict()
        self._objects_min_cardinality: dict[Restriction, OWLObjectMinCardinality] = (
            dict()
        )
        self._objects_max_cardinality: dict[Restriction, OWLObjectMaxCardinality] = (
            dict()
        )
        self._objects_exact_cardinality: dict[
            Restriction, OWLObjectExactCardinality
        ] = dict()
        self._data_some_values_from: dict[Restriction, OWLDataSomeValuesFrom] = dict()
        self._data_all_values_from: dict[Restriction, OWLDataAllValuesFrom] = dict()
        self._data_has_value: dict[Restriction, OWLDataHasValue] = dict()
        self._data_min_cardinality: dict[Restriction, OWLDataMinCardinality] = dict()
        self._data_max_cardinality: dict[Restriction, OWLDataMaxCardinality] = dict()
        self._data_exact_cardinality: dict[Restriction, OWLDataExactCardinality] = (
            dict()
        )
        self._disjoint_unions: dict[tuple[ThingClass, ...], OWLDisjointUnion] = dict()
        self._equivalent_object_properties: dict[
            tuple[ObjectPropertyClass, ...], OWLEquivalentObjectProperties
        ] = dict()
        self._disjoint_object_properties: dict[
            typing.Union[tuple[ObjectPropertyClass, ...], AllDifferent],
            OWLDisjointObjectProperties,
        ] = dict()
        self._inverse_object_properties: dict[
            tuple[ObjectPropertyClass, ...], OWLInverseObjectProperties
        ] = dict()
        self._functional_object_properties: dict[
            ObjectPropertyClass, OWLFunctionalObjectProperty
        ] = dict()
        self._inverse_functional_object_properties: dict[
            ObjectPropertyClass, OWLInverseFunctionalObjectProperty
        ] = dict()
        self._transitive_object_properties: dict[
            ObjectPropertyClass, OWLTransitiveObjectProperty
        ] = dict()
        self._symmetric_object_properties: dict[
            ObjectPropertyClass, OWLSymmetricObjectProperty
        ] = dict()
        self._asymmetric_object_properties: dict[
            ObjectPropertyClass, OWLAsymmetricObjectProperty
        ] = dict()
        self._reflexive_object_properties: dict[
            ObjectPropertyClass, OWLReflexiveObjectProperty
        ] = dict()
        self._irreflexive_object_properties: dict[
            ObjectPropertyClass, OWLIrreflexiveObjectProperty
        ] = dict()
        self._functional_data_properties: dict[
            DataPropertyClass, OWLFunctionalDataProperty
        ] = dict()
        self._equivalent_data_properties: dict[
            tuple[DataPropertyClass, ...], OWLEquivalentDataProperties
        ] = dict()
        self._disjoint_data_properties: dict[
            typing.Union[tuple[DataPropertyClass, ...], AllDifferent],
            OWLDisjointDataProperties,
        ] = dict()
        self._object_property_domains: dict[
            ObjectPropertyClass, OWLObjectPropertyDomain
        ] = dict()
        self._object_property_ranges: dict[
            ObjectPropertyClass, OWLObjectPropertyRange
        ] = dict()
        self._data_property_domains: dict[DataPropertyClass, OWLDataPropertyDomain] = (
            dict()
        )
        self._data_property_ranges: dict[DataPropertyClass, OWLDataPropertyRange] = (
            dict()
        )
        self._datatype_definitions: dict[DatatypeClass, OWLDatatypeDefinition] = dict()
        self._has_keys: dict[ThingClass, OWLHasKey] = dict()
        self._negative_object_property_assertions: dict[
            tuple[ObjectPropertyClass, NamedIndividual, NamedIndividual],
            OWLNegativeObjectPropertyAssertion,
        ] = dict()
        self._negative_data_property_assertions: dict[
            tuple[DataPropertyClass, NamedIndividual, Literal],
            OWLNegativeDataPropertyAssertion,
        ] = dict()
        self._annotation_property_domains: dict[
            AnnotationPropertyClass, OWLAnnotationPropertyDomain
        ] = dict()
        self._annotation_property_ranges: dict[
            AnnotationPropertyClass, OWLAnnotationPropertyRange
        ] = dict()
        self._annotation_assertions: dict[
            tuple[
                typing.Union[NamedIndividual, URIRef, str],
                AnnotationPropertyClass,
                typing.Union[NamedIndividual, URIRef, Literal],
            ],
            OWLAnnotationAssertion,
        ] = dict()

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
        return Namespace(self.ontology.get_namespace(self.ontology.base_iri).base_iri)

    @property
    def axioms(self) -> list[dict]:
        return [
            self.classes,
            self.object_properties,
            self.data_properties,
            self.annotation_properties,
            self.individuals,
            self.class_assertions,
            self.subclasses_of,
            self.equivalent_classes,
            self.disjoint_classes,
            self.data_unions_of,
            self.object_unions_of,
            self.data_intersections_of,
            self.object_intersections_of,
            self.data_complements_of,
            self.object_complements_of,
            self.data_ones_of,
            self.object_ones_of,
            self.datatypes,
            self.datatype_restrictions,
            self.object_property_assertions,
            self.data_property_assertions,
            self.same_individuals,
            self.different_individuals,
            self.subobject_properties_of,
            self.subdata_properties_of,
            self.subannotation_properties_of,
            self.annotations,
            self.objects_some_values_from,
            self.objects_all_values_from,
            self.objects_has_value,
            self.objects_has_self,
            self.objects_min_cardinality,
            self.objects_max_cardinality,
            self.objects_exact_cardinality,
            self.data_all_values_from,
            self.data_some_values_from,
            self.data_has_value,
            self.data_min_cardinality,
            self.data_max_cardinality,
            self.data_exact_cardinality,
            self.disjoint_unions,
            self.equivalent_object_properties,
            self.equivalent_data_properties,
            self.disjoint_object_properties,
            self.disjoint_data_properties,
            self.inverse_object_properties,
            self.functional_object_properties,
            self.inverse_functional_object_properties,
            self.irreflexive_object_properties,
            self.reflexive_object_properties,
            self.transitive_object_properties,
            self.symmetric_object_properties,
            self.asymmetric_object_properties,
            self.functional_data_properties,
            self.object_property_domains,
            self.object_property_ranges,
            self.data_property_domains,
            self.data_property_ranges,
            self.datatype_definitions,
            self.has_keys,
            self.negative_object_property_assertions,
            self.negative_data_property_assertions,
            self.annotation_property_domains,
            self.annotation_property_ranges,
        ]

    @property
    def declarations(self) -> dict[EntityClass, EntityClass]:
        return self._declarations

    @property
    def classes(self) -> dict[ThingClass, OWLClass]:
        return self._classes

    @property
    def object_properties(self) -> dict[ObjectPropertyClass, OWLObjectProperty]:
        return self._object_properties

    @property
    def data_properties(self) -> dict[DataPropertyClass, OWLDataProperty]:
        return self._data_properties

    @property
    def annotation_properties(
        self,
    ) -> dict[AnnotationPropertyClass, OWLAnnotationProperty]:
        return self._annotation_properties

    @property
    def individuals(self) -> dict[NamedIndividual, OWLIndividual]:
        return self._individuals

    @property
    def class_assertions(
        self,
    ) -> dict[tuple[ThingClass, NamedIndividual], OWLClassAssertion]:
        return self._class_assertions

    @property
    def subclasses_of(self) -> dict[tuple[ThingClass, ThingClass], OWLSubClassOf]:
        return self._subclasses_of

    @property
    def equivalent_classes(self) -> dict[tuple[ThingClass, ...], OWLEquivalentClasses]:
        return self._equivalent_classes

    @property
    def disjoint_classes(
        self,
    ) -> dict[typing.Union[tuple[ThingClass, ...], AllDifferent], OWLDisjointClasses]:
        return self._disjoint_classes

    @property
    def data_unions_of(self) -> dict[tuple[Or], OWLDataUnionOf]:
        return self._data_unions_of

    @property
    def object_unions_of(
        self,
    ) -> dict[tuple[And], OWLObjectUnionOf]:
        return self._object_unions_of

    @property
    def data_intersections_of(self) -> dict[tuple[And], OWLDataIntersectionOf]:
        return self._data_intersections_of

    @property
    def object_intersections_of(self) -> dict[tuple[And], OWLObjectIntersectionOf]:
        return self._object_intersections_of

    @property
    def data_complements_of(self) -> dict[tuple[Not], OWLDataComplementOf]:
        return self._data_complements_of

    @property
    def object_complements_of(self) -> dict[tuple[Not], OWLObjectComplementOf]:
        return self._object_complements_of

    @property
    def data_ones_of(self) -> dict[tuple[OneOf], OWLDataOneOf]:
        return self._data_ones_of

    @property
    def object_ones_of(self) -> dict[tuple[OneOf], OWLObjectOneOf]:
        return self._object_ones_of

    @property
    def datatypes(
        self,
    ) -> dict[DatatypeClass, OWLDatatype]:
        return self._datatypes

    @property
    def datatype_restrictions(
        self,
    ) -> dict[ConstrainedDatatype, OWLDatatypeRestriction]:
        return self._datatype_restrictions

    @property
    def object_property_assertions(
        self,
    ) -> dict[
        tuple[ObjectPropertyClass, NamedIndividual, NamedIndividual],
        OWLObjectPropertyAssertion,
    ]:
        return self._object_property_assertions

    @property
    def data_property_assertions(
        self,
    ) -> dict[
        tuple[DataPropertyClass, NamedIndividual, Literal],
        OWLDataPropertyAssertion,
    ]:
        return self._data_property_assertions

    @property
    def same_individuals(self) -> dict[tuple[NamedIndividual, ...], OWLSameIndividual]:
        return self._same_individuals

    @property
    def different_individuals(
        self,
    ) -> dict[
        typing.Union[tuple[NamedIndividual, ...], AllDifferent], OWLDifferentIndividuals
    ]:
        return self._different_individuals

    @property
    def subobject_properties_of(
        self,
    ) -> dict[tuple[ObjectPropertyClass, ObjectPropertyClass], OWLSubObjectPropertyOf]:
        return self._subobject_properties_of

    @property
    def subdata_properties_of(
        self,
    ) -> dict[tuple[DataPropertyClass, DataPropertyClass], OWLSubDataPropertyOf]:
        return self._subdata_properties_of

    @property
    def subannotation_properties_of(
        self,
    ) -> dict[
        tuple[AnnotationPropertyClass, AnnotationPropertyClass],
        OWLSubAnnotationPropertyOf,
    ]:
        return self._subannotation_properties_of

    @property
    def annotations(self) -> dict[EntityClass, tuple[URIRef, OWLAnnotation]]:
        return self._annotations

    @property
    def general_axioms(self) -> dict[EntityClass, OWLAnnotationAssertion]:
        return self._general_axioms

    @property
    def objects_some_values_from(self) -> dict[Restriction, OWLObjectSomeValuesFrom]:
        return self._objects_some_values_from

    @property
    def objects_all_values_from(self) -> dict[Restriction, OWLObjectAllValuesFrom]:
        return self._objects_all_values_from

    @property
    def objects_has_value(self) -> dict[Restriction, OWLObjectHasValue]:
        return self._objects_has_value

    @property
    def objects_has_self(self) -> dict[Restriction, OWLObjectHasSelf]:
        return self._objects_has_self

    @property
    def objects_min_cardinality(self) -> dict[Restriction, OWLObjectMinCardinality]:
        return self._objects_min_cardinality

    @property
    def objects_max_cardinality(self) -> dict[Restriction, OWLObjectMaxCardinality]:
        return self._objects_max_cardinality

    @property
    def objects_exact_cardinality(self) -> dict[Restriction, OWLObjectExactCardinality]:
        return self._objects_exact_cardinality

    @property
    def data_some_values_from(self) -> dict[Restriction, OWLDataSomeValuesFrom]:
        return self._data_some_values_from

    @property
    def data_all_values_from(self) -> dict[Restriction, OWLDataAllValuesFrom]:
        return self._data_all_values_from

    @property
    def data_has_value(self) -> dict[Restriction, OWLDataHasValue]:
        return self._data_has_value

    @property
    def data_min_cardinality(self) -> dict[Restriction, OWLDataMinCardinality]:
        return self._data_min_cardinality

    @property
    def data_max_cardinality(self) -> dict[Restriction, OWLDataMaxCardinality]:
        return self._data_max_cardinality

    @property
    def data_exact_cardinality(self) -> dict[Restriction, OWLDataExactCardinality]:
        return self._data_exact_cardinality

    @property
    def disjoint_unions(self) -> dict[tuple[ThingClass, ...], OWLDisjointUnion]:
        return self._disjoint_unions

    @property
    def equivalent_object_properties(
        self,
    ) -> dict[tuple[ObjectPropertyClass, ...], OWLEquivalentObjectProperties]:
        return self._equivalent_object_properties

    @property
    def disjoint_object_properties(
        self,
    ) -> dict[
        typing.Union[tuple[ObjectPropertyClass, ...], AllDifferent],
        OWLDisjointObjectProperties,
    ]:
        return self._disjoint_object_properties

    @property
    def inverse_object_properties(
        self,
    ) -> dict[tuple[ObjectPropertyClass, ...], OWLInverseObjectProperties]:
        return self._inverse_object_properties

    @property
    def functional_object_properties(
        self,
    ) -> dict[ObjectPropertyClass, OWLFunctionalObjectProperty]:
        return self._functional_object_properties

    @property
    def inverse_functional_object_properties(
        self,
    ) -> dict[ObjectPropertyClass, OWLInverseFunctionalObjectProperty]:
        return self._inverse_functional_object_properties

    @property
    def transitive_object_properties(
        self,
    ) -> dict[ObjectPropertyClass, OWLTransitiveObjectProperty]:
        return self._transitive_object_properties

    @property
    def symmetric_object_properties(
        self,
    ) -> dict[ObjectPropertyClass, OWLSymmetricObjectProperty]:
        return self._symmetric_object_properties

    @property
    def asymmetric_object_properties(
        self,
    ) -> dict[ObjectPropertyClass, OWLAsymmetricObjectProperty]:
        return self._asymmetric_object_properties

    @property
    def reflexive_object_properties(
        self,
    ) -> dict[ObjectPropertyClass, OWLReflexiveObjectProperty]:
        return self._reflexive_object_properties

    @property
    def irreflexive_object_properties(
        self,
    ) -> dict[ObjectPropertyClass, OWLIrreflexiveObjectProperty]:
        return self._irreflexive_object_properties

    @property
    def functional_data_properties(
        self,
    ) -> dict[DataPropertyClass, OWLFunctionalDataProperty]:
        return self._functional_data_properties

    @property
    def equivalent_data_properties(
        self,
    ) -> dict[tuple[DataPropertyClass, ...], OWLEquivalentDataProperties]:
        return self._equivalent_data_properties

    @property
    def disjoint_data_properties(
        self,
    ) -> dict[
        typing.Union[tuple[DataPropertyClass, ...], AllDifferent],
        OWLDisjointDataProperties,
    ]:
        return self._disjoint_data_properties

    @property
    def object_property_domains(
        self,
    ) -> dict[ObjectPropertyClass, OWLObjectPropertyDomain]:
        return self._object_property_domains

    @property
    def object_property_ranges(
        self,
    ) -> dict[ObjectPropertyClass, OWLObjectPropertyRange]:
        return self._object_property_ranges

    @property
    def data_property_domains(self) -> dict[DataPropertyClass, OWLDataPropertyDomain]:
        return self._data_property_domains

    @property
    def data_property_ranges(self) -> dict[DataPropertyClass, OWLDataPropertyRange]:
        return self._data_property_ranges

    @property
    def datatype_definitions(self) -> dict[DatatypeClass, OWLDatatypeDefinition]:
        return self._datatype_definitions

    @property
    def has_keys(self) -> dict[ThingClass, OWLHasKey]:
        return self._has_keys

    @property
    def negative_object_property_assertions(
        self,
    ) -> dict[
        tuple[ObjectPropertyClass, NamedIndividual, NamedIndividual],
        OWLNegativeObjectPropertyAssertion,
    ]:
        return self._negative_object_property_assertions

    @property
    def negative_data_property_assertions(
        self,
    ) -> dict[
        tuple[DataPropertyClass, NamedIndividual, Literal],
        OWLNegativeDataPropertyAssertion,
    ]:
        return self._negative_data_property_assertions

    @property
    def annotation_property_domains(
        self,
    ) -> dict[AnnotationPropertyClass, OWLAnnotationPropertyDomain]:
        return self._annotation_property_domains

    @property
    def annotation_property_ranges(
        self,
    ) -> dict[AnnotationPropertyClass, OWLAnnotationPropertyRange]:
        return self._annotation_property_ranges

    @property
    def annotation_assertions(
        self,
    ) -> dict[
        tuple[
            typing.Union[NamedIndividual, URIRef, str],
            AnnotationPropertyClass,
            typing.Union[NamedIndividual, URIRef, Literal],
        ],
        OWLAnnotationAssertion,
    ]:
        return self._annotation_assertions

    def get(self, element: AxiomsType) -> list[EntityClass]:
        if element == AxiomsType.DECLARATIONS:
            return (
                self.get_owl_classes()
                + self.get_owl_object_properties()
                + self.get_owl_datatype_properties()
                + self.get_owl_annotation_properties()
                + self.get_owl_individuals()
                + self.get_owl_datatypes()
            )
        if element == AxiomsType.GENERAL_CLASS_AXIOMS:
            return self.get_owl_general_axiom()
        if element == AxiomsType.CLASS_ASSERTIONS:
            return self.get_owl_class_assertions()
        if element == AxiomsType.ANNOTATION_PROPERTIES:
            return self.get_owl_annotation_properties()
        if element == AxiomsType.CLASSES:
            return self.get_owl_classes()
        if element == AxiomsType.OBJECT_PROPERTIES:
            return self.get_owl_object_properties()
        if element == AxiomsType.DATA_PROPERTIES:
            return self.get_owl_datatype_properties()
        if element == AxiomsType.INDIVIDUALS:
            return self.get_owl_individuals()
        if element == AxiomsType.SUBCLASSES:
            return self.get_owl_subclass_relationships()
        if element == AxiomsType.EQUIVALENT_CLASSES:
            return self.get_owl_equivalent_classes()
        if element == AxiomsType.DISJOINT_CLASSES:
            return self.get_owl_disjoint_classes()
        if element == AxiomsType.OBJECT_UNION_OF:
            return self.get_owl_object_union_of()
        if element == AxiomsType.DATA_UNION_OF:
            return self.get_owl_data_union_of()
        if element == AxiomsType.OBJECT_INTERSECTION_OF:
            return self.get_owl_object_intersection_of()
        if element == AxiomsType.DATA_INTERSECTION_OF:
            return self.get_owl_data_intersection_of()
        if element == AxiomsType.OBJECT_COMPLEMENT_OF:
            return self.get_owl_object_complement_of()
        if element == AxiomsType.DATA_COMPLEMENT_OF:
            return self.get_owl_data_complement_of()
        if element == AxiomsType.OBJECTS_ONE_OF:
            return self.get_owl_object_one_of()
        if element == AxiomsType.DATA_ONE_OF:
            return self.get_owl_data_one_of()
        if element == AxiomsType.DATATYPE_RESTRICTIONS:
            return self.get_owl_datatype_restrictions()
        if element == AxiomsType.INVERSE_OBJECT_PROPERTIES:
            return self.get_owl_inverse_object_properties()
        if element == AxiomsType.HAS_KEYS:
            return self.get_owl_has_keys()
        if element == AxiomsType.DATATYPES:
            return self.get_owl_datatypes()
        if element == AxiomsType.NEGATIVE_OBJECT_PROPERTY_ASSERTIONS:
            return self.get_owl_negative_object_property_assertions()
        if element == AxiomsType.NEGATIVE_DATA_PROPERTY_ASSERTIONS:
            return self.get_owl_negative_data_property_assertions()
        if element == AxiomsType.OBJECT_PROPERTY_ASSERTIONS:
            return self.get_owl_object_property_assertions()
        if element == AxiomsType.DATA_PROPERTY_ASSERTIONS:
            return self.get_owl_data_property_assertions()
        if element == AxiomsType.SAME_INDIVIDUALS:
            return self.get_owl_same_individuals()
        if element == AxiomsType.DIFFERENT_INDIVIDUALS:
            return self.get_owl_different_individuals()
        if element == AxiomsType.SUB_OBJECT_PROPERTIES:
            return self.get_owl_sub_object_property_of()
        if element == AxiomsType.SUB_DATA_PROPERTIES:
            return self.get_owl_sub_data_property_of()
        if element == AxiomsType.SUB_ANNOTATION_PROPERTIES:
            return self.get_owl_sub_annotation_property_of()
        if element == AxiomsType.EQUIVALENT_OBJECT_PROPERTIES:
            return self.get_owl_equivalent_object_properties()
        if element == AxiomsType.DISJOINT_OBJECT_PROPERTIES:
            return self.get_owl_disjoint_object_properties()
        if element == AxiomsType.ANNOTATIONS:
            return self.get_owl_annotations()
        if element == AxiomsType.OBJECTS_SOME_VALUES_FROM:
            return self.get_owl_object_some_values_from()
        if element == AxiomsType.OBJECTS_ALL_VALUES_FROM:
            return self.get_owl_object_all_values_from()
        if element == AxiomsType.OBJECTS_HAS_VALUE:
            return self.get_owl_object_has_value()
        if element == AxiomsType.OBJECTS_HAS_SELF:
            return self.get_owl_object_has_self()
        if element == AxiomsType.OBJECTS_MIN_CARDINALITY:
            return self.get_owl_object_min_cardinality()
        if element == AxiomsType.OBJECTS_MAX_CARDINALITY:
            return self.get_owl_object_max_cardinality()
        if element == AxiomsType.OBJECTS_EXACT_CARDINALITY:
            return self.get_owl_object_exact_cardinality()
        if element == AxiomsType.DATA_SOME_VALUES_FROM:
            return self.get_owl_data_some_values_from()
        if element == AxiomsType.DATA_ALL_VALUES_FROM:
            return self.get_owl_data_all_values_from()
        if element == AxiomsType.DATAS_HAS_VALUE:
            return self.get_owl_data_has_value()
        if element == AxiomsType.DATA_MIN_CARDINALITY:
            return self.get_owl_data_min_cardinality()
        if element == AxiomsType.DATA_MAX_CARDINALITY:
            return self.get_owl_data_max_cardinality()
        if element == AxiomsType.DATA_EXACT_CARDINALITY:
            return self.get_owl_data_exact_cardinality()
        if element == AxiomsType.DISJOINT_UNIONS:
            return self.get_owl_disjoint_unions()
        if element == AxiomsType.FUNCTIONAL_OBJECT_PROPERTIES:
            return self.get_owl_functional_object_properties()
        if element == AxiomsType.INVERSE_FUNCTIONAL_OBJECT_PROPERTIES:
            return self.get_owl_inverse_functional_object_properties()
        if element == AxiomsType.TRANSITIVE_OBJECT_PROPERTIES:
            return self.get_owl_transitive_object_properties()
        if element == AxiomsType.SYMMETRIC_OBJECT_PROPERTIES:
            return self.get_owl_symmetric_object_properties()
        if element == AxiomsType.ASYMMETRIC_OBJECT_PROPERTIES:
            return self.get_owl_asymmetric_object_properties()
        if element == AxiomsType.REFLEXIVE_OBJECT_PROPERTIES:
            return self.get_owl_reflexive_object_properties()
        if element == AxiomsType.IRREFLEXIVE_OBJECT_PROPERTIES:
            return self.get_owl_irreflexive_object_properties()
        if element == AxiomsType.FUNCIONAL_DATA_PROPERTIES:
            return self.get_owl_functional_data_properties()
        if element == AxiomsType.EQUIVALENT_DATA_PROPERTIES:
            return self.get_owl_equivalent_data_properties()
        if element == AxiomsType.DISJOINT_DATA_PROPERTIES:
            return self.get_owl_disjoint_data_properties()
        if element == AxiomsType.OBJECT_PROPERTY_DOMAIN:
            return self.get_owl_object_property_domains()
        if element == AxiomsType.OBJECT_PROPERTY_RANGE:
            return self.get_owl_object_property_ranges()
        if element == AxiomsType.DATA_PROPERTY_DOMAIN:
            return self.get_owl_data_property_domains()
        if element == AxiomsType.DATA_PROPERTY_RANGE:
            return self.get_owl_data_property_ranges()
        if element == AxiomsType.DATATYPE_DEFINITION:
            return self.get_owl_datatype_definitions()
        if element == AxiomsType.ANNOTATION_PROPERTY_DOMAINS:
            return self.get_owl_annotation_property_domains()
        if element == AxiomsType.ANNOTATION_PROPERTY_RANGES:
            return self.get_owl_annotation_property_ranges()
        raise ValueError

    def nothing_to_owl_class(self) -> OWLClass:
        entity = OWL.Nothing
        if entity not in self.classes:
            self.classes[entity] = OWLClass(
                IRI(
                    Namespace(OWL._NS),
                    OWL.Nothing,
                )
            )
        return self.classes[entity]

    def thing_to_owl_class(self) -> OWLClass:
        entity = OWL.Thing
        if entity not in self.classes:
            self.classes[entity] = OWLClass(
                IRI(
                    Namespace(OWL._NS),
                    OWL.Thing,
                )
            )
        return self.classes[entity]

    def to_owl_class(self, entity: ThingClass) -> typing.Optional[OWLClass]:
        if not entity or not isinstance(entity, ThingClass):
            return None
        is_nothing: bool = entity == Nothing or entity.iri == OWL.Nothing
        is_thing: bool = entity == Thing or entity.iri == OWL.Thing
        if is_nothing:
            entity = OWL.Nothing
        if is_thing:
            entity = OWL.Thing
        if entity not in self.classes:
            self.classes[entity] = OWLClass(
                IRI(
                    (
                        self.namespace
                        if not (is_nothing or is_thing)
                        else Namespace(OWL._NS)
                    ),
                    (
                        entity.name
                        if not (is_nothing or is_thing)
                        else (OWL.Nothing if is_nothing else OWL.Thing)
                    ),
                )
            )
        return self.classes[entity]

    def to_owl_object_intersection_of(
        self, entity: And
    ) -> typing.Optional[OWLObjectIntersectionOf]:
        if not entity or not isinstance(entity, And):
            return None
        # if any(not isinstance(c, ThingClass) for c in entity.Classes):
        #     return None
        if entity not in self.object_intersections_of:
            classes = [self.get_owl_class_expression(c) for c in entity.Classes]
            if None in classes:
                return None
            self.object_intersections_of[entity] = OWLObjectIntersectionOf(classes)
        return self.object_intersections_of[entity]

    def to_owl_data_intersection_of(
        self, entity: And
    ) -> typing.Optional[OWLDataIntersectionOf]:
        if not entity or not isinstance(entity, And):
            return None
        if any(
            not isinstance(c, (DataPropertyClass, DatatypeClass, ConstrainedDatatype))
            and c not in BASE_DATATYPES
            for c in entity.Classes
        ):
            return None
        if entity not in self.data_intersections_of:
            data_ranges = [self.get_owl_data_range(c) for c in entity.Classes]
            if None in data_ranges:
                return None
            self.data_intersections_of[entity] = OWLDataIntersectionOf(data_ranges)
        return self.data_intersections_of[entity]

    def to_owl_object_union_of(self, entity: Or) -> typing.Optional[OWLObjectUnionOf]:
        if not entity or not isinstance(entity, Or):
            return None
        # if any(not isinstance(c, ThingClass) for c in entity.Classes):
        #     return None
        if entity not in self.object_unions_of:
            classes = [self.get_owl_class_expression(c) for c in entity.Classes]
            if None in classes:
                return None
            self.object_unions_of[entity] = OWLObjectUnionOf(classes)
        return self.object_unions_of[entity]

    def to_owl_data_union_of(self, entity: Or) -> typing.Optional[OWLObjectUnionOf]:
        if not entity or not isinstance(entity, Or):
            return None
        if any(
            not isinstance(c, (DataPropertyClass, DatatypeClass, ConstrainedDatatype))
            and c not in BASE_DATATYPES
            for c in entity.Classes
        ):
            return None
        if entity not in self.data_unions_of:
            data_ranges = [self.get_owl_data_range(c) for c in entity.Classes]
            if None in data_ranges:
                return None
            self.data_unions_of[entity] = OWLDataUnionOf(data_ranges)
        return self.data_unions_of[entity]

    def to_owl_object_complement_of(
        self, entity: Not, expression: ThingClass
    ) -> typing.Optional[OWLObjectComplementOf]:
        if not entity or not isinstance(entity, Not):
            return None
        if entity not in self.object_complements_of:
            _class = self.get_owl_class_expression(expression)
            if not _class:
                return None
            self.object_complements_of[entity] = OWLObjectComplementOf(_class)
        return self.object_complements_of[entity]

    def to_owl_data_complement_of(
        self, entity: Not, data_range: EntityClass
    ) -> typing.Optional[OWLDataComplementOf]:
        if not entity or not isinstance(entity, Not):
            return None
        if entity not in self.data_complements_of:
            data_range = self.get_owl_data_range(data_range)
            if not data_range:
                return None
            self.data_complements_of[entity] = OWLDataComplementOf(data_range)
        return self.data_complements_of[entity]

    def to_owl_object_one_of(self, entity: OneOf) -> typing.Optional[OWLObjectOneOf]:
        if not entity or not isinstance(entity, OneOf):
            return None
        if len(entity.instances) == 0:
            return None
        if any(not is_named_individual(c) for c in entity.instances):
            return None
        if entity not in self.object_ones_of:
            individuals = [self.to_owl_individual(c) for c in entity.instances]
            if None in individuals:
                return None
            self.object_ones_of[entity] = OWLObjectOneOf(individuals)
        return self.object_ones_of[entity]

    def to_owl_data_one_of(self, entity: OneOf) -> typing.Optional[OWLDataOneOf]:
        if not entity or not isinstance(entity, OneOf):
            return None
        if len(entity.instances) == 0:
            return None
        if any(
            not isinstance(c, Literal) and not isinstance(c, BASE_DATATYPES)
            for c in entity.instances
        ):
            return None
        if entity not in self.data_ones_of:
            self.data_ones_of[entity] = OWLDataOneOf(
                [OWLLiteral(Literal(c)) for c in entity.instances]
            )
        return self.data_ones_of[entity]

    def to_owl_object_some_values_from(
        self, entity: Restriction
    ) -> typing.Optional[OWLObjectSomeValuesFrom]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type != get_abbreviation(OWL.someValuesFrom):
            return None
        if not isinstance(entity.property, ObjectPropertyClass):
            return None
        if entity not in self.objects_some_values_from:
            property, expression = (
                self.to_owl_object_property(entity.property),
                self.get_owl_class_expression(entity.value),
            )
            if not property or not expression:
                return None
            self.objects_some_values_from[entity] = OWLObjectSomeValuesFrom(
                property, expression
            )
        return self.objects_some_values_from[entity]

    def to_owl_object_all_values_from(
        self, entity: Restriction
    ) -> typing.Optional[OWLObjectAllValuesFrom]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type != get_abbreviation(OWL.allValuesFrom):
            return None
        if not isinstance(entity.property, ObjectPropertyClass):
            return None
        if entity not in self.objects_all_values_from:
            property, expression = (
                self.to_owl_object_property(entity.property),
                self.get_owl_class_expression(entity.value),
            )
            if not property or not expression:
                return None
            self.objects_all_values_from[entity] = OWLObjectAllValuesFrom(
                property, expression
            )
        return self.objects_all_values_from[entity]

    def to_owl_object_has_value(
        self, entity: Restriction
    ) -> typing.Optional[OWLObjectHasValue]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type != get_abbreviation(OWL.hasValue):
            return None
        if not isinstance(entity.property, ObjectPropertyClass):
            return None
        if entity not in self.objects_has_value:
            property, individual = (
                self.to_owl_object_property(entity.property),
                self.to_owl_individual(entity.value),
            )
            if not property or not individual:
                return None
            self.objects_has_value[entity] = OWLObjectHasValue(property, individual)
        return self.objects_has_value[entity]

    def to_owl_object_has_self(
        self, entity: Restriction
    ) -> typing.Optional[OWLObjectHasSelf]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type != get_abbreviation(OWL.hasSelf):
            return None
        if not isinstance(entity.property, ObjectPropertyClass):
            return None
        if entity not in self.objects_has_self:
            property = self.to_owl_object_property(entity.property)
            if not property:
                return None
            self.objects_has_self[entity] = OWLObjectHasSelf(property)
        return self.objects_has_self[entity]

    def to_owl_object_min_cardinality(
        self, entity: Restriction
    ) -> typing.Optional[OWLObjectMinCardinality]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type not in [
            get_abbreviation(OWL.minCardinality),
            get_abbreviation(OWL.minQualifiedCardinality),
        ]:
            return None
        if not isinstance(entity.property, ObjectPropertyClass):
            return None
        if entity not in self.objects_min_cardinality:
            property, expression = (
                self.to_owl_object_property(entity.property),
                self.get_owl_class_expression(entity.value),
            )
            if not property or not expression:
                return None
            self.objects_min_cardinality[entity] = OWLObjectMinCardinality(
                entity.cardinality, property, expression
            )
        return self.objects_min_cardinality[entity]

    def to_owl_object_max_cardinality(
        self, entity: Restriction
    ) -> typing.Optional[OWLObjectMaxCardinality]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type not in [
            get_abbreviation(OWL.maxCardinality),
            get_abbreviation(OWL.maxQualifiedCardinality),
        ]:
            return None
        if not isinstance(entity.property, ObjectPropertyClass):
            return None
        if entity not in self.objects_max_cardinality:
            property, expression = (
                self.to_owl_object_property(entity.property),
                self.get_owl_class_expression(entity.value),
            )
            if not property or not expression:
                return None
            self.objects_max_cardinality[entity] = OWLObjectMaxCardinality(
                entity.cardinality, property, expression
            )
        return self.objects_max_cardinality[entity]

    def to_owl_object_exact_cardinality(
        self, entity: Restriction
    ) -> typing.Optional[OWLObjectExactCardinality]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type != get_abbreviation(OWL.qualifiedCardinality):
            return None
        if not isinstance(entity.property, ObjectPropertyClass):
            return None
        if entity not in self.objects_exact_cardinality:
            property, expression = (
                self.to_owl_object_property(entity.property),
                self.get_owl_class_expression(entity.value),
            )
            if not property or not expression:
                return None
            self.objects_exact_cardinality[entity] = OWLObjectExactCardinality(
                entity.cardinality, property, expression
            )
        return self.objects_exact_cardinality[entity]

    def to_owl_data_some_values_from(
        self, entity: Restriction
    ) -> typing.Optional[OWLDataSomeValuesFrom]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type != get_abbreviation(OWL.someValuesFrom):
            return None
        if not isinstance(entity.property, DataPropertyClass):
            return None
        if entity not in self.data_some_values_from:
            data_range = self.graph.value(entity.storid, OWL.someValuesFrom)
            expressions = [self.to_owl_data_property(entity.property)]
            if not data_range or None in expressions:
                return None
            self.data_some_values_from[entity] = OWLDataSomeValuesFrom(
                expressions, OWLDatatype(data_range)
            )
        return self.data_some_values_from[entity]

    def to_owl_data_all_values_from(
        self, entity: Restriction
    ) -> typing.Optional[OWLDataAllValuesFrom]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type != get_abbreviation(OWL.allValuesFrom):
            return None
        if not isinstance(entity.property, DataPropertyClass):
            return None
        if entity not in self.data_all_values_from:
            data_range = self.graph.value(entity.storid, OWL.allValuesFrom)
            expressions = [self.to_owl_data_property(entity.property)]
            if not data_range or None in expressions:
                return None
            self.data_all_values_from[entity] = OWLDataAllValuesFrom(
                expressions, OWLDatatype(data_range)
            )
        return self.data_all_values_from[entity]

    def to_owl_data_has_value(
        self, entity: Restriction
    ) -> typing.Optional[OWLDataHasValue]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type != get_abbreviation(OWL.hasValue):
            return None
        if not isinstance(entity.property, DataPropertyClass):
            return None
        if entity not in self.data_has_value:
            self.data_has_value[entity] = OWLDataHasValue(
                self.to_owl_data_property(entity.property),
                OWLLiteral(Literal(entity.value)),
            )
        return self.data_has_value[entity]

    def to_owl_data_min_cardinality(
        self, entity: Restriction
    ) -> typing.Optional[OWLDataMinCardinality]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type not in [
            get_abbreviation(OWL.minCardinality),
            get_abbreviation(OWL.minQualifiedCardinality),
        ]:
            return None
        if not isinstance(entity.property, DataPropertyClass):
            return None
        if entity not in self.data_min_cardinality:
            data_range = self.graph.value(entity.storid, OWL.onDataRange)
            if data_range is not None:
                data_range = OWLDatatype(data_range)
            property = self.to_owl_data_property(entity.property)
            if not data_range or not property:
                return None
            self.data_min_cardinality[entity] = OWLDataMinCardinality(
                entity.cardinality,
                property,
                data_range,
            )
        return self.data_min_cardinality[entity]

    def to_owl_data_max_cardinality(
        self, entity: Restriction
    ) -> typing.Optional[OWLDataMaxCardinality]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type not in [
            get_abbreviation(OWL.maxCardinality),
            get_abbreviation(OWL.maxQualifiedCardinality),
        ]:
            return None
        if not isinstance(entity.property, DataPropertyClass):
            return None
        if entity not in self.data_max_cardinality:
            data_range = self.graph.value(entity.storid, OWL.onDataRange)
            if data_range is not None:
                data_range = OWLDatatype(data_range)
            property = self.to_owl_data_property(entity.property)
            if not data_range or not property:
                return None
            self.data_max_cardinality[entity] = OWLDataMaxCardinality(
                entity.cardinality,
                property,
                data_range,
            )
        return self.data_max_cardinality[entity]

    def to_owl_data_exact_cardinality(
        self, entity: Restriction
    ) -> typing.Optional[OWLDataExactCardinality]:
        if not entity or not isinstance(entity, Restriction):
            return None
        if entity.type not in [
            get_abbreviation(OWL.qualifiedCardinality),
            get_abbreviation(OWL.cardinality),
        ]:
            return None
        if not isinstance(entity.property, DataPropertyClass):
            return None
        if entity not in self.data_exact_cardinality:
            data_range = self.graph.value(entity.storid, OWL.onDataRange)
            if data_range is not None:
                data_range = OWLDatatype(data_range)
            property = self.to_owl_data_property(entity.property)
            if not data_range or not property:
                return None
            self.data_exact_cardinality[entity] = OWLDataExactCardinality(
                entity.cardinality,
                property,
                data_range,
            )
        return self.data_exact_cardinality[entity]

    def to_owl_datatype(
        self, entity: typing.Union[DatatypeClass, type]
    ) -> typing.Optional[typing.Union[OWLDatatype, set[OWLDatatype]]]:
        if not entity:
            return None
        if entity in BASE_DATATYPES:
            if entity == str:
                entity = XSD.string
            elif entity == int:
                entity = XSD.integer
            elif entity == float:
                entity = XSD.decimal
            elif entity == bool:
                entity = XSD.boolean
            elif entity == bytes:
                entity = XSD.byte
            if entity not in self.datatypes:
                self.datatypes[entity] = OWLDatatype(IRI(Namespace(XSD._NS), entity))
            return self.datatypes[entity]
        if not isinstance(entity, DatatypeClass):
            return None
        # if isinstance(entity, DatatypeClass):
        if entity not in self.datatypes:
            self.datatypes[entity] = OWLDatatype(IRI(self.namespace, entity.name))
        # elif isinstance(entity, ConstrainedDatatype):
        #     for subcls in entity.subclasses():
        #         if subcls in self.datatypes:
        #             continue
        #         self.datatypes[subcls] = OWLDatatype(IRI(self.namespace, subcls.name))
        #         self.datatypes[entity] = self.datatypes.get(entity, set()) | set(
        #             [self.datatypes[subcls]]
        #         )
        return self.datatypes[entity]

    def to_owl_datatype_restriction(
        self, entity: ConstrainedDatatype
    ) -> typing.Optional[OWLDatatypeRestriction]:
        if not entity:
            return None
        if not isinstance(entity, ConstrainedDatatype):
            return None

        def mapping(x) -> list[tuple[str, XSD]]:
            values = []
            if hasattr(x, "min_inclusive"):
                values.append(("min_inclusive", XSD.minInclusive))
            if hasattr(x, "min_exclusive"):
                values.append(("min_exclusive", XSD.minExclusive))
            if hasattr(x, "max_inclusive"):
                values.append(("max_inclusive", XSD.maxInclusive))
            if hasattr(x, "max_exclusive"):
                values.append(("max_exclusive", XSD.maxExclusive))
            return values

        if entity not in self.datatype_restrictions:
            base_datatype = self.graph.value(entity.storid, OWL.onDatatype)
            if base_datatype is None:
                return None
            self.datatype_restrictions[entity] = OWLDatatypeRestriction(
                OWLDatatype(base_datatype),
                [
                    OWLFacet(d, OWLLiteral(Literal(getattr(entity, str_d))))
                    for str_d, d in mapping(entity)
                ],
            )
        return self.datatype_restrictions[entity]

    def to_owl_subclass_of(
        self,
        sub_class: EntityClass,
        super_class: EntityClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLSubClassOf]:
        if not sub_class or not super_class:
            return None
        # if not isinstance(sub_class, ThingClass) or not isinstance(
        #     super_class, ThingClass
        # ):
        #     return None
        key = (sub_class, super_class)
        if key not in self.subclasses_of:
            sub_class_expr, super_class_expr = self.get_owl_class_expression(
                sub_class
            ), self.get_owl_class_expression(super_class)
            if not sub_class_expr or not super_class_expr:
                return None
            self.subclasses_of[key] = OWLSubClassOf(
                sub_class_expr,
                super_class_expr,
                annotations=(
                    self.get_owl_axiom_annotations_for(
                        sub_class, get_abbreviation(RDFS.subClassOf), super_class
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.subclasses_of[key]

    def to_owl_equivalent_classes(
        self,
        classes: tuple[EntityClass],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLEquivalentClasses]:
        if not classes:
            return None
        if len(classes) < 2:  # or any(not isinstance(c, ThingClass) for c in classes):
            return None
        if classes not in self.equivalent_classes:
            equiv_classes = [self.get_owl_class_expression(c) for c in classes]
            if None in equiv_classes:
                return None
            self.equivalent_classes[classes] = OWLEquivalentClasses(
                equiv_classes,
                annotations=annotations,
            )
        return self.equivalent_classes[classes]

    def to_owl_disjoint_classes(
        self, classes: typing.Union[tuple[ThingClass], AllDifferent]
    ) -> typing.Optional[OWLDisjointClasses]:
        if not classes:
            return None
        if (
            isinstance(classes, tuple)
            and len(classes) == 2
            # and all(isinstance(c, ThingClass) for c in classes)
        ):
            disj_classes = [self.get_owl_class_expression(c) for c in classes]
            if None in disj_classes:
                return None
            self.disjoint_classes[classes] = OWLDisjointClasses(
                disj_classes,
                annotations=self.get_owl_axiom_annotations_for(
                    classes[0], get_abbreviation(OWL.disjointWith), classes[1]
                ),
            )
        elif isinstance(classes, AllDifferent):
            # if any(not isinstance(c, ThingClass) for c in classes.entities):
            #     return None
            disj_classes = [self.get_owl_class_expression(c) for c in classes.entities]
            if None in disj_classes:
                return None
            self.disjoint_classes[classes] = OWLDisjointClasses(
                disj_classes,
                annotations=self.get_owl_axiom_annotations_for(
                    classes,
                    get_abbreviation(RDF.type),
                    get_abbreviation(OWL.AllDisjointClasses),
                ),
            )
        return self.disjoint_classes.get(classes)

    def to_owl_disjoint_union(
        self, main_class: EntityClass, classes: tuple[EntityClass]
    ) -> typing.Optional[OWLDisjointUnion]:
        if not main_class or not classes:
            return None
        if len(classes) < 3:
            return None
        # if any(not isinstance(c, ThingClass) for c in classes):
        #     return None
        if classes not in self.disjoint_unions:
            disj_class, disj_classes = self.to_owl_class(main_class), [
                self.get_owl_class_expression(c) for c in classes
            ]
            if not disj_class or None in disj_classes:
                return None
            self.disjoint_unions[classes] = OWLDisjointUnion(
                disj_class,
                disj_classes,
                annotations=self.get_owl_axiom_annotations_for(
                    main_class, get_abbreviation(OWL.disjointUnionOf)
                ),
            )
        return self.disjoint_unions[classes]

    def to_owl_sub_object_property_of(
        self,
        sub_property: typing.Union[tuple[ObjectPropertyClass], ObjectPropertyClass],
        super_property: ObjectPropertyClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLSubObjectPropertyOf]:
        if not sub_property or not super_property:
            return None
        if not isinstance(super_property, ObjectPropertyClass):
            return None
        if isinstance(sub_property, tuple) and all(
            isinstance(p, ObjectPropertyClass) for p in sub_property
        ):
            key = tuple(sorted(list(sub_property) + [super_property]))
            if key not in self.subobject_properties_of:
                properties = [self.to_owl_object_property(c) for c in sub_property]
                super_property_expr = self.to_owl_object_property(super_property)
                if not super_property_expr or None in properties:
                    return None
                self.subobject_properties_of[key] = OWLSubObjectPropertyOf(
                    OWLObjectPropertyChain(properties),
                    super_property_expr,
                    annotations=(
                        self.get_owl_axiom_annotations_for(
                            super_property, get_abbreviation(OWL.propertyChainAxiom)
                        )
                        if not annotations
                        else annotations
                    ),
                )
            return self.subobject_properties_of[key]
        elif isinstance(sub_property, ObjectPropertyClass):
            key = tuple(sorted([sub_property, super_property]))
            if key not in self.subobject_properties_of:
                sub_property_expr, super_property_expr = self.to_owl_object_property(
                    sub_property
                ), self.to_owl_object_property(super_property)
                if not sub_property_expr or not super_property_expr:
                    return None
                self.subobject_properties_of[key] = OWLSubObjectPropertyOf(
                    sub_property_expr,
                    super_property_expr,
                    annotations=(
                        self.get_owl_axiom_annotations_for(
                            sub_property,
                            get_abbreviation(RDFS.subPropertyOf),
                            super_property,
                        )
                        if not annotations
                        else annotations
                    ),
                )
            return self.subobject_properties_of[key]
        return None

    def to_owl_equivalent_object_properties(
        self,
        properties: tuple[ObjectPropertyClass],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLEquivalentObjectProperties]:
        if not properties:
            return None
        if any(not isinstance(p, ObjectPropertyClass) for p in properties):
            return None
        if properties not in self.equivalent_object_properties:
            equiv_properties = [self.to_owl_object_property(p) for p in properties]
            if None in equiv_properties:
                return None
            self.equivalent_object_properties[properties] = (
                OWLEquivalentObjectProperties(
                    equiv_properties,
                    annotations=annotations,
                )
            )
        return self.equivalent_object_properties[properties]

    def to_owl_disjoint_object_properties(
        self, properties: typing.Union[tuple[ObjectPropertyClass], AllDifferent]
    ) -> typing.Optional[OWLDisjointObjectProperties]:
        if not properties:
            return None
        if (
            isinstance(properties, tuple)
            and len(properties) == 2
            and all(isinstance(p, ObjectPropertyClass) for p in properties)
        ):
            if properties not in self.disjoint_object_properties:
                disj_properties = [self.to_owl_object_property(p) for p in properties]
                if None in disj_properties:
                    return None
                self.disjoint_object_properties[properties] = (
                    OWLDisjointObjectProperties(
                        disj_properties,
                        annotations=self.get_owl_axiom_annotations_for(
                            properties[0],
                            get_abbreviation(OWL.propertyDisjointWith),
                            properties[1],
                        ),
                    )
                )
        elif isinstance(properties, AllDifferent):
            if any(not isinstance(c, ObjectPropertyClass) for c in properties.entities):
                return None
            if properties not in self.disjoint_object_properties:
                disj_properties = [
                    self.to_owl_object_property(p) for p in properties.entities
                ]
                if None in disj_properties:
                    return None
                self.disjoint_object_properties[properties] = (
                    OWLDisjointObjectProperties(
                        disj_properties,
                        annotations=self.get_owl_axiom_annotations_for(
                            properties,
                            get_abbreviation(RDF.type),
                            get_abbreviation(OWL.AllDisjointProperties),
                        ),
                    )
                )
        return self.disjoint_object_properties.get(properties)

    def to_owl_inverse_object_properties(
        self,
        property: typing.Union[Inverse, ObjectPropertyClass, int],
        inv_property: typing.Union[Inverse, ObjectPropertyClass],
    ) -> typing.Optional[
        typing.Union[OWLInverseObjectProperty, OWLInverseObjectProperties]
    ]:
        if (not property and not isinstance(property, int)) or not inv_property:
            return None

        if isinstance(property, int):
            property = self.graph.value(property)
            if not property or not isinstance(property, BNode):
                return None
            inv_property_expr = self.to_owl_object_property(inv_property)
            if not inv_property_expr:
                return None
            self.inverse_object_properties[property] = OWLInverseObjectProperty(
                inv_property_expr
            )
            return self.inverse_object_properties[property]

        if isinstance(property, Inverse) and not isinstance(
            property.property, ObjectPropertyClass
        ):
            return None
        elif not isinstance(property, ObjectPropertyClass):
            return None
        if isinstance(inv_property, Inverse) and not isinstance(
            inv_property.property, ObjectPropertyClass
        ):
            return None
        elif not isinstance(inv_property, ObjectPropertyClass):
            return None

        chain: tuple[ObjectPropertyClass, ObjectPropertyClass] = (
            property,
            inv_property,
        )
        if (inv_property, property) in self.inverse_object_properties:
            chain = (inv_property, property)

        if chain not in self.inverse_object_properties:
            property_expr = (
                self.to_owl_object_property(chain[0])
                if isinstance(chain[0], ObjectPropertyClass)
                else OWLInverseObjectProperty(
                    self.to_owl_object_property(chain[0].property)
                )
            )
            inv_property_expr = (
                self.to_owl_object_property(chain[1])
                if isinstance(chain[1], ObjectPropertyClass)
                else OWLInverseObjectProperty(
                    self.to_owl_object_property(chain[1].property)
                )
            )
            if not property_expr or not inv_property_expr:
                return None

            self.inverse_object_properties[chain] = OWLInverseObjectProperties(
                property_expr,
                inv_property_expr,
                annotations=(
                    self.get_owl_axiom_annotations_for(
                        chain[0], get_abbreviation(OWL.inverseOf)
                    )
                    if isinstance(chain[0], ObjectPropertyClass)
                    else self.get_owl_axiom_annotations_for(
                        chain[1], get_abbreviation(OWL.inverseOf)
                    )
                ),
            )
        return self.inverse_object_properties[chain]

    def to_owl_object_property_domain(
        self,
        property: ObjectPropertyClass,
        cls: ThingClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLObjectPropertyDomain]:
        if not property or not isinstance(property, ObjectPropertyClass):
            return None
        if not cls:
            return None
        # if not isinstance(cls, ThingClass):
        #     return None
        if property not in self.object_property_domains:
            obj_property, cls_expr = self.to_owl_object_property(
                property
            ), self.get_owl_class_expression(cls)
            if not obj_property or not cls_expr:
                return None
            self.object_property_domains[property] = OWLObjectPropertyDomain(
                obj_property,
                cls_expr,
                annotations=(
                    self.get_owl_axiom_annotations_for(
                        property, get_abbreviation(RDFS.domain), cls
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.object_property_domains[property]

    def to_owl_object_property_range(
        self,
        property: ObjectPropertyClass,
        cls: ThingClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLObjectPropertyRange]:
        if not property or not isinstance(property, ObjectPropertyClass):
            return None
        if not cls:
            return None
        # if not isinstance(cls, ThingClass):
        #     return None
        if property not in self.object_property_ranges:
            obj_property, cls_expr = self.to_owl_object_property(
                property
            ), self.get_owl_class_expression(cls)
            if not obj_property or not cls_expr:
                return None
            self.object_property_ranges[property] = OWLObjectPropertyRange(
                obj_property,
                cls_expr,
                annotations=(
                    self.get_owl_axiom_annotations_for(
                        property, get_abbreviation(RDFS.range), cls
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.object_property_ranges[property]

    def to_owl_functional_object_property(
        self, property: ObjectPropertyClass
    ) -> typing.Optional[OWLFunctionalObjectProperty]:
        if not property or not isinstance(property, ObjectPropertyClass):
            return None
        if not any(p == FunctionalProperty for p in property.is_a):
            return None
        if property not in self.functional_object_properties:
            obj_property = self.to_owl_object_property(property)
            if not obj_property:
                return None
            self.functional_object_properties[property] = OWLFunctionalObjectProperty(
                obj_property,
                annotations=self.get_owl_axiom_annotations_for(
                    property,
                    get_abbreviation(RDF.type),
                    get_abbreviation(OWL.FunctionalProperty),
                ),
            )
        return self.functional_object_properties[property]

    def to_owl_inverse_functional_object_property(
        self, property: ObjectPropertyClass
    ) -> typing.Optional[OWLInverseFunctionalObjectProperty]:
        if not property or not isinstance(property, ObjectPropertyClass):
            return None
        if not any(p == InverseFunctionalProperty for p in property.is_a):
            return None
        if property not in self.inverse_functional_object_properties:
            obj_property = self.to_owl_object_property(property)
            if not obj_property:
                return None
            self.inverse_functional_object_properties[property] = (
                OWLInverseFunctionalObjectProperty(
                    obj_property,
                    annotations=self.get_owl_axiom_annotations_for(
                        property,
                        get_abbreviation(RDF.type),
                        get_abbreviation(OWL.InverseFunctionalProperty),
                    ),
                )
            )
        return self.inverse_functional_object_properties[property]

    def to_owl_reflexive_object_property(
        self, property: ObjectPropertyClass
    ) -> typing.Optional[OWLReflexiveObjectProperty]:
        if not property or not isinstance(property, ObjectPropertyClass):
            return None
        if not any(p == ReflexiveProperty for p in property.is_a):
            return None
        if property not in self.reflexive_object_properties:
            obj_property = self.to_owl_object_property(property)
            if not obj_property:
                return None
            self.reflexive_object_properties[property] = OWLReflexiveObjectProperty(
                obj_property,
                annotations=self.get_owl_axiom_annotations_for(
                    property,
                    get_abbreviation(RDF.type),
                    get_abbreviation(OWL.ReflexiveProperty),
                ),
            )
        return self.reflexive_object_properties[property]

    def to_owl_irreflexive_object_property(
        self, property: ObjectPropertyClass
    ) -> typing.Optional[OWLIrreflexiveObjectProperty]:
        if not property or not isinstance(property, ObjectPropertyClass):
            return None
        if not any(p == IrreflexiveProperty for p in property.is_a):
            return None
        if property not in self.irreflexive_object_properties:
            obj_property = self.to_owl_object_property(property)
            if not obj_property:
                return None
            self.irreflexive_object_properties[property] = OWLIrreflexiveObjectProperty(
                obj_property,
                annotations=self.get_owl_axiom_annotations_for(
                    property,
                    get_abbreviation(RDF.type),
                    get_abbreviation(OWL.IrreflexiveProperty),
                ),
            )
        return self.irreflexive_object_properties[property]

    def to_owl_symmetric_object_property(
        self, property: ObjectPropertyClass
    ) -> typing.Optional[OWLSymmetricObjectProperty]:
        if not property or not isinstance(property, ObjectPropertyClass):
            return None
        if not any(p == SymmetricProperty for p in property.is_a):
            return None
        if property not in self.symmetric_object_properties:
            obj_property = self.to_owl_object_property(property)
            if not obj_property:
                return None
            self.symmetric_object_properties[property] = OWLSymmetricObjectProperty(
                obj_property,
                annotations=self.get_owl_axiom_annotations_for(
                    property,
                    get_abbreviation(RDF.type),
                    get_abbreviation(OWL.SymmetricProperty),
                ),
            )
        return self.symmetric_object_properties[property]

    def to_owl_asymmetric_object_property(
        self, property: ObjectPropertyClass
    ) -> typing.Optional[OWLAsymmetricObjectProperty]:
        if not property or not isinstance(property, ObjectPropertyClass):
            return None
        if not any(p == AsymmetricProperty for p in property.is_a):
            return None
        if property not in self.asymmetric_object_properties:
            obj_property = self.to_owl_object_property(property)
            if not obj_property:
                return None
            self.asymmetric_object_properties[property] = OWLAsymmetricObjectProperty(
                obj_property,
                annotations=self.get_owl_axiom_annotations_for(
                    property,
                    get_abbreviation(RDF.type),
                    get_abbreviation(OWL.AsymmetricProperty),
                ),
            )
        return self.asymmetric_object_properties[property]

    def to_owl_transitive_object_property(
        self, property: ObjectPropertyClass
    ) -> typing.Optional[OWLTransitiveObjectProperty]:
        if not property or not isinstance(property, ObjectPropertyClass):
            return None
        if not any(p == TransitiveProperty for p in property.is_a):
            return None
        if property not in self.transitive_object_properties:
            obj_property = self.to_owl_object_property(property)
            if not obj_property:
                return None
            self.transitive_object_properties[property] = OWLTransitiveObjectProperty(
                obj_property,
                annotations=self.get_owl_axiom_annotations_for(
                    property,
                    get_abbreviation(RDF.type),
                    get_abbreviation(OWL.TransitiveProperty),
                ),
            )
        return self.transitive_object_properties[property]

    def to_owl_sub_data_property_of(
        self,
        sub_property: DataPropertyClass,
        super_property: DataPropertyClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLSubDataPropertyOf]:
        if not sub_property or not super_property:
            return None
        if not isinstance(sub_property, DataPropertyClass) or not isinstance(
            super_property, DataPropertyClass
        ):
            return None
        key = (sub_property, super_property)
        if key not in self.subdata_properties_of:
            sub_property_expr, super_property_expr = self.to_owl_data_property(
                sub_property
            ), self.to_owl_data_property(super_property)
            if not sub_property_expr or not super_property_expr:
                return None
            self.subdata_properties_of[key] = OWLSubDataPropertyOf(
                sub_property_expr,
                super_property_expr,
                annotations=(
                    self.get_owl_axiom_annotations_for(
                        sub_property,
                        get_abbreviation(RDFS.subPropertyOf),
                        super_property,
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.subdata_properties_of[key]

    def to_owl_equivalent_data_properties(
        self,
        classes: tuple[DataPropertyClass, ...],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLEquivalentDataProperties]:
        if not classes:
            return None
        if not isinstance(classes, tuple):
            return None
        if any(not isinstance(c, DataPropertyClass) for c in classes):
            return None
        if classes not in self.equivalent_data_properties:
            equiv_properties = [self.to_owl_data_property(c) for c in classes]
            if None in equiv_properties:
                return None
            self.equivalent_data_properties[classes] = OWLEquivalentDataProperties(
                equiv_properties, annotations=annotations
            )
        return self.equivalent_data_properties[classes]

    def to_owl_disjoint_data_properties(
        self, classes: typing.Union[tuple[DataPropertyClass, ...], AllDifferent]
    ) -> typing.Optional[OWLDisjointDataProperties]:
        if not classes:
            return None
        if not isinstance(classes, tuple) and not isinstance(classes, AllDifferent):
            return None
        if isinstance(classes, tuple) and (
            len(classes) != 2
            or any(not isinstance(c, DataPropertyClass) for c in classes)
        ):
            return None
        if isinstance(classes, AllDifferent) and any(
            not isinstance(c, DataPropertyClass) for c in classes.entities
        ):
            return None
        if isinstance(classes, tuple):
            disj_properties = [self.to_owl_data_property(c) for c in classes]
            if None in disj_properties:
                return None
            self.disjoint_data_properties[classes] = OWLDisjointDataProperties(
                disj_properties,
                annotations=self.get_owl_axiom_annotations_for(
                    classes[0],
                    get_abbreviation(OWL.propertyDisjointWith),
                    classes[1],
                ),
            )
        else:
            disj_properties = [self.to_owl_data_property(c) for c in classes.entities]
            if None in disj_properties:
                return None
            self.disjoint_data_properties[classes] = OWLDisjointDataProperties(
                disj_properties,
                annotations=self.get_owl_axiom_annotations_for(
                    classes,
                    get_abbreviation(RDF.type),
                    get_abbreviation(OWL.AllDisjointProperties),
                ),
            )
        return self.disjoint_data_properties[classes]

    def to_owl_data_property_domain(
        self,
        property: DataPropertyClass,
        domain: ThingClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLDataPropertyDomain]:
        if not property or not domain:
            return None
        if not isinstance(property, DataPropertyClass):
            return None
        # if not isinstance(domain, ThingClass):
        #     return None
        if property not in self.data_property_domains:
            data_property, cls_expr = self.to_owl_data_property(
                property
            ), self.get_owl_class_expression(domain)
            if not data_property or not cls_expr:
                return None
            self.data_property_domains[property] = OWLDataPropertyDomain(
                data_property,
                cls_expr,
                annotations=(
                    self.get_owl_axiom_annotations_for(
                        property, get_abbreviation(RDFS.domain), domain
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.data_property_domains[property]

    def to_owl_data_property_range(
        self,
        property: DataPropertyClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLDataPropertyRange]:
        if not property:
            return None
        if not isinstance(property, DataPropertyClass):
            return None
        if property not in self.data_property_ranges:
            data_range = self.get_owl_data_range(property.range[0])
            if not data_range:
                return None
            # data_range = self.graph.value(property.storid, RDFS.range)
            # if data_range is not None:
            #     data_range = OWLDatatype(data_range)
            data_property = self.to_owl_data_property(property)
            if not data_range or not data_property:
                return None
            self.data_property_ranges[property] = OWLDataPropertyRange(
                data_property,
                data_range,
                annotations=(
                    self.get_owl_axiom_annotations_for(
                        property, get_abbreviation(RDFS.range)
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.data_property_ranges[property]

    def to_owl_functional_data_property(
        self,
        property: DataPropertyClass,
    ) -> typing.Optional[OWLFunctionalDataProperty]:
        if not property:
            return None
        if not isinstance(property, DataPropertyClass):
            return None
        if not any(p == FunctionalProperty for p in property.is_a):
            return None
        if property not in self.functional_data_properties:
            data_property = self.to_owl_data_property(property)
            if not data_property:
                return None
            self.functional_data_properties[property] = OWLFunctionalDataProperty(
                data_property,
                annotations=self.get_owl_axiom_annotations_for(
                    property,
                    get_abbreviation(RDF.type),
                    get_abbreviation(OWL.FunctionalProperty),
                ),
            )
        return self.functional_data_properties[property]

    def to_owl_same_individual(
        self,
        individuals: tuple[NamedIndividual, ...],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLSameIndividual]:
        if not individuals:
            return None
        if not isinstance(individuals, tuple):
            return None
        if any(not is_named_individual(i) for i in individuals):
            return None
        if individuals not in self.same_individuals:
            same_individuals = [self.to_owl_individual(i) for i in individuals]
            if None in same_individuals:
                return None
            self.same_individuals[individuals] = OWLSameIndividual(
                same_individuals,
                annotations=annotations,
            )
        return self.same_individuals[individuals]

    def to_owl_different_individuals(
        self, individuals: typing.Union[tuple[NamedIndividual, ...], AllDifferent]
    ) -> typing.Optional[OWLDifferentIndividuals]:
        if not individuals:
            return None
        if not isinstance(individuals, tuple) and not isinstance(
            individuals, AllDifferent
        ):
            return None
        if isinstance(individuals, tuple) and (
            len(individuals) < 2 or any(not is_named_individual(i) for i in individuals)
        ):
            return None
        if isinstance(individuals, AllDifferent) and any(
            not is_named_individual(i) for i in individuals.entities
        ):
            return None
        if isinstance(individuals, tuple):
            diff_individuals = [self.to_owl_individual(i) for i in individuals]
            if None in diff_individuals:
                return None
            self.different_individuals[individuals] = OWLDifferentIndividuals(
                diff_individuals,
                annotations=self.get_owl_axiom_annotations_for(
                    individuals[0],
                    get_abbreviation(OWL.differentFrom),
                    individuals[1],
                ),
            )
        else:
            if individuals not in self.different_individuals:
                diff_individuals = [
                    self.to_owl_individual(i) for i in individuals.entities
                ]
                if None in diff_individuals:
                    return None
                self.different_individuals[individuals] = OWLDifferentIndividuals(
                    diff_individuals,
                    annotations=self.get_owl_axiom_annotations_for(
                        individuals,
                        get_abbreviation(RDF.type),
                        get_abbreviation(OWL.AllDifferent),
                    ),
                )
        return self.different_individuals[individuals]

    def to_owl_class_assertion(
        self, individual: NamedIndividual, individual_class: ThingClass
    ) -> typing.Optional[OWLClassAssertion]:
        if None in (individual, individual_class):
            return None
        # if not isinstance(individual, individual_class):
        #     return None
        # if not isinstance(individual_class, ThingClass):
        #     return None
        if (individual_class, individual) not in self.class_assertions:
            cls_expr, individual_expr = self.get_owl_class_expression(
                individual_class
            ), self.to_owl_individual(individual)
            if not cls_expr or not individual_expr:
                return None
            self.class_assertions[(individual_class, individual)] = OWLClassAssertion(
                cls_expr,
                individual_expr,
                annotations=self.get_owl_axiom_annotations_for(
                    individual, get_abbreviation(RDF.type), individual_class
                ),
            )
        return self.class_assertions[(individual_class, individual)]

    def to_owl_object_property_assertion(
        self,
        individual_source: NamedIndividual,
        property: ObjectPropertyClass,
        individual_target: NamedIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLObjectPropertyAssertion]:
        if None in (individual_source, property, individual_target):
            return None
        if not isinstance(property, ObjectPropertyClass):
            return None
        if not is_named_individual(individual_source) or not is_named_individual(
            individual_target
        ):
            return None
        key = (property, individual_source, individual_target)
        inv_key = (property.inverse_property, individual_target, individual_source)

        if property.inverse_property and str(property.name) >= str(
            property.inverse_property.name
        ):
            key = inv_key
            property, individual_source, individual_target = inv_key

        # if inv_key in self.object_property_assertions:
        #     key = inv_key
        if key not in self.object_property_assertions:
            obj_property, source, target = (
                self.to_owl_object_property(property),
                self.to_owl_individual(individual_source),
                self.to_owl_individual(individual_target),
            )
            if not obj_property or not source or not target:
                return None
            self.object_property_assertions[key] = OWLObjectPropertyAssertion(
                obj_property,
                source,
                target,
                annotations=(
                    self.get_owl_axiom_annotations_for(
                        individual_source, property, individual_target
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.object_property_assertions[key]

    def to_owl_negative_object_property_assertion(
        self,
        individual_source: NamedIndividual,
        property: ObjectPropertyClass,
        individual_target: NamedIndividual,
    ) -> typing.Optional[OWLNegativeObjectPropertyAssertion]:
        if None in (individual_source, property, individual_target):
            return None
        if not isinstance(property, ObjectPropertyClass):
            return None
        if not is_named_individual(individual_source) or not is_named_individual(
            individual_target
        ):
            return None
        key = (property, individual_source, individual_target)
        inv_key = (property.inverse_property, individual_target, individual_source)

        if property.inverse_property and str(property.name) >= str(
            property.inverse_property.name
        ):
            key = inv_key
            property, individual_source, individual_target = inv_key
        # if inv_key in self.negative_object_property_assertions:
        #     key = inv_key
        if key not in self.negative_object_property_assertions:
            obj_property, source, target = (
                self.to_owl_object_property(property),
                self.to_owl_individual(individual_source),
                self.to_owl_individual(individual_target),
            )
            if not obj_property or not source or not target:
                return None
            annotations: list[OWLAnnotation] = (
                self._get_owl_negative_property_assertion_annotations(
                    OWLNegativeObjectPropertyAssertion,
                    (individual_source, property, individual_target),
                )
            )
            self.negative_object_property_assertions[key] = (
                OWLNegativeObjectPropertyAssertion(
                    obj_property,
                    source,
                    target,
                    annotations=annotations if len(annotations) > 0 else None,
                )
            )
        return self.negative_object_property_assertions[key]

    def to_owl_data_property_assertion(
        self,
        individual_source: NamedIndividual,
        property: DataPropertyClass,
        target: Literal,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLDataPropertyAssertion]:
        if None in (individual_source, property, target):
            return None
        if not isinstance(property, DataPropertyClass):
            return None
        if not is_named_individual(individual_source):
            return None
        if not isinstance(target, Literal):
            return None
        key = (property, individual_source, target)
        if key not in self.data_property_assertions:
            data_property, source = self.to_owl_data_property(
                property
            ), self.to_owl_individual(individual_source)
            if not data_property or not source:
                return None
            self.data_property_assertions[key] = OWLDataPropertyAssertion(
                data_property,
                source,
                OWLLiteral(target),
                annotations=(
                    self.get_owl_axiom_annotations_for(individual_source, property)
                    if not annotations
                    else annotations
                ),
            )
        return self.data_property_assertions[key]

    def to_owl_negative_data_property_assertion(
        self,
        individual_source: NamedIndividual,
        property: DataPropertyClass,
        target: Literal,
    ) -> typing.Optional[OWLNegativeDataPropertyAssertion]:
        if None in (individual_source, property, target):
            return None
        if not isinstance(property, DataPropertyClass):
            return None
        if not is_named_individual(individual_source):
            return None
        if not isinstance(target, Literal):
            return None
        key = (property, individual_source, target)
        if key not in self.negative_data_property_assertions:
            data_property, source = self.to_owl_data_property(
                property
            ), self.to_owl_individual(individual_source)
            if not data_property or not source:
                return None
            annotations: list[OWLAnnotation] = (
                self._get_owl_negative_property_assertion_annotations(
                    OWLNegativeDataPropertyAssertion,
                    (individual_source, property, target.value),
                )
            )
            self.negative_data_property_assertions[key] = (
                OWLNegativeDataPropertyAssertion(
                    data_property,
                    source,
                    OWLLiteral(target),
                    annotations=annotations if len(annotations) > 0 else None,
                )
            )
        return self.negative_data_property_assertions[key]

    def nothing_to_owl_class_declaration(
        self,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLDeclaration]:
        entity = OWL.Nothing
        if entity not in self.declarations:
            obj = self.nothing_to_owl_class()
            if not obj:
                return None
            self.declarations[entity] = OWLDeclaration(
                obj,
                annotations=(
                    self.get_owl_declaration_annotations_for(
                        entity, get_abbreviation(OWL.Nothing)
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.declarations[entity]

    def thing_to_owl_class_declaration(
        self,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLDeclaration]:
        entity = OWL.Thing
        if entity not in self.declarations:
            obj = self.thing_to_owl_class()
            if not obj:
                return None
            self.declarations[entity] = OWLDeclaration(
                obj,
                annotations=(
                    self.get_owl_declaration_annotations_for(
                        entity, get_abbreviation(OWL.Thing)
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.declarations[entity]

    def to_owl_class_declaration(
        self,
        entity: EntityClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLDeclaration]:
        if not entity or not isinstance(entity, EntityClass):
            return None
        if entity not in self.declarations:
            obj = self.to_owl_class(entity)
            if not obj:
                return None
            self.declarations[entity] = OWLDeclaration(
                obj,
                annotations=(
                    self.get_owl_declaration_annotations_for(
                        entity, get_abbreviation(OWL.Class)
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.declarations[entity]

    def to_owl_datatype_declaration(
        self,
        entity: DatatypeClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLDeclaration]:
        if not entity or not isinstance(entity, DatatypeClass):
            return None
        if entity not in self.declarations:
            obj = self.to_owl_datatype(entity)
            if not obj:
                return None
            self.declarations[entity] = OWLDeclaration(
                obj,
                annotations=(
                    self.get_owl_declaration_annotations_for(
                        entity, get_abbreviation(RDFS.Datatype)
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.declarations[entity]

    def to_owl_object_property(
        self, property: ObjectPropertyClass
    ) -> typing.Optional[OWLObjectProperty]:
        if not property or not isinstance(property, ObjectPropertyClass):
            return None
        if property not in self.object_properties:
            self.object_properties[property] = OWLObjectProperty(
                IRI(
                    self.namespace,
                    property.name,
                )
            )
        return self.object_properties[property]

    def to_owl_object_property_declaration(
        self,
        property: ObjectPropertyClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLDeclaration]:
        if not property or not isinstance(property, ObjectPropertyClass):
            return None
        if property not in self.declarations:
            obj = self.to_owl_object_property(property)
            if not obj:
                return None
            self.declarations[property] = OWLDeclaration(
                obj,
                annotations=(
                    self.get_owl_declaration_annotations_for(
                        property, get_abbreviation(OWL.ObjectProperty)
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.declarations[property]

    def to_owl_data_property(
        self, property: DataPropertyClass
    ) -> typing.Optional[OWLDataProperty]:
        if not property or not isinstance(property, DataPropertyClass):
            return None
        if property not in self.data_properties:
            self.data_properties[property] = OWLDataProperty(
                IRI(
                    self.namespace,
                    property.name,
                )
            )
        return self.data_properties[property]

    def to_owl_data_property_declaration(
        self,
        property: DataPropertyClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLDeclaration]:
        if not property or not isinstance(property, DataPropertyClass):
            return None
        if property not in self.declarations:
            obj = self.to_owl_data_property(property)
            if not obj:
                return None
            self.declarations[property] = OWLDeclaration(
                obj,
                annotations=(
                    self.get_owl_declaration_annotations_for(
                        property, get_abbreviation(OWL.DatatypeProperty)
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.declarations[property]

    def to_owl_annotation_property(
        self, property: AnnotationPropertyClass
    ) -> typing.Optional[OWLAnnotationProperty]:
        if not property or not isinstance(property, AnnotationPropertyClass):
            return None
        if property not in self.annotation_properties:
            self.annotation_properties[property] = OWLAnnotationProperty(
                IRI(
                    self.namespace,
                    property.name,
                )
            )
        return self.annotation_properties[property]

    def to_owl_annotation_property_declaration(
        self,
        property: AnnotationPropertyClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLDeclaration]:
        if not property or not isinstance(property, AnnotationPropertyClass):
            return None
        if property not in self.declarations:
            obj = self.to_owl_annotation_property(property)
            if not obj:
                return None
            self.declarations[property] = OWLDeclaration(
                obj,
                annotations=(
                    self.get_owl_declaration_annotations_for(
                        property, get_abbreviation(OWL.AnnotationProperty)
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.declarations[property]

    def to_owl_individual(
        self, individual: NamedIndividual
    ) -> typing.Optional[OWLIndividual]:
        if not individual or not is_named_individual(individual):
            return None
        if individual not in self.individuals:
            cls_func = (
                OWLAnonymousIndividual
                if isinstance(individual.iri, URIRef)
                else OWLNamedIndividual
            )
            self.individuals[individual] = cls_func(
                IRI(
                    self.namespace,
                    individual.name,
                )
            )
        return self.individuals[individual]

    def to_owl_individual_declaration(
        self,
        individual: NamedIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLDeclaration]:
        if not individual or not is_named_individual(individual):
            return None
        if individual not in self.declarations:
            obj = self.to_owl_individual(individual)
            if not obj:
                return None
            self.declarations[individual] = OWLDeclaration(
                obj,
                annotations=(
                    self.get_owl_declaration_annotations_for(
                        individual, get_abbreviation(OWL.NamedIndividual)
                    )
                    if not annotations
                    else annotations
                ),
            )
        return self.declarations[individual]

    def to_owl_annotation_assertion(
        self,
        subject: typing.Union[NamedIndividual, URIRef, str],
        property: AnnotationPropertyClass,
        value: typing.Union[NamedIndividual, URIRef, Literal],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLAnnotationAssertion]:
        if None in (subject, property, value):
            return None
        if not isinstance(subject, (URIRef, str)) and not is_named_individual(subject):
            return None
        if not isinstance(value, (URIRef, Literal)) and not is_named_individual(value):
            return None
        if not isinstance(property, AnnotationPropertyClass):
            return None
        key = (subject, property, value)
        if key not in self.annotation_assertions:
            source = (
                self.to_owl_individual(subject)
                if is_named_individual(subject)
                else IRI(self.namespace, subject)
            )
            ann_property = self.to_owl_annotation_property(property)
            value = (
                self.to_owl_individual(value)
                if is_named_individual(value)
                else (
                    IRI(self.namespace, value)
                    if isinstance(value, URIRef)
                    else OWLLiteral(value)
                )
            )
            if not source or not value or not ann_property:
                return None
            self.annotation_assertions[key] = OWLAnnotationAssertion(
                source,
                ann_property,
                value,
                annotations,
            )
        return self.annotation_assertions[key]

    def to_owl_sub_annotation_property_of(
        self,
        sub_property: AnnotationPropertyClass,
        super_property: AnnotationPropertyClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLSubAnnotationPropertyOf]:
        if not sub_property or not isinstance(sub_property, AnnotationPropertyClass):
            return None
        if not super_property or not isinstance(
            super_property, AnnotationPropertyClass
        ):
            return None
        key = (sub_property, super_property)
        if key not in self.subannotation_properties_of:
            sub_property_expr, super_property_expr = self.to_owl_annotation_property(
                sub_property
            ), self.to_owl_annotation_property(super_property)
            if not sub_property_expr or not super_property_expr:
                return None
            self.subannotation_properties_of[key] = OWLSubAnnotationPropertyOf(
                sub_property_expr,
                super_property_expr,
                annotations,
            )
        return self.subannotation_properties_of[key]

    def to_owl_annotation_property_domain(
        self,
        property: AnnotationPropertyClass,
        domain: URIRef,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLAnnotationPropertyDomain]:
        if not property or not isinstance(property, AnnotationPropertyClass):
            return None
        if not domain or not isinstance(domain, URIRef):
            return None
        if property not in self.annotation_property_domains:
            self.annotation_property_domains[property] = OWLAnnotationPropertyDomain(
                self.to_owl_annotation_property(property),
                IRI(self.namespace, domain),
                annotations,
            )
        return self.annotation_property_domains[property]

    def to_owl_annotation_property_range(
        self,
        property: AnnotationPropertyClass,
        range: URIRef,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLAnnotationPropertyRange]:
        if not property or not isinstance(property, AnnotationPropertyClass):
            return None
        if not range or not isinstance(range, URIRef):
            return None
        if property not in self.annotation_property_ranges:
            ann_property = self.to_owl_annotation_property(property)
            if not ann_property:
                return None
            self.annotation_property_ranges[property] = OWLAnnotationPropertyRange(
                ann_property,
                IRI(self.namespace, range),
                annotations,
            )
        return self.annotation_property_ranges[property]

    def to_owl_general_class_axiom(
        self,
        left: typing.Union[And, Or, Not, Restriction],
        property: URIRef,
        right: EntityClass,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> typing.Optional[OWLGeneralClassAxiom]:
        if not left or not isinstance(left, (And, Or, Not, Restriction)):
            return None
        if not right:
            return None
        # if not isinstance(right, (And, Or, Not, Restriction)):
        #     return None
        if not property or not isinstance(property, URIRef):
            return None
        key = (property, left, right)
        if key not in self.general_axioms:
            left_expr, right_expr = self.get_owl_class_expression(
                left
            ), self.get_owl_class_expression(right)
            if not left_expr or not right_expr:
                return None
            self.general_axioms[key] = OWLGeneralClassAxiom(
                left_expr,
                IRI(self.namespace, property),
                right_expr,
                annotations,
            )
        return self.general_axioms[key]

    def _map_functions(
        self, functions: list[typing.Callable], *params: tuple[OWLObject, ...]
    ) -> OWLObject:
        for function in functions:
            # if len(params) != len(inspect.getfullargspec(function).args) - 1:
            #     continue
            if len(params) != len(inspect.signature(function).parameters):
                continue
            obj = function(*params)
            if not obj:
                continue
            return obj
        raise TypeError

    def get_owl_class_expression(
        self, *params: tuple[OWLObject, ...]
    ) -> OWLClassExpression:
        functions: list[typing.Callable] = [
            self.to_owl_class,
            self.to_owl_object_intersection_of,
            self.to_owl_object_union_of,
            self.to_owl_object_complement_of,
            self.to_owl_object_one_of,
            self.to_owl_object_some_values_from,
            self.to_owl_object_all_values_from,
            self.to_owl_object_has_value,
            self.to_owl_object_has_self,
            self.to_owl_object_min_cardinality,
            self.to_owl_object_max_cardinality,
            self.to_owl_object_exact_cardinality,
            self.to_owl_data_some_values_from,
            self.to_owl_data_all_values_from,
            self.to_owl_data_has_value,
            self.to_owl_data_min_cardinality,
            self.to_owl_data_max_cardinality,
            self.to_owl_data_exact_cardinality,
        ]
        return self._map_functions(functions, *params)

    def get_owl_data_range(self, *params: tuple[OWLObject, ...]) -> OWLDataRange:
        functions: list[typing.Callable] = [
            self.to_owl_datatype,
            self.to_owl_data_intersection_of,
            self.to_owl_data_union_of,
            self.to_owl_data_complement_of,
            self.to_owl_data_one_of,
            self.to_owl_datatype_restriction,
        ]
        return self._map_functions(functions, *params)

    def get_owl_class_axiom(self, *params: tuple[OWLObject, ...]) -> OWLClassAxiom:
        functions: list[typing.Callable] = [
            self.to_owl_subclass_of,
            self.to_owl_equivalent_classes,
            self.to_owl_disjoint_classes,
            self.to_owl_disjoint_union,
        ]
        return self._map_functions(functions, *params)

    def get_owl_object_property_axiom(
        self, *params: tuple[OWLObject, ...]
    ) -> OWLObjectPropertyAxiom:
        functions: list[typing.Callable] = [
            self.to_owl_sub_object_property_of,
            self.to_owl_equivalent_object_properties,
            self.to_owl_disjoint_object_properties,
            self.to_owl_inverse_object_properties,
            self.to_owl_object_property_domain,
            self.to_owl_object_property_range,
            self.to_owl_functional_object_property,
            self.to_owl_inverse_functional_object_property,
            self.to_owl_reflexive_object_property,
            self.to_owl_irreflexive_object_property,
            self.to_owl_symmetric_object_property,
            self.to_owl_asymmetric_object_property,
            self.to_owl_transitive_object_property,
        ]
        return self._map_functions(functions, *params)

    def get_owl_data_property_axiom(
        self, *params: tuple[OWLObject, ...]
    ) -> OWLDataPropertyAxiom:
        functions: list[typing.Callable] = [
            self.to_owl_sub_data_property_of,
            self.to_owl_equivalent_data_properties,
            self.to_owl_disjoint_data_properties,
            self.to_owl_data_property_domain,
            self.to_owl_data_property_range,
            self.to_owl_functional_data_property,
        ]
        return self._map_functions(functions, *params)

    def get_owl_assertion(self, *params: tuple[OWLObject, ...]) -> OWLAssertion:
        functions: list[typing.Callable] = [
            self.to_owl_same_individual,
            self.to_owl_different_individuals,
            self.to_owl_class_assertion,
            self.to_owl_object_property_assertion,
            self.to_owl_negative_object_property_assertion,
            self.to_owl_data_property_assertion,
            self.to_owl_negative_data_property_assertion,
        ]
        return self._map_functions(functions, *params)

    def get_owl_declaration(self, *params: tuple[OWLObject, ...]) -> OWLDeclaration:
        functions: list[typing.Callable] = [
            self.to_owl_class_declaration,
            self.to_owl_datatype_declaration,
            self.to_owl_object_property_declaration,
            self.to_owl_data_property_declaration,
            self.to_owl_annotation_property_declaration,
            self.to_owl_individual_declaration,
        ]
        return self._map_functions(functions, *params)

    def get_owl_datatype_definition(
        self,
        datatype: typing.Union[DatatypeClass, ConstrainedDatatype],
        data_range: typing.Union[DatatypeClass, ConstrainedDatatype, And],
    ) -> typing.Optional[OWLDatatypeDefinition]:
        if not isinstance(datatype, (DatatypeClass, ConstrainedDatatype)):
            return None
        if datatype not in self.datatype_definitions:
            obj = self.to_owl_datatype(datatype)
            if not obj:
                return None
            if isinstance(data_range, And):
                data_range = self.to_owl_data_intersection_of(data_range)
            elif isinstance(data_range, ConstrainedDatatype):
                data_range = self.to_owl_datatype(data_range)
            else:
                data_range = OWLDatatype(
                    self.graph.value(data_range.storid, OWL.onDatatype)
                )
            self.datatype_definitions[datatype] = OWLDatatypeDefinition(
                obj,
                data_range,
                annotations=self.get_owl_axiom_annotations_for(
                    datatype, get_abbreviation(OWL.equivalentClass)
                ),
            )
        return self.datatype_definitions[datatype]

    def get_owl_has_key(
        self,
        entity: EntityClass,
        objects: tuple[ObjectPropertyClass, ...],
        data: tuple[DataPropertyClass, ...],
    ) -> typing.Optional[OWLHasKey]:
        if not isinstance(entity, EntityClass):
            return None
        if not isinstance(objects, tuple):
            return None
        elif any(not isinstance(o, ObjectPropertyClass) for o in objects):
            return None
        if not isinstance(data, tuple):
            return None
        elif any(not isinstance(d, DataPropertyClass) for d in data):
            return None
        if entity not in self.has_keys:
            self.has_keys[entity] = OWLHasKey(
                self.get_owl_class_expression(entity),
                [self.to_owl_object_property(ob) for ob in objects],
                [self.to_owl_data_property(dp) for dp in data],
                annotations=self.get_owl_axiom_annotations_for(
                    entity, get_abbreviation(OWL.hasKey)
                ),
            )
        return self.has_keys[entity]

    def get_owl_annotation_axiom(
        self, *params: tuple[OWLObject, ...]
    ) -> OWLAnnotationAxiom:
        functions: list[typing.Callable] = [
            self.to_owl_annotation_assertion,
            self.to_owl_sub_annotation_property_of,
            self.to_owl_annotation_property_domain,
            self.to_owl_annotation_property_range,
        ]
        return self._map_functions(functions, *params)

    def get_owl_axiom(self, *params: tuple[OWLObject, ...]) -> OWLAxiom:
        functions: list[typing.Callable] = [
            self.get_owl_declaration,
            self.get_owl_class_axiom,
            self.get_owl_object_property_axiom,
            self.get_owl_data_property_axiom,
            self.get_owl_datatype_definition,
            self.get_owl_has_key,
            self.get_owl_assertion,
            self.get_owl_annotation_axiom,
        ]
        return self._map_functions(functions, *params)

    def exists_element_by_iri_type(self, iri: URIRef, type=URIRef) -> bool:
        result = self.world.search(iri=iri, type=get_abbreviation(type))
        return True if len(result) > 0 else False

    def exists_object_property(self, object: URIRef) -> bool:
        return self.exists_element_by_iri_type(object, OWL.ObjectProperty)

    def exists_data_property(self, data: URIRef) -> bool:
        return self.exists_element_by_iri_type(data, OWL.DatatypeProperty)

    def exists_annotation_property(self, property: URIRef) -> bool:
        return self.exists_element_by_iri_type(property, OWL.AnnotationProperty)

    def exists_class(self, class_: URIRef) -> bool:
        return self.exists_element_by_iri_type(class_, OWL.Class)

    def exists_datatype(self, datatype: URIRef) -> bool:
        return self.exists_element_by_iri_type(datatype, RDFS.Datatype)

    def exists_data_range(self, data_range: URIRef) -> bool:
        return self.exists_element_by_iri_type(data_range, OWL.DataRange)

    def _to_annotation_property(
        self, property: typing.Union[int, AnnotationPropertyClass]
    ) -> typing.Union[URIRef, AnnotationPropertyClass]:
        if property in self.annotation_properties:
            return property
        if type(property) == int:
            if property in RDFXMLGetter.STANDARD_ANNOTATIONS:
                iri_property = URIRef(RDFXMLGetter.STANDARD_ANNOTATIONS[property].iri)
                self.annotation_properties[iri_property] = OWLAnnotationProperty(
                    iri_property
                )
                return iri_property
            else:
                iri_property = URIRef(_universal_abbrev_2_iri.get(property))
                if iri_property is None:
                    return
                self.annotation_properties[iri_property] = OWLAnnotationProperty(
                    iri_property
                )
                return iri_property
        elif isinstance(property, AnnotationPropertyClass):
            self.annotation_properties[property] = OWLAnnotationProperty(property.iri)
            return property
        else:
            raise TypeError

    def get_owl_ontology_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        query: str = """
        SELECT ?comment ?literal
        WHERE {
            ?ontology rdf:type owl:Ontology .
            ?ontology ?comment ?literal .
            ?comment rdf:type owl:AnnotationProperty .
            FILTER(isIRI(?comment))
            FILTER(isLiteral(?literal))
        }
        """
        annotations: list[OWLAnnotation] = []
        for cls in self.world.sparql(query):
            cls[0] = self._to_annotation_property(cls[0])
            annotations.append(
                OWLAnnotation(
                    self.annotation_properties[cls[0]], OWLLiteral(Literal(cls[1]))
                )
            )
        return annotations if len(annotations) > 0 else None

    def get_owl_axiom_annotations_for(
        self,
        source: EntityClass,
        property: typing.Optional[EntityClass] = None,
        target: typing.Optional[EntityClass] = None,
    ) -> typing.Optional[list[OWLAnnotation]]:
        annotations: list[OWLAnnotation] = []
        query: str = (
            f"SELECT ?comment ?literal\n"
            "WHERE {\n"
            "\t{?axiom rdf:type owl:Axiom .} UNION {?axiom rdf:type owl:Annotation .}\n"
            f"\t?axiom owl:annotatedSource {'??' if source else '?source'} .\n"
            f"\t?axiom owl:annotatedProperty {'??' if property else '?property'} .\n"
            f"\t?axiom owl:annotatedTarget {'??' if target else '?target'} .\n"
            "\t?axiom ?comment ?literal .\n"
            "\t?comment rdf:type owl:AnnotationProperty .\n"
            "\tFILTER(isIRI(?comment))\n"
            "\tFILTER(isLiteral(?literal))\n"
            "\tFILTER(isBlank(?axiom))\n"
            "}"
        )

        params = tuple(filter(bool, (source, property, target)))
        for cls in self.world.sparql(query, params, error_on_undefined_entities=False):
            cls[0] = self._to_annotation_property(cls[0])
            annotations.append(
                OWLAnnotation(
                    self.annotation_properties[cls[0]], OWLLiteral(Literal(cls[1]))
                )
            )
        return annotations if len(annotations) > 0 else None

    def get_owl_declaration_annotations_for(
        self,
        source: EntityClass,
        target: EntityClass = None,
    ) -> typing.Optional[list[OWLAnnotation]]:
        annotations: list[OWLAnnotation] = []
        query: str = """
        SELECT ?comment ?literal
        WHERE {
            ??1 rdf:type ??2 .
            ??1 ?comment ?literal .
            ?comment rdf:type owl:AnnotationProperty .
            FILTER(isIRI(?comment))
            FILTER(isLiteral(?literal))
        }
        """
        for cls in self.world.sparql(query, (source, target)):
            cls[0] = self._to_annotation_property(cls[0])
            annotations.append(
                OWLAnnotation(
                    self.annotation_properties[cls[0]], OWLLiteral(Literal(cls[1]))
                )
            )
        return annotations if len(annotations) > 0 else None

    def _get_owl_property_from_integer(
        self, int_property: int, predicate_ref: URIRef
    ) -> URIRef:
        if int_property in _universal_abbrev_2_iri:
            return URIRef(_universal_abbrev_2_iri[int_property])
        else:
            return self.graph.value(
                list(self.graph.subject_predicates(int_property))[0][0],
                predicate_ref,
            )

    def get_owl_general_axiom(self) -> list[EntityClass]:
        """
        Get all OWL general axioms using SPARQL.

        Returns:
            List of class URIs
        """
        query = """
        SELECT DISTINCT ?source ?property ?target ?target_owl_type ?comment ?literal
        WHERE {
            ?axiom rdf:type owl:Axiom .
            ?axiom owl:annotatedSource ?source .
            ?axiom owl:annotatedProperty ?property .
            ?axiom owl:annotatedTarget ?target .
            ?target rdf:type ?target_owl_type .
            ?axiom ?comment ?literal .
            ?comment rdf:type owl:AnnotationProperty .
            FILTER(isBlank(?axiom))
            FILTER(isIRI(?comment))
            FILTER(isLiteral(?literal))
        }
        """
        for cls in self.world.sparql_query(query):
            key = tuple(cls)
            if key in self.general_axioms:
                continue
            (
                annotated_source,
                annotated_property,
                annotated_target,
                annotated_target_owl_type,
                comment,
                literal,
            ) = cls
            if not isinstance(annotated_source, (And, Or, Not, Restriction)):
                continue
            # if not isinstance(annotated_target, (And, Or, Not, Restriction)):
            #     continue
            if isinstance(annotated_property, int):
                annotated_property = self._get_owl_property_from_integer(
                    annotated_property, OWL.annotatedProperty
                )
            if isinstance(annotated_target_owl_type, int):
                annotated_target_owl_type = self._get_owl_property_from_integer(
                    annotated_target_owl_type, RDF.type
                )
            annotations: typing.Optional[list[OWLAnnotation]] = None
            if comment and literal:
                if comment not in self.annotation_properties:
                    comment = self._to_annotation_property(comment)
                annotations = (
                    [
                        OWLAnnotation(
                            self.annotation_properties[comment],
                            OWLLiteral(Literal(literal)),
                        )
                    ],
                )
            key = (annotated_property, annotated_source, annotated_target)
            if key in self.general_axioms:
                self.general_axioms[key].axiom_annotations = annotations
            else:
                self.general_axioms[key] = self.to_owl_general_class_axiom(
                    annotated_source, annotated_property, annotated_target, annotations
                )
        return list(self.general_axioms.values())

    def get_owl_classes(self) -> list[OWLClass]:
        """
        Get all OWL classes using SPARQL.

        Returns:
            List of class URIs
        """
        query = """
        SELECT DISTINCT ?class
        WHERE {
            { ?class rdf:type owl:Class . }
            UNION
            {
                ?x rdf:type owl:Axiom .
                ?x owl:annotatedSource ?class .
                ?x owl:annotatedProperty rdf:type .
                ?x owl:annotatedTarget owl:Class .
                FILTER(isBlank(?x))
                FILTER(isIRI(?class))
            }
        }
        """
        for cls in self.world.sparql_query(query):
            if isinstance(cls[0], (And, Or, Not, Restriction, OneOf)):
                continue
            self.to_owl_class(cls[0])
            self.to_owl_class_declaration(cls[0])

        # parse class expressions for compatibility with OWL 1 DL
        query_nothing = """
        SELECT DISTINCT ?class
        WHERE {
            ?class rdf:type owl:Class .
            { ?class owl:unionOf ?list . }
            UNION
            { ?class owl:oneOf ?list . }
            ?list rdf:rest*/rdf:first ?member .
        }
        GROUP BY ?class
        HAVING (COUNT(?member) = 1)
        """
        for cls in self.world.sparql_query(query_nothing):
            curr_cls: typing.Union[Or, OneOf] = cls[0]
            if not isinstance(curr_cls, (Or, OneOf)):
                continue
            if isinstance(curr_cls, Or):
                if len(curr_cls.Classes) != 0:
                    continue
            elif isinstance(curr_cls, OneOf):
                if len(curr_cls.instances) != 0:
                    continue
            self.nothing_to_owl_class()
            self.nothing_to_owl_class_declaration()

        special_query = """
        SELECT DISTINCT ?x
        WHERE {
            ?x rdf:type owl:Class .
            { ?x owl:unionOf ?list . }
            UNION
            { ?x owl:intersectionOf ?list . }
            ?list rdf:rest*/rdf:first ?class .
        }
        GROUP BY ?x
        HAVING (COUNT(?class) = 1)
        """
        for cls in self.world.sparql_query(special_query):
            curr_cls: typing.Union[And, Or] = cls[0]
            if not isinstance(curr_cls, (And, Or)):
                continue
            if isinstance(curr_cls, And) and len(curr_cls.Classes) == 0:
                self.thing_to_owl_class()
                self.thing_to_owl_class_declaration()
                continue
            if len(curr_cls.Classes) != 1:  # only one class
                continue
            curr_cls = curr_cls.Classes[0]
            self.to_owl_class(curr_cls)
            self.to_owl_class_declaration(curr_cls)

        return list(v for k, v in self.declarations.items() if k in self.classes)

    def get_owl_object_properties(self) -> list[OWLObjectProperty]:
        """
        Get all object properties using SPARQL.

        Returns:
            List of object property URIs
        """
        query = """
        SELECT DISTINCT ?prop
        WHERE {
            { ?prop rdf:type owl:ObjectProperty . }
            UNION
            {
                ?x rdf:type owl:Axiom .
                ?x owl:annotatedSource ?prop .
                ?x owl:annotatedProperty rdf:type .
                ?x owl:annotatedTarget owl:ObjectProperty .
                FILTER(isBlank(?x))
                FILTER(isIRI(?prop))
            }
        }
        """
        for cls in self.world.sparql_query(query):
            if not isinstance(cls[0], ObjectPropertyClass):
                continue
            self.to_owl_object_property(cls[0])
            self.to_owl_object_property_declaration(cls[0])
        return list(
            v for k, v in self.declarations.items() if k in self.object_properties
        )

    def get_owl_datatype_properties(self) -> list[OWLDataProperty]:
        """
        Get all datatype properties using SPARQL.

        Returns:
            List of datatype property URIs
        """
        query = """
        SELECT DISTINCT ?prop
        WHERE {
            { ?prop rdf:type owl:DatatypeProperty . }
            UNION
            {
                ?x rdf:type owl:Axiom .
                ?x owl:annotatedSource ?prop .
                ?x owl:annotatedProperty rdf:type .
                ?x owl:annotatedTarget owl:DatatypeProperty .
                FILTER(isBlank(?x))
                FILTER(isIRI(?prop))
            }
        }
        """
        for cls in self.world.sparql_query(query):
            if not isinstance(cls[0], DataPropertyClass):
                continue
            self.to_owl_data_property(cls[0])
            self.to_owl_data_property_declaration(cls[0])
        return list(
            v for k, v in self.declarations.items() if k in self.data_properties
        )

    def get_owl_annotation_properties(self) -> list[OWLAnnotationProperty]:
        """
        Get all annotation properties using SPARQL.

        Returns:
            List of annotation property URIs
        """
        query = """
        SELECT DISTINCT ?prop
        WHERE {
            { ?prop rdf:type owl:AnnotationProperty . }
            UNION
            {
                ?x rdf:type owl:Axiom .
                ?x owl:annotatedSource ?prop .
                ?x owl:annotatedProperty rdf:type .
                ?x owl:annotatedTarget owl:AnnotationProperty .
                FILTER(isBlank(?x))
                FILTER(isIRI(?prop))
            }
        }
        """
        for cls in self.world.sparql_query(query):
            if not isinstance(cls[0], AnnotationPropertyClass):
                continue
            self.to_owl_annotation_property(cls[0])
            self.to_owl_annotation_property_declaration(cls[0])
        return list(
            v for k, v in self.declarations.items() if k in self.annotation_properties
        )

    def get_owl_annotation_property_domains(self) -> list[OWLAnnotationPropertyDomain]:
        """
        Get all annotation properties using SPARQL.

        Returns:
            List of annotation property URIs
        """
        query = """
        SELECT DISTINCT ?prop ?domain
        WHERE {
            ?prop rdf:type owl:AnnotationProperty .
            ?prop rdfs:domain ?domain .
        }
        """
        for cls in self.world.sparql_query(query):
            if not isinstance(cls[0], AnnotationPropertyClass):
                continue
            domain = self.graph.value(cls[0].storid, RDFS.domain)
            self.to_owl_annotation_property_domain(
                cls[0],
                domain,
                self.get_owl_axiom_annotations_for(
                    cls[0], get_abbreviation(RDFS.domain)
                ),
            )
        return list(self.annotation_property_domains.values())

    def get_owl_annotation_property_ranges(self) -> list[OWLAnnotationPropertyRange]:
        """
        Get all annotation properties using SPARQL.

        Returns:
            List of annotation property URIs
        """
        query = """
        SELECT DISTINCT ?prop ?range
        WHERE {
            ?prop rdf:type owl:AnnotationProperty .
            ?prop rdfs:range ?range .
        }
        """
        for cls in self.world.sparql_query(query):
            if not isinstance(cls[0], AnnotationPropertyClass):
                continue
            range = self.graph.value(cls[0].storid, RDFS.range)
            self.to_owl_annotation_property_range(
                cls[0],
                range,
                self.get_owl_axiom_annotations_for(
                    cls[0], get_abbreviation(RDFS.range)
                ),
            )
        return list(self.annotation_property_ranges.values())

    def get_owl_individuals(self) -> list[OWLIndividual]:
        """
        Get all individuals using SPARQL.

        Returns:
            List of individual URIs
        """
        query = """
        SELECT DISTINCT ?ind
        WHERE {
            { ?ind rdf:type owl:NamedIndividual . }
            UNION
            {
                ?x rdf:type owl:Axiom .
                ?x owl:annotatedSource ?ind .
                ?x owl:annotatedProperty rdf:type .
                ?x owl:annotatedTarget owl:NamedIndividual .
                FILTER(isBlank(?x))
            }
            UNION
            {
                ?ind rdf:type ?class .
                ?class rdf:type owl:Class .
            }
        }
        """
        for cls in self.world.sparql_query(query):
            if not is_named_individual(cls[0]):
                continue
            self.to_owl_individual(cls[0])
            self.to_owl_individual_declaration(cls[0])
            self.to_owl_class_assertion(cls[0], type(cls[0]))
        return list(v for k, v in self.declarations.items() if k in self.individuals)

    def get_owl_subclass_relationships(self) -> list[OWLSubClassOf]:
        """
        Get all subclass relationships.

        Returns:
            List of (subclass, superclass) tuples
        """
        query = """
        SELECT DISTINCT ?subclass ?superclass ?comment ?annotation
        WHERE {
            {
                ?subclass rdfs:subClassOf ?superclass .
            }
            UNION
            {
                ?b rdf:type owl:Axiom .
                ?b owl:annotatedSource ?subclass .
                ?b owl:annotatedProperty rdfs:subClassOf .
                ?b owl:annotatedTarget ?superclass .
                ?b ?comment ?annotation .
                ?comment rdf:type owl:AnnotationProperty
                FILTER(isBlank(?b))
            }
            FILTER(?subclass != ?superclass)
        }
        """
        for cls in self.world.sparql_query(query):
            sub_class: ThingClass = cls[0]
            super_class: ThingClass = cls[1]
            # if not isinstance(sub_class, ThingClass) or not isinstance(
            #     super_class, ThingClass
            # ):
            #     continue
            if cls[2] is not None:
                cls[2] = self._to_annotation_property(cls[2])
                cls[3] = OWLAnnotation(
                    self.annotation_properties[cls[2]], OWLLiteral(Literal(cls[1]))
                )
            self.to_owl_subclass_of(sub_class, super_class, cls[3])
        return list(self.subclasses_of.values())

    def _get_owl_chain(
        self,
        marked: dict[ThingClass, bool],
        chain: dict[ThingClass, ThingClass],
        annotations: dict[EntityClass, set[OWLAnnotation]],
    ) -> typing.Generator[
        tuple[tuple[ThingClass], typing.Optional[list[OWLAnnotation]]], None, None
    ]:
        keys: tuple = iter(marked.keys())
        while not all(marked.values()):
            chain_annotations: set[OWLAnnotation] = set()
            full_chain: set[ThingClass] = set()
            k = next(keys)
            if marked[k]:
                continue
            while k is not None and k not in full_chain:
                full_chain.add(k)
                marked[k] = True
                if k in annotations:
                    chain_annotations.update(annotations[k])
                k = chain.get(k)
            yield tuple(filter(bool, full_chain)), (
                list(chain_annotations) if len(chain_annotations) > 0 else None
            )

    def get_owl_equivalent_classes(self) -> list[OWLEquivalentClasses]:
        """
        Get all equivalent class relationships.

        Returns:
            List of (class1, class2) tuples
        """
        # ?class1 rdf:type owl:Class .
        # ?class2 rdf:type owl:Class .
        query = """
        SELECT DISTINCT ?class1 ?class2
        WHERE {
            ?class1 owl:equivalentClass ?class2 .
            ?class1 rdf:type owl:Class .
            FILTER(?class1 != ?class2)
        }
        """
        # _ = self.get_owl_classes()
        annotations: dict[ThingClass, set[OWLAnnotation]] = dict()
        marked: dict[ThingClass, bool] = dict()
        equivalence_chain: dict[ThingClass, ThingClass] = dict()
        for cls in self.world.sparql_query(query):
            if not isinstance(cls[0], ThingClass):
                continue
            # if not isinstance(cls[1], ThingClass):
            #     continue
            class1: ThingClass = cls[0]
            class2: ThingClass = cls[1]
            equivalence_chain[class1] = class2
            marked[class1] = False
            marked[class2] = False
            curr_annotations = self.get_owl_axiom_annotations_for(
                class1, get_abbreviation(OWL.equivalentClass), class2
            )
            if curr_annotations:
                annotations[class1] = annotations.get(class1, set()) | set(
                    curr_annotations
                )

        for chain, annotations in self._get_owl_chain(
            marked, equivalence_chain, annotations
        ):
            if len(chain) < 2:
                continue
            if chain in self.equivalent_classes:
                continue
            # if any(not isinstance(c, ThingClass) for c in chain):
            #     continue
            self.to_owl_equivalent_classes(chain, annotations)

        # Parsing of Axioms for Compatibility with OWL 1 DL
        querys = [
            """
            SELECT DISTINCT ?class1 ?class2
            WHERE {
                ?class1 owl:complementOf ?class2 .
                ?class1 rdf:type owl:Class .
                ?class2 rdf:type owl:Class .
                FILTER(?class1 != ?class2)
            }
            """,
            """
            SELECT DISTINCT ?class1 ?list
            WHERE {
                ?class1 owl:unionOf ?list .
                ?class1 rdf:type owl:Class .
                ?list rdf:rest*/rdf:first ?class2 .
            }
            """,
            """
            SELECT DISTINCT ?class1 ?list
            WHERE {
                ?class1 owl:intersectionOf ?list .
                ?class1 rdf:type owl:Class .
                ?list rdf:rest*/rdf:first ?class2 .
            }
            """,
            """
            SELECT DISTINCT ?class1 ?list
            WHERE {
                ?class1 owl:oneOf ?list .
                ?class1 rdf:type owl:Class .
                ?list rdf:rest*/rdf:first ?class2 .
            }
            """,
        ]
        for i, query in enumerate(querys):
            for cls in self.world.sparql_query(query):
                if i == 0:
                    self.to_owl_equivalent_classes([cls[0], cls[1]])
                elif i == 1:
                    curr_cls: ThingClass = cls[0]
                    union: Or = cls[1]
                    if not isinstance(curr_cls, ThingClass):
                        continue
                    if not isinstance(union, Or):
                        continue
                    if len(union.Classes) == 0:
                        self.to_owl_equivalent_classes(
                            [curr_cls, OWLClass(IRI(self.namespace, OWL.Nothing))]
                        )
                    elif len(union.Classes) == 1:
                        self.to_owl_equivalent_classes([curr_cls, union.Classes[0]])
                    elif len(union.Classes) > 1:
                        classes = cls
                        if classes not in self.equivalent_classes:
                            self.equivalent_classes[classes] = OWLEquivalentClasses(
                                [
                                    self.get_owl_class_expression(curr_cls),
                                    self.to_owl_object_union_of(union.Classes),
                                ]
                            )
                elif i == 2:
                    curr_cls: ThingClass = cls[0]
                    intersection: And = cls[1]
                    if not isinstance(curr_cls, ThingClass):
                        continue
                    if not isinstance(intersection, And):
                        continue
                    if len(intersection.Classes) == 0:
                        self.to_owl_equivalent_classes(
                            [curr_cls, OWLClass(IRI(Namespace(OWL._NS), OWL.Thing))]
                        )
                    elif len(intersection.Classes) == 1:
                        self.to_owl_equivalent_classes(
                            [curr_cls, intersection.Classes[0]]
                        )
                    elif len(intersection.Classes) > 1:
                        classes = cls
                        if classes not in self.equivalent_classes:
                            self.equivalent_classes[classes] = OWLEquivalentClasses(
                                [
                                    self.get_owl_class_expression(curr_cls),
                                    self.to_owl_object_intersection_of(
                                        intersection.Classes
                                    ),
                                ]
                            )
                elif i == 3:
                    curr_cls: ThingClass = cls[0]
                    one_of: OneOf = cls[1]
                    if not isinstance(curr_cls, ThingClass):
                        continue
                    if not isinstance(one_of, OneOf):
                        continue
                    if len(one_of.instances) == 0:
                        self.to_owl_equivalent_classes(
                            [curr_cls, OWLClass(IRI(Namespace(OWL._NS), OWL.Nothing))]
                        )
                    elif len(one_of.instances) > 1:
                        classes = cls
                        if classes not in self.equivalent_classes:
                            self.equivalent_classes[classes] = OWLEquivalentClasses(
                                [
                                    self.get_owl_class_expression(curr_cls),
                                    self.to_owl_object_one_of(one_of.instances),
                                ]
                            )

        return list(self.equivalent_classes.values())

    def get_owl_disjoint_classes(self) -> list[OWLDisjointClasses]:
        """
        Get all disjoint class relationships.

        Returns:
            List of (class1, class2) tuples
        """
        # ?class1 rdf:type owl:Class .
        # ?class2 rdf:type owl:Class .
        # Direct disjoint statements
        query1 = """
        SELECT DISTINCT ?class1 ?class2
        WHERE {
            ?class1 owl:disjointWith ?class2 .
            FILTER(?class1 != ?class2)
        }
        """

        # Disjoint classes through owl:AllDisjointClasses
        query2 = """
        SELECT DISTINCT ?x
        WHERE {
            ?x rdf:type owl:AllDisjointClasses .
            ?x owl:members ?list .
            ?list rdf:rest*/rdf:first ?class .
        }
        GROUP BY ?x
        HAVING (COUNT(?class) >= 2)
        """

        for cls in self.world.sparql_query(query1):
            self.to_owl_disjoint_classes(tuple(cls))

        for cls in self.world.sparql_query(query2):
            self.to_owl_disjoint_classes(cls[0])
        return list(self.disjoint_classes.values())

    def get_owl_data_union_of(self) -> list[OWLDataUnionOf]:
        """
        Get all class unions (owl:unionOf).

        Returns:
            List of (union_class, [component_classes]) tuples
        """
        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type rdfs:Datatype .
            ?blank owl:unionOf ?union .
            ?union rdf:rest*/rdf:first ?member .
            FILTER(isBlank(?blank))
        }
        GROUP BY ?blank
        HAVING(COUNT(?member) >= 2)
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_data_union_of(cls[0])
        return list(self.data_unions_of.values())

    def get_owl_object_union_of(self) -> list[OWLObjectUnionOf]:
        """
        Get all object unions of (owl:unionOf).

        Returns:
            List of (union_class, [component_classes]) tuples
        """
        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Class .
            ?blank owl:unionOf ?union .
            ?union rdf:rest*/rdf:first ?member .
            FILTER(isBlank(?blank))
        }
        GROUP BY ?blank
        HAVING(COUNT(?member) >= 2)
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_object_union_of(cls[0])
        return list(self.object_unions_of.values())

    def get_owl_disjoint_unions(self) -> list[OWLDisjointUnion]:
        """
        Get all disjoint unions (owl:disjointUnionOf).

        Returns:
            List of (union_class, [component_classes]) tuples
        """
        # query = """
        # SELECT DISTINCT ?class ?class1 ?class2
        # WHERE {
        #     ?class owl:disjointUnionOf ?list .
        #     ?list rdf:rest*/rdf:first ?class1 .
        #     ?list rdf:rest*/rdf:first ?class2 .
        #     ?class rdf:type owl:Class .
        #     ?class1 rdf:type owl:Class .
        #     ?class2 rdf:type owl:Class .
        #     FILTER(!isBlank(?class1))
        #     FILTER(!isBlank(?class2))
        #     FILTER(?class1 != ?class2)
        # }
        # """
        query: str = """
        SELECT DISTINCT ?class ?member
        WHERE {
            ?class owl:disjointUnionOf ?list .
            ?list rdf:rest*/rdf:first ?member .
            FILTER(?class != ?member)
        }
        """
        mapping: dict[ThingClass, set[ThingClass]] = dict()
        for cls in self.world.sparql_query(query):
            curr_cls: ThingClass = cls[0]
            cls: ThingClass = cls[1]
            assert isinstance(curr_cls, ThingClass)
            assert isinstance(cls, ThingClass)
            if curr_cls in self.disjoint_unions:
                continue
            mapping[curr_cls] = mapping.get(curr_cls, set()) | set([cls])

        # mapping: dict[ThingClass, set[ThingClass]] = dict()
        # for cls in self.world.sparql_query(query):
        #     curr_cls: ThingClass = cls[0]
        #     classes: list[ThingClass] = cls[1:]
        #     assert isinstance(curr_cls, ThingClass)
        #     assert all(isinstance(c, ThingClass) for c in classes)
        #     if curr_cls in self.disjoint_unions:
        #         continue
        #     mapping[curr_cls] = mapping.get(curr_cls, set()) | set(classes)

        for curr_cls, classes in mapping.items():
            if curr_cls in self.disjoint_unions:
                continue
            self.to_owl_disjoint_union(curr_cls, tuple(classes))
        return list(self.disjoint_unions.values())

    def get_owl_data_intersection_of(
        self,
    ) -> list[OWLDataIntersectionOf]:
        """
        Get all class intersections (owl:intersectionOf).

        Returns:
            List of (intersection_class, [component_classes]) tuples
        """
        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type rdfs:Datatype .
            ?blank owl:intersectionOf ?list .
            ?list rdf:rest*/rdf:first ?member .
            FILTER(isBlank(?blank))
        }
        GROUP BY ?blank
        HAVING(COUNT(?member) >= 2)
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_data_intersection_of(cls[0])
        return list(self.data_intersections_of.values())

    def get_owl_object_intersection_of(
        self,
    ) -> list[OWLObjectIntersectionOf]:
        """
        Get all class intersections (owl:intersectionOf).

        Returns:
            List of (intersection_class, [component_classes]) tuples
        """
        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Class .
            ?blank owl:intersectionOf ?list .
            ?list rdf:rest*/rdf:first ?member .
            FILTER(isBlank(?blank))
        }
        GROUP BY ?blank
        HAVING(COUNT(?member) >= 2)
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_object_intersection_of(cls[0])
        return list(self.object_intersections_of.values())

    def get_owl_data_complement_of(self) -> list[OWLDataComplementOf]:
        """
        Get all datatype complements (owl:datatypeComplementOf).

        Returns:
            List of (complement_class, complemented_class) tuples
        """
        # owl:datatypeComplementOf are not handled by owlready2
        query = """
        SELECT DISTINCT ?class1 ?class2
        WHERE {
            {
                ?class1 rdf:type rdfs:Datatype .
                ?class1 owl:datatypeComplementOf ?class2 .
            }
            UNION
            {
                ?class1 rdf:type owl:DataRange .
                ?class1 owl:oneOf ?list .
                ?list rdf:rest*/rdf:first ?class2 .
            }
            FILTER(isBlank(?class1))
            FILTER(?class1 != ?class2)
        }
        """
        print("Warning: OWLDataComplementOf is not handled")
        for cls in self.graph.query(query):
            data_range = self.ontology.search_one(iri=cls[1])
            if data_range is None:
                continue
            self.to_owl_data_complement_of(Not(data_range), data_range)

        return list(self.data_complements_of.values())

    def get_owl_object_complement_of(self) -> list[OWLObjectComplementOf]:
        """
        Get all class complements (owl:complementOf).

        Returns:
            List of (complement_class, complemented_class) tuples
        """
        query = """
        SELECT DISTINCT ?class1 ?class2
        WHERE {
            ?class1 rdf:type owl:Class .
            ?class1 owl:complementOf ?class2 .
            FILTER(!isBlank(?class2))
            FILTER(?class1 != ?class2)
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_object_complement_of(cls[0], cls[1])

        return list(self.object_complements_of.values())

    def get_owl_data_one_of(self) -> list[OWLDataOneOf]:
        """
        Get all enumerated classes (owl:oneOf).

        Returns:
            List of (enum_class, [individuals]) tuples
        """
        query = """
        SELECT DISTINCT ?class1
        WHERE {
            {?class1 rdf:type rdfs:Datatype .}
            UNION
            {?class1 rdf:type owl:DataRange .}
            ?class1 owl:oneOf ?class2 .
            ?class2 rdf:rest*/rdf:first ?member .
            FILTER(isLiteral(?member))
        }
        GROUP BY ?class1
        HAVING(COUNT(?member) >= 1)
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_data_one_of(cls[0])

        return list(self.data_ones_of.values())

    def get_owl_object_one_of(self) -> list[OWLObjectOneOf]:
        """
        Get all enumerated classes (owl:oneOf).

        Returns:
            List of (enum_class, [individuals]) tuples
        """

        query = """
        SELECT DISTINCT ?class1
        WHERE {
            ?class1 rdf:type owl:Class .
            ?class1 owl:oneOf ?class2 .
            ?class2 rdf:rest*/rdf:first ?member .
        }
        GROUP BY ?class1
        HAVING(COUNT(?member) >= 1)
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_object_one_of(cls[0])

        return list(self.object_ones_of.values())

    def get_owl_datatype_restrictions(self) -> list[OWLDatatypeRestriction]:
        """
        Get all datatype restrictions (owl:withRestrictions).

        Returns:
            List of OWLDatatypeRestriction
        """
        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type rdfs:Datatype .
            ?blank owl:onDatatype ?datatype .
            ?blank owl:withRestrictions ?list .
            ?list rdf:rest*/rdf:first ?class .
            ?class ?facet ?literal .
            FILTER(isBlank(?blank))

            { ?datatype rdf:type rdfs:Datatype . }
            UNION
            { FILTER(isIRI(?datatype)) }
        }
        GROUP BY ?blank
        HAVING(COUNT(?class) >= 1)
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_datatype_restriction(cls[0])
        return list(self.datatype_restrictions.values())

    def get_owl_object_some_values_from(self) -> list[OWLObjectSomeValuesFrom]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            ?blank owl:onProperty ?property .
            ?blank owl:someValuesFrom ?from .
            FILTER(isBlank(?blank))
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_object_some_values_from(cls[0])
        return list(self.objects_some_values_from.values())

    def get_owl_object_all_values_from(self) -> list[OWLObjectAllValuesFrom]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            ?blank owl:onProperty ?property .
            ?blank owl:allValuesFrom ?from .
            FILTER(isBlank(?blank))
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_object_all_values_from(cls[0])
        return list(self.objects_all_values_from.values())

    def get_owl_object_has_value(self) -> list[OWLObjectHasValue]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            ?blank owl:onProperty ?property .
            ?blank owl:hasValue ?from .
            FILTER(isBlank(?blank))
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_object_has_value(cls[0])
        return list(self.objects_has_value.values())

    def get_owl_object_has_self(self) -> list[OWLObjectHasSelf]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            ?blank owl:onProperty ?property .
            ?blank owl:hasSelf ?from .
            FILTER(?from = "true"^^xsd:boolean)
            FILTER(isBlank(?blank))
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_object_has_self(cls[0])
        return list(self.objects_has_self.values())

    def get_owl_object_min_cardinality(self) -> list[OWLObjectMinCardinality]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            ?blank owl:onProperty ?property .
            {
                ?blank owl:minCardinality ?cardinality .
            }
            UNION
            {
                ?blank owl:minQualifiedCardinality ?cardinality .
                ?blank owl:onClass ?class .
            }
            FILTER(isBlank(?blank))
            FILTER(isNumeric(?cardinality))
            FILTER(datatype(?cardinality) = xsd:nonNegativeInteger)
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_object_min_cardinality(cls[0])
        return list(self.objects_min_cardinality.values())

    def get_owl_object_max_cardinality(self) -> list[OWLObjectMaxCardinality]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            ?blank owl:onProperty ?property .
            {
                ?blank owl:maxCardinality ?cardinality .
            }
            UNION
            {
                ?blank owl:maxQualifiedCardinality ?cardinality .
                ?blank owl:onClass ?class .
            }
            FILTER(isBlank(?blank))
            FILTER(isNumeric(?cardinality))
            FILTER(datatype(?cardinality) = xsd:nonNegativeInteger)
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_object_max_cardinality(cls[0])
        return list(self.objects_max_cardinality.values())

    def get_owl_object_exact_cardinality(self) -> list[OWLObjectExactCardinality]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            ?blank owl:onProperty ?property .
            {
                ?blank owl:cardinality ?cardinality .
            }
            UNION
            {
                ?blank owl:qualifiedCardinality ?cardinality .
                ?blank owl:onClass ?class .
            }
            FILTER(isBlank(?blank))
            FILTER(isNumeric(?cardinality))
            FILTER(datatype(?cardinality) = xsd:nonNegativeInteger)
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_object_exact_cardinality(cls[0])
        return list(self.objects_exact_cardinality.values())

    def get_owl_data_some_values_from(self) -> list[OWLDataSomeValuesFrom]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            {
                ?blank owl:onProperty ?property .
            }
            UNION
            {
                ?blank owl:onProperties ?properties .
                ?properties rdf:rest*/rdf:first ?property .
            }
            ?blank owl:someValuesFrom ?data_range .
            FILTER(isBlank(?blank))
        }
        GROUP BY ?blank
        HAVING(COUNT(?property) >= 1)
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_data_some_values_from(cls[0])
        return list(self.data_some_values_from.values())

    def get_owl_data_all_values_from(self) -> list[OWLDataAllValuesFrom]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            {
                ?blank owl:onProperty ?property .
            }
            UNION
            {
                ?blank owl:onProperties ?properties .
                ?properties rdf:rest*/rdf:first ?property .
            }
            ?blank owl:allValuesFrom ?data_range .
            FILTER(isBlank(?blank))
        }
        GROUP BY ?blank
        HAVING(COUNT(?property) >= 1)
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_data_all_values_from(cls[0])
        return list(self.data_all_values_from.values())

    def get_owl_data_has_value(self) -> list[OWLDataHasValue]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            ?blank owl:onProperty ?property .
            ?blank owl:hasValue ?literal .
            FILTER(isBlank(?blank))
            FILTER(isLiteral(?literal))
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_data_has_value(cls[0])
        return list(self.data_has_value.values())

    def get_owl_data_min_cardinality(self) -> list[OWLDataMinCardinality]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            ?blank owl:onProperty ?property .
            {
                ?blank owl:minCardinality ?cardinality .
            }
            UNION
            {
                ?blank owl:minQualifiedCardinality ?cardinality .
                ?blank owl:onDataRange ?data_range .
            }
            FILTER(isBlank(?blank))
            FILTER(isNumeric(?cardinality))
            FILTER(datatype(?cardinality) = xsd:nonNegativeInteger)
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_data_min_cardinality(cls[0])
        return list(self.data_min_cardinality.values())

    def get_owl_data_max_cardinality(self) -> list[OWLDataMaxCardinality]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            ?blank rdf:type owl:Restriction .
            ?blank owl:onProperty ?property .
            {
                ?blank owl:maxCardinality ?cardinality .
            }
            UNION
            {
                ?blank owl:maxQualifiedCardinality ?cardinality .
                ?blank owl:onDataRange ?data_range .
            }
            FILTER(isBlank(?blank))
            FILTER(isNumeric(?cardinality))
            FILTER(datatype(?cardinality) = xsd:nonNegativeInteger)
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_data_max_cardinality(cls[0])
        return list(self.data_max_cardinality.values())

    def get_owl_data_exact_cardinality(self) -> list[OWLDataExactCardinality]:
        """
        Get all property restrictions.

        Returns:
            List of restriction dictionaries with details
        """

        query = """
        SELECT DISTINCT ?blank
        WHERE {
            {
                ?blank rdf:type owl:Restriction .
                ?blank owl:onProperty ?property .
                ?blank owl:cardinality ?cardinality .
            }
            UNION
            {
                ?blank rdf:type owl:Restriction .
                ?blank owl:onProperty ?property .
                ?blank owl:qualifiedCardinality ?cardinality .
                ?blank owl:onDataRange ?data_range .
            }
            FILTER(isBlank(?blank))
            FILTER(isNumeric(?cardinality))
            FILTER(datatype(?cardinality) = xsd:nonNegativeInteger)
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_data_exact_cardinality(cls[0])
        return list(self.data_exact_cardinality.values())

    def get_owl_inverse_object_properties(self) -> list[OWLInverseObjectProperties]:
        """
        Get all inverse property pairs.

        Returns:
            List of (property1, property2) tuples
        """
        query = """
        SELECT DISTINCT ?prop1 ?prop2
        WHERE {
            ?prop1 owl:inverseOf ?prop2 .
            FILTER(?prop1 != ?prop2)
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_inverse_object_properties(cls[0], cls[1])
        return list(self.inverse_object_properties.values())

    def get_owl_has_keys(self) -> list[OWLHasKey]:
        """
        Get all key property sets (owl:hasKey).

        Returns:
            List of (class, [key_properties]) tuples
        """
        query = """
        SELECT DISTINCT ?class ?x1
        WHERE {
            ?class owl:hasKey ?list .
            ?list rdf:rest*/rdf:first ?x1 .
            { ?x1 rdf:type owl:ObjectProperty . }
            UNION
            { ?x1 rdf:type owl:DatatypeProperty . }
        }
        """
        has_keys: dict[
            ThingClass,
            dict[str, set[typing.Union[ObjectPropertyClass, DataPropertyClass]]],
        ] = dict()
        for cls in self.world.sparql_query(query):
            if cls[0] in self.has_keys:
                continue
            if cls[0] not in has_keys:
                has_keys[cls[0]] = {"obj": set(), "data": set()}
            if isinstance(cls[1], ObjectPropertyClass):
                has_keys[cls[0]]["obj"].add(cls[1])
            if isinstance(cls[1], DataPropertyClass):
                has_keys[cls[0]]["data"].add(cls[1])

        for key in has_keys:
            self.get_owl_has_key(
                key, tuple(has_keys[key]["obj"]), tuple(has_keys[key]["data"])
            )
        return list(self.has_keys.values())

    def get_owl_datatypes(self) -> list[OWLDatatype]:
        """
        Get all defined datatypes.

        Returns:
            List of datatype URIs
        """
        # owl:datatypeComplementOf are not handled by owlready2
        query = """
        SELECT DISTINCT ?datatype
        WHERE {
            {
                ?datatype rdf:type rdfs:Datatype .
            }
            UNION
            {
                ?x rdf:type owl:Axiom .
                ?x owl:annotatedSource ?datatype .
                ?x owl:annotatedProperty rdf:type .
                ?x owl:annotatedTarget rdfs:Datatype .
                FILTER(isBlank(?x))
                FILTER(isIRI(?datatype))
            }
            FILTER NOT EXISTS { ?datatype owl:datatypeComplementOf ?dt }
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_datatype(cls[0])
            self.to_owl_datatype_declaration(cls[0])
        return list([v for k, v in self.declarations.items() if k in self.datatypes])

    def _get_owl_negative_property_assertion_annotations(
        self, property_type: type, params: tuple[EntityClass, ...]
    ) -> list[OWLAnnotation]:
        target_owl_str: str = (
            "\t?assertion owl:targetIndividual ?? .\n"
            if property_type == OWLNegativeObjectPropertyAssertion
            else "\t?assertion owl:targetValue ?? .\n"
        )
        target_owl_type: str = (
            "\t?target rdf:type owl:NamedIndividual .\n"
            if property_type == OWLNegativeObjectPropertyAssertion
            else ""
        )
        query_annotation: str = (
            "SELECT DISTINCT ?comment ?literal\n"
            "WHERE {\n"
            "\t?assertion rdf:type owl:NegativePropertyAssertion .\n"
            "\t?assertion owl:sourceIndividual ?? .\n"
            "\t?assertion owl:assertionProperty ?? .\n"
            f"{target_owl_str}"
            "\t?assertion ?comment ?literal .\n"
            "\t?source rdf:type owl:NamedIndividual .\n"
            f"{target_owl_type}"
            "\t?comment rdf:type owl:AnnotationProperty .\n"
            "\tFILTER(isBlank(?assertion))\n"
            "\tFILTER(isLiteral(?literal))\n"
            "\tFILTER(isIRI(?comment))\n"
            "}"
        )
        annotations: set[OWLAnnotation] = set()
        for ann in self.world.sparql(query_annotation, params):
            label, literal = ann
            if label not in self.annotation_properties:
                if type(label) == int:
                    if label not in RDFXMLGetter.STANDARD_ANNOTATIONS:
                        continue
                    self.annotation_properties[label] = OWLAnnotationProperty(
                        RDFXMLGetter.STANDARD_ANNOTATIONS[label].iri
                    )
                elif isinstance(label, AnnotationPropertyClass):
                    self.annotation_properties[label] = OWLAnnotationProperty(label.iri)
                else:
                    raise TypeError
            annotations.add(
                OWLAnnotation(
                    self.annotation_properties[label], OWLLiteral(Literal(literal))
                )
            )
        return list(annotations)

    def get_owl_negative_object_property_assertions(
        self,
    ) -> list[OWLNegativeObjectPropertyAssertion]:
        """
        Get all negative property assertions.

        Returns:
            List of dictionaries with assertion details
        """
        # Object property negative assertions
        query_object = """
        SELECT DISTINCT ?source ?property ?target
        WHERE {
            ?assertion rdf:type owl:NegativePropertyAssertion .
            ?assertion owl:sourceIndividual ?source .
            ?assertion owl:assertionProperty ?property .
            ?assertion owl:targetIndividual ?target .
            ?source rdf:type owl:NamedIndividual .
            ?property rdf:type owl:ObjectProperty .
            ?target rdf:type owl:NamedIndividual .
            FILTER(isBlank(?assertion))
        }
        """
        for cls in self.world.sparql_query(query_object):
            self.to_owl_negative_object_property_assertion(cls[0], cls[1], cls[2])
        return list(self.negative_object_property_assertions.values())

    def get_owl_negative_data_property_assertions(
        self,
    ) -> list[OWLNegativeDataPropertyAssertion]:
        """
        Get all negative property assertions.

        Returns:
            List of dictionaries with assertion details
        """
        # Data property negative assertions
        query_data = """
        SELECT ?source ?property ?target
        WHERE {
            ?assertion rdf:type owl:NegativePropertyAssertion .
            ?assertion owl:sourceIndividual ?source .
            ?assertion owl:assertionProperty ?property .
            ?assertion owl:targetValue ?target .
            ?property rdf:type owl:DatatypeProperty .
            ?source rdf:type owl:NamedIndividual .
            FILTER(isBlank(?assertion))
            FILTER(isLiteral(?target))
        }
        """
        for cls in self.world.sparql_query(query_data):
            if not isinstance(cls[2], Literal):
                cls[2] = Literal(cls[2])
            self.to_owl_negative_data_property_assertion(cls[0], cls[1], cls[2])
        return list(self.negative_data_property_assertions.values())

    def get_owl_class_assertions(self) -> list[OWLClassAssertion]:
        """
        Get all class assertions (individual type declarations).

        Returns:
            List of (individual, class) tuples
        """
        query = """
        SELECT DISTINCT ?individual ?class
        WHERE {
            ?individual rdf:type ?class .
            ?individual rdf:type owl:NamedIndividual .
            FILTER(?class != owl:NamedIndividual)
        }
        """

        for cls in self.world.sparql_query(query):
            self.to_owl_class_assertion(cls[0], cls[1])
        return list(self.class_assertions.values())

    def get_owl_object_property_assertions(
        self,
    ) -> list[OWLObjectPropertyAssertion]:
        """
        Get all property assertions.

        Returns:
            List of property assertions.
        """
        query = """
        SELECT DISTINCT ?individual1 ?property ?individual2
        WHERE {
            ?individual1 ?property ?individual2 .
            ?individual1 rdf:type owl:NamedIndividual .
            ?individual2 rdf:type owl:NamedIndividual .
        }
        """
        # _ = self.get_owl_individuals()
        # _ = self.get_owl_object_properties()
        for cls in self.world.sparql_query(query):
            self.to_owl_object_property_assertion(cls[0], cls[1], cls[2])
        return list(self.object_property_assertions.values())

    def get_owl_data_property_assertions(
        self,
    ) -> list[OWLDataPropertyAssertion]:
        """
        Get all property assertions.

        Returns:
            List of property assertions.
        """
        query = """
        SELECT DISTINCT ?individual ?property ?literal
        WHERE {
            ?individual ?property ?literal .
            ?individual rdf:type owl:NamedIndividual .
            ?property rdf:type owl:DatatypeProperty .
            FILTER(isLiteral(?literal))
        }
        """
        for cls in self.world.sparql_query(query):
            if not isinstance(cls[2], Literal):
                cls[2] = Literal(cls[2])
            self.to_owl_data_property_assertion(cls[0], cls[1], cls[2])
        return list(self.data_property_assertions.values())

    def get_owl_same_individuals(self) -> list[OWLSameIndividual]:
        """
        Get all sameAs assertions between individuals.

        Returns:
            List of (individual1, individual2) tuples
        """
        query = """
        SELECT DISTINCT ?ind1 ?ind2
        WHERE {
            ?ind1 owl:sameAs ?ind2 .
            ?ind1 rdf:type owl:NamedIndividual .
            ?ind2 rdf:type owl:NamedIndividual .
            FILTER(?ind1 != ?ind2)
        }
        """
        # _ = self.get_owl_individuals()
        annotations: dict[ThingClass, set[OWLAnnotation]] = dict()
        marked: dict[ThingClass, bool] = dict()
        equivalence_chain: dict[ThingClass, ThingClass] = dict()
        for cls in self.world.sparql_query(query):
            equivalence_chain[cls[0]] = cls[1]
            marked[cls[0]] = False
            marked[cls[1]] = False
            curr_annotations = self.get_owl_axiom_annotations_for(
                cls[0], get_abbreviation(OWL.sameAs), cls[1]
            )
            if curr_annotations:
                annotations[cls[0]] = annotations.get(cls[0], set()) | set(
                    curr_annotations
                )

        for chain, annotations in self._get_owl_chain(
            marked, equivalence_chain, annotations
        ):
            self.to_owl_same_individual(tuple(chain), annotations)
        return list(self.same_individuals.values())

    def get_owl_different_individuals(self) -> list[OWLDifferentIndividuals]:
        """
        Get all differentFrom assertions between individuals.

        Returns:
            List of (individual1, individual2) tuples
        """
        # Direct differentFrom statements
        query1 = """
        SELECT DISTINCT ?ind1 ?ind2
        WHERE {
            ?ind1 owl:differentFrom ?ind2 .
            ?ind1 rdf:type owl:NamedIndividual .
            ?ind2 rdf:type owl:NamedIndividual .
            FILTER(?ind1 != ?ind2)
        }
        """

        # AllDifferent statements
        query2 = """
        SELECT DISTINCT ?x ?ind
        WHERE {
            ?x rdf:type owl:AllDifferent .
            ?x (owl:members|owl:distinctMembers) ?list .
            ?list rdf:rest*/rdf:first ?ind .
            ?ind rdf:type owl:NamedIndividual .
            FILTER(isBlank(?x))
        }
        GROUP BY ?x
        HAVING(COUNT(?ind) >= 2)
        """

        for cls in self.world.sparql_query(query1):
            self.to_owl_different_individuals(cls)

        for cls in self.world.sparql_query(query2):
            self.to_owl_different_individuals(cls[0])

        return list(self.different_individuals.values())

    def get_owl_annotations(self) -> list[OWLAnnotation]:
        """
        Get all annotations for resources.

        Returns:
            Dictionary mapping resource URIs to lists of (property, value) tuples
        """
        _ = self.get_owl_individuals()
        _ = self.get_owl_annotation_properties()
        annotation_props = set(
            [
                (
                    URIRef(a.iri)
                    if hasattr(a, "iri")
                    else (a if isinstance(a, URIRef) else a)
                )
                for a in self.annotation_properties
            ]
        )

        # Add standard annotation properties if not already in the set
        standard_props = set(
            [
                RDFS.label,
                RDFS.comment,
                OWL.versionInfo,
                OWL.Annotation,
                URIRef("http://www.w3.org/2004/02/skos/core#prefLabel"),
                URIRef("http://www.w3.org/2004/02/skos/core#altLabel"),
                URIRef("http://purl.org/dc/elements/1.1/title"),
                URIRef("http://purl.org/dc/elements/1.1/description"),
                URIRef("http://purl.org/dc/terms/title"),
                URIRef("http://purl.org/dc/terms/description"),
            ]
        )

        for s, p, o in self.graph.triples((None, None, None)):
            if isinstance(s, URIRef) and p in standard_props | annotation_props:
                if s in self.annotations:
                    continue
                if p in standard_props:
                    self.annotation_properties[p] = OWLAnnotationProperty(
                        IRI(self.namespace, p)
                    )
                else:
                    p = [
                        a
                        for a in self.annotation_properties
                        if (
                            URIRef(a.iri) == p
                            if isinstance(a, AnnotationPropertyClass)
                            else a == p
                        )
                    ][0]

                if o in self.individuals:
                    o = self.individuals[o]
                elif isinstance(o, Literal):
                    o = OWLLiteral(o)
                else:
                    o = IRI(self.namespace, o)

                self.annotations[(s, p, o)] = OWLAnnotation(
                    self.annotation_properties[p],
                    o,
                )
        return list(self.annotations.values())

    def get_owl_sub_object_property_chain(self) -> list[OWLSubObjectPropertyOf]:
        """
        Get all subproperty relationships.

        Returns:
            List of (subproperty, superproperty) tuples
        """
        query = """
        SELECT DISTINCT ?subprop ?prop1 ?prop2
        WHERE {
            ?subprop owl:propertyChainAxiom ?list .
            ?list rdf:rest*/rdf:first ?prop1 .
            ?list rdf:rest*/rdf:first ?prop2 .
            FILTER(?prop1 != ?prop2)
        }
        """
        mapping: dict[ThingClass, set[ThingClass]] = dict()
        for cls in self.world.sparql_query(query):
            mapping[cls[0]] = mapping.get(cls[0], set()) | set(cls[1:])

        for curr_cls, classes in mapping.items():
            self.to_owl_sub_object_property_of(
                OWLObjectPropertyChain(
                    [self.to_owl_object_property(c) for c in classes]
                ),
                curr_cls,
            )
        return list(self.subobject_properties_of.values())

    def get_owl_sub_object_property_of(
        self,
    ) -> list[OWLSubObjectPropertyOf]:
        """
        Get all sub object property.

        Returns:
            List of OWLSubObjectPropertyOf
        """
        query = """
        SELECT DISTINCT ?subprop ?superprop
        WHERE {
            ?subprop rdfs:subPropertyOf ?superprop .
            ?superprop rdf:type owl:ObjectProperty .
            ?subprop rdf:type owl:ObjectProperty .
            FILTER(?subprop != ?superprop)
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_sub_object_property_of(cls[0], cls[1])
        self.get_owl_sub_object_property_chain()
        return list(self.subobject_properties_of.values())

    def get_owl_sub_data_property_of(
        self,
    ) -> list[OWLSubDataPropertyOf]:
        """
        Get all sub data property.

        Returns:
            List of OWLSubDataPropertyOf
        """
        query = """
        SELECT DISTINCT ?subprop ?superprop
        WHERE {
            ?subprop rdfs:subPropertyOf ?superprop .
            ?superprop rdf:type owl:DatatypeProperty .
            ?subprop rdf:type owl:DatatypeProperty .
            FILTER(?subprop != ?superprop)
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_sub_data_property_of(cls[0], cls[1])
        return list(self.subdata_properties_of.values())

    def get_owl_sub_annotation_property_of(
        self,
    ) -> list[OWLSubAnnotationPropertyOf]:
        """
        Get all sub data property.

        Returns:
            List of OWLSubAnnotationPropertyOf
        """
        query = """
        SELECT DISTINCT ?subprop ?superprop
        WHERE {
            ?subprop rdfs:subPropertyOf ?superprop .
            ?superprop rdf:type owl:AnnotationProperty .
            ?subprop rdf:type owl:AnnotationProperty .
            FILTER(?subprop != ?superprop)
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_sub_annotation_property_of(
                cls[0],
                cls[1],
                self.get_owl_axiom_annotations_for(
                    cls[0], get_abbreviation(RDFS.subPropertyOf), cls[1]
                ),
            )
        return list(self.subannotation_properties_of.values())

    def get_owl_equivalent_object_properties(
        self,
    ) -> list[OWLEquivalentObjectProperties]:
        """
        Get all equivalent property relationships.

        Returns:
            List of (property1, property2) tuples
        """
        query = """
        SELECT DISTINCT ?prop1 ?prop2
        WHERE {
            ?prop1 owl:equivalentProperty ?prop2 .
            ?prop1 rdf:type owl:ObjectProperty .
            ?prop2 rdf:type owl:ObjectProperty .
            FILTER(?prop1 != ?prop2)
        }
        """

        annotations: dict[ObjectPropertyClass, set[OWLAnnotation]] = dict()
        marked: dict[ThingClass, bool] = dict()
        equivalence_chain: dict[ThingClass, ThingClass] = dict()
        for cls in self.world.sparql_query(query):
            if not isinstance(cls[0], ObjectPropertyClass):
                continue
            if not isinstance(cls[1], ObjectPropertyClass):
                continue
            equivalence_chain[cls[0]] = cls[1]
            marked[cls[0]] = False
            marked[cls[1]] = False
            curr_annotations = self.get_owl_axiom_annotations_for(
                cls[0], get_abbreviation(OWL.equivalentProperty), cls[1]
            )
            if curr_annotations:
                annotations[cls[0]] = annotations.get(cls[0], set()) | set(
                    curr_annotations
                )

        for chain, annotations in self._get_owl_chain(
            marked, equivalence_chain, annotations
        ):
            self.to_owl_equivalent_object_properties(tuple(chain), annotations)
        return list(self.equivalent_object_properties.values())

    def get_owl_disjoint_object_properties(self) -> list[OWLDisjointObjectProperties]:
        """
        Get all disjoint property pairs.

        Returns:
            List of (property1, property2) tuples
        """
        # Direct disjoint statements
        query1 = """
        SELECT DISTINCT ?prop1 ?prop2
        WHERE {
            ?prop1 owl:propertyDisjointWith ?prop2 .
            ?prop1 rdf:type owl:ObjectProperty .
            ?prop2 rdf:type owl:ObjectProperty .
            FILTER(?prop1 != ?prop2)
        }
        """

        # AllDisjointProperties
        query2 = """
        SELECT DISTINCT ?x
        WHERE {
            ?x rdf:type owl:AllDisjointProperties .
            ?x owl:members ?list .
            ?list rdf:rest*/rdf:first ?prop .
            ?prop rdf:type owl:ObjectProperty .
        }
        GROUP BY ?x
        HAVING(COUNT(?prop) >= 2)
        """

        for cls in self.world.sparql_query(query1):
            self.to_owl_disjoint_object_properties(cls)

        for cls in self.world.sparql_query(query2):
            self.to_owl_disjoint_object_properties(cls[0])

        return list(self.disjoint_object_properties.values())

    def get_owl_functional_object_properties(self) -> list[OWLFunctionalObjectProperty]:
        """
        Get all functional object properties.

        Returns:
            List of functional object properties
        """
        query = """
        SELECT DISTINCT ?property
        WHERE {
            ?property rdf:type owl:FunctionalProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_functional_object_property(cls[0])
        return list(self.functional_object_properties.values())

    def get_owl_inverse_functional_object_properties(
        self,
    ) -> list[OWLInverseFunctionalObjectProperty]:
        """
        Get all inverse functional object properties.

        Returns:
            List of inverse functional object properties
        """
        query = """
        SELECT DISTINCT ?property
        WHERE {
            ?property rdf:type owl:InverseFunctionalProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_inverse_functional_object_property(cls[0])
        return list(self.inverse_functional_object_properties.values())

    def get_owl_reflexive_object_properties(self) -> list[OWLReflexiveObjectProperty]:
        """
        Get all reflexive object properties.

        Returns:
            List of reflexive object properties
        """
        query = """
        SELECT DISTINCT ?property
        WHERE {
            ?property rdf:type owl:ReflexiveProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_reflexive_object_property(cls[0])
        return list(self.reflexive_object_properties.values())

    def get_owl_irreflexive_object_properties(
        self,
    ) -> list[OWLIrreflexiveObjectProperty]:
        """
        Get all irreflexive object properties.

        Returns:
            List of irreflexive object properties
        """
        query = """
        SELECT DISTINCT ?property
        WHERE {
            ?property rdf:type owl:IrreflexiveProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_irreflexive_object_property(cls[0])
        return list(self.irreflexive_object_properties.values())

    def get_owl_symmetric_object_properties(self) -> list[OWLSymmetricObjectProperty]:
        """
        Get all symmetric object properties.

        Returns:
            List of symmetric object properties
        """
        query = """
        SELECT DISTINCT ?property
        WHERE {
            ?property rdf:type owl:SymmetricProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_symmetric_object_property(cls[0])
        return list(self.symmetric_object_properties.values())

    def get_owl_asymmetric_object_properties(self) -> list[OWLObjectProperty]:
        """
        Get all asymmetric object properties.

        Returns:
            List of asymmetric object properties
        """
        query = """
        SELECT DISTINCT ?property
        WHERE {
            ?property rdf:type owl:AsymmetricProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_asymmetric_object_property(cls[0])
        return list(self.asymmetric_object_properties.values())

    def get_owl_transitive_object_properties(self) -> list[OWLTransitiveObjectProperty]:
        """
        Get all transitive object properties.

        Returns:
            List of transitive object properties
        """

        query = """
        SELECT DISTINCT ?property
        WHERE {
            ?property rdf:type owl:TransitiveProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_transitive_object_property(cls[0])
        return list(self.transitive_object_properties.values())

    def get_owl_functional_data_properties(self) -> list[OWLFunctionalDataProperty]:
        """
        Get all functional data properties.

        Returns:
            List of functional data properties
        """
        query = """
        SELECT DISTINCT ?property
        WHERE {
            ?property rdf:type owl:FunctionalProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_functional_data_property(cls[0])
        return list(self.functional_data_properties.values())

    def get_owl_equivalent_data_properties(self) -> list[OWLEquivalentDataProperties]:
        """
        Get all equivalent data property relationships.

        Returns:
            List of (property1, property2) tuples
        """
        query = """
        SELECT DISTINCT ?prop1 ?prop2
        WHERE {
            ?prop1 owl:equivalentProperty ?prop2 .
            ?prop1 rdf:type owl:DatatypeProperty .
            ?prop2 rdf:type owl:DatatypeProperty .
            FILTER(?prop1 != ?prop2)
        }
        """

        annotations: dict[DataPropertyClass, set[OWLAnnotation]] = dict()
        marked: dict[ThingClass, bool] = dict()
        equivalence_chain: dict[ThingClass, ThingClass] = dict()
        for cls in self.world.sparql_query(query):
            if not isinstance(cls[0], DataPropertyClass):
                continue
            if not isinstance(cls[1], DataPropertyClass):
                continue
            equivalence_chain[cls[0]] = cls[1]
            marked[cls[0]] = False
            marked[cls[1]] = False
            curr_annotations = self.get_owl_axiom_annotations_for(
                cls[0], get_abbreviation(OWL.equivalentProperty), cls[1]
            )
            if curr_annotations:
                annotations[cls[0]] = annotations.get(cls[0], set()) | set(
                    curr_annotations
                )

        for chain, annotations in self._get_owl_chain(
            marked, equivalence_chain, annotations
        ):
            self.to_owl_equivalent_data_properties(chain, annotations)
        return list(self.equivalent_data_properties.values())

    def get_owl_disjoint_data_properties(self) -> list[OWLDisjointDataProperties]:
        """
        Get all disjoint data property pairs.

        Returns:
            List of disjoint data properties
        """
        # Direct disjoint statements
        query1 = """
        SELECT DISTINCT ?prop1 ?prop2
        WHERE {
            ?prop1 owl:propertyDisjointWith ?prop2 .
            ?prop1 rdf:type owl:DatatypeProperty .
            ?prop2 rdf:type owl:DatatypeProperty .
            FILTER(?prop1 != ?prop2)
        }
        """

        # AllDisjointProperties
        query2 = """
        SELECT DISTINCT ?x
        WHERE {
            ?x rdf:type owl:AllDisjointProperties .
            ?x owl:members ?list .
            ?list rdf:rest*/rdf:first ?prop .
            ?prop rdf:type owl:DatatypeProperty .
        }
        GROUP BY ?x
        HAVING(COUNT(?prop) >= 2)
        """

        for cls in self.world.sparql_query(query1):
            self.to_owl_disjoint_data_properties(cls)

        for cls in self.world.sparql_query(query2):
            self.to_owl_disjoint_data_properties(cls[0])

        return list(self.disjoint_data_properties.values())

    def get_owl_object_property_domains(self) -> list[OWLObjectPropertyDomain]:
        """
        Get all object property domains.

        Returns:
            List of object property domains
        """
        query = """
        SELECT DISTINCT ?property ?class
        WHERE {
            ?property rdfs:domain ?class .
            ?property rdf:type owl:ObjectProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_object_property_domain(cls[0], cls[1])
        return list(self.object_property_domains.values())

    def get_owl_object_property_ranges(self) -> list[OWLObjectPropertyRange]:
        """
        Get all object property ranges.

        Returns:
            List of object property ranges
        """
        query = """
        SELECT DISTINCT ?property ?class
        WHERE {
            ?property rdfs:range ?class .
            ?property rdf:type owl:ObjectProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_object_property_range(cls[0], cls[1])
        return list(self.object_property_ranges.values())

    def get_owl_data_property_domains(self) -> list[OWLDataPropertyDomain]:
        """
        Get all data property domains.

        Returns:
            List of data property domains
        """
        query = """
        SELECT DISTINCT ?property ?class
        WHERE {
            ?property rdfs:domain ?class .
            ?property rdf:type owl:DatatypeProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_data_property_domain(cls[0], cls[1])
        return list(self.data_property_domains.values())

    def get_owl_data_property_ranges(self) -> list[OWLDataPropertyRange]:
        """
        Get all data property ranges.

        Returns:
            List of data property ranges
        """
        query = """
        SELECT DISTINCT ?property ?class
        WHERE {
            ?property rdfs:range ?class .
            ?property rdf:type owl:DatatypeProperty .
        }
        """
        for cls in self.world.sparql_query(query):
            self.to_owl_data_property_range(cls[0])
        return list(self.data_property_ranges.values())

    def get_owl_datatype_definitions(self) -> list[OWLDatatypeDefinition]:
        """
        Get all datatype definitions.

        Returns:
            List of datatype definitions
        """

        # ?restriction owl:onDatatype ?onDatatype .
        query = """
        SELECT DISTINCT ?class1 ?restriction
        WHERE {
            ?class1 owl:equivalentClass ?restriction .
            ?restriction ?facet ?value .
            FILTER(isBlank(?restriction))
        }
        """
        for cls in self.world.sparql_query(query):
            self.get_owl_datatype_definition(cls[0], cls[1])
        return list(self.datatype_definitions.values())
