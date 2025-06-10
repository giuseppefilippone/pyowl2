pyowl2.data_range.datatype_restriction
======================================

.. py:module:: pyowl2.data_range.datatype_restriction


Classes
-------

.. autoapisummary::

   pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction
   pyowl2.data_range.datatype_restriction.OWLFacet
   pyowl2.data_range.datatype_restriction.OWLFacetTypes


Module Contents
---------------

.. py:class:: OWLDatatypeRestriction(datatype: pyowl2.base.datatype.OWLDatatype, restrictions: list[OWLFacet])

   Bases: :py:obj:`pyowl2.abstracts.data_range.OWLDataRange`


   A datatype that is constrained by specific facets, such as value ranges or lengths.


   .. py:method:: __str__() -> str


   .. py:property:: datatype
      :type: pyowl2.base.datatype.OWLDatatype


      Getter for datatype.


   .. py:property:: restrictions
      :type: list[OWLFacet]


      Getter for facets.


.. py:class:: OWLFacet(constraint: Union[rdflib.URIRef, pyowl2.base.iri.IRI], value: pyowl2.literal.literal.OWLLiteral)

   .. py:method:: __eq__(value: object) -> bool


   .. py:method:: __ge__(value: object) -> bool


   .. py:method:: __gt__(value: object) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __le__(value: object) -> bool


   .. py:method:: __lt__(value: object) -> bool


   .. py:method:: __ne__(value: object) -> bool


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: constraint_to_uriref() -> rdflib.URIRef


   .. py:attribute:: MAX_EXCLUSIVE
      :type:  rdflib.URIRef


   .. py:attribute:: MAX_INCLUSIVE
      :type:  rdflib.URIRef


   .. py:attribute:: MIN_EXCLUSIVE
      :type:  rdflib.URIRef


   .. py:attribute:: MIN_INCLUSIVE
      :type:  rdflib.URIRef


   .. py:property:: constraint
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]



   .. py:attribute:: valid_restrictions
      :type:  list[rdflib.URIRef]


   .. py:property:: value
      :type: pyowl2.literal.literal.OWLLiteral



.. py:class:: OWLFacetTypes

   Bases: :py:obj:`enum.StrEnum`


   Enum where members are also (and must be) strings


   .. py:attribute:: MAX_EXCLUSIVE


   .. py:attribute:: MAX_INCLUSIVE


   .. py:attribute:: MIN_EXCLUSIVE


   .. py:attribute:: MIN_INCLUSIVE


