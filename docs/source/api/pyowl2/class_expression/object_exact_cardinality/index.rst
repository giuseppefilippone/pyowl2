pyowl2.class_expression.object_exact_cardinality
================================================

.. py:module:: pyowl2.class_expression.object_exact_cardinality


Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality


Module Contents
---------------

.. py:class:: OWLObjectExactCardinality(value: int, property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, expression: Optional[pyowl2.abstracts.class_expression.OWLClassExpression] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`


   An object property restriction specifying that an individual must be related to exactly a certain number of instances of a given class.


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


