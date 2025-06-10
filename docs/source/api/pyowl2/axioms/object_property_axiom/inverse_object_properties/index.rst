pyowl2.axioms.object_property_axiom.inverse_object_properties
=============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.inverse_object_properties


Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties


Module Contents
---------------

.. py:class:: OWLInverseObjectProperties(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, inverse_expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`


   An axiom stating that one object property is the inverse of another, meaning if one relates A to B, the other relates B to A.


   .. py:method:: __str__() -> str


   .. py:property:: inverse_object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for inverse_object_property_expression.


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for object_property_expression.


