pyowl2.class_expression.data_min_cardinality
============================================

.. py:module:: pyowl2.class_expression.data_min_cardinality



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an OWL class expression that restricts individuals to possess a minimum number of values for a specific data property, optionally constrained by a data range.


Description
-----------


The implementation models a restriction where an individual must have at least a specific number of data property assertions to be considered a member of the defined class. A non-negative integer cardinality is stored alongside a data property expression to define this constraint, ensuring that the threshold is valid upon initialization. Support for qualified restrictions is provided through an optional data range, which limits the count to only those values that match a specific datatype or set of literals. Properties expose the internal state for modification, and a string representation adhering to OWL functional syntax is generated to describe the restriction structure.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_data_min_cardinality_OWLDataMinCardinality.png
       :alt: UML Class Diagram for OWLDataMinCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataMinCardinality**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_data_min_cardinality_OWLDataMinCardinality.pdf
       :alt: UML Class Diagram for OWLDataMinCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataMinCardinality**

.. py:class:: OWLDataMinCardinality(value: int, expression: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, data_range: Optional[pyowl2.abstracts.data_range.OWLDataRange] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.data_min_cardinality.OWLDataMinCardinality
      :parts: 1
      :private-bases:


   This class represents a restriction within an ontology that defines a minimum threshold for the number of data values an individual must possess for a specific data property. It functions by combining a non-negative integer cardinality with a data property expression to specify that a valid individual must have at least that many associated values. Users can optionally provide a data range to create a qualified restriction, which constrains the count to only those values that match a specific datatype or set of literals, thereby enabling precise definitions of class characteristics.

   :param cardinality: The minimum number of values an individual must possess for the specified data property, represented as a non-negative integer.
   :type cardinality: int
   :param data_property_expression: Defines the relationship between the subject individual and the data values subject to the minimum cardinality restriction.
   :type data_property_expression: OWLDataPropertyExpression
   :param data_range: An optional data range that restricts the specific values counted towards the minimum cardinality. If provided, the restriction is qualified, requiring the minimum number of values to belong to this range; otherwise, it applies to any values of the data property.
   :type data_range: typing.Optional[OWLDataRange]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the OWL data minimum cardinality restriction, formatted using a functional syntax. The output includes the cardinality value and the associated data property expression, enclosed within parentheses and prefixed by 'DataMinCardinality'. If a specific data range is defined for the restriction, it is appended to the string; otherwise, the representation consists solely of the cardinality and the property expression.

      :return: A string representation of the data minimum cardinality restriction, comprising the cardinality, data property expression, and optionally the data range.

      :rtype: str



   .. py:attribute:: _cardinality
      :type:  int


   .. py:attribute:: _data_property_expression
      :type:  pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


   .. py:attribute:: _data_range
      :type:  Optional[pyowl2.abstracts.data_range.OWLDataRange]
      :value: None



   .. py:property:: cardinality
      :type: int


      Assigns the provided integer value to the internal `_cardinality` attribute, thereby updating the minimum cardinality constraint for this OWL data restriction. This operation modifies the object's state in place. Although the method accepts any integer, standard OWL semantics imply that the value should be non-negative, though this specific implementation does not enforce validation.

      :param value: The new value for the cardinality.
      :type value: int


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Updates the specific data property expression to which this minimum cardinality restriction applies. This setter assigns the provided `OWLDataPropertyExpression` instance to the internal state, overwriting any existing value. As a side effect, the object's state is mutated to reflect the new property definition.

      :param value: The OWL data property expression to assign to the object.
      :type value: OWLDataPropertyExpression


   .. py:property:: data_range
      :type: Optional[pyowl2.abstracts.data_range.OWLDataRange]


      Sets the data range for this OWL minimum cardinality restriction. This method updates the internal state by assigning the provided `OWLDataRange` instance (or None) to the underlying private attribute, effectively replacing the existing data type constraint that property values must satisfy.

      :param value: The OWL data range to assign, or None to clear the value.
      :type value: typing.Optional[OWLDataRange]


   .. py:property:: is_qualified
      :type: bool


      Indicates whether this minimum cardinality restriction is qualified by a specific data range. In the context of OWL, a restriction is considered qualified if it limits the count of values to those belonging to a particular data type, rather than applying to all values of the associated data property. This property returns True if a data range is explicitly defined for the restriction, and False otherwise.

      :return: True if the data range is not None, indicating the instance is qualified.

      :rtype: bool

