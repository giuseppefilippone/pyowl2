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

    .. figure:: /_uml/pyowl2_abstracts_class_expression_OWLClassExpression.png
       :alt: UML Class Diagram for OWLClassExpression
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLClassExpression**

.. only:: latex

    .. figure:: /_uml/pyowl2_abstracts_class_expression_OWLClassExpression.pdf
       :alt: UML Class Diagram for OWLClassExpression
       :align: center
       :width: 9.6cm
       :class: uml-diagram

       UML Class Diagram for **OWLClassExpression**

.. py:class:: OWLClassExpression

   Bases: :py:obj:`pyowl2.abstracts.property_range.OWLPropertyRange`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.class_expression.OWLClassExpression
      :parts: 1
      :private-bases:


   This abstract base class represents a class expression within the Web Ontology Language (OWL), serving as a fundamental construct for defining classes based on their relationships to other entities and properties. It acts as a common interface for various types of class descriptions, ranging from simple named classes to complex logical restrictions, and can be utilized as a range for property definitions. As an abstract class, it is intended to be subclassed rather than instantiated directly. Implementations of this class determine equality and ordering by comparing their string representations, implying that logical equivalence is evaluated based on the specific serialization format used.


   .. py:method:: __eq__(value: object) -> bool

      Determines equality by comparing the string representation of the current instance with the string representation of the provided value. This implementation allows the object to be considered equal to any other object—regardless of its type—as long as their string representations match exactly.

      :param value: The object to compare against. Equality is determined by comparing the string representation of the current instance with the string representation of the provided object.
      :type value: object

      :return: True if the string representation of the instance is equal to the string representation of the provided value, False otherwise.

      :rtype: bool



   .. py:method:: __ge__(value: object) -> bool

      Determines whether the current instance is greater than or equal to the specified object by comparing their string representations. This method enables the use of the greater-than-or-equal-to operator (`>=`) for `OWLClassExpression` objects, relying on lexicographical ordering rather than semantic meaning. It returns `True` if the string representation of the current instance is greater than or equal to that of the provided value, and `False` otherwise.

      :param value: The object to compare against, converted to a string for comparison.
      :type value: object

      :return: True if the string representation of the object is greater than or equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __gt__(value: object) -> bool

      Implements the greater-than comparison by evaluating the lexicographical order of the string representations of the current instance and the provided value. The method converts both the `OWLClassExpression` and the input argument to strings, returning `True` if the string representation of the current instance is greater than that of the argument. This comparison accepts any object type for `value` and relies on string conversion rather than the semantic meaning or internal structure of the ontology elements.

      :param value: The object to compare against, where the comparison is performed on the string representations of the two objects.
      :type value: object

      :return: True if the string representation of the current object is lexicographically greater than the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Computes the hash value for the object by hashing its string representation. This allows instances of the class to be used as keys in dictionaries and members of sets. Because the hash is derived from the string representation, any modification to the object's state that alters the output of `__str__` will result in a different hash value.

      :return: An integer hash value derived from the object's string representation.

      :rtype: int



   .. py:method:: __le__(value: object) -> bool

      Determines if the current object is less than or equal to another object based on their string representations. This method enables the use of the `<=` operator for instances of this class, performing a lexicographical comparison after converting both the current instance and the provided value to strings. It accepts any object as the comparison value, provided it can be successfully converted to a string, and returns `True` if the string representation of the current instance precedes or matches that of the value.

      :param value: The object to compare against, evaluated based on its string representation.
      :type value: object

      :return: True if the string representation of the instance is less than or equal to the string representation of the provided value, False otherwise.

      :rtype: bool



   .. py:method:: __lt__(value: object) -> bool

      Determines if the current instance is considered less than the provided value based on their string representations. This method enables the use of the less-than operator (`<`) for sorting or ordering instances of this class. The comparison is performed lexicographically by converting both the current object and the argument to strings using the built-in `str()` function. Note that this comparison relies on the textual representation of the objects rather than their semantic meaning within the ontology.

      :param value: The object to compare against, where the comparison is based on the string representations of the objects.
      :type value: object

      :return: True if the string representation of the object is lexicographically less than the string representation of the provided value.

      :rtype: bool



   .. py:method:: __ne__(value: object) -> bool

      Determines inequality between the current instance and another object by comparing their string representations. The method converts both the `OWLClassExpression` and the provided value to strings and returns `True` if they differ. This implementation relies on the specific output of the `__str__` method for comparison rather than structural or semantic equivalence, meaning two objects are considered equal only if their string representations match exactly. It accepts any object type for the comparison, provided the object can be converted to a string.

      :param value: The object to compare against. The comparison is based on the string representations of the two objects.
      :type value: object

      :return: True if the string representation of the instance is not equal to the string representation of the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns a string representation of the OWL class expression by delegating to the object's `__str__` method. This ensures that the representation used in debugging and interactive sessions matches the standard string output. The method does not modify the object's state and relies entirely on the implementation of the string conversion logic.

      :return: A string representation of the object, identical to the informal string representation.

      :rtype: str



   .. py:attribute:: __slots__
      :value: ()


