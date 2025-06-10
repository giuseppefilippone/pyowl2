pyowl2.axioms.class_axiom.disjoint_union
========================================

.. py:module:: pyowl2.axioms.class_axiom.disjoint_union


Classes
-------

.. autoapisummary::

   pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion


Module Contents
---------------

.. py:class:: OWLDisjointUnion(expression: pyowl2.base.owl_class.OWLClass, expressions: list[pyowl2.abstracts.class_expression.OWLClassExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_axiom.OWLClassAxiom`


   An axiom stating that a class is equivalent to the union of several disjoint classes.


   .. py:method:: __str__() -> str


   .. py:property:: disjoint_class_expressions
      :type: list[pyowl2.abstracts.class_expression.OWLClassExpression]


      Getter for disjointc_class_expressions.


   .. py:property:: union_class
      :type: pyowl2.base.owl_class.OWLClass


      Getter for union_class.


