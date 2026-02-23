pyowl2.axioms.assertion.negative_object_property_assertion
==========================================================

.. py:module:: pyowl2.axioms.assertion.negative_object_property_assertion



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a Python class representing a Web Ontology Language axiom that explicitly negates a relationship between two individuals.


Description
-----------


The implementation centers on the ``OWLNegativeObjectPropertyAssertion`` class, which models the logical construct of stating that a specific object property does not hold between a source individual and a target individual. By inheriting from a base assertion class, it integrates into a broader ontology framework while encapsulating the specific components required to define a negative relationship, namely the property expression and the two involved individuals. Access to these components is managed through properties that allow for both retrieval and modification, ensuring the internal state remains consistent with the logical constraints of the ontology. Additionally, the class supports the attachment of optional annotations to provide metadata, and it overrides the string conversion method to generate a functional syntax representation that clearly displays the negated relationship and any associated metadata.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.negative_object_property_assertion.OWLNegativeObjectPropertyAssertion


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_assertion_negative_object_property_assertion_OWLNegativeObjectPropertyAssertion.png
       :alt: UML Class Diagram for OWLNegativeObjectPropertyAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLNegativeObjectPropertyAssertion**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_assertion_negative_object_property_assertion_OWLNegativeObjectPropertyAssertion.pdf
       :alt: UML Class Diagram for OWLNegativeObjectPropertyAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLNegativeObjectPropertyAssertion**

.. py:class:: OWLNegativeObjectPropertyAssertion(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, source: pyowl2.abstracts.individual.OWLIndividual, target: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.assertion.negative_object_property_assertion.OWLNegativeObjectPropertyAssertion
      :parts: 1
      :private-bases:


   This class represents an axiom in the Web Ontology Language (OWL) that explicitly negates a relationship between two specific individuals. It is used to assert that a given object property expression does not link a source individual to a target individual, allowing for the precise definition of what is false within an ontology. Users can instantiate this class by providing the property to be negated, the subject and object individuals, and an optional list of annotations to attach metadata to the assertion.

   :parm object_property_expression: The object property expression that is asserted not to hold between the source and target individuals.
   :type object_property_expression: OWLObjectPropertyExpression
   :parm source_individual: The individual from which the relationship is asserted not to originate.
   :type source_individual: OWLIndividual
   :parm target_individual: The individual to which the relationship is asserted not to point.
   :type target_individual: OWLIndividual


   .. py:method:: __str__() -> str

      Returns a string representation of the negative object property assertion using a functional syntax format. The output includes the axiom type, the list of annotations (represented as an empty list if none are present), the object property expression, the source individual, and the target individual. This ensures a consistent textual format that explicitly indicates the presence or absence of annotations.

      :return: A string representation of the negative object property assertion in functional syntax, displaying the annotations, object property expression, source individual, and target individual.

      :rtype: str



   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:attribute:: _source_individual
      :type:  pyowl2.abstracts.individual.OWLIndividual


   .. py:attribute:: _target_individual
      :type:  pyowl2.abstracts.individual.OWLIndividual


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Assigns the specified object property expression to this negative object property assertion, replacing any existing value. This method updates the internal state of the instance to reflect the new relationship that is being negated. The provided value must be an instance of OWLObjectPropertyExpression to maintain semantic validity within the OWL structure.

      :param value: The OWL object property expression to assign.
      :type value: OWLObjectPropertyExpression


   .. py:property:: source_individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Updates the subject of the negative object property assertion to the provided OWLIndividual. This setter modifies the internal state by overwriting the current source individual with the new value.

      :param value:
      :type value: OWLIndividual


   .. py:property:: target_individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Updates the target individual associated with this negative object property assertion. This method assigns the provided OWLIndividual instance to the internal state, overwriting any previously stored value. It defines the specific individual that is asserted not to participate in the object property relationship with the source individual.

      :param value: The OWLIndividual to be set as the target individual.
      :type value: OWLIndividual

