pyowl2.axioms.object_property_axiom.transitive_object_property
==============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.transitive_object_property


Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty


Module Contents
---------------

.. py:class:: OWLTransitiveObjectProperty(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`


   An axiom stating that if an object property relates A to B and B to C, then it must also relate A to C.


   .. py:method:: __str__() -> str


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for object_property_expression.


