pyowl2.axioms
=============

.. only:: html

    .. figure:: /_uml/pyowl2_axioms.png
       :alt: UML Class Diagram for pyowl2.axioms
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.axioms**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms.pdf
       :alt: UML Class Diagram for pyowl2.axioms
       :align: center
       :width: 9.6cm
       :class: uml-diagram

       UML Class Diagram for **pyowl2.axioms**

.. py:module:: pyowl2.axioms



.. ── LLM-GENERATED DESCRIPTION START ──

An object-oriented implementation of Web Ontology Language (OWL) axioms that models logical assertions, property constraints, and entity declarations.


Description
-----------


The software provides a comprehensive framework for representing the logical constructs of the Web Ontology Language, enabling the definition of entities, relationships, and constraints within an ontology. By extending a shared base class, the components establish a unified architecture that handles diverse axiom types ranging from class hierarchies and property characteristics to individual assertions and datatype definitions. Internal state management emphasizes mutability and consistency, with mechanisms for automatic sorting of property expressions to ensure canonical forms and support for optional metadata annotations to enrich semantic context. String representation methods are integrated throughout to generate standard functional syntax, facilitating debugging and interoperability with other semantic web tools.


Modules
-------


* [``pyowl2.axioms.datatype_definition``] — Represents an OWL axiom that defines a new datatype by equating it to a specific data range.
* [``pyowl2.axioms.declaration``] — Defines a class representing an OWL declaration axiom that formally introduces named entities into an ontology.
* [``pyowl2.axioms.general``] — Models a logical assertion within an ontology that links a subject class expression to an object class expression via a specific property.
* [``pyowl2.axioms.has_key``] — Implements the OWL HasKey axiom to define unique identifiers for class instances using a combination of object and data properties.


Sub-packages
------------


* [``pyowl2.axioms.annotations``] — A set of object-oriented models representing Web Ontology Language (OWL) axioms that define and constrain annotation properties within an ontology.
* [``pyowl2.axioms.assertion``] — Implements a suite of Python classes that model specific Web Ontology Language (OWL) assertion axioms for defining relationships and properties within an ontology.
* [``pyowl2.axioms.class_axiom``] — A software component that implements core Web Ontology Language (OWL) class axioms to define logical relationships and constraints between ontology classes.
* [``pyowl2.axioms.data_property_axiom``] — A collection of Python classes implements Web Ontology Language (OWL) axioms specifically designed to define and constrain data properties within an ontology.
* [``pyowl2.axioms.object_property_axiom``] — A collection of Python classes modeling Web Ontology Language axioms that define the characteristics, constraints, and hierarchical relationships of object properties.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/pyowl2/axioms/annotations/index
   /api/pyowl2/axioms/assertion/index
   /api/pyowl2/axioms/class_axiom/index
   /api/pyowl2/axioms/data_property_axiom/index
   /api/pyowl2/axioms/datatype_definition/index
   /api/pyowl2/axioms/declaration/index
   /api/pyowl2/axioms/general/index
   /api/pyowl2/axioms/has_key/index
   /api/pyowl2/axioms/object_property_axiom/index

