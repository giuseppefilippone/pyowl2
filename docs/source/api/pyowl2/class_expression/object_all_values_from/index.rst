pyowl2.class_expression.object_all_values_from
==============================================

.. py:module:: pyowl2.class_expression.object_all_values_from



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a Python class representing the OWL universal restriction ObjectAllValuesFrom, which constrains the range of an object property to a specific class expression.


Description
-----------


The implementation models the Web Ontology Language (OWL) universal restriction, a logical construct asserting that every individual connected via a specific object property must belong to a designated class. By inheriting from a base class expression, it integrates into a broader ontology framework, storing an object property expression that defines the relationship and a class expression that serves as the constraint or filler. Access to these internal components is managed through property getters and setters, allowing the logical definition of the restriction to be queried or modified dynamically during runtime. A string representation method is provided to generate a human-readable format of the restriction, which aids in debugging and logging by displaying the property and the associated class expression.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_object_all_values_from_OWLObjectAllValuesFrom.png
       :alt: UML Class Diagram for OWLObjectAllValuesFrom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectAllValuesFrom**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_object_all_values_from_OWLObjectAllValuesFrom.pdf
       :alt: UML Class Diagram for OWLObjectAllValuesFrom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectAllValuesFrom**

.. py:class:: OWLObjectAllValuesFrom(property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, expression: pyowl2.abstracts.class_expression.OWLClassExpression)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.object_all_values_from.OWLObjectAllValuesFrom
      :parts: 1
      :private-bases:


   This class represents a universal restriction in the Web Ontology Language (OWL), defining a condition where every individual related via a specific object property must be an instance of a designated class expression. It is initialized with an object property expression, which establishes the relationship, and a class expression, which acts as the constraint that all related individuals must satisfy. Semantically, an individual belongs to this restriction if and only if all values reachable through the specified property are members of the provided class expression, enabling the precise definition of complex class hierarchies and domain constraints.

   :parm object_property_expression: The object property expression defining the relationship between the subject individual and the objects that must satisfy the class expression.
   :type object_property_expression: OWLObjectPropertyExpression
   :parm class_expression: Defines the class that all values of the object property must be instances of.
   :type class_expression: OWLClassExpression


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the OWL object all values from restriction, formatted to display the class name followed by the object property expression and the class expression enclosed in parentheses. This method is primarily used for debugging and logging, providing a concise textual summary of the restriction's components without modifying the object's state.

      :return: A human-readable string representation of the object, formatted as 'ObjectAllValuesFrom(object_property_expression class_expression)'.

      :rtype: str



   .. py:attribute:: _class_expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Assigns the specified OWL class expression to this restriction, replacing any existing value. This method accepts an instance of `OWLClassExpression` and updates the internal state by setting the `_class_expression` attribute. As a side effect, it mutates the object, altering the semantic definition of the "all values from" restriction to reflect the new class expression.

      :param value: The OWL class expression to assign.
      :type value: OWLClassExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Updates the object property expression used in this universal restriction by assigning the provided value. The input must be an instance of `OWLObjectPropertyExpression`, which defines the property over which the 'all values from' condition is applied. This operation modifies the internal state of the `OWLObjectAllValuesFrom` object, replacing any previously stored property expression.

      :param value: The OWL object property expression to assign to the instance.
      :type value: OWLObjectPropertyExpression

