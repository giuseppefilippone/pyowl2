pyowl2.axioms.data_property_axiom.disjoint_data_properties
==========================================================

.. py:module:: pyowl2.axioms.data_property_axiom.disjoint_data_properties


Classes
-------

.. autoapisummary::

   pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties


Module Contents
---------------

.. py:class:: OWLDisjointDataProperties(expressions: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom`


   An axiom stating that two or more data properties cannot have the same values for the same individual.


   .. py:method:: __str__() -> str


   .. py:property:: data_property_expressions
      :type: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


      Getter for data_property_expressions.


