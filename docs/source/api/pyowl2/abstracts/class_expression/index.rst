pyowl2.abstracts.class_expression
=================================

.. py:module:: pyowl2.abstracts.class_expression



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class representing Web Ontology Language (OWL) class expressions that standardizes equality, ordering, and hashing operations based on string serialization.


Description
-----------


Designed to serve as a foundational interface within the Web Ontology Language (OWL) framework, the class defines the contract for various class descriptions, ranging from simple named classes to complex logical restrictions. By extending ``OWLPropertyRange``, it allows these expressions to function as valid ranges for property definitions, integrating seamlessly into the broader ontology structure. A core design decision involves basing object identity and ordering entirely on string serialization, meaning that equality checks, sorting mechanisms, and hash generation all delegate to the specific string representation of the expression. This approach ensures that two distinct instances are treated as equivalent if their serialized forms match, effectively decoupling logical comparison from internal structural analysis and relying instead on the output of the string conversion method.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.class_expression.OWLClassExpression


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_abstracts_class_expression_OWLClassExpression.png
       :alt: UML Class Diagram for OWLClassExpression
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLClassExpression**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_class_expression_OWLClassExpression.pdf
       :alt: UML Class Diagram for OWLClassExpression
       :align: center
       :width: 6.2cm
       :class: uml-diagram

       UML Class Diagram for **OWLClassExpression**

.. py:class:: OWLClassExpression

   Bases: :py:obj:`pyowl2.abstracts.property_range.OWLPropertyRange`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.class_expression.OWLClassExpression
      :parts: 1
      :private-bases:


   This abstract base class represents a class expression within the Web Ontology Language (OWL), serving as a fundamental construct for defining classes based on their relationships to other entities and properties. It acts as a common interface for various types of class descriptions, ranging from simple named classes to complex logical restrictions, and can be utilized as a range for property definitions. As an abstract class, it is intended to be subclassed rather than instantiated directly. Implementations of this class determine equality and ordering by comparing their string representations, implying that logical equivalence is evaluated based on the specific serialization format used.


   .. py:attribute:: __slots__
      :value: ()


