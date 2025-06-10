pyowl2.axioms.assertion.same_individual
=======================================

.. py:module:: pyowl2.axioms.assertion.same_individual


Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.same_individual.OWLSameIndividual


Module Contents
---------------

.. py:class:: OWLSameIndividual(individuals: list[pyowl2.abstracts.individual.OWLIndividual], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`


   An axiom stating that two or more named individuals are the same.


   .. py:method:: __str__() -> str


   .. py:property:: individuals
      :type: list[pyowl2.abstracts.individual.OWLIndividual]


      Getter for Individuals.


