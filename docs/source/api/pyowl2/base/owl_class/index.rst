pyowl2.base.owl_class
=====================

.. py:module:: pyowl2.base.owl_class


Classes
-------

.. autoapisummary::

   pyowl2.base.owl_class.OWLClass


Module Contents
---------------

.. py:class:: OWLClass(iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI])

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`, :py:obj:`pyowl2.abstracts.entity.OWLEntity`


   A collection of individuals that share common characteristics.


   .. py:method:: __str__() -> str


   .. py:method:: is_nothing() -> bool


   .. py:method:: is_thing() -> bool


   .. py:method:: nothing() -> Self
      :staticmethod:


      Returns the OWLNothing class.



   .. py:method:: thing() -> Self
      :staticmethod:


      Returns the OWLThing class.



   .. py:property:: iri
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]



