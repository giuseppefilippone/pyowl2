pyowl2.getter.rdf_xml_clear
===========================

.. py:module:: pyowl2.getter.rdf_xml_clear


Classes
-------

.. autoapisummary::

   pyowl2.getter.rdf_xml_clear.RDFXMLClear


Functions
---------

.. autoapisummary::

   pyowl2.getter.rdf_xml_clear.get_abbreviation
   pyowl2.getter.rdf_xml_clear.is_named_individual


Module Contents
---------------

.. py:class:: RDFXMLClear(ontology: owlready2.Ontology)

   .. py:method:: clear() -> None


   .. py:property:: graph
      :type: rdflib.Graph



   .. py:property:: namespace
      :type: rdflib.Namespace



   .. py:property:: ontology
      :type: owlready2.Ontology



   .. py:property:: world
      :type: owlready2.World



.. py:function:: get_abbreviation(iri: rdflib.URIRef) -> int

.. py:function:: is_named_individual(obj)

