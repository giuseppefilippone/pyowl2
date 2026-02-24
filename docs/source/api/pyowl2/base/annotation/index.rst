pyowl2.base.annotation
======================

.. py:module:: pyowl2.base.annotation



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a data structure for representing OWL annotations, which associate specific properties with values to attach metadata to ontology entities without affecting logical semantics.


Description
-----------


The implementation models the concept of an annotation within the Web Ontology Language, serving as a container for metadata that enriches ontology elements without altering their logical meaning. It establishes a relationship between an annotation property, which defines the type of metadata, and an annotation value, which holds the actual content such as a literal or IRI. To support complex metadata scenarios, the structure allows for recursive annotations, meaning an annotation can itself be annotated with additional context or provenance information. The design provides mutable access to these core components through properties, enabling dynamic modification of the metadata payload, while also offering string representations for debugging and logging purposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.base.annotation.OWLAnnotation


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_base_annotation_OWLAnnotation.png
       :alt: UML Class Diagram for OWLAnnotation
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotation**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_base_annotation_OWLAnnotation.pdf
       :alt: UML Class Diagram for OWLAnnotation
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotation**

.. py:class:: OWLAnnotation(property: pyowl2.base.annotation_property.OWLAnnotationProperty, value: pyowl2.abstracts.annotation_value.OWLAnnotationValue, annotations: list[Self] = None)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`

   .. autoapi-inheritance-diagram:: pyowl2.base.annotation.OWLAnnotation
      :parts: 1
      :private-bases:


   This construct represents a piece of metadata attached to an ontology, axiom, or entity that does not alter the logical semantics of the underlying model. It is defined by a specific property that characterizes the type of metadata, such as a label or comment, and a corresponding value, which may be a literal, an IRI, or an anonymous individual. Users can instantiate this class to enrich ontology elements with human-readable descriptions or provenance data, and it supports recursive annotation to provide context about the annotation itself. By separating non-logical information from the axiomatic structure, it allows for the documentation of entities without impacting automated reasoning tasks.

   :param annotation_annotations: A list of annotations associated with this annotation, providing additional metadata or context about the annotation itself.
   :type annotation_annotations: typing.Optional[list[OWLAnnotation]]
   :param annotation_property: The property that defines the relationship between the subject and the value, characterizing the specific type of metadata being asserted.
   :type annotation_property: OWLAnnotationProperty
   :param annotation_value: The specific data or content of the annotation, which can be a literal, an IRI, or an anonymous individual, serving as the value associated with the annotation property.
   :type annotation_value: OWLAnnotationValue


   .. py:method:: __repr__() -> str

      Returns a string representation of the OWLAnnotation instance, primarily intended for debugging and interactive use. This implementation delegates directly to the `__str__` method, ensuring that the output format is consistent with the standard string conversion of the object. Consequently, the representation is human-readable and mirrors the result of calling `str()` on the instance.

      :return: Returns a string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a string representation of the annotation formatted in a functional style. The output includes the list of meta-annotations, the annotation property, and the annotation value. If no meta-annotations are present, the representation explicitly displays an empty list in their place. This method is useful for debugging or logging to provide a concise summary of the annotation's structure.

      :return: A string representation of the annotation, displaying its annotations, property, and value.

      :rtype: str



   .. py:attribute:: _annotation_annotations
      :type:  Optional[list[OWLAnnotation]]
      :value: None



   .. py:attribute:: _annotation_property
      :type:  pyowl2.base.annotation_property.OWLAnnotationProperty


   .. py:attribute:: _annotation_value
      :type:  pyowl2.abstracts.annotation_value.OWLAnnotationValue


   .. py:property:: annotation_annotations
      :type: list[Self]


      Replaces the current list of annotations associated with this annotation instance with the provided list. The input value must be a list of instances of the same class, representing nested annotations. This method performs a direct assignment, meaning subsequent modifications to the input list will affect the internal state of the object.

      :param value: A list of annotation instances of the same type to assign.
      :type value: list[typing.Self]


   .. py:property:: annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Sets the annotation property for this OWLAnnotation instance to the specified value. This method accepts an object of type OWLAnnotationProperty and updates the internal state of the annotation, overwriting any previously assigned property. As a setter, it modifies the object in place and does not return a value.

      :param value: The OWL annotation property instance to assign.
      :type value: OWLAnnotationProperty


   .. py:property:: annotation_value
      :type: pyowl2.abstracts.annotation_value.OWLAnnotationValue


      Assigns a new value to the annotation, replacing the current content. The method accepts an instance of OWLAnnotationValue and updates the internal state of the object accordingly. This operation effectively changes the semantic payload of the annotation without altering its property.

      :param value: The OWL annotation value to set, which can be a literal, IRI, or anonymous individual.
      :type value: OWLAnnotationValue

