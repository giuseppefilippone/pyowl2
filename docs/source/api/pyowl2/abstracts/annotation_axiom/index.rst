pyowl2.abstracts.annotation_axiom
=================================

.. py:module:: pyowl2.abstracts.annotation_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a specialized axiom class used to attach metadata and descriptive information to logical assertions within an ontology without affecting their semantic meaning.


Description
-----------


The class extends the base axiom structure to provide a mechanism for associating descriptive information, such as comments, labels, or provenance details, with specific logical assertions. By separating metadata from the core logic, it ensures that these annotations do not alter the underlying semantics of the ontology, allowing automated reasoners to ignore them while preserving the logical integrity of the system. This approach facilitates comprehensive documentation and provides necessary context for human users, enabling a richer understanding of the data structures without interfering with computational processing.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_abstracts_annotation_axiom_OWLAnnotationAxiom.png
       :alt: UML Class Diagram for OWLAnnotationAxiom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationAxiom**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_annotation_axiom_OWLAnnotationAxiom.pdf
       :alt: UML Class Diagram for OWLAnnotationAxiom
       :align: center
       :width: 13.8cm
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationAxiom**

.. py:class:: OWLAnnotationAxiom(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.axiom.OWLAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom
      :parts: 1
      :private-bases:


   Represents a logical statement within an ontology that serves as a vehicle for attaching metadata to other axioms. It allows for the association of descriptive information, such as comments, labels, or provenance details, with specific logical assertions without altering the underlying semantics. This mechanism is essential for documenting the ontology and providing context for human users, as these annotations are typically ignored by automated reasoners.


   .. py:attribute:: __slots__
      :value: ()


