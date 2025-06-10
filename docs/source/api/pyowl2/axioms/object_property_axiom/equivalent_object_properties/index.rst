pyowl2.axioms.object_property_axiom.equivalent_object_properties
================================================================

.. py:module:: pyowl2.axioms.object_property_axiom.equivalent_object_properties


Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties


Module Contents
---------------

.. py:class:: OWLEquivalentObjectProperties(expressions: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`


   An axiom stating that two or more object properties have the same property extension.


   .. py:method:: __str__() -> str


   .. py:property:: object_property_expressions
      :type: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


      Getter for object_property_expression.


