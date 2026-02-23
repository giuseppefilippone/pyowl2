pyowl2.abstracts.entity
=======================

.. py:module:: pyowl2.abstracts.entity



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an abstract base class for named OWL ontology elements where identity, ordering, and hashing are derived strictly from string representations.


Description
-----------


The class serves as a structural ancestor for various components within an OWL ontology, such as classes, object properties, and individuals, ensuring they share a common interface and cannot be instantiated directly. A central design choice dictates that the identity and ordering of these components are determined exclusively by their string representations rather than internal object references or semantic properties. By implementing comparison and hashing operations that delegate to the string form of the object, the implementation ensures that entities with identical textual identifiers are treated as indistinguishable for storage in collections like sets and dictionaries. This approach simplifies the handling of ontology elements by standardizing how they are compared and sorted, relying on lexicographical ordering of their string outputs to drive all relational logic.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.entity.OWLEntity


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_abstracts_entity_OWLEntity.png
       :alt: UML Class Diagram for OWLEntity
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLEntity**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_entity_OWLEntity.pdf
       :alt: UML Class Diagram for OWLEntity
       :align: center
       :width: 6.2cm
       :class: uml-diagram

       UML Class Diagram for **OWLEntity**

.. py:class:: OWLEntity

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.entity.OWLEntity
      :parts: 1
      :private-bases:


   This abstract base class serves as the foundational representation for named elements within an OWL ontology, such as classes, object properties, and individuals. It is designed to be subclassed rather than instantiated directly, providing a common structural ancestor for all distinct ontology components. The class implements comparison and hashing logic that relies entirely on the string representation of the entity; therefore, equality, ordering, and hash values are determined by comparing the string forms of the objects. This behavior ensures that entities with identical string identifiers are treated as indistinguishable for the purposes of sorting and storage in collections like sets and dictionaries.


   .. py:method:: __eq__(value: object) -> bool

      Determines equality between the current entity and another object by comparing their string representations. The method returns true if the string representation of the current instance is identical to the string representation of the provided value. This approach allows the entity to be considered equal to objects of different types, provided their string outputs match.

      :param value: The object to compare against, where equality is determined by comparing the string representations of the current instance and this value.
      :type value: object

      :return: True if the string representation of the instance equals the string representation of the provided value, False otherwise.

      :rtype: bool



   .. py:method:: __ge__(value: object) -> bool

      Determines if the current entity is greater than or equal to the specified object by comparing their string representations. This method converts both the entity and the provided value to strings using the built-in `str()` function and performs a lexicographical comparison. It allows for sorting operations involving `OWLEntity` instances, though the ordering is strictly defined by the textual output rather than semantic properties or internal identifiers.

      :param value: The object to compare against, converted to a string for the comparison.
      :type value: object

      :return: True if the string representation of the instance is greater than or equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __gt__(value: object) -> bool

      Determines if the current entity is considered greater than the specified value based on their string representations. The comparison is performed lexicographically by converting both the entity and the provided object to strings. This allows the entity to be compared against other objects using the standard greater-than operator, relying on the output of their `__str__` methods for the ordering logic.

      :param value: The object to compare against, where the comparison is performed based on the string representation of the object.
      :type value: object

      :return: True if the string representation of the current instance is greater than the string representation of the provided value.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Computes the hash value for the entity by hashing its string representation. This allows the object to be used as a key in dictionaries or as a member of sets, provided that the string representation remains consistent throughout the object's lifetime. The method delegates the calculation to the built-in hash function applied to the result of the entity's `__str__` method.

      :return: An integer hash value derived from the object's string representation.

      :rtype: int



   .. py:method:: __le__(value: object) -> bool

      Determines if the current entity is less than or equal to a specified value by comparing their string representations. This implementation enables the use of the `<=` operator for ordering instances, relying on lexicographical comparison of the stringified forms of both the entity and the provided value. Consequently, the comparison logic depends entirely on the output of the `__str__` method for both operands, allowing the entity to be compared against any object that can be converted to a string.

      :param value: The object to compare against the current instance, converted to a string for comparison.
      :type value: object

      :return: True if the string representation of the object is less than or equal to the string representation of the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __lt__(value: object) -> bool

      Determines whether the current entity is considered less than a specified value by comparing their string representations. This method enables the use of the less-than operator (`<`) for sorting and ordering operations, relying on lexicographical comparison of the stringified forms of the objects. It can compare against any object that supports conversion to a string, not just other instances of the same class.

      :param value: The object to compare against. The comparison is performed based on the string representation of the provided object.
      :type value: object

      :return: True if the string representation of the object is lexicographically less than the string representation of the provided value.

      :rtype: bool



   .. py:method:: __ne__(value: object) -> bool

      Determines whether the current entity is not equal to the specified object by comparing their string representations. The method converts both the entity and the provided value to strings and returns `True` if the resulting strings differ, otherwise `False`. This implementation implies that inequality is strictly defined by the output of the `__str__` method, potentially treating objects of different types as equal if their string representations coincide.

      :param value: The object to compare against. The comparison is performed based on the string representations of the two objects.
      :type value: object

      :return: True if the string representation of the current object is not equal to the string representation of the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns the official string representation of the OWL entity, which is intended to be unambiguous and useful for debugging. This implementation delegates directly to the `__str__` method, resulting in an output that is identical to the informal string representation. Consequently, the behavior of this method is tightly coupled with the string formatting logic defined in the entity's string conversion handler.

      :return: A string representation of the object.

      :rtype: str



   .. py:attribute:: __slots__
      :value: ()


