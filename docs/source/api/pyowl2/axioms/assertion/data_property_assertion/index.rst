pyowl2.axioms.assertion.data_property_assertion
===============================================

.. py:module:: pyowl2.axioms.assertion.data_property_assertion



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing an OWL axiom that asserts a specific data property value for an individual.


Description
-----------


The class models a fundamental statement within an ontology where a subject individual is associated with a concrete data value, such as a string or number, through a defined data property expression. References to the property expression, the source individual, and the target literal are stored to ensure the relationship is fully encapsulated within a single object. By extending a base assertion class, the structure supports the attachment of optional annotations, enabling the inclusion of metadata or contextual information alongside the core logical statement. A string representation method generates a functional syntax format of the assertion, which facilitates serialization and debugging by clearly displaying the components and any associated annotations.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_assertion_data_property_assertion_OWLDataPropertyAssertion.png
       :alt: UML Class Diagram for OWLDataPropertyAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataPropertyAssertion**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_assertion_data_property_assertion_OWLDataPropertyAssertion.pdf
       :alt: UML Class Diagram for OWLDataPropertyAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataPropertyAssertion**

.. py:class:: OWLDataPropertyAssertion(expression: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, source: pyowl2.abstracts.individual.OWLIndividual, value: pyowl2.literal.literal.OWLLiteral, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.assertion.data_property_assertion.OWLDataPropertyAssertion
      :parts: 1
      :private-bases:


   This class represents a fundamental axiom used to define facts about an individual within an OWL ontology by associating it with a specific data value via a data property. It serves as a structured container linking a subject individual to a target literal—such as a number or string—through a specific property expression, enabling the representation of statements like "Alice hasAge 30". To utilize this component, one must provide the data property expression, the source individual, and the target literal during instantiation, with the option to attach annotations for further context or metadata.

   :parm data_property_expression: The data property expression that relates the source individual to the target value.
   :type data_property_expression: OWLDataPropertyExpression
   :parm source_individual: The individual that is the subject of the assertion, possessing the specific data value for the data property.
   :type source_individual: OWLIndividual
   :parm target_value: The data value to which the relationship points, such as "30" in the assertion "Alice hasAge 30".
   :type target_value: OWLLiteral


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the data property assertion axiom, formatted according to a functional syntax style. The representation includes the axiom's annotations, data property expression, source individual, and target value, enclosed within parentheses. If the axiom has no associated annotations, an empty list is displayed in their place to preserve the structural format. This method does not modify the object's state.

      :return: A string representation of the data property assertion in functional syntax format.

      :rtype: str



   .. py:attribute:: _data_property_expression
      :type:  pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


   .. py:attribute:: _source_individual
      :type:  pyowl2.abstracts.individual.OWLIndividual


   .. py:attribute:: _target_value
      :type:  pyowl2.literal.literal.OWLLiteral


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Updates the specific data property expression used in this assertion by assigning the provided value to the internal state. This setter replaces the existing `_data_property_expression` attribute with the new `OWLDataPropertyExpression` instance. The method expects the input to be a valid data property expression object, ensuring the assertion maintains a valid OWL structure.

      :param value: The OWL data property expression to assign to the object.
      :type value: OWLDataPropertyExpression


   .. py:property:: source_individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Assigns the provided individual as the source (or subject) of this data property assertion. This operation directly updates the internal state of the assertion, overwriting any existing source individual. The method expects an instance of OWLIndividual, though no runtime validation is explicitly performed to ensure the type matches the hint.

      :param value: The OWL individual to set as the source individual.
      :type value: OWLIndividual


   .. py:property:: target_value
      :type: pyowl2.literal.literal.OWLLiteral


      Updates the literal value associated with this data property assertion by assigning the provided `OWLLiteral` instance to the internal `_target_value` attribute. This setter overwrites any previously stored value, effectively modifying the assertion to reference the new data value.

      :param value: The literal to assign as the target value.
      :type value: OWLLiteral

