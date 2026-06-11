import unittest

from rdflib import XSD, Literal

from pyowl2 import (
    IRI,
    OWLAnnotation,
    OWLAnnotationAssertion,
    OWLAnnotationProperty,
    OWLAnnotationPropertyDomain,
    OWLAnnotationPropertyRange,
    OWLClass,
    OWLDatatype,
    OWLDeclaration,
    OWLOntology,
    OWLSubAnnotationPropertyOf,
)
from pyowl2.getter.rdf_xml_getter import AxiomsType

from .helpers import NS, REF, XSD_NS, roundtrip


class TestAnnotations(unittest.TestCase):

    def test_annotation_assertion(self):
        label = OWLAnnotationProperty(IRI(NS, "label"))
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLAnnotationAssertion(person.iri, label, Literal("A person"))
        results = roundtrip(
            [axiom, OWLDeclaration(person), OWLDeclaration(label)],
            AxiomsType.ANNOTATIONS,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_annotation_property_domain(self):
        label = OWLAnnotationProperty(IRI(NS, "label"))
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLAnnotationPropertyDomain(label, person)
        results = roundtrip(
            [axiom, OWLDeclaration(label), OWLDeclaration(person)],
            AxiomsType.ANNOTATION_PROPERTY_DOMAINS,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_annotation_property_range(self):
        label = OWLAnnotationProperty(IRI(NS, "label"))
        axiom = OWLAnnotationPropertyRange(label, OWLDatatype(IRI(XSD_NS, XSD.string)))
        results = roundtrip(
            [axiom, OWLDeclaration(label)],
            AxiomsType.ANNOTATION_PROPERTY_RANGES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_sub_annotation_property(self):
        label = OWLAnnotationProperty(IRI(NS, "label"))
        display_name = OWLAnnotationProperty(IRI(NS, "displayName"))
        axiom = OWLSubAnnotationPropertyOf(display_name, label)
        results = roundtrip(
            [axiom, OWLDeclaration(label), OWLDeclaration(display_name)],
            AxiomsType.SUB_ANNOTATION_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_ontology_annotations(self):
        """OWLOntology annotations getter returns empty."""
        import os
        import tempfile

        label = OWLAnnotationProperty(IRI(NS, "label"))
        annotation = OWLAnnotation(label, Literal("Test Ontology"))
        onto = OWLOntology(REF)
        onto.add_annotation(annotation)
        tmp_dir = tempfile.mkdtemp()
        filepath = os.path.join(tmp_dir, "test.owl")
        onto.save(filepath)

        onto2 = OWLOntology(REF, filepath)
        annotations = onto2.get_axioms(AxiomsType.ANNOTATIONS)
        os.unlink(filepath)
        os.rmdir(tmp_dir)

        self.assertGreaterEqual(len(annotations), 1)

    def test_empty_ontology_annotations(self):
        """Test ontology with no annotations."""
        import os
        import tempfile

        onto = OWLOntology(REF)
        tmp_dir = tempfile.mkdtemp()
        filepath = os.path.join(tmp_dir, "test.owl")
        onto.save(filepath)

        onto2 = OWLOntology(REF, filepath)
        annotations = onto2.get_axioms(AxiomsType.ANNOTATIONS)
        os.unlink(filepath)
        os.rmdir(tmp_dir)

        # Should have no annotations
        self.assertEqual(len(annotations), 0)

    def test_multiple_ontology_annotations(self):
        """Test ontology with multiple custom annotations."""
        import os
        import tempfile

        onto = OWLOntology(REF)
        label1 = OWLAnnotationProperty(IRI(NS, "label"))
        label2 = OWLAnnotationProperty(IRI(NS, "description"))
        label3 = OWLAnnotationProperty(IRI(NS, "version"))

        annotation1 = OWLAnnotation(label1, Literal("Test Ontology"))
        annotation2 = OWLAnnotation(label2, Literal("A test ontology for pyowl2"))
        annotation3 = OWLAnnotation(label3, Literal("1.0.0"))

        onto.add_annotation(annotation1)
        onto.add_annotation(annotation2)
        onto.add_annotation(annotation3)

        tmp_dir = tempfile.mkdtemp()
        filepath = os.path.join(tmp_dir, "test.owl")
        onto.save(filepath)

        onto2 = OWLOntology(REF, filepath)
        annotations = onto2.get_axioms(AxiomsType.ANNOTATIONS)
        os.unlink(filepath)
        os.rmdir(tmp_dir)

        self.assertGreaterEqual(len(annotations), 3)

    def test_mixed_annotation_types(self):
        """Test ontology with standard and custom annotations."""
        import os
        import tempfile
        from rdflib import RDFS

        onto = OWLOntology(REF)
        # Custom annotation
        custom_label = OWLAnnotationProperty(IRI(NS, "customLabel"))
        custom_annotation = OWLAnnotation(custom_label, Literal("Custom Label"))
        onto.add_annotation(custom_annotation)

        # Standard annotation (rdfs:label)
        standard_label = OWLAnnotationProperty(IRI(RDFS, "label"))
        standard_annotation = OWLAnnotation(standard_label, Literal("Standard Label"))
        onto.add_annotation(standard_annotation)

        tmp_dir = tempfile.mkdtemp()
        filepath = os.path.join(tmp_dir, "test.owl")
        onto.save(filepath)

        onto2 = OWLOntology(REF, filepath)
        annotations = onto2.get_axioms(AxiomsType.ANNOTATIONS)
        os.unlink(filepath)
        os.rmdir(tmp_dir)

        self.assertGreaterEqual(len(annotations), 2)


if __name__ == "__main__":
    unittest.main()
