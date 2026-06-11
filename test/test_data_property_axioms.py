import unittest

from rdflib import XSD

from pyowl2 import (
    IRI,
    OWLClass,
    OWLDataPropertyDomain,
    OWLDataPropertyRange,
    OWLDatatype,
    OWLDeclaration,
    OWLDisjointDataProperties,
    OWLEquivalentDataProperties,
    OWLFunctionalDataProperty,
    OWLSubDataPropertyOf,
)
from pyowl2.expressions.data_property import OWLDataProperty as DataPropertyExpr
from pyowl2.getter.rdf_xml_getter import AxiomsType

from .helpers import NS, XSD_NS, roundtrip


class TestDataPropertyAxioms(unittest.TestCase):

    def test_sub_data_property(self):
        has_name = DataPropertyExpr(IRI(NS, "hasName"))
        has_label = DataPropertyExpr(IRI(NS, "hasLabel"))
        axiom = OWLSubDataPropertyOf(has_name, has_label)
        results = roundtrip(
            [axiom, OWLDeclaration(has_name), OWLDeclaration(has_label)],
            AxiomsType.SUB_DATA_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_equivalent_data_properties(self):
        has_name = DataPropertyExpr(IRI(NS, "hasName"))
        has_label = DataPropertyExpr(IRI(NS, "hasLabel"))
        axiom = OWLEquivalentDataProperties([has_name, has_label])
        results = roundtrip(
            [axiom, OWLDeclaration(has_name), OWLDeclaration(has_label)],
            AxiomsType.EQUIVALENT_DATA_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_disjoint_data_properties(self):
        """OWLDisjointDataProperties getter returns empty."""
        has_name = DataPropertyExpr(IRI(NS, "hasName"))
        has_id = DataPropertyExpr(IRI(NS, "hasId"))
        axiom = OWLDisjointDataProperties([has_name, has_id])
        results = roundtrip(
            [axiom, OWLDeclaration(has_name), OWLDeclaration(has_id)],
            AxiomsType.DISJOINT_DATA_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_data_property_domain(self):
        has_age = DataPropertyExpr(IRI(NS, "hasAge"))
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLDataPropertyDomain(has_age, person)
        results = roundtrip(
            [axiom, OWLDeclaration(has_age), OWLDeclaration(person)],
            AxiomsType.DATA_PROPERTY_DOMAIN,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_data_property_range(self):
        has_age = DataPropertyExpr(IRI(NS, "hasAge"))
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDataPropertyRange(has_age, integer_dt)
        results = roundtrip(
            [axiom, OWLDeclaration(has_age)],
            AxiomsType.DATA_PROPERTY_RANGE,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_functional_data_property(self):
        has_age = DataPropertyExpr(IRI(NS, "hasAge"))
        axiom = OWLFunctionalDataProperty(has_age)
        results = roundtrip(
            [axiom, OWLDeclaration(has_age)],
            AxiomsType.FUNCIONAL_DATA_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
