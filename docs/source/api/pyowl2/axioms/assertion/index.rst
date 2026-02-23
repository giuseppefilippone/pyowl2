pyowl2.axioms.assertion
=======================

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_assertion.png
       :alt: UML Class Diagram for pyowl2.axioms.assertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.axioms.assertion**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_assertion.pdf
       :alt: UML Class Diagram for pyowl2.axioms.assertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.axioms.assertion**

.. py:module:: pyowl2.axioms.assertion



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a suite of Python classes that model specific Web Ontology Language (OWL) assertion axioms for defining relationships and properties within an ontology.


Description
-----------


These components model a variety of logical statements found in the Web Ontology Language (OWL), including declarations of class membership, property relationships between individuals, and constraints regarding identity or distinctness. By inheriting from a shared base class, the implementation ensures a consistent architecture that supports the attachment of optional metadata annotations across all assertion types. The design handles both positive and negative assertions, allowing for the precise definition of data and object property values, while also enforcing validation rules such as requiring a minimum number of entities for identity declarations. Internal state is managed through properties that enable dynamic modification of individuals, expressions, and values, while string representation methods provide functional syntax output to facilitate serialization and debugging.


Modules
-------


* [``pyowl2.axioms.assertion.class_assertion``] — Defines a Python class representing an OWL Class Assertion axiom that links a specific individual to a class expression within an ontology.
* [``pyowl2.axioms.assertion.data_property_assertion``] — Defines a class representing an OWL axiom that asserts a specific data property value for an individual.
* [``pyowl2.axioms.assertion.different_individuals``] — Defines a class representing the OWL DifferentIndividuals axiom to assert that a specific group of individuals are mutually distinct.
* [``pyowl2.axioms.assertion.negative_data_property_assertion``] — An implementation of an OWL negative data property assertion that formally declares a specific individual does not possess a particular literal value for a given data property.
* [``pyowl2.axioms.assertion.negative_object_property_assertion``] — Defines a Python class representing a Web Ontology Language axiom that explicitly negates a relationship between two individuals.
* [``pyowl2.axioms.assertion.object_property_assertion``] — Defines a class representing an OWL axiom that asserts a specific binary relationship between two individuals.
* [``pyowl2.axioms.assertion.same_individual``] — Models an OWL axiom asserting that a collection of named individuals are identical within the domain of discourse.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/pyowl2/axioms/assertion/class_assertion/index
   /api/pyowl2/axioms/assertion/data_property_assertion/index
   /api/pyowl2/axioms/assertion/different_individuals/index
   /api/pyowl2/axioms/assertion/negative_data_property_assertion/index
   /api/pyowl2/axioms/assertion/negative_object_property_assertion/index
   /api/pyowl2/axioms/assertion/object_property_assertion/index
   /api/pyowl2/axioms/assertion/same_individual/index

