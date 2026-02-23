pyowl2.axioms.annotations
=========================

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_annotations.png
       :alt: UML Class Diagram for pyowl2.axioms.annotations
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.axioms.annotations**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_annotations.pdf
       :alt: UML Class Diagram for pyowl2.axioms.annotations
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.axioms.annotations**

.. py:module:: pyowl2.axioms.annotations



.. ── LLM-GENERATED DESCRIPTION START ──

A set of object-oriented models representing Web Ontology Language (OWL) axioms that define and constrain annotation properties within an ontology.


Description
-----------


These classes model semantic structures such as linking subjects to properties, restricting domains and ranges, and establishing sub-property hierarchies to facilitate semantic inference. The architecture leverages inheritance from a common base to manage optional metadata annotations separately from the logical content of the axioms, allowing for provenance tracking and contextual information. Core components like subjects, properties, and values are encapsulated within the objects, while standardized string representation methods ensure compatibility with functional syntax for serialization and debugging. By abstracting these specific OWL constructs, the software provides a robust foundation for building and manipulating complex ontological relationships.


Modules
-------


* [``pyowl2.axioms.annotations.annotation_assertion``] — Defines a class representing an OWL annotation assertion axiom that links a specific subject to a property and a value to attach metadata within an ontology.
* [``pyowl2.axioms.annotations.annotation_property_domain``] — Defines an OWL axiom that restricts the domain of an annotation property to a specific class identified by an IRI.
* [``pyowl2.axioms.annotations.annotation_property_range``] — Implements an OWL axiom that constrains the valid range of values for a specific annotation property.
* [``pyowl2.axioms.annotations.sub_annotation_property_of``] — Implements a data structure representing the OWL SubAnnotationPropertyOf axiom, which establishes a hierarchical relationship where one annotation property is a sub-property of another.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/pyowl2/axioms/annotations/annotation_assertion/index
   /api/pyowl2/axioms/annotations/annotation_property_domain/index
   /api/pyowl2/axioms/annotations/annotation_property_range/index
   /api/pyowl2/axioms/annotations/sub_annotation_property_of/index

