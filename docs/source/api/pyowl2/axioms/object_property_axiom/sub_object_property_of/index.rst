pyowl2.axioms.object_property_axiom.sub_object_property_of
==========================================================

.. py:module:: pyowl2.axioms.object_property_axiom.sub_object_property_of


Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf


Module Contents
---------------

.. py:class:: OWLSubObjectPropertyOf(sub_property: Union[pyowl2.axioms.object_property_axiom.object_property_chain.OWLObjectPropertyChain, pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], super_property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`


   An axiom stating that one object property is a subproperty of another object property.


   .. py:method:: __str__() -> str


   .. py:property:: sub_object_property_expression
      :type: Union[pyowl2.axioms.object_property_axiom.object_property_chain.OWLObjectPropertyChain, pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


      Getter for sub_object_property_expression.


   .. py:property:: super_object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for super_object_property_expression.


