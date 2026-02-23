pyowl2.class_expression.data_all_values_from
============================================

.. py:module:: pyowl2.class_expression.data_all_values_from



.. ── LLM-GENERATED DESCRIPTION START ──

A Python class implementation representing the OWL DataAllValuesFrom restriction, which enforces that all values of specific data properties must belong to a defined data range.


Description
-----------


The software models a universal restriction within the Web Ontology Language (OWL), specifically focusing on data properties where every associated value must fall within a specified data range. By inheriting from the base class expression, it integrates into a broader ontology framework, allowing developers to define complex constraints such as ensuring all ages are integers or all prices are positive numbers. A key design aspect involves the automatic sorting of the provided data property expressions upon initialization and modification, which guarantees a canonical internal state and facilitates consistent comparisons or hashing operations. The implementation exposes these components through managed properties and provides a human-readable string representation that mirrors standard logical notation, making it easier to debug and inspect the structure of the restriction.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_class_expression_data_all_values_from_OWLDataAllValuesFrom.png
       :alt: UML Class Diagram for OWLDataAllValuesFrom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataAllValuesFrom**

.. only:: latex

    .. figure:: /_uml/pyowl2_class_expression_data_all_values_from_OWLDataAllValuesFrom.pdf
       :alt: UML Class Diagram for OWLDataAllValuesFrom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataAllValuesFrom**

.. py:class:: OWLDataAllValuesFrom(expressions: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], data_range: pyowl2.abstracts.data_range.OWLDataRange)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.data_all_values_from.OWLDataAllValuesFrom
      :parts: 1
      :private-bases:


   This class represents a universal restriction on data properties within an ontology, specifying that for any individual belonging to this class, all values of the associated data properties must fall within a defined data range. It is used to enforce constraints on literal values, ensuring that data such as ages or prices conform to specific types or intervals. To construct an instance, provide a list of data property expressions and the target data range; the implementation automatically sorts the property list to ensure consistent representation.

   :parm data_property_expressions: Sorted data property expressions defining the properties restricted by the data range.
   :type data_property_expressions: list[OWLDataPropertyExpression]
   :parm data_range: The data range that defines the set of permissible values for the associated data properties.
   :type data_range: OWLDataRange


   .. py:method:: __str__() -> str

      Returns a string representation of the universal data property restriction, formatted to resemble a logical expression. The method concatenates the string representations of all data property expressions associated with this restriction and appends the string representation of the data range, wrapping them in a "DataAllValuesFrom" prefix. This operation is side-effect free, though the exact output depends on the string representations of the nested property expressions and data range objects.

      :return: A string representation of the object, formatted as a `DataAllValuesFrom` expression containing the data property expressions and data range.

      :rtype: str



   .. py:attribute:: _data_property_expressions
      :type:  list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


   .. py:attribute:: _data_range
      :type:  pyowl2.abstracts.data_range.OWLDataRange


   .. py:property:: data_property_expressions
      :type: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


      Sets the data property expressions for this OWLDataAllValuesFrom restriction by assigning the provided list of OWLDataPropertyExpression objects. The input list is sorted before being stored in the private attribute to maintain a deterministic internal state.

      :param value: The OWL data property expressions to assign. The list will be sorted internally before storage.
      :type value: list[OWLDataPropertyExpression]


   .. py:property:: data_range
      :type: pyowl2.abstracts.data_range.OWLDataRange


      Updates the data range filler for this 'all values from' restriction, defining the specific set of data values that the property must take. This method assigns the provided `OWLDataRange` instance to the internal `_data_range` attribute, replacing any previously stored value. The operation performs a direct assignment without performing explicit validation or triggering side effects beyond the state modification.

      :param value: The new data range to assign to the object.
      :type value: OWLDataRange

