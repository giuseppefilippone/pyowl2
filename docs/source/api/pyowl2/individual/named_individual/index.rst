pyowl2.individual.named_individual
==================================

.. py:module:: pyowl2.individual.named_individual


Classes
-------

.. autoapisummary::

   pyowl2.individual.named_individual.OWLNamedIndividual


Module Contents
---------------

.. py:class:: OWLNamedIndividual(iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI])

   Bases: :py:obj:`pyowl2.abstracts.individual.OWLIndividual`


   An individual that is identified by a unique IRI.


   .. py:method:: __str__() -> str


   .. py:property:: iri
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]


      Getter for iri.


