pyowl2.class_expression.object_one_of
=====================================

.. py:module:: pyowl2.class_expression.object_one_of


Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_one_of.OWLObjectOneOf


Module Contents
---------------

.. py:class:: OWLObjectOneOf(individuals: list[pyowl2.abstracts.individual.OWLIndividual])

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`


   A class expression that explicitly lists a finite set of individuals as its members.


   .. py:method:: __str__() -> str


   .. py:property:: individuals
      :type: list[pyowl2.abstracts.individual.OWLIndividual]


      Getter for individuals.


