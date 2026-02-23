pyowl2.abstracts.property_range
===============================

.. py:module:: pyowl2.abstracts.property_range



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an abstract base class representing the range of an OWL property.


Description
-----------


In the context of the Web Ontology Language, the range of a property acts as a constraint that defines the specific types of values or individuals a property can associate with a given subject. By serving as a common interface, this abstraction unifies diverse entities such as class expressions and data ranges that are legally permissible to serve as a range within property axioms. It inherits from the base object class and utilizes the Abstract Base Class module to enforce a contract that ensures all concrete implementations adhere to the expected structural requirements. Consequently, specific implementations must subclass this definition to provide the necessary logic for handling property ranges, as direct instantiation is not supported.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.property_range.OWLPropertyRange


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_abstracts_property_range_OWLPropertyRange.png
       :alt: UML Class Diagram for OWLPropertyRange
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLPropertyRange**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_property_range_OWLPropertyRange.pdf
       :alt: UML Class Diagram for OWLPropertyRange
       :align: center
       :width: 4.9cm
       :class: uml-diagram

       UML Class Diagram for **OWLPropertyRange**

.. py:class:: OWLPropertyRange

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.property_range.OWLPropertyRange
      :parts: 1
      :private-bases:


   This class serves as an abstract base class representing the range of an OWL property. In the Web Ontology Language, the range of a property constrains the types of values or individuals that the property can associate with a subject. As a common interface, it unifies the various entities—such as class expressions and data ranges—that can legally serve as the range in property axioms. Because this is an abstract class, it is intended to be subclassed by specific implementations rather than instantiated directly.


   .. py:attribute:: __slots__
      :value: ()


