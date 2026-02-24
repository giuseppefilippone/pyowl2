pyowl2.data_range.data_one_of
=============================

.. py:module:: pyowl2.data_range.data_one_of



.. ── LLM-GENERATED DESCRIPTION START ──

An implementation of the OWL DataOneOf data range that restricts property values to an explicit, finite enumeration of sorted literals.


Description
-----------


Designed to represent a closed set of specific values within an ontology, this component restricts data membership to a finite, explicitly defined list of literals. By inheriting from the abstract ``OWLDataRange`` base, it integrates into the broader type system while enforcing that the provided collection of ``OWLLiteral`` objects is non-empty. A key design choice involves automatically sorting the internal collection of literals upon initialization and modification, which guarantees a canonical representation and simplifies comparison operations. The resulting structure supports string serialization in functional syntax, allowing the enumerated data range to be easily rendered or debugged as a human-readable expression.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.data_range.data_one_of.OWLDataOneOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_data_range_data_one_of_OWLDataOneOf.png
       :alt: UML Class Diagram for OWLDataOneOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataOneOf**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_data_range_data_one_of_OWLDataOneOf.pdf
       :alt: UML Class Diagram for OWLDataOneOf
       :align: center
       :width: 8.4cm
       :class: uml-diagram

       UML Class Diagram for **OWLDataOneOf**

.. py:class:: OWLDataOneOf(literals: list[pyowl2.literal.literal.OWLLiteral])

   Bases: :py:obj:`pyowl2.abstracts.data_range.OWLDataRange`

   .. autoapi-inheritance-diagram:: pyowl2.data_range.data_one_of.OWLDataOneOf
      :parts: 1
      :private-bases:


   This class models a data range defined by an explicit enumeration of specific literal values, effectively restricting data membership to a finite, closed set. It is utilized within ontologies to define properties that can only take on one of the pre-defined values, such as a specific set of integers or strings. Upon instantiation, the class requires a non-empty list of `OWLLiteral` objects and automatically maintains these literals in a sorted order to ensure consistency.

   :param literals: The sorted list of literal values explicitly enumerated in this data range, guaranteed to be non-empty.
   :type literals: list[OWLLiteral]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the data one-of expression using a functional syntax format. The output string begins with "DataOneOf" followed by the string representations of the literals contained within the object, joined by spaces and enclosed in parentheses. This method is typically invoked implicitly when the object is passed to the print function or converted to a string.

      :return: A string representation of the object, formatted as 'DataOneOf(...)' containing the space-separated string values of the internal literals.

      :rtype: str



   .. py:attribute:: _literals
      :type:  list[pyowl2.literal.literal.OWLLiteral]


   .. py:property:: literals
      :type: list[pyowl2.literal.literal.OWLLiteral]


      Updates the collection of literal values that define this data range by assigning the provided list of OWLLiteral objects. The method enforces a specific ordering by sorting the input list before storing it internally, which ensures a canonical representation but may alter the original sequence of the provided arguments. This operation overwrites the existing internal state and requires that all elements in the input list be comparable to avoid raising a TypeError during the sorting process.

      :param value: A list of OWL literals to be assigned to the object.
      :type value: list[OWLLiteral]

