pyowl2.axioms.class_axiom.equivalent_classes
============================================

.. py:module:: pyowl2.axioms.class_axiom.equivalent_classes


Classes
-------

.. autoapisummary::

   pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses


Module Contents
---------------

.. py:class:: OWLEquivalentClasses(expressions: list[pyowl2.abstracts.class_expression.OWLClassExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_axiom.OWLClassAxiom`


   An axiom stating that two or more classes have the same set of instances.


   .. py:method:: __str__() -> str


   .. py:property:: class_expressions
      :type: list[pyowl2.abstracts.class_expression.OWLClassExpression]


      Getter for class_expressions.


