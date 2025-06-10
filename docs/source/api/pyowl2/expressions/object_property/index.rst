pyowl2.expressions.object_property
==================================

.. py:module:: pyowl2.expressions.object_property


Classes
-------

.. autoapisummary::

   pyowl2.expressions.object_property.OWLObjectProperty


Module Contents
---------------

.. py:class:: OWLObjectProperty(iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI])

   Bases: :py:obj:`pyowl2.abstracts.entity.OWLEntity`, :py:obj:`pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression`


   A property that links individuals to other individuals.


   .. py:method:: __str__() -> str


   .. py:method:: bottom() -> Self
      :staticmethod:



   .. py:method:: is_bottom_object_property() -> bool


   .. py:method:: is_top_object_property() -> bool


   .. py:method:: top() -> Self
      :staticmethod:



   .. py:property:: iri
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]



