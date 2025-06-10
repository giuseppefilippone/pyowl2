pyowl2.class_expression.object_union_of
=======================================

.. py:module:: pyowl2.class_expression.object_union_of


Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_union_of.OWLObjectUnionOf


Module Contents
---------------

.. py:class:: OWLObjectUnionOf(expressions: list[pyowl2.abstracts.class_expression.OWLClassExpression])

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`


   A class expression representing the union of multiple classes, containing individuals that belong to at least one of the given classes.


   .. py:method:: __str__() -> str


   .. py:property:: classes_expressions
      :type: list[pyowl2.abstracts.class_expression.OWLClassExpression]


      Getter for classes_expressions.


