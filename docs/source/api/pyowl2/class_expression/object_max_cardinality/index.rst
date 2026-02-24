pyowl2.class_expression.object_max_cardinality
==============================================

.. py:module:: pyowl2.class_expression.object_max_cardinality



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a Python class representing an OWL object maximum cardinality restriction, which limits the number of relationships an individual can have via a specific object property.


Description
-----------


This software component models a specific type of restriction within the Web Ontology Language (OWL) by enforcing an upper bound on the number of distinct individuals an entity can be related to through a given object property. The design accommodates both unqualified constraints, which apply to any related individual, and qualified constraints that require the related individuals to also belong to a specific class expression. By encapsulating the cardinality value, the property being restricted, and an optional filler class, the implementation allows for the dynamic definition and modification of these semantic rules. Additional logic determines whether the restriction is qualified and provides a string representation in functional syntax format to support ontology serialization and debugging.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_object_max_cardinality_OWLObjectMaxCardinality.png
       :alt: UML Class Diagram for OWLObjectMaxCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectMaxCardinality**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_object_max_cardinality_OWLObjectMaxCardinality.pdf
       :alt: UML Class Diagram for OWLObjectMaxCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectMaxCardinality**

.. py:class:: OWLObjectMaxCardinality(value: int, property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, expression: Optional[pyowl2.abstracts.class_expression.OWLClassExpression] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.object_max_cardinality.OWLObjectMaxCardinality
      :parts: 1
      :private-bases:


   This class represents a restriction in an ontology that defines an upper bound on the number of distinct individuals an entity can be related to via a specific object property. It is used to construct class expressions where instances must satisfy a condition of having at most a certain number of relationships, such as a person having no more than two siblings. The restriction can be unqualified, applying to any individual connected by the property, or qualified, where the connected individuals must also belong to a specific class expression. To utilize this class, instantiate it with a non-negative integer representing the maximum cardinality, the object property expression defining the relationship, and an optional class expression to further constrain the type of the related individuals.

   :param cardinality: The non-negative integer defining the maximum number of distinct individuals an instance can be related to via the specified object property.
   :type cardinality: int
   :param object_property_expression: The object property expression defining the relationship being restricted, which may be a simple property or a complex expression involving property chains or inverses.
   :type object_property_expression: OWLObjectPropertyExpression
   :param class_expression: Optional class expression that restricts the type of individuals the subject can be related to. If provided, it creates a qualified cardinality restriction; otherwise, the restriction applies to any individual.
   :type class_expression: typing.Optional[OWLClassExpression]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object using a functional syntax format. The representation includes the cardinality value and the object property expression. If a class expression is defined, it is appended to the output; otherwise, the string is generated using only the cardinality and property components.

      :return: A string representation of the object max cardinality restriction in functional syntax format.

      :rtype: str



   .. py:attribute:: _cardinality
      :type:  int


   .. py:attribute:: _class_expression
      :type:  Optional[pyowl2.abstracts.class_expression.OWLClassExpression]
      :value: None



   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: cardinality
      :type: int


      Sets the maximum cardinality value for this OWL object restriction. This method updates the internal state by assigning the provided integer to the private `_cardinality` attribute. It modifies the instance in place and does not return a value, allowing the constraint limit to be changed after object creation.

      :param value: The desired cardinality to set.
      :type value: int


   .. py:property:: class_expression
      :type: Optional[pyowl2.abstracts.class_expression.OWLClassExpression]


      Assigns a new class expression to this maximum cardinality restriction, replacing the existing value. The method accepts an `OWLClassExpression` object or `None` and updates the internal `_class_expression` attribute accordingly. This operation directly mutates the object's state without returning a value.

      :param value: The OWL class expression to assign, or None to clear the current value.
      :type value: typing.Optional[OWLClassExpression]


   .. py:property:: is_qualified
      :type: bool


      Determines whether the object max cardinality restriction is qualified by checking for the presence of a specific class expression. In the context of OWL restrictions, a qualified restriction explicitly defines the class of the filler, whereas an unqualified restriction implicitly defaults to the universal class. This property returns True if the internal `class_expression` attribute is not None, indicating that a specific filler class has been defined, and False otherwise.

      :return: True if a class expression is defined, False otherwise.

      :rtype: bool


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Assigns the specified object property expression to this maximum cardinality restriction, defining the property whose occurrences are being limited. This method updates the internal state of the restriction, replacing any previously associated property expression with the new value. The input is expected to be a valid object property expression compatible with the underlying OWL ontology structure.

      :param value: The OWL object property expression to assign to the instance.
      :type value: OWLObjectPropertyExpression

