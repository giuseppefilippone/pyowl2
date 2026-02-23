pyowl2.class_expression.data_has_value
======================================

.. py:module:: pyowl2.class_expression.data_has_value



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a Web Ontology Language (OWL) class expression that restricts individuals to those possessing a specific data property with a defined literal value.


Description
-----------


The software models a specific type of restriction within the Web Ontology Language known as a data value restriction, which defines a class consisting of individuals that have a particular data property filled with a specific literal. By extending the abstract class expression interface, this implementation encapsulates a data property expression and a literal value to enforce constraints where an individual must possess an exact data attribute match to be considered a member of the class. The design utilizes property getters and setters to manage the internal state, allowing the associated property and literal to be modified dynamically after instantiation. Furthermore, a string representation method is provided to generate a human-readable functional syntax output, which aids in debugging and serialization by displaying the restriction type alongside its constituent property and value.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.data_has_value.OWLDataHasValue


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_class_expression_data_has_value_OWLDataHasValue.png
       :alt: UML Class Diagram for OWLDataHasValue
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataHasValue**

.. only:: latex

    .. figure:: /_uml/pyowl2_class_expression_data_has_value_OWLDataHasValue.pdf
       :alt: UML Class Diagram for OWLDataHasValue
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataHasValue**

.. py:class:: OWLDataHasValue(expression: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, literal: pyowl2.literal.literal.OWLLiteral)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.data_has_value.OWLDataHasValue
      :parts: 1
      :private-bases:


   This class represents a restriction in the Web Ontology Language (OWL) that defines a class of individuals based on the existence of a specific data property value. It asserts that an individual belongs to the defined class if it possesses a particular data property filled with a specific literal value, such as having an age of exactly 30. By encapsulating a data property expression and a target literal, this entity enables the precise formulation of class definitions that depend on concrete data assertions within an ontology.

   :parm data_property_expression: The data property expression that defines the relationship between the subject individual and the specific literal value required by the restriction.
   :type data_property_expression: OWLDataPropertyExpression
   :parm literal: The specific literal value that the data property expression must take for the restriction to be satisfied.
   :type literal: OWLLiteral


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the data property value restriction, formatted in a functional syntax style. The resulting string concatenates the class name with the string representations of the underlying data property expression and the literal value, separated by a space within parentheses. This representation is useful for debugging and logging, and it has no side effects on the object's internal state.

      :return: A string representation of the object, formatted as 'DataHasValue(data_property_expression literal)'.

      :rtype: str



   .. py:attribute:: _data_property_expression
      :type:  pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


   .. py:attribute:: _literal
      :type:  pyowl2.literal.literal.OWLLiteral


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Assigns the specified data property expression to this `OWLDataHasValue` restriction, updating the internal state of the object. This method replaces any previously associated data property expression with the provided value, which must be an instance of `OWLDataPropertyExpression`. The modification effectively changes which data property is being constrained by this specific class expression.

      :param value: The OWL data property expression to assign to the object.
      :type value: OWLDataPropertyExpression


   .. py:property:: literal
      :type: pyowl2.literal.literal.OWLLiteral


      Updates the specific literal value associated with this data property restriction. The method accepts an OWLLiteral object and assigns it to the internal state, effectively defining the concrete value that the data property must match. This operation overwrites any previously stored literal and does not return a value.

      :param value: The OWL literal value to set.
      :type value: OWLLiteral

