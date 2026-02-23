pyowl2.abstracts.data_property_expression
=========================================

.. py:module:: pyowl2.abstracts.data_property_expression



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an abstract base class representing expressions involving OWL data properties that link individuals to literal values.


Description
-----------


Acting as a root interface within the ontology model, the class distinguishes data properties—which associate individuals with literals like strings or integers—from object properties that link individuals to other individuals. It utilizes Python's abstract base class framework to mandate that subclasses implement logic for identifying specific semantic states, such as whether the expression represents the universal top data property or the empty bottom data property. These checks are critical for reasoning tasks and ontology normalization, as they allow the system to treat the top property as an identity element and the bottom property as a contradiction. By enforcing this contract, the implementation ensures consistent behavior across different types of data property expressions used throughout the broader software architecture.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_abstracts_data_property_expression_OWLDataPropertyExpression.png
       :alt: UML Class Diagram for OWLDataPropertyExpression
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataPropertyExpression**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_data_property_expression_OWLDataPropertyExpression.pdf
       :alt: UML Class Diagram for OWLDataPropertyExpression
       :align: center
       :width: 7.0cm
       :class: uml-diagram

       UML Class Diagram for **OWLDataPropertyExpression**

.. py:class:: OWLDataPropertyExpression

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression
      :parts: 1
      :private-bases:


   This abstract base class represents expressions involving OWL data properties, which define relationships between an individual and a literal value, such as a string or integer. It serves as the root interface for data property constructs within the ontology model, distinguishing them from object properties that link individuals to other individuals. Users can utilize this class to check specific characteristics of a property expression, such as whether it represents the universal (top) data property or the empty (bottom) data property.


   .. py:method:: is_bottom_data_property() -> bool
      :abstractmethod:


      Determines whether this data property expression represents the bottom data property, which is the property that no individual can possess. In OWL semantics, the bottom data property corresponds to the empty set of data property assertions. This method returns `True` if the expression is equivalent to the built-in `owl:bottomDataProperty`, and `False` for any other data property expression.

      :return: True if the data property is the bottom-most one, False otherwise.

      :rtype: bool



   .. py:method:: is_top_data_property() -> bool
      :abstractmethod:


      Determines whether this specific data property expression represents the top data property, which is the universal property that relates every individual to every literal in the ontology. This check is essential for reasoning tasks and ontology normalization, as the top property acts as the identity element for certain property operations. The method returns a boolean value indicating if the expression is equivalent to the built-in top data property, without modifying the underlying expression.

      :return: True if the property is the top data property, False otherwise.

      :rtype: bool



   .. py:attribute:: __slots__
      :value: ()


