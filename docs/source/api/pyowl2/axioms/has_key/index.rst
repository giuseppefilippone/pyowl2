pyowl2.axioms.has_key
=====================

.. py:module:: pyowl2.axioms.has_key


Classes
-------

.. autoapisummary::

   pyowl2.axioms.has_key.OWLHasKey


Module Contents
---------------

.. py:class:: OWLHasKey(expression: pyowl2.abstracts.class_expression.OWLClassExpression, object_properties: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], data_properties: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_axiom.OWLClassAxiom`


   An axiom specifying a set of properties that uniquely identify instances of a particular class.


   .. py:method:: __str__() -> str


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Getter for class_expression.


   .. py:property:: data_property_expressions
      :type: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


      Getter for data_property_expressions.


   .. py:property:: object_property_expressions
      :type: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


      Getter for object_property_expressions.


