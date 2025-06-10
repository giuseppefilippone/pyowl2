pyowl2.axioms.data_property_axiom.sub_data_property_of
======================================================

.. py:module:: pyowl2.axioms.data_property_axiom.sub_data_property_of


Classes
-------

.. autoapisummary::

   pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf


Module Contents
---------------

.. py:class:: OWLSubDataPropertyOf(sub_property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, super_property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom`


   An axiom stating that one data property is a subproperty of another data property.


   .. py:method:: __str__() -> str


   .. py:property:: sub_data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Getter for sub_data_property_expression.


   .. py:property:: super_data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Getter for super_data_property_expression.


