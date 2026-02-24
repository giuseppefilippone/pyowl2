pyowl2.class_expression.object_min_cardinality
==============================================

.. py:module:: pyowl2.class_expression.object_min_cardinality



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a Python class that models an OWL minimum cardinality restriction, requiring individuals to participate in a specific object property relationship at least a defined number of times.


Description
-----------


The implementation represents a semantic constraint within an ontology where an entity must be linked to a minimum number of distinct individuals via a designated object property. It supports both unqualified restrictions, which apply to any related individual, and qualified restrictions, which limit the count to individuals belonging to a specific class expression. Internal state management relies on properties to encapsulate the cardinality value, the property expression, and the optional class filler, ensuring that the constraint can be dynamically inspected or modified. By subclassing the abstract class expression, the logic integrates seamlessly into larger logical constructs, providing a boolean check for qualification status and a formatted string representation for debugging or serialization purposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_object_min_cardinality_OWLObjectMinCardinality.png
       :alt: UML Class Diagram for OWLObjectMinCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectMinCardinality**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_object_min_cardinality_OWLObjectMinCardinality.pdf
       :alt: UML Class Diagram for OWLObjectMinCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectMinCardinality**

.. py:class:: OWLObjectMinCardinality(value: int, property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, expression: Optional[pyowl2.abstracts.class_expression.OWLClassExpression] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.object_min_cardinality.OWLObjectMinCardinality
      :parts: 1
      :private-bases:


   This class models a restriction that requires an individual to be linked to at least a specific number of other individuals through a defined object property. To use it, instantiate the class with a non-negative integer representing the minimum count, an object property expression describing the relationship, and an optional class expression to filter the type of the target individuals. If the class expression is omitted, the restriction applies to any related individual; if included, it creates a qualified restriction where the targets must also belong to the specified class. As a subclass of class expression, it can be nested within other logical constructs to define complex ontology axioms.

   :param cardinality: The non-negative integer value representing the minimum number of individuals that the subject individual must be related to via the specified object property.
   :type cardinality: int
   :param object_property_expression: The object property expression defining the relationship that the subject individual must satisfy a minimum number of times. It can be a simple property or a complex expression involving inverses or property chains.
   :type object_property_expression: OWLObjectPropertyExpression
   :param class_expression: Optional class expression that restricts the type of individuals counted towards the minimum cardinality. If provided, the restriction is qualified, requiring related individuals to be instances of this class; if omitted, the restriction applies to any related individual.
   :type class_expression: typing.Optional[OWLClassExpression]


   .. py:method:: __str__() -> str

      Returns a string representation of the OWL minimum cardinality restriction, formatted to display the restriction type, the specific cardinality value, and the associated object property expression. The method conditionally includes the class expression in the output if it is present; otherwise, the representation is limited to the cardinality and property components. This implementation is primarily intended for debugging or logging purposes and does not alter the state of the object.

      :return: A string representation of the object min cardinality restriction, including the cardinality, object property expression, and optionally the class expression.

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


      Updates the minimum cardinality value for this OWL object restriction by assigning the provided integer to the internal state. This method allows the constraint to be modified after the object has been created, replacing the existing cardinality with the new value. The provided value should be a non-negative integer representing the minimum number of times the associated property must participate in a relationship.

      :param value: The integer value to set as the cardinality.
      :type value: int


   .. py:property:: class_expression
      :type: Optional[pyowl2.abstracts.class_expression.OWLClassExpression]


      Sets the class expression (filler) associated with this minimum cardinality restriction. It accepts an optional `OWLClassExpression` instance and updates the object's internal state by assigning the provided value to the private `_class_expression` attribute, overwriting any existing value.

      :param value: The OWL class expression to assign to the property, or None.
      :type value: typing.Optional[OWLClassExpression]


   .. py:property:: is_qualified
      :type: bool


      Indicates whether this minimum cardinality restriction is qualified by a specific class expression. It returns True if the restriction defines a filler class that the property values must instantiate, and False otherwise. This distinction separates simple cardinality constraints from those that restrict the range to a particular type.

      :return: True if the class expression is not None, False otherwise.

      :rtype: bool


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Sets the object property expression for this minimum cardinality restriction, defining the specific relationship that the cardinality constraint applies to. The provided value, which must be an instance of OWLObjectPropertyExpression, replaces any previously assigned property expression. This method mutates the internal state of the object by updating the private attribute storing the property.

      :param value: The OWL object property expression to assign.
      :type value: OWLObjectPropertyExpression

