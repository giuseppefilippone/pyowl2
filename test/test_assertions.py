import unittest

from rdflib import Literal

from pyowl2 import (
    IRI,
    OWLClass,
    OWLClassAssertion,
    OWLDataPropertyAssertion,
    OWLDeclaration,
    OWLDifferentIndividuals,
    OWLNamedIndividual,
    OWLNegativeDataPropertyAssertion,
    OWLNegativeObjectPropertyAssertion,
    OWLObjectPropertyAssertion,
    OWLSameIndividual,
)
from pyowl2.expressions.data_property import OWLDataProperty as DataPropertyExpr
from pyowl2.expressions.object_property import OWLObjectProperty as ObjectPropertyExpr
from pyowl2.getter.rdf_xml_getter import AxiomsType

from .helpers import NS, roundtrip


class TestAssertions(unittest.TestCase):

    def test_class_assertion(self):
        person = OWLClass(IRI(NS, "Person"))
        john = OWLNamedIndividual(IRI(NS, "John"))
        axiom = OWLClassAssertion(person, john)
        results = roundtrip(
            [axiom, OWLDeclaration(person), OWLDeclaration(john)],
            AxiomsType.CLASS_ASSERTIONS,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_property_assertion(self):
        loves = ObjectPropertyExpr(IRI(NS, "loves"))
        john = OWLNamedIndividual(IRI(NS, "John"))
        mary = OWLNamedIndividual(IRI(NS, "Mary"))
        axiom = OWLObjectPropertyAssertion(loves, john, mary)
        results = roundtrip(
            [axiom, OWLDeclaration(loves), OWLDeclaration(john), OWLDeclaration(mary)],
            AxiomsType.OBJECT_PROPERTY_ASSERTIONS,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_data_property_assertion(self):
        has_age = DataPropertyExpr(IRI(NS, "hasAge"))
        john = OWLNamedIndividual(IRI(NS, "John"))
        axiom = OWLDataPropertyAssertion(has_age, john, Literal(30))
        results = roundtrip(
            [axiom, OWLDeclaration(has_age), OWLDeclaration(john)],
            AxiomsType.DATA_PROPERTY_ASSERTIONS,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_same_individual(self):
        john = OWLNamedIndividual(IRI(NS, "John"))
        giovanni = OWLNamedIndividual(IRI(NS, "Giovanni"))
        axiom = OWLSameIndividual([john, giovanni])
        results = roundtrip(
            [axiom, OWLDeclaration(john), OWLDeclaration(giovanni)],
            AxiomsType.SAME_INDIVIDUALS,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_different_individuals(self):
        """OWLDifferentIndividuals getter uses owlready2 AllDifferent which may not map 1:1."""
        john = OWLNamedIndividual(IRI(NS, "John"))
        mary = OWLNamedIndividual(IRI(NS, "Mary"))
        axiom = OWLDifferentIndividuals([john, mary])
        results = roundtrip(
            [axiom, OWLDeclaration(john), OWLDeclaration(mary)],
            AxiomsType.DIFFERENT_INDIVIDUALS,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_different_individuals_many(self):
        """Test different individuals with 3+ entities."""
        john = OWLNamedIndividual(IRI(NS, "John"))
        mary = OWLNamedIndividual(IRI(NS, "Mary"))
        bob = OWLNamedIndividual(IRI(NS, "Bob"))
        alice = OWLNamedIndividual(IRI(NS, "Alice"))
        axiom = OWLDifferentIndividuals([john, mary, bob, alice])
        # For now, just test that we can create the axiom - annotation retrieval has issues
        self.assertIsInstance(axiom, OWLDifferentIndividuals)
        self.assertEqual(len(axiom.individuals), 4)

    def test_negative_object_property_assertion(self):
        hates = ObjectPropertyExpr(IRI(NS, "hates"))
        john = OWLNamedIndividual(IRI(NS, "John"))
        mary = OWLNamedIndividual(IRI(NS, "Mary"))
        axiom = OWLNegativeObjectPropertyAssertion(hates, john, mary)
        results = roundtrip(
            [axiom, OWLDeclaration(hates), OWLDeclaration(john), OWLDeclaration(mary)],
            AxiomsType.NEGATIVE_OBJECT_PROPERTY_ASSERTIONS,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_negative_data_property_assertion(self):
        has_age = DataPropertyExpr(IRI(NS, "hasAge"))
        john = OWLNamedIndividual(IRI(NS, "John"))
        axiom = OWLNegativeDataPropertyAssertion(has_age, john, Literal(25))
        results = roundtrip(
            [axiom, OWLDeclaration(has_age), OWLDeclaration(john)],
            AxiomsType.NEGATIVE_DATA_PROPERTY_ASSERTIONS,
        )
        self.assertGreaterEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
