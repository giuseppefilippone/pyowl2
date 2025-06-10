pyowl2.utils.object_property
============================

.. py:module:: pyowl2.utils.object_property


Classes
-------

.. autoapisummary::

   pyowl2.utils.object_property.OWLFullObjectProperty


Module Contents
---------------

.. py:class:: OWLFullObjectProperty(iri: pyowl2.base.iri.IRI, domain: Optional[pyowl2.abstracts.class_expression.OWLClassExpression] = None, range: Optional[pyowl2.abstracts.class_expression.OWLClassExpression] = None, is_symmetric: bool = False, is_asymmetric: bool = False, is_functional: bool = False, is_inverse_functional: bool = False, is_transitive: bool = False, is_reflexive: bool = False, is_irreflexive: bool = False)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`


   Abstract class for OWL objects.


   .. py:method:: add_assertion(individual_1: pyowl2.abstracts.individual.OWLIndividual, individual_2: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: add_domain_annotations(annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None


   .. py:method:: add_negative_assertion(individual_1: pyowl2.abstracts.individual.OWLIndividual, individual_2: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: add_property_annotations(property_class: pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom, annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None


   .. py:method:: add_range_annotations(annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None


   .. py:method:: all(cls: pyowl2.abstracts.class_expression.OWLClassExpression) -> None


   .. py:method:: del_assertion(assertion: Union[pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion, pyowl2.axioms.assertion.negative_object_property_assertion.OWLNegativeObjectPropertyAssertion]) -> None


   .. py:method:: exact_cardinality(cardinality: int, cls: pyowl2.abstracts.class_expression.OWLClassExpression) -> None


   .. py:method:: has_self() -> None


   .. py:method:: has_value(individual: pyowl2.abstracts.individual.OWLIndividual) -> None


   .. py:method:: is_disjoint_from(properties: Union[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_equivalent_to(properties: Union[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_inverse_of(property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: is_sub_property_of(super_property: Union[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, Self], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_super_property_of(sub_property: Union[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, pyowl2.axioms.object_property_axiom.object_property_chain.OWLObjectPropertyChain, Self], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: max_cardinality(cardinality: int, cls: pyowl2.abstracts.class_expression.OWLClassExpression) -> None


   .. py:method:: min_cardinality(cardinality: int, cls: pyowl2.abstracts.class_expression.OWLClassExpression) -> None


   .. py:method:: some(cls: pyowl2.abstracts.class_expression.OWLClassExpression) -> None


   .. py:attribute:: PROPERTY_CLASSES
      :type:  list[type]


   .. py:property:: all_axioms
      :type: list[pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom]



   .. py:property:: annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]



   .. py:property:: assertions
      :type: list[pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion]



   .. py:property:: axioms
      :type: list[Any]



   .. py:property:: disjoint_properties
      :type: list[pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties]



   .. py:property:: domain
      :type: Optional[pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain]



   .. py:property:: equivalent_properties
      :type: list[pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties]



   .. py:property:: exact_axioms
      :type: list[pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality]



   .. py:property:: has_self_axioms
      :type: list[pyowl2.class_expression.object_has_self.OWLObjectHasSelf]



   .. py:property:: has_value_axioms
      :type: list[pyowl2.class_expression.object_has_value.OWLObjectHasValue]



   .. py:property:: inverses
      :type: list[pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties]



   .. py:property:: is_asymmetric
      :type: bool



   .. py:property:: is_functional
      :type: bool



   .. py:property:: is_inverse_functional
      :type: bool



   .. py:property:: is_irreflexive
      :type: bool



   .. py:property:: is_reflexive
      :type: bool



   .. py:property:: is_symmetric
      :type: bool



   .. py:property:: is_transitive
      :type: bool



   .. py:property:: max_axioms
      :type: list[pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality]



   .. py:property:: min_axioms
      :type: list[pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality]



   .. py:property:: object_property
      :type: pyowl2.expressions.object_property.OWLObjectProperty



   .. py:property:: properties
      :type: list[pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom]



   .. py:property:: range
      :type: Optional[pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange]



   .. py:property:: some_axioms
      :type: list[pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom]



   .. py:property:: sub_properties
      :type: list[pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]



   .. py:property:: super_properties
      :type: list[pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf]



