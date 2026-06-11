import unittest

from rdflib import XSD, Literal

from pyowl2 import (
    IRI,
    OWLDataComplementOf,
    OWLDataIntersectionOf,
    OWLDataOneOf,
    OWLDatatype,
    OWLDatatypeDefinition,
    OWLDatatypeRestriction,
    OWLDataUnionOf,
    OWLDeclaration,
)
from pyowl2.data_range.datatype_restriction import OWLFacet, OWLFacetTypes
from pyowl2.getter.rdf_xml_getter import AxiomsType
from pyowl2.literal.literal import OWLTypedLiteral

from .helpers import NS, XSD_NS, roundtrip


class TestDataRanges(unittest.TestCase):

    def test_data_complement_of(self):
        """OWLDataComplementOf getter not implemented (logs warning)."""
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDataComplementOf(integer_dt)
        results = roundtrip([axiom], AxiomsType.DATA_COMPLEMENT_OF)
        self.assertGreaterEqual(len(results), 1)

    def test_data_intersection_of(self):
        """DataIntersectionOf needs >=2 ranges (OWL 2 spec)."""
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        string_dt = OWLDatatype(IRI(XSD_NS, XSD.string))
        axiom = OWLDataIntersectionOf([integer_dt, string_dt])
        results = roundtrip([axiom], AxiomsType.DATA_INTERSECTION_OF)
        self.assertGreaterEqual(len(results), 1)

    def test_data_union_of(self):
        """DataUnionOf needs >=2 ranges (OWL 2 spec)."""
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        string_dt = OWLDatatype(IRI(XSD_NS, XSD.string))
        axiom = OWLDataUnionOf([integer_dt, string_dt])
        results = roundtrip([axiom], AxiomsType.DATA_UNION_OF)
        self.assertGreaterEqual(len(results), 1)

    def test_data_one_of(self):
        axiom = OWLDataOneOf([Literal(1), Literal(2)])
        results = roundtrip([axiom], AxiomsType.DATA_ONE_OF)
        self.assertGreaterEqual(len(results), 1)

    def test_datatype_restriction(self):
        """OWLDatatypeRestriction mapper: facet URI not converted to rdflib term."""
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        facet = OWLFacet(OWLFacetTypes.MIN_INCLUSIVE, OWLTypedLiteral(0, integer_dt))
        axiom = OWLDatatypeRestriction(integer_dt, [facet])
        results = roundtrip([axiom], AxiomsType.DATATYPE_RESTRICTIONS)
        self.assertGreaterEqual(len(results), 1)

    def test_datatype_definition(self):
        """OWLDatatypeDefinition getter returns empty."""
        my_int = OWLDatatype(IRI(NS, "myInt"))
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDatatypeDefinition(my_int, integer_dt)
        results = roundtrip(
            [axiom, OWLDeclaration(my_int)], AxiomsType.DATATYPE_DEFINITION
        )
        self.assertGreaterEqual(len(results), 1)

    def test_nested_datatype_restrictions(self):
        """Test complex datatype restriction with multiple facets."""
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        min_facet = OWLFacet(OWLFacetTypes.MIN_INCLUSIVE, OWLTypedLiteral(0, integer_dt))
        max_facet = OWLFacet(OWLFacetTypes.MAX_EXCLUSIVE, OWLTypedLiteral(100, integer_dt))
        axiom = OWLDatatypeRestriction(integer_dt, [min_facet, max_facet])
        results = roundtrip([axiom], AxiomsType.DATATYPE_RESTRICTIONS)
        self.assertGreaterEqual(len(results), 1)
        # Verify it has 2 facets
        self.assertTrue(any(isinstance(r, OWLDatatypeRestriction) and len(r.restrictions) == 2 for r in results))

    def test_data_intersection_many_ranges(self):
        """Test data intersection with many ranges."""
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        string_dt = OWLDatatype(IRI(XSD_NS, XSD.string))
        boolean_dt = OWLDatatype(IRI(XSD_NS, XSD.boolean))
        decimal_dt = OWLDatatype(IRI(XSD_NS, XSD.decimal))
        axiom = OWLDataIntersectionOf([integer_dt, string_dt, boolean_dt, decimal_dt])
        results = roundtrip([axiom], AxiomsType.DATA_INTERSECTION_OF)
        self.assertGreaterEqual(len(results), 1)
        # Verify it has 4 ranges
        self.assertTrue(any(isinstance(r, OWLDataIntersectionOf) and len(r.data_ranges) == 4 for r in results))

    def test_data_union_many_ranges(self):
        """Test data union with many ranges."""
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        string_dt = OWLDatatype(IRI(XSD_NS, XSD.string))
        boolean_dt = OWLDatatype(IRI(XSD_NS, XSD.boolean))
        decimal_dt = OWLDatatype(IRI(XSD_NS, XSD.decimal))
        axiom = OWLDataUnionOf([integer_dt, string_dt, boolean_dt, decimal_dt])
        results = roundtrip([axiom], AxiomsType.DATA_UNION_OF)
        self.assertGreaterEqual(len(results), 1)
        # Verify it has 4 ranges
        self.assertTrue(any(isinstance(r, OWLDataUnionOf) and len(r.data_ranges) == 4 for r in results))


if __name__ == "__main__":
    unittest.main()
