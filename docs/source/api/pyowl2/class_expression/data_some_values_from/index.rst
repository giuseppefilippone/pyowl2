pyowl2.class_expression.data_some_values_from
=============================================

.. py:module:: pyowl2.class_expression.data_some_values_from


Classes
-------

.. autoapisummary::

   pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom


Module Contents
---------------

.. py:class:: OWLDataSomeValuesFrom(expressions: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], data_range: pyowl2.abstracts.data_range.OWLDataRange = None)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`


   A data property restriction specifying that there exists at least one value for a particular data property within a specified data range.


   .. py:method:: __str__() -> str


   .. py:property:: data_property_expressions
      :type: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


      Getter for data_property_expressions.


   .. py:property:: data_range
      :type: pyowl2.abstracts.data_range.OWLDataRange


      Getter for data_range.


