pyowl2.axioms.annotations.sub_annotation_property_of
====================================================

.. py:module:: pyowl2.axioms.annotations.sub_annotation_property_of


Classes
-------

.. autoapisummary::

   pyowl2.axioms.annotations.sub_annotation_property_of.OWLSubAnnotationPropertyOf


Module Contents
---------------

.. py:class:: OWLSubAnnotationPropertyOf(sub_property: pyowl2.base.annotation_property.OWLAnnotationProperty, super_property: pyowl2.base.annotation_property.OWLAnnotationProperty, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom`


   An axiom stating that one annotation property is a subproperty of another annotation property.


   .. py:method:: __str__() -> str


   .. py:property:: sub_annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Getter for sub_annotation_property.


   .. py:property:: super_annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Getter for super_annotation_property.


