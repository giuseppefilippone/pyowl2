pyowl2.axioms.assertion.object_property_assertion
=================================================

.. py:module:: pyowl2.axioms.assertion.object_property_assertion



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing an OWL axiom that asserts a specific binary relationship between two individuals.


Description
-----------


The software models a specific type of Web Ontology Language (OWL) axiom that declares a binary relationship exists between two distinct individuals. By inheriting from a base assertion class, it manages the core components of the relationship, including the property expression defining the link, the source individual acting as the subject, and the target individual acting as the object. Optional metadata annotations can be attached to the assertion to provide additional context or information, which are handled through the parent class initialization. Access to the internal state is provided via properties that allow both retrieval and modification of the property expression and the involved individuals, ensuring the encapsulated data remains consistent with the ontology's structure. A string representation method generates the axiom in a functional syntax format, facilitating debugging or serialization by displaying the relationship and its components clearly.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_assertion_object_property_assertion_OWLObjectPropertyAssertion.png
       :alt: UML Class Diagram for OWLObjectPropertyAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyAssertion**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_assertion_object_property_assertion_OWLObjectPropertyAssertion.pdf
       :alt: UML Class Diagram for OWLObjectPropertyAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyAssertion**

.. py:class:: OWLObjectPropertyAssertion(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, source: pyowl2.abstracts.individual.OWLIndividual, target: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.assertion.object_property_assertion.OWLObjectPropertyAssertion
      :parts: 1
      :private-bases:


   This axiom represents a specific factual statement within an ontology, declaring that a binary relationship defined by an object property exists between two distinct individuals. It serves to ground abstract properties by connecting a specific source individual to a specific target individual, effectively stating that the source relates to the target via the given property. To construct this assertion, provide the object property expression, the source individual, and the target individual during initialization, optionally including a list of annotations to attach metadata to the axiom itself. Once instantiated, the components of the relationship can be accessed or modified via their corresponding properties.

   :param object_property_expression: The object property expression that relates the source and target individuals.
   :type object_property_expression: OWLObjectPropertyExpression
   :param source_individual: The individual from which the object property relationship originates, representing the subject of the assertion.
   :type source_individual: OWLIndividual
   :param target_individual: The individual to which the object property relationship points, serving as the object of the assertion.
   :type target_individual: OWLIndividual


   .. py:method:: __str__() -> str

      Returns a string representation of the object property assertion axiom in a functional syntax style. The output includes the axiom annotations, object property expression, source individual, and target individual. If no annotations are present, an empty list is used in the string representation to preserve the structural format.

      :return: A string representation of the object property assertion in functional syntax, including annotations, the object property expression, and the source and target individuals.

      :rtype: str



   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:attribute:: _source_individual
      :type:  pyowl2.abstracts.individual.OWLIndividual


   .. py:attribute:: _target_individual
      :type:  pyowl2.abstracts.individual.OWLIndividual


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Sets the object property expression for this assertion, defining the specific relationship that holds between the involved individuals. The provided value, which must be an instance of OWLObjectPropertyExpression, replaces the existing property expression stored within the object. This method updates the internal state of the assertion in place and returns nothing.

      :param value: The object property expression to assign.
      :type value: OWLObjectPropertyExpression


   .. py:property:: source_individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Sets the source individual for this object property assertion, effectively defining the subject of the relationship. This method updates the internal state by assigning the provided `OWLIndividual` instance to the corresponding private attribute, overwriting any previously stored value. It is intended to be used to modify the assertion's subject after the object has been initialized.

      :param value: The OWLIndividual to be set as the source individual.
      :type value: OWLIndividual


   .. py:property:: target_individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Sets the target individual (the object) of this OWL object property assertion to the provided value. This method updates the internal state of the assertion, replacing the existing target with the specified `OWLIndividual`. This operation mutates the instance, altering the semantic relationship defined by the assertion.

      :param value: The OWL individual to assign as the target.
      :type value: OWLIndividual

