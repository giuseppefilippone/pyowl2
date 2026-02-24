pyowl2.class_expression.data_max_cardinality
============================================

.. py:module:: pyowl2.class_expression.data_max_cardinality



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing an OWL restriction that limits the maximum number of data values an individual may possess for a specific data property.


Description
-----------


The implementation models a specific type of class expression used in ontologies to enforce upper bounds on the number of data values associated with an individual via a particular property. By combining a non-negative integer cardinality with a data property expression, the logic ensures that instances do not exceed the specified limit for the defined attribute. An optional data range parameter allows for the creation of qualified restrictions, where the cardinality constraint applies exclusively to values belonging to that specific range rather than all possible values of the property. The design includes internal validation to guarantee that the cardinality remains non-negative and exposes properties to determine whether the restriction is qualified based on the presence of the data range. String representation logic dynamically adjusts to include the data range only when it is defined, providing a clear textual summary of the constraint.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_data_max_cardinality_OWLDataMaxCardinality.png
       :alt: UML Class Diagram for OWLDataMaxCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataMaxCardinality**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_data_max_cardinality_OWLDataMaxCardinality.pdf
       :alt: UML Class Diagram for OWLDataMaxCardinality
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataMaxCardinality**

.. py:class:: OWLDataMaxCardinality(value: int, expression: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, data_range: Optional[pyowl2.abstracts.data_range.OWLDataRange] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.data_max_cardinality.OWLDataMaxCardinality
      :parts: 1
      :private-bases:


   This class represents a restriction in an ontology that defines the maximum number of data values an individual may have for a specific data property. It is constructed using a non-negative integer cardinality and a data property expression, which identifies the attribute being restricted. An optional data range can be included to create a qualified restriction, specifying that the cardinality limit applies only to values within that particular range, whereas its absence applies the limit to all values of the property.

   :param cardinality: The non-negative integer defining the upper limit of values an individual may possess for the associated data property.
   :type cardinality: int
   :param data_property_expression: The data property expression defining the relationship between the subject individual and the data values subject to the maximum cardinality restriction.
   :type data_property_expression: OWLDataPropertyExpression
   :param data_range: Optional data range that restricts the values counted towards the maximum cardinality. If specified, the restriction is qualified, applying only to values within this range; otherwise, it applies to all values of the data property.
   :type data_range: typing.Optional[OWLDataRange]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the data maximum cardinality restriction, formatted to display the class name followed by the cardinality value and the associated data property expression. The method conditionally appends the data range to the output string only if it is defined; otherwise, the representation omits the range. This ensures a concise and accurate textual summary of the object's state without causing errors when the data range attribute is unset.

      :return: A string representation of the `DataMaxCardinality` object, displaying the cardinality, data property expression, and data range (if defined).

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


      Updates the maximum cardinality value for this OWL data restriction to the specified integer. This method directly modifies the internal state of the object by assigning the new value to the underlying `_cardinality` attribute. While the implementation performs no explicit validation, the value is expected to be a non-negative integer consistent with OWL semantics, and changing it will affect any subsequent logic or comparisons that depend on this constraint.

      :param value: The new cardinality value to assign.
      :type value: int


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Sets the data property expression that this maximum cardinality restriction applies to. This method accepts an instance of OWLDataPropertyExpression and updates the internal state of the object, effectively reconfiguring the restriction to constrain the specified property. Any subsequent operations or evaluations involving this OWLDataMaxCardinality instance will reflect the newly assigned data property.

      :param value: The OWL data property expression to assign to the object.
      :type value: OWLDataPropertyExpression


   .. py:property:: data_range
      :type: Optional[pyowl2.abstracts.data_range.OWLDataRange]


      Assigns a new data range to this maximum cardinality restriction, defining the specific type of data values allowed. The method accepts an optional OWLDataRange instance; if provided, it replaces the existing data range, effectively altering the semantic constraints of the ontology element. This operation updates the object's internal state immediately.

      :param value: The OWL data range to assign, or None to clear the current value.
      :type value: typing.Optional[OWLDataRange]


   .. py:property:: is_qualified
      :type: bool


      Indicates whether this data maximum cardinality restriction is qualified by checking for the presence of a specific data range. A restriction is considered qualified if it limits the count to values belonging to a particular data range, rather than applying to the general range of the data property. This property returns True if the data range attribute is explicitly set, and False otherwise.

      :return: True if a data range is defined, False otherwise.

      :rtype: bool

