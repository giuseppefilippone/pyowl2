pyowl2.axioms.data_property_axiom.data_property_domain
======================================================

.. py:module:: pyowl2.axioms.data_property_axiom.data_property_domain


Classes
-------

.. autoapisummary::

   pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain


Module Contents
---------------

.. py:class:: OWLDataPropertyDomain(property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, expression: pyowl2.abstracts.class_expression.OWLClassExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom`


   An axiom specifying the class of individuals to which a data property applies.


   .. py:method:: __str__() -> str


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Getter for class_expression.


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Getter for data_property_expression.


