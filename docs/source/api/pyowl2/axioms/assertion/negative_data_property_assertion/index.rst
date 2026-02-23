pyowl2.axioms.assertion.negative_data_property_assertion
========================================================

.. py:module:: pyowl2.axioms.assertion.negative_data_property_assertion



.. ── LLM-GENERATED DESCRIPTION START ──

An implementation of an OWL negative data property assertion that formally declares a specific individual does not possess a particular literal value for a given data property.


Description
-----------


The software models a specific type of axiom used in ontology engineering to represent the absence of a relationship between an individual and a data value. By inheriting from a base assertion class, it encapsulates a source individual, a target literal value, and a data property expression to define the negation, while also supporting optional annotations for metadata. The internal state is managed through properties that allow both retrieval and modification of the core components, ensuring the assertion can be inspected or updated dynamically after instantiation. A string representation method generates a functional syntax format that includes the annotations and the structural elements of the assertion, facilitating serialization or debugging within the broader ontology framework.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.negative_data_property_assertion.OWLNegativeDataPropertyAssertion


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_assertion_negative_data_property_assertion_OWLNegativeDataPropertyAssertion.png
       :alt: UML Class Diagram for OWLNegativeDataPropertyAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLNegativeDataPropertyAssertion**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_assertion_negative_data_property_assertion_OWLNegativeDataPropertyAssertion.pdf
       :alt: UML Class Diagram for OWLNegativeDataPropertyAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLNegativeDataPropertyAssertion**

.. py:class:: OWLNegativeDataPropertyAssertion(expression: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, source: pyowl2.abstracts.individual.OWLIndividual, value: pyowl2.literal.literal.OWLLiteral, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.assertion.negative_data_property_assertion.OWLNegativeDataPropertyAssertion
      :parts: 1
      :private-bases:


   This entity models a negative assertion within an ontology, formally declaring that a specific individual is not associated with a particular literal value through a given data property. It is constructed by defining a source individual, a target data value, and the data property expression that connects them, effectively stating that the relationship does not exist. Users can optionally attach a list of annotations to the axiom to provide context or metadata. The internal components—the property, the individual, and the target value—are accessible and mutable, allowing for the assertion to be inspected or modified after creation.

   :parm data_property_expression: The data property expression that is asserted not to relate the source individual to the target value.
   :type data_property_expression: OWLDataPropertyExpression
   :parm source_individual: The individual that serves as the subject of the negative assertion, representing the entity that is asserted not to possess the specified data property value.
   :type source_individual: OWLIndividual
   :parm target_value: The concrete data value that the source individual is asserted not to possess for the given data property.
   :type target_value: OWLLiteral


   .. py:method:: __str__() -> str

      Returns a string representation of the negative data property assertion using a functional syntax format. The output string includes the axiom annotations, the data property expression, the source individual, and the target value. If the object has no associated annotations, the representation explicitly displays an empty list in the annotation position.

      :return: A string representation of the negative data property assertion in a functional syntax, including the annotations, data property expression, source individual, and target value.

      :rtype: str



   .. py:attribute:: _data_property_expression
      :type:  pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


   .. py:attribute:: _source_individual
      :type:  pyowl2.abstracts.individual.OWLIndividual


   .. py:attribute:: _target_value
      :type:  pyowl2.literal.literal.OWLLiteral


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Assigns a new data property expression to this negative data property assertion, replacing any previously held value. The method accepts an instance of OWLDataPropertyExpression, defining the specific data property that is being negated for the subject individual. This setter directly mutates the internal state of the object.

      :param value: The OWL data property expression to assign to the object.
      :type value: OWLDataPropertyExpression


   .. py:property:: source_individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Updates the subject individual associated with the negative data property assertion. This method assigns the provided OWLIndividual object to the internal state, overwriting any previously stored source individual.

      :param value: The OWL individual to assign as the source.
      :type value: OWLIndividual


   .. py:property:: target_value
      :type: pyowl2.literal.literal.OWLLiteral


      Assigns the specific literal value that is being negated by this assertion. The method accepts an OWLLiteral object representing the data value and updates the internal state to reflect this new target. This operation modifies the object in place, changing the semantic meaning of the assertion to deny that the subject individual has this specific property value.

      :param value: The OWLLiteral to assign as the target value.
      :type value: OWLLiteral

