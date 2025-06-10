pyowl2.expressions.data_property
================================

.. py:module:: pyowl2.expressions.data_property


Classes
-------

.. autoapisummary::

   pyowl2.expressions.data_property.OWLDataProperty


Module Contents
---------------

.. py:class:: OWLDataProperty(iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI])

   Bases: :py:obj:`pyowl2.abstracts.entity.OWLEntity`, :py:obj:`pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression`


   A property that links individuals to data values.


   .. py:method:: __str__() -> str


   .. py:method:: bottom() -> Self
      :staticmethod:



   .. py:method:: is_bottom_data_property() -> bool


   .. py:method:: is_top_data_property() -> bool


   .. py:method:: top() -> Self
      :staticmethod:



   .. py:property:: iri
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]



