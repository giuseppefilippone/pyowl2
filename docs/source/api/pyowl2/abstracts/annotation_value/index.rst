pyowl2.abstracts.annotation_value
=================================

.. py:module:: pyowl2.abstracts.annotation_value



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class representing values assigned to annotation properties in the Web Ontology Language, enforcing string-based comparison and hashing.


Description
-----------


Acting as a foundational component for handling annotation data within the ontology framework, the class provides a unified type for diverse value representations such as anonymous individuals, IRIs, and literals. A central design aspect involves overriding standard Python comparison and hashing dunder methods to base all logical equivalence and ordering operations on the string representation of the object. By delegating equality checks and hash generation to the string output, the implementation ensures that two distinct objects are considered identical if their textual forms match, regardless of their specific concrete types. This approach facilitates consistent sorting and storage in hash-based collections while abstracting away the complexities of the underlying semantic structures.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.annotation_value.OWLAnnotationValue


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_abstracts_annotation_value_OWLAnnotationValue.png
       :alt: UML Class Diagram for OWLAnnotationValue
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationValue**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_annotation_value_OWLAnnotationValue.pdf
       :alt: UML Class Diagram for OWLAnnotationValue
       :align: center
       :width: 6.2cm
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationValue**

.. py:class:: OWLAnnotationValue

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.annotation_value.OWLAnnotationValue
      :parts: 1
      :private-bases:


   Represents the specific value assigned to an annotation property for a given subject in the Web Ontology Language (OWL). As an abstract base class, it defines a common interface for different types of values, which may include anonymous individuals, IRIs, or Literals. The implementation enforces that equality, ordering, and hashing are determined solely by the string representation of the object, ensuring that comparisons are based on lexical form rather than object identity.


   .. py:attribute:: __slots__
      :value: ()


