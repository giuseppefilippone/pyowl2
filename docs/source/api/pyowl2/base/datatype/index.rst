pyowl2.base.datatype
====================

.. py:module:: pyowl2.base.datatype


Classes
-------

.. autoapisummary::

   pyowl2.base.datatype.OWLDatatype


Module Contents
---------------

.. py:class:: OWLDatatype(iri: Union[pyowl2.base.iri.IRI, rdflib.URIRef])

   Bases: :py:obj:`pyowl2.abstracts.entity.OWLEntity`, :py:obj:`pyowl2.abstracts.data_range.OWLDataRange`


   A category of data values, such as integers or strings, defined by a set of permissible values.


   .. py:method:: __str__() -> str


   .. py:method:: is_anyuri() -> bool


   .. py:method:: is_boolean() -> bool


   .. py:method:: is_date() -> bool


   .. py:method:: is_decimal() -> bool


   .. py:method:: is_double() -> bool


   .. py:method:: is_float() -> bool


   .. py:method:: is_integer() -> bool


   .. py:method:: is_rational() -> bool


   .. py:method:: is_real() -> bool


   .. py:method:: is_string() -> bool


   .. py:method:: to_uriref() -> rdflib.URIRef


   .. py:property:: iri
      :type: Union[pyowl2.base.iri.IRI, rdflib.URIRef]



