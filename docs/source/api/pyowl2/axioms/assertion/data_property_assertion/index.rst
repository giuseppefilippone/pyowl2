pyowl2.axioms.assertion.data_property_assertion
===============================================

.. py:module:: pyowl2.axioms.assertion.data_property_assertion


Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion


Module Contents
---------------

.. py:class:: OWLDataPropertyAssertion(expression: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, source: pyowl2.abstracts.individual.OWLIndividual, value: pyowl2.literal.literal.OWLLiteral, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`


   An axiom stating that a specific individual has a particular data value for a given data property.


   .. py:method:: __str__() -> str


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Getter for data_property_expression.


   .. py:property:: source_individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Getter for source_individual.


   .. py:property:: target_value
      :type: pyowl2.literal.literal.OWLLiteral


      Getter for target_value.


