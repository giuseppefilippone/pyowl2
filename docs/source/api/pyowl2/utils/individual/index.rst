pyowl2.utils.individual
=======================

.. py:module:: pyowl2.utils.individual


Classes
-------

.. autoapisummary::

   pyowl2.utils.individual.OWLFullIndividual


Module Contents
---------------

.. py:class:: OWLFullIndividual(iri: Union[pyowl2.base.iri.IRI, rdflib.URIRef], is_anonymous: bool = False)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`


   Abstract class for OWL objects.


   .. py:method:: add_assertion(cls: pyowl2.abstracts.class_expression.OWLClassExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: add_data_property_assertion(data_property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, value: pyowl2.literal.literal.OWLLiteral, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: add_negative_data_property_assertion(data_property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, value: pyowl2.literal.literal.OWLLiteral, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: add_negative_object_property_assertion(object_property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, target_individual: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: add_object_property_assertion(object_property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, target_individual: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_different_from(individuals: Union[pyowl2.abstracts.individual.OWLIndividual, list[pyowl2.abstracts.individual.OWLIndividual], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_one_of(individuals: list[pyowl2.abstracts.individual.OWLIndividual]) -> None


   .. py:method:: is_same_as(individuals: Union[pyowl2.abstracts.individual.OWLIndividual, list[pyowl2.abstracts.individual.OWLIndividual], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)


   .. py:property:: annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]



   .. py:property:: assertions
      :type: list[pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]



   .. py:property:: axioms
      :type: list[Any]



   .. py:property:: class_assertions
      :type: list[pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]



   .. py:property:: different_individuals
      :type: list[pyowl2.axioms.assertion.different_individuals.OWLDifferentIndividuals]



   .. py:property:: individual
      :type: pyowl2.abstracts.individual.OWLIndividual



   .. py:property:: one_of
      :type: list[pyowl2.class_expression.object_one_of.OWLObjectOneOf]



   .. py:property:: same_individuals
      :type: list[pyowl2.axioms.assertion.same_individual.OWLSameIndividual]



