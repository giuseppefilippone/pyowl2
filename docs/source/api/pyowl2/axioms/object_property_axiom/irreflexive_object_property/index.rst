pyowl2.axioms.object_property_axiom.irreflexive_object_property
===============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.irreflexive_object_property


Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty


Module Contents
---------------

.. py:class:: OWLIrreflexiveObjectProperty(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`


   An axiom stating that an object property cannot relate an individual to itself.


   .. py:method:: __str__() -> str


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Getter for object_property_expression.


