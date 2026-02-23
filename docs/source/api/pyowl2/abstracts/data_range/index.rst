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


   .. py:method:: __eq__(value: object) -> bool

      Determines equality between the current instance and another object by comparing their string representations. The method returns `True` if the result of converting the current instance to a string matches the result of converting the provided value to a string. This approach allows for comparison based on the textual serialization of the data range, meaning two objects are considered equal if their string forms are identical, regardless of whether they are the same object in memory or share the same type.

      :param value: The object to compare against. Equality is determined by comparing the string representations of both objects.
      :type value: object

      :return: True if the string representation of the current object is equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __ge__(value: object) -> bool

      Determines whether the current instance is greater than or equal to the specified object by comparing their string representations. This method enables the use of the greater-than-or-equal-to operator, facilitating sorting and ordering operations based on the lexical value of the objects. The comparison is case-sensitive and relies on standard lexicographical ordering, converting the provided value to a string if necessary.

      :param value: The object to compare against, converted to a string for comparison.
      :type value: object

      :return: True if the string representation of the object is greater than or equal to the string representation of the provided value.

      :rtype: bool



   .. py:method:: __gt__(value: object) -> bool

      Determines whether the current instance is considered greater than the specified value by comparing their string representations. The method converts both the instance and the provided value to strings and performs a lexicographical comparison, returning `True` if the instance's string representation is greater. This implementation allows for comparison with any object type, provided the object can be converted to a string, and does not modify the state of either operand.

      :param value: The object to compare against the current instance, where the comparison is performed on the string representations of the objects.
      :type value: object

      :return: True if the string representation of the current object is lexicographically greater than the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Computes a hash value for the instance, allowing it to be used as a key in dictionaries or stored in sets. The implementation delegates to the hash of the object's string representation, meaning the resulting integer is directly derived from the output of the `__str__` method. This ensures that objects with identical string representations produce the same hash code.

      :return: An integer hash value computed from the string representation of the object.

      :rtype: int



   .. py:method:: __le__(value: object) -> bool

      Determines whether the current instance is less than or equal to the specified value by comparing their string representations. The comparison is performed lexicographically by converting both the instance and the provided object to strings, regardless of the object's type. This behavior allows for sorting and ordering operations based on the textual representation of the data range, rather than its semantic properties.

      :param value: The object to compare against, which is converted to a string for the comparison.
      :type value: object

      :return: True if the string representation of the current object is less than or equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __lt__(value: object) -> bool

      Implements the less-than comparison operator by evaluating the lexicographical order of the string representations of the current object and the provided value. This method enables the use of the standard `<` operator for sorting or ordering instances, relying on the output of the `str()` function rather than logical equivalence or internal structure. It accepts any object type as the comparison value, converting it to a string before evaluation, and does not modify the state of the object.

      :param value: The object to compare against, evaluated based on its string representation.
      :type value: object

      :return: True if the string representation of the current instance is lexicographically less than the string representation of the provided value.

      :rtype: bool



   .. py:method:: __ne__(value: object) -> bool

      Determines inequality between the current instance and another object by comparing their string representations. This method returns `True` if the string representation of the current `OWLDataRange` differs from that of the provided value, and `False` otherwise. Because the comparison relies on string conversion, objects of differing types may be considered equal if their string representations happen to match.

      :param value: The object to compare against the current instance.
      :type value: object

      :return: True if the string representation of the current instance is not equal to the string representation of the provided value; otherwise, False.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns the official string representation of the OWL data range object. This implementation delegates the formatting logic directly to the `__str__` method, ensuring that the output used for debugging and logging mirrors the user-facing string representation. The method does not modify the state of the object and simply returns the result of the string conversion.

      :return: A string representation of the object.

      :rtype: str



   .. py:attribute:: __slots__
      :value: ()


