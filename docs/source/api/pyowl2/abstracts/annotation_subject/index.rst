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

    .. figure:: /_uml/class_pyowl2_abstracts_annotation_subject_OWLAnnotationSubject.png
       :alt: UML Class Diagram for OWLAnnotationSubject
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationSubject**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_annotation_subject_OWLAnnotationSubject.pdf
       :alt: UML Class Diagram for OWLAnnotationSubject
       :align: center
       :width: 6.2cm
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationSubject**

.. py:class:: OWLAnnotationSubject

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.annotation_subject.OWLAnnotationSubject
      :parts: 1
      :private-bases:


   Represents the entity to which an annotation is applied within the Web Ontology Language (OWL) framework, acting as a polymorphic abstraction for Internationalized Resource Identifiers (IRIs), anonymous individuals, and literals. This abstract base class enforces a comparison strategy where equality and ordering are determined solely by the string representation of the subject's underlying value, rather than by object identity or type. It is designed to be subclassed by specific entity types that define the `value` attribute, ensuring consistent string conversion and hashing behavior across different annotation targets.


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the annotation subject by delegating to the string conversion of the underlying `value` attribute. This method is invoked implicitly by the `str()` built-in function and during string formatting operations, providing a direct textual representation of the entity being annotated. The behavior depends entirely on the type of the wrapped value, and no side effects occur during the conversion process.

      :return: The string representation of the object's value.

      :rtype: str



   .. py:attribute:: __slots__
      :value: ()


