pyowl2.class_expression.data_has_value
======================================

.. py:module:: pyowl2.class_expression.data_has_value


Classes
-------

.. autoapisummary::

   pyowl2.class_expression.data_has_value.OWLDataHasValue


Module Contents
---------------

.. py:class:: OWLDataHasValue(expression: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, literal: pyowl2.literal.literal.OWLLiteral)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`


   A data property restriction specifying that a particular data property must have at least one specific value.


   .. py:method:: __str__() -> str


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Getter for data_property_expression.


   .. py:property:: literal
      :type: pyowl2.literal.literal.OWLLiteral


      Getter for literal.


