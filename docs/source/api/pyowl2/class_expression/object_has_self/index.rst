pyowl2.class_expression.object_has_self
=======================================

.. py:module:: pyowl2.class_expression.object_has_self


Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_has_self.OWLObjectHasSelf


Module Contents
---------------

.. py:class:: OWLObjectHasSelf(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`


   An object property restriction stating that an individual must be related to itself via a specific object property.


   .. py:method:: __str__() -> str


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for object_property_expression.


