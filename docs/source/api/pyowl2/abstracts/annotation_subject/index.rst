pyowl2.abstracts.annotation_subject
===================================

.. py:module:: pyowl2.abstracts.annotation_subject



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an abstract base class for Web Ontology Language annotation subjects where equality and ordering are determined by string representation.


Description
-----------


Acts as a polymorphic abstraction for entities within the Web Ontology Language framework that can be the target of an annotation, such as Internationalized Resource Identifiers or anonymous individuals. The implementation enforces a specific comparison strategy where equality and ordering are determined exclusively by the string representation of the subject's underlying value rather than object identity or type. By delegating all rich comparison methods and hashing operations to this string conversion, the design ensures that instances can be consistently sorted, compared, and used within hash-based collections like sets and dictionaries. Subclasses are expected to define a specific ``value`` attribute, which acts as the source of truth for generating the textual representation used throughout these operations.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.annotation_subject.OWLAnnotationSubject


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_abstracts_annotation_subject_OWLAnnotationSubject.png
       :alt: UML Class Diagram for OWLAnnotationSubject
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationSubject**

.. only:: latex

    .. figure:: /_uml/pyowl2_abstracts_annotation_subject_OWLAnnotationSubject.pdf
       :alt: UML Class Diagram for OWLAnnotationSubject
       :align: center
       :width: 12.4cm
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationSubject**

.. py:class:: OWLAnnotationSubject

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.annotation_subject.OWLAnnotationSubject
      :parts: 1
      :private-bases:


   Represents the entity to which an annotation is applied within the Web Ontology Language (OWL) framework, acting as a polymorphic abstraction for Internationalized Resource Identifiers (IRIs), anonymous individuals, and literals. This abstract base class enforces a comparison strategy where equality and ordering are determined solely by the string representation of the subject's underlying value, rather than by object identity or type. It is designed to be subclassed by specific entity types that define the `value` attribute, ensuring consistent string conversion and hashing behavior across different annotation targets.


   .. py:method:: __eq__(value: object) -> bool

      Determines equality between the current `OWLAnnotationSubject` instance and another object by comparing their string representations. This method returns `True` if the result of converting both the subject and the provided value to strings are identical, and `False` otherwise. Consequently, it allows for comparison with objects of different types, provided their string output matches that of the subject.

      :param value: The object to compare against. Equality is determined by comparing the string representation of the current instance with the string representation of this value.
      :type value: object

      :return: True if the string representation of the instance equals the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __ge__(value: object) -> bool

      This method implements the greater-than-or-equal-to comparison operator for the annotation subject by evaluating the string representations of the current instance and the provided value. It performs a lexicographical comparison between the string representation of the current object and the string representation of the argument, returning a boolean that indicates if the current instance is greater than or equal to the other. This behavior enables sorting and ordering operations involving annotation subjects and other objects based on their stringified forms.

      :param value: The object to compare against.
      :type value: object

      :return: True if the string representation of the current object is greater than or equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __gt__(value: object) -> bool

      Determines whether the current annotation subject is considered greater than the provided value. The comparison is performed by converting both the current instance and the input value to their string representations and evaluating them lexicographically. This method returns True if the string representation of the current object is greater than that of the other object, and False otherwise, enabling sorting and ordering operations based on the textual form of the subjects.

      :param value: The object to compare against the current instance, where the comparison is performed on the string representations of the objects.
      :type value: object

      :return: True if the string representation of the object is lexicographically greater than that of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Returns the hash value of the object, allowing it to be used in sets and as dictionary keys. The implementation calculates the hash based on the string representation of the instance, ensuring that objects considered equal based on their string form will result in the same hash. This method assumes that the string representation of the object is stable and unique for distinct entities, which is critical for maintaining the integrity of hash-based collections.

      :return: An integer hash value computed from the object's string representation.

      :rtype: int



   .. py:method:: __le__(value: object) -> bool

      Determines whether the current instance is less than or equal to the specified object by comparing their string representations. The method converts both the instance and the provided value to strings and performs a lexicographical comparison to establish the ordering relationship. This allows instances of the class to be sorted or compared using the standard less-than-or-equal-to operator based on their string identifiers.

      :param value: The object to compare against, converted to a string for lexicographical comparison.
      :type value: object

      :return: True if the string representation of the instance is less than or equal to the string representation of the provided value, False otherwise.

      :rtype: bool



   .. py:method:: __lt__(value: object) -> bool

      Determines if the current instance is considered less than the specified value by comparing their string representations. The method converts both the subject and the provided object to strings and performs a lexicographical comparison to establish the ordering. This behavior enables instances to be sorted or compared based on their textual format, even when the value is not of the same type, provided it supports string conversion.

      :param value: The object to compare against, where the comparison is performed on the string representations of the instances.
      :type value: object

      :return: True if the string representation of the object is less than the string representation of the specified value.

      :rtype: bool



   .. py:method:: __ne__(value: object) -> bool

      Checks for inequality between the current instance and the provided object. The comparison is performed by evaluating whether the string representation of the current instance differs from the string representation of the value. This implementation allows the subject to be compared against any object, provided both can be successfully converted to strings.

      :param value: The object to compare against. The comparison is performed based on the string representation of the provided value.
      :type value: object

      :return: True if the string representation of the current object is not equal to the string representation of the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns a string representation of the OWL annotation subject. This implementation delegates directly to the standard string conversion method, ensuring that the official representation matches the informal string output. It is primarily intended for debugging and logging purposes.

      :return: The string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the annotation subject by delegating to the string conversion of the underlying `value` attribute. This method is invoked implicitly by the `str()` built-in function and during string formatting operations, providing a direct textual representation of the entity being annotated. The behavior depends entirely on the type of the wrapped value, and no side effects occur during the conversion process.

      :return: The string representation of the object's value.

      :rtype: str



   .. py:attribute:: __slots__
      :value: ()


