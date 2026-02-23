pyowl2.axioms.annotations.annotation_assertion
==============================================

.. py:module:: pyowl2.axioms.annotations.annotation_assertion



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing an OWL annotation assertion axiom that links a specific subject to a property and a value to attach metadata within an ontology.


Description
-----------


The implementation models the semantic structure of an annotation assertion by creating a triple that connects a subject entity to a specific property and a corresponding value. By inheriting from a base axiom class, it manages the storage of annotations that apply to the assertion itself, separate from the assertion's content, allowing for provenance tracking or contextual metadata. Internal state is managed through properties that expose the subject, property, and value, enabling modification of these core components while maintaining the integrity of the assertion structure. A string representation method generates a functional syntax output, which facilitates debugging and serialization by displaying the assertion's components and any associated annotations in a standardized format.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.annotations.annotation_assertion.OWLAnnotationAssertion


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_annotations_annotation_assertion_OWLAnnotationAssertion.png
       :alt: UML Class Diagram for OWLAnnotationAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationAssertion**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_annotations_annotation_assertion_OWLAnnotationAssertion.pdf
       :alt: UML Class Diagram for OWLAnnotationAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationAssertion**

.. py:class:: OWLAnnotationAssertion(subject: pyowl2.abstracts.annotation_subject.OWLAnnotationSubject, property: pyowl2.base.annotation_property.OWLAnnotationProperty, value: pyowl2.abstracts.annotation_value.OWLAnnotationValue, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.annotations.annotation_assertion.OWLAnnotationAssertion
      :parts: 1
      :private-bases:


   This class represents an axiom used to attach metadata to entities within an OWL ontology by asserting that a specific annotation property holds a particular value for a given subject. It functions as a triple connecting a subject—which can be an IRI, anonymous individual, or literal—to a property and a corresponding value, effectively labeling or describing the subject. Users can instantiate this object to define relationships such as labels, comments, or custom metadata, and optionally include a list of annotations on the axiom itself to capture provenance or other contextual information.

   :parm annotation_property: The annotation property being asserted to have a specific value for the subject.
   :type annotation_property: OWLAnnotationProperty
   :parm annotation_subject: The entity being annotated, which can be an IRI, an anonymous individual, or a literal.
   :type annotation_subject: OWLAnnotationSubject
   :parm annotation_value: The specific value being asserted for the annotation property and subject, which can be an IRI, an anonymous individual, or a literal.
   :type annotation_value: OWLAnnotationValue


   .. py:method:: __str__() -> str

      Returns a string representation of the annotation assertion formatted in a functional-style syntax. The output string includes the list of annotations associated with the axiom itself, followed by the annotation property, the subject, and the value. If the axiom has no associated annotations, the representation explicitly displays an empty list in the corresponding position.

      :return: A string representation of the annotation assertion, formatted as "AnnotationAssertion(annotations property subject value)".

      :rtype: str



   .. py:attribute:: _annotation_property
      :type:  pyowl2.base.annotation_property.OWLAnnotationProperty


   .. py:attribute:: _annotation_subject
      :type:  pyowl2.abstracts.annotation_subject.OWLAnnotationSubject


   .. py:attribute:: _annotation_value
      :type:  pyowl2.abstracts.annotation_value.OWLAnnotationValue


   .. py:property:: annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Assigns the specified OWLAnnotationProperty to this assertion, replacing any existing value. This method directly modifies the internal state of the object to reflect the new annotation property. While the type hint indicates an OWLAnnotationProperty is expected, the implementation performs no runtime validation, so passing incompatible types may lead to errors elsewhere in the module.

      :param value: The OWL annotation property to assign to the object.
      :type value: OWLAnnotationProperty


   .. py:property:: annotation_subject
      :type: pyowl2.abstracts.annotation_subject.OWLAnnotationSubject


      Updates the subject of the annotation assertion to the specified value, replacing any previously assigned subject. The provided value must be an instance of OWLAnnotationSubject, representing the entity (such as an IRI or anonymous individual) to which the annotation is attached. This method directly mutates the internal state of the object.

      :param value: The IRI or anonymous individual that serves as the subject of the annotation.
      :type value: OWLAnnotationSubject


   .. py:property:: annotation_value
      :type: pyowl2.abstracts.annotation_value.OWLAnnotationValue


      Updates the value associated with this annotation assertion. It replaces the currently stored annotation value with the specified OWLAnnotationValue, effectively mutating the object's state.

      :param value: The annotation value to assign.
      :type value: OWLAnnotationValue

