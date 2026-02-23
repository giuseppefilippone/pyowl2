pyowl2.class_expression.data_exact_cardinality
==============================================

.. py:module:: pyowl2.class_expression.data_exact_cardinality



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a class representing an OWL data exact cardinality restriction that constrains individuals to possess exactly a specific number of values for a given data property.


Description
-----------


The software models the Web Ontology Language (OWL) concept of exact cardinality restrictions for data properties, ensuring that an individual possesses exactly a defined number of data values. It supports both qualified and unqualified restrictions by allowing an optional data range parameter, which, when provided, limits the count to values falling within a specific datatype. Internal state management is handled through properties that expose the cardinality, the associated data property expression, and the optional data range, enabling validation and modification of these constraints. A boolean helper indicates whether the restriction is qualified, and a string representation method generates a functional syntax output to facilitate debugging or serialization.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_class_expression_data_exact_cardinality_OWLDataExactCardinality.png
       :alt: UML Class Diagram for OWLDataExactCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataExactCardinality**

.. only:: latex

    .. figure:: /_uml/pyowl2_class_expression_data_exact_cardinality_OWLDataExactCardinality.pdf
       :alt: UML Class Diagram for OWLDataExactCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataExactCardinality**

.. py:class:: OWLDataExactCardinality(value: int, expression: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, data_range: Optional[pyowl2.abstracts.data_range.OWLDataRange] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.data_exact_cardinality.OWLDataExactCardinality
      :parts: 1
      :private-bases:


   This class represents a restriction used in ontology modeling to define that an individual must have exactly a specific number of values for a given data property. It functions as a class expression that can be used to construct complex class definitions, ensuring that instances satisfy a precise count of data property assertions. To use this class, instantiate it with a non-negative integer representing the required cardinality, a data property expression identifying the relationship, and an optional data range to constrain the type of values counted. If the data range is provided, the restriction becomes qualified, meaning the exact count applies only to values that fall within that specific range; otherwise, the count applies to all values associated with the property.

   :parm cardinality: Stores the non-negative integer defining the exact number of data property values required for an individual to satisfy this restriction.
   :type cardinality: int
   :parm data_property_expression: The data property expression that defines the relationship between the subject individual and the data values.
   :type data_property_expression: OWLDataPropertyExpression
   :parm data_range: Optional data range that restricts the specific values the data property must take. If provided, the restriction is qualified, requiring the exact number of values to fall within this range; otherwise, the restriction applies to any data value.
   :type data_range: typing.Optional[OWLDataRange]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the data exact cardinality restriction, formatted in a functional syntax style. The output includes the specific cardinality value and the associated data property expression. If the restriction defines a specific data range, this range is appended to the string; otherwise, the representation consists solely of the cardinality and the property. This method does not modify the state of the object.

      :return: A string representation of the object, formatted to include the cardinality, data property expression, and optionally the data range.

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


      Updates the exact number of values required for the data property restriction represented by this instance. This setter assigns the provided integer value to the internal `_cardinality` attribute, effectively modifying the constraint definition. It allows the specific cardinality of the `OWLDataExactCardinality` object to be changed after it has been created.

      :param value: The new count or size to assign.
      :type value: int


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Assigns the specified data property expression to this exact cardinality restriction, replacing any previously held value. This method directly modifies the internal state of the object by updating the private attribute storing the property expression. While the type hint expects an instance of `OWLDataPropertyExpression`, the implementation performs no runtime validation, so passing an incompatible type may lead to errors in subsequent operations.

      :param value: The OWL data property expression to assign to the object.
      :type value: OWLDataPropertyExpression


   .. py:property:: data_range
      :type: Optional[pyowl2.abstracts.data_range.OWLDataRange]


      Assigns a new data range to this exact cardinality restriction, replacing any previously defined range. The method accepts an optional `OWLDataRange` instance; setting the value to `None` effectively removes the data range constraint. This operation directly modifies the internal state of the object by updating the underlying `_data_range` attribute.

      :param value: The OWL data range to assign, or None to clear the property.
      :type value: typing.Optional[OWLDataRange]


   .. py:property:: is_qualified
      :type: bool


      Determines whether this exact cardinality restriction is qualified by a specific data range. In the context of OWL, a qualified restriction limits the count to values that belong to a particular datatype, whereas an unqualified restriction applies to all values of the property. This property returns `True` if the `data_range` attribute is defined, and `False` if it is `None`.

      :return: True if a data range is defined, False otherwise.

      :rtype: bool

