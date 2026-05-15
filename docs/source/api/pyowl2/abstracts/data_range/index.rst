pyowl2.abstracts.data_range
===========================

.. py:module:: pyowl2.abstracts.data_range



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class representing sets of literal values within an ontology that enforces comparison and hashing based on string representations.


Description
-----------


Serving as a foundational component for defining value spaces in an ontology, this class establishes a contract for representing specific datatypes or logical combinations of literal values. It enforces a strict behavioral model where object identity, ordering, and hash values are derived exclusively from the string serialization of the instance rather than internal state or memory location. By delegating rich comparison operators and hashing mechanisms to the string representation, the implementation ensures that two distinct instances are treated as identical if their textual forms match. This design allows concrete subclasses to focus solely on defining the specific structure of the data range while inheriting a consistent and predictable mechanism for storage in collections and logical evaluation.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.data_range.OWLDataRange


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_abstracts_data_range_OWLDataRange.png
       :alt: UML Class Diagram for OWLDataRange
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataRange**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_data_range_OWLDataRange.pdf
       :alt: UML Class Diagram for OWLDataRange
       :align: center
       :width: 6.2cm
       :class: uml-diagram

       UML Class Diagram for **OWLDataRange**

.. py:class:: OWLDataRange

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.data_range.OWLDataRange
      :parts: 1
      :private-bases:


   This abstract base class represents a set of literal values within an ontology, typically corresponding to specific datatypes or logical combinations of datatypes. It serves as the foundational type for defining the value space of data properties, specifying what kinds of literal inputs—such as integers, strings, or restricted value sets—are permissible. Equality, ordering, and hashing for instances are determined exclusively by their string representations, meaning two objects are considered equal if their string forms match. Because this is an abstract class, it is intended to be subclassed by concrete implementations that define specific data ranges rather than instantiated directly.


   .. py:attribute:: __slots__
      :value: ()


