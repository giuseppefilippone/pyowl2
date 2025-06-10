pyowl2.axioms.object_property_axiom.object_property_domain
==========================================================

.. py:module:: pyowl2.axioms.object_property_axiom.object_property_domain


Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain


Module Contents
---------------

.. py:class:: OWLObjectPropertyDomain(property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, expression: pyowl2.abstracts.class_expression.OWLClassExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`


   An axiom specifying the class of individuals to which an object property applies.


   .. py:method:: __str__() -> str


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Getter for class_expression.


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for object_property_expression.


