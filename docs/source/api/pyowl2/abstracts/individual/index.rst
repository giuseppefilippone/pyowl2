pyowl2.abstracts.individual
===========================

.. py:module:: pyowl2.abstracts.individual



.. ── LLM-GENERATED DESCRIPTION START ──

Establishes the abstract interface for named individuals in an OWL ontology.


Description
-----------


By extending ``OWLEntity`` and utilizing the Abstract Base Class framework, the code defines the fundamental characteristics of objects that represent specific members of a class in the domain of discourse. The design enforces a clear semantic distinction between the instance itself and the classes or properties that describe it, ensuring that concrete implementations adhere to the structural requirements of an OWL individual. Since direct instantiation is prevented, the class serves strictly as a contract that guides the creation of concrete entities used to assert the existence of specific objects and their relationships within an ontology model. The use of an empty ``__slots__`` tuple suggests a memory-efficient structure intended to be expanded by subclasses without adding default attributes at this level of abstraction.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.individual.OWLIndividual


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_abstracts_individual_OWLIndividual.png
       :alt: UML Class Diagram for OWLIndividual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLIndividual**

.. only:: latex

    .. figure:: /_uml/pyowl2_abstracts_individual_OWLIndividual.pdf
       :alt: UML Class Diagram for OWLIndividual
       :align: center
       :width: 9.6cm
       :class: uml-diagram

       UML Class Diagram for **OWLIndividual**

.. py:class:: OWLIndividual

   Bases: :py:obj:`pyowl2.abstracts.entity.OWLEntity`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.individual.OWLIndividual
      :parts: 1
      :private-bases:


   Represents a specific instance or member of a class within an OWL ontology, acting as the abstract base class for all named individuals. Inheriting from `OWLEntity`, it defines the semantic role of an object that exists in the domain of discourse, distinct from the classes or properties that describe it. This class should not be instantiated directly; rather, it serves as the interface for concrete implementations used to assert the existence of specific entities and their relationships within an ontology model.


   .. py:attribute:: __slots__
      :value: ()


