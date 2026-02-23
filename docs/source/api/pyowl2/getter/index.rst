pyowl2.getter
=============

.. only:: html

    .. figure:: /_uml/module_pyowl2_getter.png
       :alt: UML Class Diagram for pyowl2.getter
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.getter**

.. only:: latex

    .. figure:: /_uml/module_pyowl2_getter.pdf
       :alt: UML Class Diagram for pyowl2.getter
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.getter**

.. py:module:: pyowl2.getter



.. ── LLM-GENERATED DESCRIPTION START ──

An ontology processing utility that sanitizes RDF/XML graphs and transforms them into a structured OWL 2 object model.


Description
-----------


The software facilitates the manipulation and interpretation of RDF/XML ontologies by providing mechanisms to sanitize the underlying graph structure and extract semantic entities. Sanitization logic interacts directly with the triple store to strip away specific type declarations and normalize property definitions, such as converting ontology properties to annotation properties, thereby preparing the data model for further processing. Complementing this cleaning process, a parsing component utilizes SPARQL queries on an ``rdflib`` graph to retrieve OWL 2 components, ranging from simple classes to complex class expressions, and maps them to a high-level object-oriented representation. The architecture employs a caching system to ensure object consistency and separates the logic of graph querying from object construction, allowing for the efficient transformation of low-level RDF triples into a hierarchy of axioms and expressions.


Modules
-------


* [``pyowl2.getter.rdf_xml_clear``] — A utility class that sanitizes an ontology by removing specific RDF/XML type declarations and normalizing property definitions within the underlying graph.
* [``pyowl2.getter.rdf_xml_getter``] — The software implements a comprehensive parser and transformer that extracts OWL 2 entities and axioms from an RDF/XML ontology using ``owlready2`` and ``rdflib``, converting them into a structured object model.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/pyowl2/getter/rdf_xml_clear/index
   /api/pyowl2/getter/rdf_xml_getter/index

