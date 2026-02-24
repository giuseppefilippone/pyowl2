pyowl2.class_expression.object_has_value
========================================

.. py:module:: pyowl2.class_expression.object_has_value



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a class representing an OWL object property restriction that constrains individuals to be related to a specific named individual via a particular property.


Description
-----------


The implementation models the OWL "ObjectHasValue" restriction, which is used to define a class of individuals that must be associated with a specific, named individual through a defined object property. By accepting an object property expression and a target individual during initialization, the logic allows for the creation of complex class expressions that assert exact value constraints within an ontology. State management is handled through property accessors that permit the retrieval and modification of both the relationship property and the specific individual value, ensuring the restriction can be dynamically updated. A string representation method is provided to generate a human-readable format of the restriction, which is useful for debugging and logging the logical structure of the ontology components.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_has_value.OWLObjectHasValue


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_object_has_value_OWLObjectHasValue.png
       :alt: UML Class Diagram for OWLObjectHasValue
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectHasValue**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_object_has_value_OWLObjectHasValue.pdf
       :alt: UML Class Diagram for OWLObjectHasValue
       :align: center
       :width: 13.5cm
       :class: uml-diagram

       UML Class Diagram for **OWLObjectHasValue**

.. py:class:: OWLObjectHasValue(property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, individual: pyowl2.abstracts.individual.OWLIndividual)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.object_has_value.OWLObjectHasValue
      :parts: 1
      :private-bases:


   This class represents an OWL object property restriction that defines a class of individuals which must be related to a specific, named individual via a particular object property. It is used to express exact value constraints, such as defining the class of "people who have a specific child" or "cities located at a specific coordinate." To use this class, instantiate it with an `OWLObjectPropertyExpression` that defines the relationship and an `OWLIndividual` that serves as the required target value. This restriction can then be employed as a class expression within axioms to construct complex logical definitions or to assert necessary conditions for class membership in an ontology.

   :param object_property_expression: The object property expression defining the relationship between the subject individual and the specific individual value in the restriction.
   :type object_property_expression: OWLObjectPropertyExpression
   :param individual: The specific individual instance that the subject must be related to via the object property expression to satisfy the restriction.
   :type individual: OWLIndividual


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object property value restriction, formatted to display the class name followed by the specific property and individual involved. The output follows the pattern "ObjectHasValue({property} {individual})", where the property and individual are converted to their respective string representations. This method is primarily used for debugging or logging purposes, providing a concise summary of the restriction's components without altering the object's state.

      :return: A human-readable string representation of the object, formatted as 'ObjectHasValue({object_property_expression} {individual})'.

      :rtype: str



   .. py:attribute:: _individual
      :type:  pyowl2.abstracts.individual.OWLIndividual


   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Updates the specific individual filler for this object-has-value restriction by assigning the provided `OWLIndividual` instance to the internal state. This operation directly mutates the object, replacing any previously associated individual with the new value. It does not return a result, ensuring the restriction now references the specified individual.

      :param value: The individual to assign to the object.
      :type value: OWLIndividual


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Sets the object property expression for this `OWLObjectHasValue` restriction, defining the specific property that is being constrained. This method updates the internal state by assigning the provided `OWLObjectPropertyExpression` to the instance, overwriting any previously set value. It effectively changes the predicate of the class expression to the new property supplied.

      :param value: The OWL object property expression to assign.
      :type value: OWLObjectPropertyExpression

