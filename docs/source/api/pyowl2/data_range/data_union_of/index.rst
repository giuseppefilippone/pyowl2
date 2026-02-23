pyowl2.data_range.data_union_of
===============================

.. py:module:: pyowl2.data_range.data_union_of



.. ── LLM-GENERATED DESCRIPTION START ──

A logical union of multiple data ranges within an ontology that defines a set of permissible values belonging to at least one constituent range.


Description
-----------


Extending the base data range type, this implementation models the OWL union construct by combining a collection of data range objects into a single composite entity. It enforces a semantic constraint requiring at least two operands to form a valid union, ensuring the logical integrity of the expression during initialization. To maintain a canonical representation and facilitate consistent comparisons, the internal list of constituent ranges is automatically sorted upon assignment and modification. The logic also includes a string conversion method that outputs a human-readable format, listing the sorted components within a specific notation style.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.data_range.data_union_of.OWLDataUnionOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_data_range_data_union_of_OWLDataUnionOf.png
       :alt: UML Class Diagram for OWLDataUnionOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataUnionOf**

.. only:: latex

    .. figure:: /_uml/pyowl2_data_range_data_union_of_OWLDataUnionOf.pdf
       :alt: UML Class Diagram for OWLDataUnionOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataUnionOf**

.. py:class:: OWLDataUnionOf(data_ranges: list[pyowl2.abstracts.data_range.OWLDataRange])

   Bases: :py:obj:`pyowl2.abstracts.data_range.OWLDataRange`

   .. autoapi-inheritance-diagram:: pyowl2.data_range.data_union_of.OWLDataUnionOf
      :parts: 1
      :private-bases:


   This class represents a logical union of multiple data ranges within an ontology, defining a set of permissible values that belong to at least one of the constituent ranges. It extends the base data range type and is initialized with a list of `OWLDataRange` objects, requiring a minimum of two ranges to form a valid union. Upon initialization and modification, the class automatically sorts the internal list of data ranges to maintain a canonical representation, ensuring consistent behavior for comparisons and storage.

   :parm data_ranges: The sorted list of data ranges forming the union.
   :type data_ranges: list[OWLDataRange]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the data union, formatted as "DataUnionOf(...)" where the constituent data ranges are separated by spaces. This method constructs the string by converting each element in the internal collection of data ranges to its string representation and joining them. It does not modify the state of the object and relies on the string conversion logic of the contained data ranges; if the union is empty, it returns "DataUnionOf()".

      :return: A string representation of the object, formatted as 'DataUnionOf(...)' with the data ranges joined by spaces.

      :rtype: str



   .. py:attribute:: _data_ranges
      :type:  list[pyowl2.abstracts.data_range.OWLDataRange]


   .. py:property:: data_ranges
      :type: list[pyowl2.abstracts.data_range.OWLDataRange]


      Sets the list of data ranges that constitute the union. The provided list of OWLDataRange objects is sorted before being assigned to the internal state, ensuring a consistent and deterministic ordering. This operation overwrites any previously stored data ranges.

      :param value: A list of OWLDataRange objects to assign. The list will be sorted internally before storage.
      :type value: list[OWLDataRange]

