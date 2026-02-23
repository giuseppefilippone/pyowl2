pyowl2.axioms.class_axiom.disjoint_union
========================================

.. py:module:: pyowl2.axioms.class_axiom.disjoint_union



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a semantic structure representing an OWL Disjoint Union axiom, where a specific class is equivalent to the union of mutually disjoint class expressions.


Description
-----------


The software models the Web Ontology Language (OWL) Disjoint Union axiom, which asserts that a designated named class is equivalent to the logical union of a collection of class expressions that are pairwise disjoint. To ensure consistency and canonical representation, the implementation automatically sorts the provided list of disjoint class expressions upon initialization and modification, regardless of the input order. Validation logic enforces that at least two class expressions are supplied to form a valid partition, preventing semantic errors where a disjoint union cannot be formed. Optional annotations can be associated with the axiom to provide metadata, and the structure includes a string representation method that outputs the axiom in standard functional syntax for debugging or serialization purposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_class_axiom_disjoint_union_OWLDisjointUnion.png
       :alt: UML Class Diagram for OWLDisjointUnion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDisjointUnion**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_class_axiom_disjoint_union_OWLDisjointUnion.pdf
       :alt: UML Class Diagram for OWLDisjointUnion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDisjointUnion**

.. py:class:: OWLDisjointUnion(expression: pyowl2.base.owl_class.OWLClass, expressions: list[pyowl2.abstracts.class_expression.OWLClassExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_axiom.OWLClassAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion
      :parts: 1
      :private-bases:


   This class represents a semantic axiom within an ontology that defines a specific class as the union of a set of mutually disjoint class expressions. It asserts that the designated union class is equivalent to the logical disjunction of the provided expressions, while simultaneously enforcing that those expressions share no common instances. Users must provide a primary class and a list of at least two class expressions to define the partition; the implementation automatically sorts these expressions to maintain a canonical internal state. Additionally, optional annotations can be attached to the axiom to provide context or metadata.

   :parm union_class: The named class declared to be equivalent to the union of the disjoint class expressions.
   :type union_class: OWLClass
   :parm disjoint_class_expressions: The list of class expressions that are declared to be disjoint, maintained in sorted order.
   :type disjoint_class_expressions: list[OWLClassExpression]


   .. py:method:: __str__() -> str

      Generates a human-readable string representation of the disjoint union axiom in a functional syntax format. The output string includes the axiom annotations, defaulting to an empty list '[]' if none are present, followed by the union class and the space-separated list of disjoint class expressions. This ensures a consistent textual format regardless of whether the axiom contains annotations.

      :return: A string representation of the disjoint union in functional syntax, including annotations, the union class, and the disjoint class expressions.

      :rtype: str



   .. py:attribute:: _disjoint_class_expressions
      :type:  list[pyowl2.abstracts.class_expression.OWLClassExpression]


   .. py:attribute:: _union_class
      :type:  pyowl2.base.owl_class.OWLClass


   .. py:property:: disjoint_class_expressions
      :type: list[pyowl2.abstracts.class_expression.OWLClassExpression]


      Assigns a new list of class expressions to the disjoint union definition. The input list is sorted internally before storage to ensure a canonical ordering, regardless of the sequence provided. This operation overwrites the existing set of expressions stored in the object.

      :param value: The OWL class expressions to set as disjoint.
      :type value: list[OWLClassExpression]


   .. py:property:: union_class
      :type: pyowl2.base.owl_class.OWLClass


      Assigns the specified `OWLClass` instance to the internal attribute representing the class defined by the disjoint union axiom. This method serves as the setter for the `union_class` property, effectively updating the subject of the axiom. It modifies the object's state in place, replacing any existing value without performing validation on the input type.

      :param value: The OWL class to assign as the union class.
      :type value: OWLClass

