pyowl2.axioms.assertion.different_individuals
=============================================

.. py:module:: pyowl2.axioms.assertion.different_individuals


Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.different_individuals.OWLDifferentIndividuals


Module Contents
---------------

.. py:class:: OWLDifferentIndividuals(individuals: list[pyowl2.abstracts.individual.OWLIndividual], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`


   An axiom stating that two or more individuals are distinct from each other.


   .. py:method:: __str__() -> str


   .. py:property:: individuals
      :type: list[pyowl2.abstracts.individual.OWLIndividual]


      Getter for individuals.


