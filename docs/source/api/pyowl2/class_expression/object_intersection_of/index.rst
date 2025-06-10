pyowl2.class_expression.object_intersection_of
==============================================

.. py:module:: pyowl2.class_expression.object_intersection_of


Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf


Module Contents
---------------

.. py:class:: OWLObjectIntersectionOf(expressions: list[pyowl2.abstracts.class_expression.OWLClassExpression])

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`


   A class expression representing the intersection of multiple classes, containing only individuals that belong to all the given classes.


   .. py:method:: __str__() -> str


   .. py:property:: classes_expressions
      :type: list[pyowl2.abstracts.class_expression.OWLClassExpression]


      Getter for classes_expressions.


