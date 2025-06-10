pyowl2.class_expression.object_all_values_from
==============================================

.. py:module:: pyowl2.class_expression.object_all_values_from


Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom


Module Contents
---------------

.. py:class:: OWLObjectAllValuesFrom(property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, expression: pyowl2.abstracts.class_expression.OWLClassExpression)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`


   An object property restriction specifying that all values for a particular object property must be instances of a specified class.


   .. py:method:: __str__() -> str


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Getter for class_expression.


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for object_property_expression.


