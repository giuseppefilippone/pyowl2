pyowl2.axioms.object_property_axiom.disjoint_object_properties
==============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.disjoint_object_properties


Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties


Module Contents
---------------

.. py:class:: OWLDisjointObjectProperties(expressions: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`


   An axiom stating that two or more object properties cannot relate the same pair of individuals.


   .. py:method:: __str__() -> str


   .. py:property:: object_property_expressions
      :type: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


      Getter for object_property_expressions.


