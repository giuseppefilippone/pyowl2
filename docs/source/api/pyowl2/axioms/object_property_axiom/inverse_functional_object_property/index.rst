pyowl2.axioms.object_property_axiom.inverse_functional_object_property
======================================================================

.. py:module:: pyowl2.axioms.object_property_axiom.inverse_functional_object_property


Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty


Module Contents
---------------

.. py:class:: OWLInverseFunctionalObjectProperty(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`


   An axiom stating that if two individuals are related by an object property to the same individual, they must be the same individual.


   .. py:method:: __str__() -> str


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for object_property_expression.


