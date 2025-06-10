pyowl2.axioms.class_axiom.sub_class_of
======================================

.. py:module:: pyowl2.axioms.class_axiom.sub_class_of


Classes
-------

.. autoapisummary::

   pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf


Module Contents
---------------

.. py:class:: OWLSubClassOf(sub_class: pyowl2.abstracts.class_expression.OWLClassExpression, super_class: pyowl2.abstracts.class_expression.OWLClassExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_axiom.OWLClassAxiom`


   An axiom stating that one class is a subclass of another, meaning all instances of the subclass are also instances of the superclass.


   .. py:method:: __str__() -> str


   .. py:property:: sub_class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Getter for sub_class_expression.


   .. py:property:: super_class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Getter for super_class_expression.


