pyowl2.data_range.data_intersection_of
======================================

.. py:module:: pyowl2.data_range.data_intersection_of



.. ── LLM-GENERATED DESCRIPTION START ──

A logical data range implementation representing the intersection of multiple constituent data ranges within an ontology.


Description
-----------


It defines a specific type of data range where valid values must belong to all provided constituent ranges, effectively narrowing down the set of acceptable data types. The implementation enforces a strict requirement that at least two data ranges are supplied during instantiation, preventing the creation of trivial or invalid intersections. To facilitate consistent comparisons and hashing, the internal list of operands is automatically sorted upon initialization and modification, ensuring a canonical representation regardless of the input order. String representation is handled via a functional syntax format that concatenates the string forms of the sorted operands, providing a clear and standardized textual output for debugging or serialization.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_data_range_data_intersection_of_OWLDataIntersectionOf.png
       :alt: UML Class Diagram for OWLDataIntersectionOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataIntersectionOf**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_data_range_data_intersection_of_OWLDataIntersectionOf.pdf
       :alt: UML Class Diagram for OWLDataIntersectionOf
       :align: center
       :width: 10.5cm
       :class: uml-diagram

       UML Class Diagram for **OWLDataIntersectionOf**

.. py:class:: OWLDataIntersectionOf(data_ranges: list[pyowl2.abstracts.data_range.OWLDataRange])

   Bases: :py:obj:`pyowl2.abstracts.data_range.OWLDataRange`

   .. autoapi-inheritance-diagram:: pyowl2.data_range.data_intersection_of.OWLDataIntersectionOf
      :parts: 1
      :private-bases:


   This class represents a logical data range formed by the intersection of multiple constituent data ranges, defining a set of values that must belong to every specified range. It serves to construct highly specific data type constraints within an ontology by combining broader definitions, ensuring that only values satisfying all conditions are considered valid. When instantiating this class, a list of at least two `OWLDataRange` objects must be provided; note that the input list is automatically sorted upon initialization and modification to enforce a canonical ordering.

   :parm data_ranges: The sorted list of data range operands that constitute the intersection, guaranteed to contain at least two elements.
   :type data_ranges: list[OWLDataRange]


   .. py:method:: __str__() -> str

      Returns a string representation of the data intersection using a functional syntax format. The resulting string begins with the class name followed by the string representations of the constituent data ranges, which are joined by spaces. This method delegates the string conversion of the individual components to their respective `__str__` implementations.

      :return: A string representation of the object, formatted as 'DataIntersectionOf(...)' containing the string representations of the data ranges.

      :rtype: str



   .. py:attribute:: _data_ranges
      :type:  list[pyowl2.abstracts.data_range.OWLDataRange]


   .. py:property:: data_ranges
      :type: list[pyowl2.abstracts.data_range.OWLDataRange]


      Updates the collection of data ranges that constitute this intersection by assigning the provided list of OWLDataRange objects. The input list is sorted before being stored in the internal state to ensure a canonical ordering of operands. This sorting behavior aids in the consistent comparison and hashing of the object.

      :param value: A list of OWL data ranges to assign. The list will be sorted internally before storage.
      :type value: list[OWLDataRange]

