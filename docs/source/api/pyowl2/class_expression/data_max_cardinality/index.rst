pyowl2.class_expression.data_max_cardinality
============================================

.. py:module:: pyowl2.class_expression.data_max_cardinality


Classes
-------

.. autoapisummary::

   pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality


Module Contents
---------------

.. py:class:: OWLDataMaxCardinality(value: int, expression: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, data_range: Optional[pyowl2.abstracts.data_range.OWLDataRange] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`


   A data property restriction specifying the maximum number of values an individual can have for a particular data property.


   .. py:method:: __str__() -> str


   .. py:property:: cardinality
      :type: int


      Getter for non_negative_integer.


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Getter for data_property_expression.


   .. py:property:: data_range
      :type: Optional[pyowl2.abstracts.data_range.OWLDataRange]


      Getter for data_range.


   .. py:property:: is_qualified
      :type: bool



