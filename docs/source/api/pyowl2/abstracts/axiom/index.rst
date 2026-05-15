pyowl2.abstracts.axiom
======================

.. py:module:: pyowl2.abstracts.axiom



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class representing fundamental assertions within an ontology that manages optional metadata annotations and defines equality and ordering based on string serialization.


Description
-----------


Designed to serve as the foundational component for defining the logical structure of a knowledge base, the class provides a blueprint for creating specific types of assertions within an ontology. It supports the attachment of optional metadata through annotations, which are automatically sorted upon assignment to maintain a consistent internal state regardless of the input order. A key design characteristic is the reliance on string serialization for determining object identity, where equality, hash values, and total ordering are all derived from the textual representation of the assertion rather than direct attribute comparison. This approach ensures that instances can be reliably used in hash-based collections and sorted lists, provided the string formatting remains deterministic and consistent with the logical equivalence of the axioms.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.axiom.OWLAxiom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_abstracts_axiom_OWLAxiom.png
       :alt: UML Class Diagram for OWLAxiom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAxiom**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_axiom_OWLAxiom.pdf
       :alt: UML Class Diagram for OWLAxiom
       :align: center
       :width: 13.8cm
       :class: uml-diagram

       UML Class Diagram for **OWLAxiom**

.. py:class:: OWLAxiom(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.axiom.OWLAxiom
      :parts: 1
      :private-bases:


   This abstract base class represents a fundamental assertion or statement within an ontology, serving as the foundational component for defining the logical structure of the knowledge base. It supports the attachment of optional metadata through a list of annotations, which are automatically sorted upon assignment to maintain a consistent state. Instances of this class utilize their string representation to determine equality, hash values, and ordering, meaning that comparisons are based on the textual form of the axiom rather than object identity.

   :param axiom_annotations: Sorted list of annotations providing metadata about the axiom, or None if no annotations are present.
   :type axiom_annotations: typing.Optional[list[OWLAnnotation]]


   .. py:attribute:: _axiom_annotations
      :type:  Optional[list[pyowl2.base.annotation.OWLAnnotation]]
      :value: None



   .. py:property:: axiom_annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]


      Sets the annotations associated with the OWL axiom, overwriting any previously stored annotations. The method accepts a list of OWLAnnotation objects or None; if a non-empty list is provided, it is sorted before being assigned to the internal state to maintain a consistent order. If the input is None or an empty list, it is stored as is without sorting.

      :param value: A list of OWL annotations to assign to the axiom.
      :type value: typing.Optional[list[OWLAnnotation]]

