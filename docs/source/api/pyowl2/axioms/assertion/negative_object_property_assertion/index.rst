pyowl2.axioms.assertion.negative_object_property_assertion
==========================================================

.. py:module:: pyowl2.axioms.assertion.negative_object_property_assertion


Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.negative_object_property_assertion.OWLNegativeObjectPropertyAssertion


Module Contents
---------------

.. py:class:: OWLNegativeObjectPropertyAssertion(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, source: pyowl2.abstracts.individual.OWLIndividual, target: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`


   An axiom stating that a specific object property does not relate a pair of individuals.


   .. py:method:: __str__() -> str


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for object_property_expression.


   .. py:property:: source_individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Getter for source_individual.


   .. py:property:: target_individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Getter for target_individual.


