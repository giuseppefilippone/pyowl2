pyowl2.axioms.annotations.annotation_assertion
==============================================

.. py:module:: pyowl2.axioms.annotations.annotation_assertion


Classes
-------

.. autoapisummary::

   pyowl2.axioms.annotations.annotation_assertion.OWLAnnotationAssertion


Module Contents
---------------

.. py:class:: OWLAnnotationAssertion(subject: pyowl2.abstracts.annotation_subject.OWLAnnotationSubject, property: pyowl2.base.annotation_property.OWLAnnotationProperty, value: pyowl2.abstracts.annotation_value.OWLAnnotationValue, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom`


   An axiom stating that a specific annotation property has a particular value for a given IRI, anonymous individual, or literal.


   .. py:method:: __str__() -> str


   .. py:property:: annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Getter for annotation_property.


   .. py:property:: annotation_subject
      :type: pyowl2.abstracts.annotation_subject.OWLAnnotationSubject


      Getter for annotation_subject.


   .. py:property:: annotation_value
      :type: pyowl2.abstracts.annotation_value.OWLAnnotationValue


      Getter for annotation_value.


