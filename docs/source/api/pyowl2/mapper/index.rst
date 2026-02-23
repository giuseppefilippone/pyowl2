pyowl2.mapper
=============

.. only:: html

    .. figure:: /_uml/module_pyowl2_mapper.png
       :alt: UML Class Diagram for pyowl2.mapper
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.mapper**

.. only:: latex

    .. figure:: /_uml/module_pyowl2_mapper.pdf
       :alt: UML Class Diagram for pyowl2.mapper
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.mapper**

.. py:module:: pyowl2.mapper



.. ── LLM-GENERATED DESCRIPTION START ──

A utility class that translates high-level OWL ontology constructs into standard RDF triples within an RDFLib graph.


Description
-----------


High-level OWL 2 entities, axioms, and class expressions are serialized into their corresponding RDF representations to facilitate the conversion of abstract ontology models into concrete graph data. By accepting an RDFLib graph instance, the system populates it with triples generated from complex structures such as class intersections, unions, restrictions, and property characteristics. A central dispatch method inspects the type of the input object and delegates the transformation to specialized helper methods, ensuring that anonymous classes are represented as blank nodes and collections are handled correctly using RDF lists. Support for both OWL 1 and OWL 2 annotation styles is provided, utilizing reification to attach metadata to axioms when necessary.


Modules
-------


* [``pyowl2.mapper.rdf_xml_mapper``] — A utility class that translates high-level OWL ontology constructs into standard RDF triples within an RDFLib graph.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/pyowl2/mapper/rdf_xml_mapper/index

