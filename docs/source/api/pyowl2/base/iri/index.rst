pyowl2.base.iri
===============

.. py:module:: pyowl2.base.iri


Classes
-------

.. autoapisummary::

   pyowl2.base.iri.IRI


Module Contents
---------------

.. py:class:: IRI(namespace: rdflib.Namespace, value: Union[str, rdflib.URIRef] = '')

   Bases: :py:obj:`pyowl2.abstracts.annotation_subject.OWLAnnotationSubject`, :py:obj:`pyowl2.abstracts.annotation_value.OWLAnnotationValue`


   Internationalized Resource Identifier, a global identifier used to name entities in an ontology.


   .. py:method:: __eq__(value: object) -> bool


   .. py:method:: __ge__(value: object) -> bool


   .. py:method:: __gt__(value: object) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __le__(value: object) -> bool


   .. py:method:: __lt__(value: object) -> bool


   .. py:method:: __ne__(value: object) -> bool


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: is_owl_nothing() -> bool


   .. py:method:: is_owl_thing() -> bool


   .. py:method:: nothing_iri() -> Self
      :staticmethod:



   .. py:method:: thing_iri() -> Self
      :staticmethod:



   .. py:method:: to_uriref() -> rdflib.URIRef


   .. py:property:: namespace
      :type: rdflib.Namespace


      Getter for namespace.


   .. py:property:: value
      :type: Union[str, rdflib.URIRef]


      Getter for value.


