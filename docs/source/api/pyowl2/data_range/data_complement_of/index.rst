pyowl2.data_range.data_complement_of
====================================

.. py:module:: pyowl2.data_range.data_complement_of



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a data range expression that represents the set of all values not included in a specified nested data range.


Description
-----------


Designed for use within ontology structures, the software provides a mechanism to define complex data types through logical negation. By wrapping an existing data range, it creates a new semantic entity that encompasses every possible value except those found within the wrapped range. This functionality allows developers to construct constraints that require values to be excluded from specific sets, thereby enhancing the expressiveness of type definitions. The implementation includes property management to access or modify the nested range and a string representation method to facilitate debugging and display of the logical structure.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.data_range.data_complement_of.OWLDataComplementOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_data_range_data_complement_of_OWLDataComplementOf.png
       :alt: UML Class Diagram for OWLDataComplementOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataComplementOf**

.. only:: latex

    .. figure:: /_uml/pyowl2_data_range_data_complement_of_OWLDataComplementOf.pdf
       :alt: UML Class Diagram for OWLDataComplementOf
       :align: center
       :width: 13.4cm
       :class: uml-diagram

       UML Class Diagram for **OWLDataComplementOf**

.. py:class:: OWLDataComplementOf(data_range: pyowl2.abstracts.data_range.OWLDataRange)

   Bases: :py:obj:`pyowl2.abstracts.data_range.OWLDataRange`

   .. autoapi-inheritance-diagram:: pyowl2.data_range.data_complement_of.OWLDataComplementOf
      :parts: 1
      :private-bases:


   This class models a data range expression that defines the set of all values not contained within a specific, nested data range. It is utilized within an ontology to construct complex data type definitions through negation, allowing for the specification of constraints that require values to be excluded from a particular set or type. To use this class, instantiate it with a target `OWLDataRange` object; the resulting instance will semantically represent the complement of that provided range, effectively filtering out any values that belong to it.

   :parm data_range: The data range for which this expression represents the complement.
   :type data_range: OWLDataRange


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the data complement expression using a functional syntax format. The output string consists of the class name followed by the string representation of the encapsulated data range enclosed in parentheses. This method is primarily intended for debugging and display purposes, providing a clear textual indication of the logical structure being represented.

      :return: A string representation of the object, formatted as 'DataComplementOf({data_range})'.

      :rtype: str



   .. py:attribute:: _data_range
      :type:  pyowl2.abstracts.data_range.OWLDataRange


   .. py:property:: data_range
      :type: pyowl2.abstracts.data_range.OWLDataRange


      Updates the data range operand of this complement expression to the specified value. This method modifies the internal state of the object in place, effectively changing the definition of the complement to apply to the new data range. It accepts an instance of OWLDataRange and assigns it to the underlying private attribute, replacing any previously held value.

      :param value: The data range to assign.
      :type value: OWLDataRange

