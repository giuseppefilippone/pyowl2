pyowl2.utils.datatype
=====================

.. py:module:: pyowl2.utils.datatype


Classes
-------

.. autoapisummary::

   pyowl2.utils.datatype.OWLFullDataRange


Module Contents
---------------

.. py:class:: OWLFullDataRange(iri: pyowl2.base.iri.IRI)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`


   Abstract class for OWL objects.


   .. py:method:: define(datatype: pyowl2.base.datatype.OWLDatatype) -> None


   .. py:method:: is_complement_of(other: Union[pyowl2.abstracts.data_range.OWLDataRange, Self]) -> None


   .. py:method:: is_equivalent_to(value: Union[pyowl2.abstracts.data_range.OWLDataRange, Self, list[pyowl2.abstracts.data_range.OWLDataRange], list[Self]]) -> None


   .. py:method:: is_intersection_of(data_ranges: Union[list[pyowl2.abstracts.data_range.OWLDataRange], list[Self]]) -> None


   .. py:method:: is_one_of(literals: Union[list[pyowl2.literal.literal.OWLLiteral], list[rdflib.Literal]]) -> None


   .. py:method:: is_union_of(data_ranges: Union[list[pyowl2.abstracts.data_range.OWLDataRange], list[Self]]) -> None


   .. py:method:: restrict(datatype: pyowl2.base.datatype.OWLDatatype, facets: list[pyowl2.data_range.datatype_restriction.OWLFacet]) -> None


   .. py:method:: to_complement() -> None


   .. py:property:: annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]



   .. py:property:: axioms
      :type: list[Any]



   .. py:property:: data_range
      :type: pyowl2.abstracts.data_range.OWLDataRange



   .. py:property:: intersections
      :type: list[pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf]



   .. py:property:: is_complement
      :type: bool



   .. py:property:: ones_of
      :type: list[pyowl2.data_range.data_complement_of.OWLDataComplementOf]



   .. py:property:: restrictions
      :type: list[pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction]



   .. py:property:: unions
      :type: list[pyowl2.data_range.data_union_of.OWLDataUnionOf]



