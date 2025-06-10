pyowl2.axioms.assertion.class_assertion
=======================================

.. py:module:: pyowl2.axioms.assertion.class_assertion


Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.class_assertion.OWLClassAssertion


Module Contents
---------------

.. py:class:: OWLClassAssertion(expression: pyowl2.abstracts.class_expression.OWLClassExpression, individual: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`


   An axiom stating that a specific individual is an instance of a particular class.


   .. py:method:: __str__() -> str


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Getter for class_expression.


   .. py:property:: individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Getter for individual.


