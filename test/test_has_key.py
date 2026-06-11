import unittest

from pyowl2 import IRI, OWLClass, OWLDeclaration, OWLHasKey
from pyowl2.expressions.data_property import OWLDataProperty as DataPropertyExpr
from pyowl2.getter.rdf_xml_getter import AxiomsType

from .helpers import NS, roundtrip


class TestHasKey(unittest.TestCase):

    def test_has_key(self):
        """OWLHasKey mapper: property IRIs not converted to rdflib terms."""
        person = OWLClass(IRI(NS, "Person"))
        has_id = DataPropertyExpr(IRI(NS, "hasId"))
        axiom = OWLHasKey(person, [], [has_id])
        results = roundtrip(
            [axiom, OWLDeclaration(person), OWLDeclaration(has_id)],
            AxiomsType.HAS_KEYS,
        )
        self.assertGreaterEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
