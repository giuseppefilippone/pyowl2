pyowl2.axioms.data_property_axiom.functional_data_property
==========================================================

.. py:module:: pyowl2.axioms.data_property_axiom.functional_data_property


Classes
-------

.. autoapisummary::

   pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty


Module Contents
---------------

.. py:class:: OWLFunctionalDataProperty(property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom`


   An axiom stating that a data property can have at most one value for each individual.


   .. py:method:: __str__() -> str


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Getter for data_property_expression.


