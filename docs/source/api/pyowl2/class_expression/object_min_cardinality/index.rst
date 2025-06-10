pyowl2.class_expression.object_min_cardinality
==============================================

.. py:module:: pyowl2.class_expression.object_min_cardinality


Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality


Module Contents
---------------

.. py:class:: OWLObjectMinCardinality(value: int, property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, expression: Optional[pyowl2.abstracts.class_expression.OWLClassExpression] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`


   An object property restriction specifying the minimum number of individuals to which an individual must be related via a specific object property.


   .. py:method:: __str__() -> str


   .. py:property:: cardinality
      :type: int


      Getter for non_negative_integer.


   .. py:property:: class_expression
      :type: Optional[pyowl2.abstracts.class_expression.OWLClassExpression]


      Getter for class_expression.


   .. py:property:: is_qualified
      :type: bool



   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for object_property_expression.


