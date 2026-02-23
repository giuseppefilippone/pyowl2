pyowl2.class_expression
=======================

.. only:: html

    .. figure:: /_uml/module_pyowl2_class_expression.png
       :alt: UML Class Diagram for pyowl2.class_expression
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.class_expression**

.. only:: latex

    .. figure:: /_uml/module_pyowl2_class_expression.pdf
       :alt: UML Class Diagram for pyowl2.class_expression
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.class_expression**

.. py:module:: pyowl2.class_expression



.. ── LLM-GENERATED DESCRIPTION START ──

A comprehensive implementation of Web Ontology Language (OWL) class expressions that models logical restrictions, set operations, and cardinality constraints for data and object properties.


Description
-----------


The software provides a structured framework for defining and manipulating semantic constraints within an ontology, specifically targeting the Web Ontology Language (OWL) specification. It encompasses a wide range of logical constructs, including universal and existential restrictions on both data and object properties, as well as boolean set operations like intersection, union, and complement. Furthermore, the architecture supports complex cardinality constraints—minimum, maximum, and exact counts—allowing for the definition of qualified and unqualified limits on property relationships. A key design pattern involves the automatic sorting of operands and properties during initialization and modification to maintain a canonical internal state, which ensures consistent behavior for equality checks and hashing. The components expose their internal state through managed properties and generate human-readable functional syntax strings to facilitate debugging and serialization.


Modules
-------


* [``pyowl2.class_expression.data_all_values_from``] — A Python class implementation representing the OWL DataAllValuesFrom restriction, which enforces that all values of specific data properties must belong to a defined data range.
* [``pyowl2.class_expression.data_exact_cardinality``] — Implements a class representing an OWL data exact cardinality restriction that constrains individuals to possess exactly a specific number of values for a given data property.
* [``pyowl2.class_expression.data_has_value``] — Implements a Web Ontology Language (OWL) class expression that restricts individuals to those possessing a specific data property with a defined literal value.
* [``pyowl2.class_expression.data_max_cardinality``] — Defines a class representing an OWL restriction that limits the maximum number of data values an individual may possess for a specific data property.
* [``pyowl2.class_expression.data_min_cardinality``] — Defines an OWL class expression that restricts individuals to possess a minimum number of values for a specific data property, optionally constrained by a data range.
* [``pyowl2.class_expression.data_some_values_from``] — Defines a Python class representing an OWL existential restriction that requires individuals to possess specific data property values within a defined range.
* [``pyowl2.class_expression.object_all_values_from``] — Defines a Python class representing the OWL universal restriction ObjectAllValuesFrom, which constrains the range of an object property to a specific class expression.
* [``pyowl2.class_expression.object_complement_of``] — Implements the logical negation of an OWL class expression to represent concepts that do not belong to a specific class.
* [``pyowl2.class_expression.object_exact_cardinality``] — Defines a class representing an OWL object property restriction that constrains an individual to have exactly a specific number of relationships.
* [``pyowl2.class_expression.object_has_self``] — OWLObjectHasSelf models a Web Ontology Language (OWL) class expression that restricts individuals to those related to themselves via a specific object property.
* [``pyowl2.class_expression.object_has_value``] — Implements a class representing an OWL object property restriction that constrains individuals to be related to a specific named individual via a particular property.
* [``pyowl2.class_expression.object_intersection_of``] — Represents the logical intersection of multiple OWL class expressions, ensuring a canonical representation through sorting.
* [``pyowl2.class_expression.object_max_cardinality``] — Defines a Python class representing an OWL object maximum cardinality restriction, which limits the number of relationships an individual can have via a specific object property.
* [``pyowl2.class_expression.object_min_cardinality``] — Defines a Python class that models an OWL minimum cardinality restriction, requiring individuals to participate in a specific object property relationship at least a defined number of times.
* [``pyowl2.class_expression.object_one_of``] — An implementation of the OWL ObjectOneOf class expression that defines a class by explicitly enumerating a finite set of individuals.
* [``pyowl2.class_expression.object_some_values_from``] — Defines a Python class representing the OWL ObjectSomeValuesFrom existential restriction, which describes individuals connected to a specific class via an object property.
* [``pyowl2.class_expression.object_union_of``] — An implementation of the OWL object union construct that represents the logical disjunction of multiple class expressions.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/pyowl2/class_expression/data_all_values_from/index
   /api/pyowl2/class_expression/data_exact_cardinality/index
   /api/pyowl2/class_expression/data_has_value/index
   /api/pyowl2/class_expression/data_max_cardinality/index
   /api/pyowl2/class_expression/data_min_cardinality/index
   /api/pyowl2/class_expression/data_some_values_from/index
   /api/pyowl2/class_expression/object_all_values_from/index
   /api/pyowl2/class_expression/object_complement_of/index
   /api/pyowl2/class_expression/object_exact_cardinality/index
   /api/pyowl2/class_expression/object_has_self/index
   /api/pyowl2/class_expression/object_has_value/index
   /api/pyowl2/class_expression/object_intersection_of/index
   /api/pyowl2/class_expression/object_max_cardinality/index
   /api/pyowl2/class_expression/object_min_cardinality/index
   /api/pyowl2/class_expression/object_one_of/index
   /api/pyowl2/class_expression/object_some_values_from/index
   /api/pyowl2/class_expression/object_union_of/index

