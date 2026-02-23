pyowl2.axioms.assertion.different_individuals
=============================================

.. py:module:: pyowl2.axioms.assertion.different_individuals



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing the OWL DifferentIndividuals axiom to assert that a specific group of individuals are mutually distinct.


Description
-----------


The software implements a logical construct used in ontology modeling to declare that a collection of entities are pairwise distinct, preventing reasoners from inferring that they are identical. By extending a base assertion class, it handles metadata through optional annotations while enforcing a strict requirement that at least two entities must be provided to form a valid distinctness declaration. To ensure consistency and normalization, the implementation automatically sorts the list of entities upon initialization and modification, maintaining a canonical order regardless of how the input is supplied. String representations are generated to display the axiom type and its contents, facilitating debugging or serialization processes within the broader ontology management system.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.different_individuals.OWLDifferentIndividuals


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_assertion_different_individuals_OWLDifferentIndividuals.png
       :alt: UML Class Diagram for OWLDifferentIndividuals
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDifferentIndividuals**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_assertion_different_individuals_OWLDifferentIndividuals.pdf
       :alt: UML Class Diagram for OWLDifferentIndividuals
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDifferentIndividuals**

.. py:class:: OWLDifferentIndividuals(individuals: list[pyowl2.abstracts.individual.OWLIndividual], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.assertion.different_individuals.OWLDifferentIndividuals
      :parts: 1
      :private-bases:


   This axiom asserts that a specific group of individuals within an ontology are mutually distinct, ensuring that no two individuals in the set refer to the same entity. It is utilized to enforce uniqueness constraints across the domain of discourse, preventing logical reasoners from inferring that these individuals are identical. To construct this object, a list of at least two `OWLIndividual` instances must be provided, along with an optional list of annotations for metadata. The implementation automatically sorts the provided individuals to maintain a canonical representation and raises an error if fewer than two individuals are supplied.

   :parm individuals: A sorted list of at least two individuals declared to be mutually distinct, maintained in canonical order to ensure consistency.
   :type individuals: list[OWLIndividual]


   .. py:method:: __str__() -> str

      Returns a string representation of the OWL DifferentIndividuals axiom, formatted to display the axiom type, annotations, and associated individuals. The output begins with "DifferentIndividuals(" followed by the axiom annotations if they exist, or an empty list "[]" if they are absent. The string representations of the individuals are then appended, separated by spaces. This method does not modify the object's state.

      :return: A string representation of the axiom, including any annotations and the list of individuals.

      :rtype: str



   .. py:attribute:: _individuals
      :type:  list[pyowl2.abstracts.individual.OWLIndividual]


   .. py:property:: individuals
      :type: list[pyowl2.abstracts.individual.OWLIndividual]


      Replaces the current set of individuals with the provided list of OWLIndividual objects. The input list is sorted prior to assignment to the internal attribute, ensuring a canonical ordering of the individuals within the axiom. This method is part of the OWLDifferentIndividuals class, which represents an axiom asserting that all listed individuals are pairwise distinct.

      :param value: A list of OWLIndividual objects to assign to the collection.
      :type value: list[OWLIndividual]

