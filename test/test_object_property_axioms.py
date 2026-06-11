import unittest

from pyowl2 import (
    IRI,
    OWLAsymmetricObjectProperty,
    OWLClass,
    OWLDeclaration,
    OWLDisjointObjectProperties,
    OWLEquivalentObjectProperties,
    OWLFunctionalObjectProperty,
    OWLInverseFunctionalObjectProperty,
    OWLInverseObjectProperties,
    OWLIrreflexiveObjectProperty,
    OWLObjectPropertyDomain,
    OWLObjectPropertyRange,
    OWLReflexiveObjectProperty,
    OWLSubObjectPropertyOf,
    OWLSymmetricObjectProperty,
    OWLTransitiveObjectProperty,
)
from pyowl2.expressions.object_property import OWLObjectProperty as ObjectPropertyExpr
from pyowl2.getter.rdf_xml_getter import AxiomsType

from .helpers import NS, roundtrip


class TestObjectPropertyAxioms(unittest.TestCase):

    def test_sub_object_property(self):
        has_pet = ObjectPropertyExpr(IRI(NS, "hasPet"))
        has_dog = ObjectPropertyExpr(IRI(NS, "hasDog"))
        axiom = OWLSubObjectPropertyOf(has_dog, has_pet)
        results = roundtrip(
            [axiom, OWLDeclaration(has_pet), OWLDeclaration(has_dog)],
            AxiomsType.SUB_OBJECT_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_equivalent_object_properties(self):
        knows = ObjectPropertyExpr(IRI(NS, "knows"))
        is_friend_of = ObjectPropertyExpr(IRI(NS, "isFriendOf"))
        axiom = OWLEquivalentObjectProperties([knows, is_friend_of])
        results = roundtrip(
            [axiom, OWLDeclaration(knows), OWLDeclaration(is_friend_of)],
            AxiomsType.EQUIVALENT_OBJECT_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_disjoint_object_properties(self):
        """OWLDisjointObjectProperties getter: unhashable list in dict lookup."""
        loves = ObjectPropertyExpr(IRI(NS, "loves"))
        hates = ObjectPropertyExpr(IRI(NS, "hates"))
        axiom = OWLDisjointObjectProperties([loves, hates])
        results = roundtrip(
            [axiom, OWLDeclaration(loves), OWLDeclaration(hates)],
            AxiomsType.DISJOINT_OBJECT_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_property_domain(self):
        has_pet = ObjectPropertyExpr(IRI(NS, "hasPet"))
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLObjectPropertyDomain(has_pet, person)
        results = roundtrip(
            [axiom, OWLDeclaration(has_pet), OWLDeclaration(person)],
            AxiomsType.OBJECT_PROPERTY_DOMAIN,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_property_range(self):
        has_pet = ObjectPropertyExpr(IRI(NS, "hasPet"))
        animal = OWLClass(IRI(NS, "Animal"))
        axiom = OWLObjectPropertyRange(has_pet, animal)
        results = roundtrip(
            [axiom, OWLDeclaration(has_pet), OWLDeclaration(animal)],
            AxiomsType.OBJECT_PROPERTY_RANGE,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_inverse_object_properties(self):
        loves = ObjectPropertyExpr(IRI(NS, "loves"))
        loved_by = ObjectPropertyExpr(IRI(NS, "lovedBy"))
        axiom = OWLInverseObjectProperties(loves, loved_by)
        results = roundtrip(
            [axiom, OWLDeclaration(loves), OWLDeclaration(loved_by)],
            AxiomsType.INVERSE_OBJECT_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_functional_object_property(self):
        has_mother = ObjectPropertyExpr(IRI(NS, "hasMother"))
        axiom = OWLFunctionalObjectProperty(has_mother)
        results = roundtrip(
            [axiom, OWLDeclaration(has_mother)],
            AxiomsType.FUNCTIONAL_OBJECT_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_inverse_functional_object_property(self):
        is_mother_of = ObjectPropertyExpr(IRI(NS, "isMotherOf"))
        axiom = OWLInverseFunctionalObjectProperty(is_mother_of)
        results = roundtrip(
            [axiom, OWLDeclaration(is_mother_of)],
            AxiomsType.INVERSE_FUNCTIONAL_OBJECT_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_transitive_object_property(self):
        is_ancestor_of = ObjectPropertyExpr(IRI(NS, "isAncestorOf"))
        axiom = OWLTransitiveObjectProperty(is_ancestor_of)
        results = roundtrip(
            [axiom, OWLDeclaration(is_ancestor_of)],
            AxiomsType.TRANSITIVE_OBJECT_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_symmetric_object_property(self):
        is_friend_of = ObjectPropertyExpr(IRI(NS, "isFriendOf"))
        axiom = OWLSymmetricObjectProperty(is_friend_of)
        results = roundtrip(
            [axiom, OWLDeclaration(is_friend_of)],
            AxiomsType.SYMMETRIC_OBJECT_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_asymmetric_object_property(self):
        is_parent_of = ObjectPropertyExpr(IRI(NS, "isParentOf"))
        axiom = OWLAsymmetricObjectProperty(is_parent_of)
        results = roundtrip(
            [axiom, OWLDeclaration(is_parent_of)],
            AxiomsType.ASYMMETRIC_OBJECT_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_reflexive_object_property(self):
        knows = ObjectPropertyExpr(IRI(NS, "knows"))
        axiom = OWLReflexiveObjectProperty(knows)
        results = roundtrip(
            [axiom, OWLDeclaration(knows)],
            AxiomsType.REFLEXIVE_OBJECT_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_irreflexive_object_property(self):
        is_parent_of = ObjectPropertyExpr(IRI(NS, "isParentOf"))
        axiom = OWLIrreflexiveObjectProperty(is_parent_of)
        results = roundtrip(
            [axiom, OWLDeclaration(is_parent_of)],
            AxiomsType.IRREFLEXIVE_OBJECT_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
