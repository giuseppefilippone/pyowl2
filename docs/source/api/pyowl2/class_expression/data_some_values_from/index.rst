pyowl2.class_expression.data_some_values_from
=============================================

.. py:module:: pyowl2.class_expression.data_some_values_from



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a Python class representing an OWL existential restriction that requires individuals to possess specific data property values within a defined range.


Description
-----------


The software models the Web Ontology Language (OWL) existential restriction known as "DataSomeValuesFrom," which defines a class of individuals based on the requirement that they possess at least one value for a specific data property falling within a designated data range. By inheriting from a base class expression, it integrates into a broader ontology framework, allowing for the construction of complex logical statements involving data properties and types. A key design choice involves the automatic sorting of the provided data property expressions upon initialization and modification, ensuring a canonical internal representation that supports consistent comparison and hashing regardless of the input order. Access to the underlying data properties and the associated data range is managed through properties that enforce this sorting logic, while a string representation method provides a human-readable format useful for debugging and logging.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_class_expression_data_some_values_from_OWLDataSomeValuesFrom.png
       :alt: UML Class Diagram for OWLDataSomeValuesFrom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataSomeValuesFrom**

.. only:: latex

    .. figure:: /_uml/pyowl2_class_expression_data_some_values_from_OWLDataSomeValuesFrom.pdf
       :alt: UML Class Diagram for OWLDataSomeValuesFrom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataSomeValuesFrom**

.. py:class:: OWLDataSomeValuesFrom(expressions: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], data_range: pyowl2.abstracts.data_range.OWLDataRange = None)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.data_some_values_from.OWLDataSomeValuesFrom
      :parts: 1
      :private-bases:


   This class represents an existential restriction on data properties, asserting that an individual must have at least one value for a specified property that falls within a particular data range. It serves to define a class of individuals based on the existence of data values satisfying specific criteria, such as having an age within a certain integer interval. When constructing an instance, users provide a list of data property expressions and the corresponding data range; internally, the list of properties is automatically sorted to maintain a consistent order regardless of the input sequence.

   :parm data_property_expressions: Sorted list of data property expressions defining the properties restricted by this class. The restriction requires that an individual has at least one value for any of these properties within the specified data range.
   :type data_property_expressions: list[OWLDataPropertyExpression]
   :parm data_range: The data range or datatype that at least one value of the associated data properties must fall within.
   :type data_range: OWLDataRange


   .. py:method:: __str__() -> str

      Generates a human-readable string representation of the OWL data some values from restriction, formatted to display the class identifier along with its constituent components. The resulting string concatenates the keyword 'DataSomeValuesFrom' with the string representations of the associated data property expressions and the specific data range, separated by spaces. This method is intended for logging or debugging purposes and does not modify the state of the object.

      :return: A human-readable string representation of the object, formatted as a DataSomeValuesFrom expression containing the data property expressions and data range.

      :rtype: str



   .. py:attribute:: _data_property_expressions
      :type:  list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


   .. py:attribute:: _data_range
      :type:  pyowl2.abstracts.data_range.OWLDataRange
      :value: None



   .. py:property:: data_property_expressions
      :type: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


      Assigns a new collection of data property expressions to this restriction, replacing the existing set. The provided list of OWLDataPropertyExpression objects is sorted prior to storage to maintain a canonical internal order. This normalization ensures that the sequence of properties does not affect the object's state or equality comparisons.

      :param value: The OWL data property expressions to assign. The provided list will be sorted before storage.
      :type value: list[OWLDataPropertyExpression]


   .. py:property:: data_range
      :type: pyowl2.abstracts.data_range.OWLDataRange


      Updates the data range component of this OWL data restriction to the provided value. This method replaces the existing internal data range with the new instance, effectively altering the set of literal values that the property restriction targets. The operation mutates the object's state and requires the input to be a valid OWLDataRange object.

      :param value: The OWL data range to assign.
      :type value: OWLDataRange

