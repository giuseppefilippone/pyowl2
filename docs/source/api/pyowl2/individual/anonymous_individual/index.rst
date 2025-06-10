pyowl2.individual.anonymous_individual
======================================

.. py:module:: pyowl2.individual.anonymous_individual


Classes
-------

.. autoapisummary::

   pyowl2.individual.anonymous_individual.OWLAnonymousIndividual


Module Contents
---------------

.. py:class:: OWLAnonymousIndividual(node_id: rdflib.URIRef)

   Bases: :py:obj:`pyowl2.abstracts.annotation_value.OWLAnnotationValue`, :py:obj:`pyowl2.abstracts.individual.OWLIndividual`


   An individual without a globally unique identifier (IRI), typically used for unnamed entities.


   .. py:method:: __str__() -> str


   .. py:property:: node_id
      :type: rdflib.URIRef


      Getter for node_id.


