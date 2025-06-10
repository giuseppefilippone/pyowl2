pyowl2.utils.data_property
==========================

.. py:module:: pyowl2.utils.data_property


Classes
-------

.. autoapisummary::

   pyowl2.utils.data_property.OWLFullDataProperty


Module Contents
---------------

.. py:class:: OWLFullDataProperty(iri: pyowl2.base.iri.IRI, domain: Optional[pyowl2.abstracts.class_expression.OWLClassExpression] = None, range: Optional[pyowl2.abstracts.data_range.OWLDataRange] = None, is_functional: bool = False)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`


   Abstract class for OWL objects.


   .. py:method:: add_assertion(individual: pyowl2.abstracts.individual.OWLIndividual, literal: pyowl2.literal.literal.OWLLiteral, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: add_domain_annotations(annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None


   .. py:method:: add_negative_assertion(individual: pyowl2.abstracts.individual.OWLIndividual, literal: pyowl2.literal.literal.OWLLiteral, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: add_property_annotations(property_class: pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom, annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None


   .. py:method:: add_range_annotations(annotations: list[pyowl2.base.annotation.OWLAnnotation]) -> None


   .. py:method:: all(data_range: pyowl2.abstracts.data_range.OWLDataRange) -> None


   .. py:method:: del_assertion(assertion: Union[pyowl2.axioms.assertion.negative_data_property_assertion.OWLNegativeDataPropertyAssertion, pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion]) -> None


   .. py:method:: exact_cardinality(cardinality: int, data_range: pyowl2.abstracts.data_range.OWLDataRange) -> None


   .. py:method:: has_value(literal: pyowl2.literal.literal.OWLLiteral) -> None


   .. py:method:: is_disjoint_from(properties: Union[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_equivalent_to(properties: Union[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_sub_property_of(super_property: Union[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, Self], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_super_property_of(sub_property: Union[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, Self], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: max_cardinality(cardinality: int, data_range: pyowl2.abstracts.data_range.OWLDataRange) -> None


   .. py:method:: min_cardinality(cardinality: int, data_range: pyowl2.abstracts.data_range.OWLDataRange) -> None


   .. py:method:: some(data_range: pyowl2.abstracts.data_range.OWLDataRange) -> None


   .. py:attribute:: PROPERTY_CLASSES
      :type:  list[type]


   .. py:property:: all_axioms
      :type: list[pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom]



   .. py:property:: annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]



   .. py:property:: assertions
      :type: list[pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion]



   .. py:property:: axioms
      :type: list[Any]



   .. py:property:: data_property
      :type: pyowl2.expressions.data_property.OWLDataProperty



   .. py:property:: disjoint_properties
      :type: list[pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties]



   .. py:property:: domain
      :type: Optional[pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain]



   .. py:property:: equivalent_properties
      :type: list[pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties]



   .. py:property:: exact_axioms
      :type: list[pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality]



   .. py:property:: has_value_axioms
      :type: list[pyowl2.class_expression.data_has_value.OWLDataHasValue]



   .. py:property:: is_functional
      :type: bool



   .. py:property:: max_axioms
      :type: list[pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality]



   .. py:property:: min_axioms
      :type: list[pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality]



   .. py:property:: properties
      :type: list[pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom]



   .. py:property:: range
      :type: Optional[pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange]



   .. py:property:: some_axioms
      :type: list[pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom]



   .. py:property:: sub_properties
      :type: list[pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf]



   .. py:property:: super_properties
      :type: list[pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf]



