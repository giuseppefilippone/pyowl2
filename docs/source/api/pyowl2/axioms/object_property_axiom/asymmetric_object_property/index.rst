pyowl2.axioms.object_property_axiom.asymmetric_object_property
==============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.asymmetric_object_property


Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.asymmetric_object_property.OWLAsymmetricObjectProperty


Module Contents
---------------

.. py:class:: OWLAsymmetricObjectProperty(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`


   An axiom stating that if a property relates one individual to another, the inverse relation does not hold.


   .. py:method:: __str__() -> str


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for object_property_expression.


