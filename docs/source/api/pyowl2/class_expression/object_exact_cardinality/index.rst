pyowl2.class_expression.object_exact_cardinality
================================================

.. py:module:: pyowl2.class_expression.object_exact_cardinality



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing an OWL object property restriction that constrains an individual to have exactly a specific number of relationships.


Description
-----------


It models the semantic concept of exact cardinality within an ontology, ensuring that an individual is linked to a precise count of other individuals via a defined object property. The implementation supports both qualified and unqualified restrictions by allowing an optional class expression filler, which specifies the type of the related individuals or defaults to any type if omitted. Internal state management relies on properties to encapsulate the cardinality value, the property expression, and the optional class expression, with the constructor enforcing a precondition that the cardinality must be a non-negative integer. A string representation method generates human-readable output in functional syntax, dynamically adjusting the format based on whether the restriction is qualified. By inheriting from a base class expression, this component integrates into a broader framework for constructing and manipulating complex ontology structures.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_class_expression_object_exact_cardinality_OWLObjectExactCardinality.png
       :alt: UML Class Diagram for OWLObjectExactCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectExactCardinality**

.. only:: latex

    .. figure:: /_uml/pyowl2_class_expression_object_exact_cardinality_OWLObjectExactCardinality.pdf
       :alt: UML Class Diagram for OWLObjectExactCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectExactCardinality**

.. py:class:: OWLObjectExactCardinality(value: int, property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, expression: Optional[pyowl2.abstracts.class_expression.OWLClassExpression] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.object_exact_cardinality.OWLObjectExactCardinality
      :parts: 1
      :private-bases:


   Represents an object property restriction within an ontology that constrains an individual to be related to exactly a specific number of other individuals via a defined relationship. To utilize this restriction, one must provide a non-negative integer indicating the exact count and an object property expression that defines the relationship. An optional class expression can be included to create a qualified restriction, specifying that the related individuals must also be instances of a particular class; if this is omitted, the restriction applies to any individual connected via the specified property.

   :parm cardinality: The exact non-negative integer count of distinct individuals that the subject must be related to via the object property to satisfy the restriction.
   :type cardinality: int
   :parm object_property_expression: The object property expression that defines the relationship used to count the exact number of related individuals in the restriction.
   :type object_property_expression: OWLObjectPropertyExpression
   :parm class_expression: The optional class expression defining the type of individuals that the subject must be related to via the object property. If provided, it creates a qualified restriction; otherwise, the restriction applies to any individual filling the property.
   :type class_expression: typing.Optional[OWLClassExpression]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object exact cardinality restriction, formatted to resemble functional syntax. The output dynamically adapts based on the presence of a class expression filler; if a class expression is defined, the string includes the cardinality, the object property expression, and the class expression. If the class expression is absent, the representation consists only of the cardinality and the object property expression.

      :return: A human-readable string representation of the object exact cardinality restriction, displaying the cardinality, object property, and optionally the class expression.

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


      Updates the exact cardinality value for this OWL object restriction. The method accepts an integer representing the specific number of property values required and assigns it to the object's internal state. This operation directly modifies the underlying attribute without performing explicit validation on the provided integer.

      :param value: The new cardinality value to assign.
      :type value: int


   .. py:property:: class_expression
      :type: Optional[pyowl2.abstracts.class_expression.OWLClassExpression]


      Updates the class expression associated with this OWL object exact cardinality restriction. This method accepts an optional OWLClassExpression instance, allowing the restriction's filler to be explicitly set or cleared by passing None. The operation directly mutates the instance's internal state, overwriting any previously stored class expression value.

      :param value: The new class expression to assign, or None to clear the value.
      :type value: typing.Optional[OWLClassExpression]


   .. py:property:: is_qualified
      :type: bool


      Determines whether this exact cardinality restriction is qualified by verifying the presence of a specific class expression filler. In the context of OWL restrictions, a qualified restriction limits the count of relationships to objects that are instances of a particular class, whereas an unqualified restriction simply limits the count of relationships regardless of the object type. This property returns `True` if a class expression is defined, and `False` otherwise.

      :return: True if the object has an associated class expression, False otherwise.

      :rtype: bool


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Updates the object property expression associated with this exact cardinality restriction by assigning the provided value. This method modifies the internal state of the object, replacing the existing property expression with the new one specified.

      :param value: The OWL object property expression to assign to the instance.
      :type value: OWLObjectPropertyExpression

