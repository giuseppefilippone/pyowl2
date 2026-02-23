pyowl2.abstracts.class_axiom
============================

.. py:module:: pyowl2.abstracts.class_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an abstract base class representing logical assertions specifically related to the definition and interrelation of ontology classes.


Description
-----------


Extending the general concept of an ontology axiom, this component focuses on class-level semantics to categorize logical statements that describe how concepts relate to one another. It serves as a foundational type for concrete implementations dealing with subclass hierarchies, equivalences, or disjointness, thereby distinguishing conceptual constraints from those concerning individual instances or properties. By enforcing an abstract interface, the design ensures that all derived class-specific axioms adhere to a common structural contract while allowing the broader system to filter and process these logical rules efficiently. The implementation utilizes empty ``__slots__`` to prevent dynamic attribute creation, promoting memory efficiency and enforcing a strict, predictable schema for all subclasses.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.class_axiom.OWLClassAxiom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_abstracts_class_axiom_OWLClassAxiom.png
       :alt: UML Class Diagram for OWLClassAxiom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLClassAxiom**

.. only:: latex

    .. figure:: /_uml/pyowl2_abstracts_class_axiom_OWLClassAxiom.pdf
       :alt: UML Class Diagram for OWLClassAxiom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLClassAxiom**

.. py:class:: OWLClassAxiom(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.axiom.OWLAxiom`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.class_axiom.OWLClassAxiom
      :parts: 1
      :private-bases:


   Represents a fundamental logical assertion within an ontology that specifically pertains to the definition or interrelation of classes. This abstract base class categorizes axioms that describe class-level semantics, such as declaring one class to be a subclass of another, establishing equivalence between classes, or defining disjointness. It serves as a common type for all class-specific constraints, allowing users to filter or process axioms that deal strictly with conceptual structures rather than individual instances or property characteristics.


   .. py:attribute:: __slots__
      :value: ()


