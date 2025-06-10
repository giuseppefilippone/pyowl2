pyowl2.axioms.general
=====================

.. py:module:: pyowl2.axioms.general


Classes
-------

.. autoapisummary::

   pyowl2.axioms.general.OWLGeneralClassAxiom


Module Contents
---------------

.. py:class:: OWLGeneralClassAxiom(left_expression: pyowl2.abstracts.class_expression.OWLClassExpression, property: pyowl2.base.iri.IRI, right_expression: pyowl2.abstracts.class_expression.OWLClassExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.axiom.OWLAxiom`


   A fundamental statement or assertion within an ontology that contributes to its logical structure.


   .. py:method:: __str__() -> str


   .. py:property:: left_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression



   .. py:property:: property_iri
      :type: pyowl2.base.iri.IRI



   .. py:property:: right_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression



