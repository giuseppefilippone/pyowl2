pyowl2.expressions.inverse_object_property
==========================================

.. py:module:: pyowl2.expressions.inverse_object_property


Classes
-------

.. autoapisummary::

   pyowl2.expressions.inverse_object_property.OWLInverseObjectProperty


Module Contents
---------------

.. py:class:: OWLInverseObjectProperty(property: pyowl2.expressions.object_property.OWLObjectProperty)

   Bases: :py:obj:`pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression`


   The inverse of a given object property, relating individuals in the opposite direction.


   .. py:method:: __str__() -> str


   .. py:method:: is_bottom_object_property() -> bool


   .. py:method:: is_top_object_property() -> bool


   .. py:property:: object_property
      :type: pyowl2.expressions.object_property.OWLObjectProperty


      Getter for object_property.


