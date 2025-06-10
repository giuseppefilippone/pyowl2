pyowl2.base.annotation
======================

.. py:module:: pyowl2.base.annotation


Classes
-------

.. autoapisummary::

   pyowl2.base.annotation.OWLAnnotation


Module Contents
---------------

.. py:class:: OWLAnnotation(property: pyowl2.base.annotation_property.OWLAnnotationProperty, value: pyowl2.abstracts.annotation_value.OWLAnnotationValue, annotations: list[Self] = None)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`


   A construct that provides metadata about an ontology, axiom, or individual without affecting the ontology's logical meaning.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:property:: annotation_annotations
      :type: list[Self]


      Getter for annotation_annotations.


   .. py:property:: annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Getter for annotation_property.


   .. py:property:: annotation_value
      :type: pyowl2.abstracts.annotation_value.OWLAnnotationValue


      Getter for annotation_value.


