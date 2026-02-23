pyowl2.abstracts.assertion
==========================

.. py:module:: pyowl2.abstracts.assertion



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an abstract base class for axioms that assert specific facts about individuals within an ontology.


Description
-----------


It extends the general concept of an OWL axiom to specifically handle assertions, which are statements about properties or class memberships of specific entities. By utilizing Python's Abstract Base Class module, the implementation enforces a strict interface that concrete subclasses must follow, ensuring consistency across different types of factual statements. This structure allows the system to categorize and process logical claims regarding individual entities, such as object property assertions or class assertions, without allowing direct instantiation of the abstract type itself. The inclusion of an empty ``__slots__`` tuple suggests a design choice favoring memory efficiency and preventing the addition of arbitrary attributes, maintaining a rigid schema for ontological data representation.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.assertion.OWLAssertion


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_abstracts_assertion_OWLAssertion.png
       :alt: UML Class Diagram for OWLAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAssertion**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_assertion_OWLAssertion.pdf
       :alt: UML Class Diagram for OWLAssertion
       :align: center
       :width: 13.8cm
       :class: uml-diagram

       UML Class Diagram for **OWLAssertion**

.. py:class:: OWLAssertion(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.axiom.OWLAxiom`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.assertion.OWLAssertion
      :parts: 1
      :private-bases:


   Represents an abstract base class for axioms that assert specific facts about individuals within an ontology. This class serves as a common interface for statements that declare an individual's membership in a class or its relationships with other individuals via object or data properties. As an abstract type, it is not instantiated directly; rather, it provides the foundational structure for concrete assertion implementations used to build and query ontological knowledge.


   .. py:attribute:: __slots__
      :value: ()


