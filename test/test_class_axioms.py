import unittest

from pyowl2 import (
    IRI,
    OWLClass,
    OWLDeclaration,
    OWLDisjointClasses,
    OWLDisjointUnion,
    OWLEquivalentClasses,
    OWLSubClassOf,
)
from pyowl2.getter.rdf_xml_getter import AxiomsType

from .helpers import NS, roundtrip


class TestClassAxioms(unittest.TestCase):

    def test_subclass_of(self):
        person = OWLClass(IRI(NS, "Person"))
        animal = OWLClass(IRI(NS, "Animal"))
        axiom = OWLSubClassOf(person, animal)
        results = roundtrip(
            [axiom, OWLDeclaration(person), OWLDeclaration(animal)],
            AxiomsType.SUBCLASSES,
        )
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(any(isinstance(r, OWLSubClassOf) for r in results))

    def test_equivalent_classes(self):
        human = OWLClass(IRI(NS, "Human"))
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLEquivalentClasses([human, person])
        results = roundtrip(
            [axiom, OWLDeclaration(human), OWLDeclaration(person)],
            AxiomsType.EQUIVALENT_CLASSES,
        )
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(any(isinstance(r, OWLEquivalentClasses) for r in results))

    def test_disjoint_classes(self):
        cat = OWLClass(IRI(NS, "Cat"))
        dog = OWLClass(IRI(NS, "Dog"))
        axiom = OWLDisjointClasses([cat, dog])
        results = roundtrip(
            [axiom, OWLDeclaration(cat), OWLDeclaration(dog)],
            AxiomsType.DISJOINT_CLASSES,
        )
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(any(isinstance(r, OWLDisjointClasses) for r in results))

    def test_disjoint_union(self):
        """OWLDisjointUnion getter returns empty."""
        animal = OWLClass(IRI(NS, "Animal"))
        cat = OWLClass(IRI(NS, "Cat"))
        dog = OWLClass(IRI(NS, "Dog"))
        axiom = OWLDisjointUnion(animal, [cat, dog])
        results = roundtrip(
            [axiom, OWLDeclaration(animal), OWLDeclaration(cat), OWLDeclaration(dog)],
            AxiomsType.DISJOINT_UNIONS,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_disjoint_union_minimal(self):
        """Test disjoint union with minimum 2 classes."""
        animal = OWLClass(IRI(NS, "Animal"))
        cat = OWLClass(IRI(NS, "Cat"))
        dog = OWLClass(IRI(NS, "Dog"))
        axiom = OWLDisjointUnion(animal, [cat, dog])
        results = roundtrip(
            [axiom, OWLDeclaration(animal), OWLDeclaration(cat), OWLDeclaration(dog)],
            AxiomsType.DISJOINT_UNIONS,
        )
        self.assertGreaterEqual(len(results), 1)
        # Verify it's a disjoint union with 2 classes
        self.assertTrue(any(isinstance(r, OWLDisjointUnion) and len(r.disjoint_class_expressions) == 2 for r in results))

    def test_disjoint_union_many_classes(self):
        """Test disjoint union with many classes."""
        vehicle = OWLClass(IRI(NS, "Vehicle"))
        car = OWLClass(IRI(NS, "Car"))
        truck = OWLClass(IRI(NS, "Truck"))
        motorcycle = OWLClass(IRI(NS, "Motorcycle"))
        bicycle = OWLClass(IRI(NS, "Bicycle"))
        axiom = OWLDisjointUnion(vehicle, [car, truck, motorcycle, bicycle])
        results = roundtrip(
            [axiom, OWLDeclaration(vehicle), OWLDeclaration(car), OWLDeclaration(truck),
             OWLDeclaration(motorcycle), OWLDeclaration(bicycle)],
            AxiomsType.DISJOINT_UNIONS,
        )
        self.assertGreaterEqual(len(results), 1)
        # Verify it's a disjoint union with 4 classes
        self.assertTrue(any(isinstance(r, OWLDisjointUnion) and len(r.disjoint_class_expressions) == 4 for r in results))


if __name__ == "__main__":
    unittest.main()
