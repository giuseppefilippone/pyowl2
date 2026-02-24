pyowl2.axioms.assertion.same_individual
=======================================

.. py:module:: pyowl2.axioms.assertion.same_individual



.. ── LLM-GENERATED DESCRIPTION START ──

Models an OWL axiom asserting that a collection of named individuals are identical within the domain of discourse.


Description
-----------


The software implements a specific type of Web Ontology Language (OWL) assertion used to declare that multiple distinct entities refer to the same individual within a knowledge base. By extending the base assertion class, it integrates seamlessly into the broader ontology structure while enforcing strict validation rules to ensure logical consistency. Specifically, the implementation requires a minimum of two individuals to form a valid identity assertion and automatically sorts these entities to maintain a canonical representation regardless of input order. Additionally, the logic supports the attachment of optional metadata annotations and generates a standardized string output that adheres to functional syntax conventions for interoperability.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.same_individual.OWLSameIndividual


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_assertion_same_individual_OWLSameIndividual.png
       :alt: UML Class Diagram for OWLSameIndividual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSameIndividual**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_assertion_same_individual_OWLSameIndividual.pdf
       :alt: UML Class Diagram for OWLSameIndividual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSameIndividual**

.. py:class:: OWLSameIndividual(individuals: list[pyowl2.abstracts.individual.OWLIndividual], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.assertion.same_individual.OWLSameIndividual
      :parts: 1
      :private-bases:


   This class models an OWL axiom asserting that a collection of named individuals are identical within the domain of discourse. By declaring individuals as the same, any properties or assertions applicable to one individual can be inferred for the others. To use this class, instantiate it with a list containing at least two `OWLIndividual` objects; providing fewer than two will raise an assertion error. The class automatically sorts the provided list of individuals to maintain a canonical order, and it optionally accepts a list of annotations to attach metadata to the axiom.

   :param individuals: Sorted list of named individuals asserted to be identical.
   :type individuals: list[OWLIndividual]


   .. py:method:: __str__() -> str

      Returns a string representation of the axiom formatted in a functional syntax style. The representation begins with the keyword 'SameIndividual' followed by the axiom annotations. If the axiom contains no annotations, an empty list indicator '[]' is used in their place. The string concludes with the space-separated string representations of the individuals declared to be identical.

      :return: A string representation of the axiom in the format 'SameIndividual([annotations] individuals)'.

      :rtype: str



   .. py:attribute:: _individuals
      :type:  list[pyowl2.abstracts.individual.OWLIndividual]


   .. py:property:: individuals
      :type: list[pyowl2.abstracts.individual.OWLIndividual]


      Sets the list of individuals associated with this OWL SameIndividual axiom. The method accepts a list of `OWLIndividual` objects and assigns them to the internal storage. Notably, the input list is sorted before assignment, ensuring that the individuals are maintained in a deterministic order regardless of the sequence provided.

      :param value: The new list of OWLIndividual objects to store. The list is sorted before assignment.
      :type value: list[OWLIndividual]

