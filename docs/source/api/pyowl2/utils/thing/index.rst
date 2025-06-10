pyowl2.utils.thing
==================

.. py:module:: pyowl2.utils.thing


Classes
-------

.. autoapisummary::

   pyowl2.utils.thing.OWLFullClass


Module Contents
---------------

.. py:class:: OWLFullClass(iri: pyowl2.base.iri.IRI)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`


   Abstract class for OWL objects.


   .. py:method:: add_assertion(individual: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: all_values(object: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: exact_cardinality(cardinality: int, object_property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: has_key(object_properties: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], data_properties: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_disjoint_from(classes: Union[pyowl2.abstracts.class_expression.OWLClassExpression, list[pyowl2.abstracts.class_expression.OWLClassExpression], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_disjoint_union_from(classes: Union[pyowl2.abstracts.class_expression.OWLClassExpression, list[pyowl2.abstracts.class_expression.OWLClassExpression], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_equivalent_to(classes: Union[pyowl2.abstracts.class_expression.OWLClassExpression, list[pyowl2.abstracts.class_expression.OWLClassExpression], Self, list[Self]], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_intersection_of(classes: Union[pyowl2.abstracts.class_expression.OWLClassExpression, list[pyowl2.abstracts.class_expression.OWLClassExpression], Self, list[Self]]) -> None


   .. py:method:: is_subclass_of(super_class: Union[pyowl2.abstracts.class_expression.OWLClassExpression, Self], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_superclass_of(sub_class: Union[pyowl2.abstracts.class_expression.OWLClassExpression, Self], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None) -> None


   .. py:method:: is_union_of(classes: Union[pyowl2.abstracts.class_expression.OWLClassExpression, list[pyowl2.abstracts.class_expression.OWLClassExpression], Self, list[Self]]) -> None


   .. py:method:: max_cardinality(cardinality: int, object_property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: min_cardinality(cardinality: int, object_property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: nothing() -> Self
      :staticmethod:



   .. py:method:: some_values(object: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: thing() -> Self
      :staticmethod:



   .. py:method:: to_complement() -> None


   .. py:property:: all_axioms
      :type: list[pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom]



   .. py:property:: annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]



   .. py:property:: assertions
      :type: list[pyowl2.axioms.assertion.class_assertion.OWLClassAssertion]



   .. py:property:: axioms
      :type: list[Any]



   .. py:property:: class_
      :type: pyowl2.base.owl_class.OWLClass



   .. py:property:: disjoint_classes
      :type: list[pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses]



   .. py:property:: disjoint_union_classes
      :type: list[pyowl2.axioms.class_axiom.disjoint_union.OWLDisjointUnion]



   .. py:property:: equivalent_classes
      :type: list[pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses]



   .. py:property:: exact_axioms
      :type: list[pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality]



   .. py:property:: has_key_axioms
      :type: list[pyowl2.axioms.has_key.OWLHasKey]



   .. py:property:: intersections
      :type: list[pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf]



   .. py:property:: is_complement
      :type: bool



   .. py:property:: max_axioms
      :type: list[pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality]



   .. py:property:: min_axioms
      :type: list[pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality]



   .. py:property:: some_axioms
      :type: list[pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom]



   .. py:property:: subclasses
      :type: list[pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf]



   .. py:property:: superclasses
      :type: list[pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf]



   .. py:property:: unions
      :type: list[pyowl2.class_expression.object_one_of.OWLObjectOneOf]



