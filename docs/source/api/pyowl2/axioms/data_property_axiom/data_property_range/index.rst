pyowl2.axioms.data_property_axiom.data_property_range
=====================================================

.. py:module:: pyowl2.axioms.data_property_axiom.data_property_range


Classes
-------

.. autoapisummary::

   pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange


Module Contents
---------------

.. py:class:: OWLDataPropertyRange(property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, data_range: pyowl2.abstracts.data_range.OWLDataRange, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.property_range.OWLPropertyRange`, :py:obj:`pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom`


   An axiom specifying the range of values that a data property can have.


   .. py:method:: __str__() -> str


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Getter for data_property_expression.


   .. py:property:: data_range
      :type: pyowl2.abstracts.data_range.OWLDataRange


      Getter for data_range.


