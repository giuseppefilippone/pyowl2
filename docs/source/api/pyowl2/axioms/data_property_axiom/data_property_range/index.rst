pyowl2.axioms.data_property_axiom.data_property_range
=====================================================

.. py:module:: pyowl2.axioms.data_property_axiom.data_property_range



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an OWL axiom that restricts the literal values of a data property to a specific data range.


Description
-----------


An implementation that establishes a constraint within an ontology by linking a specific data property expression to a defined data range, ensuring that any literal values assigned to the property adhere to the specified type. Inheriting from both ``OWLPropertyRange`` and ``OWLDataPropertyAxiom`` allows the component to integrate seamlessly into the broader ontology structure while supporting optional metadata annotations for additional context. Internal state is managed through private attributes for the property and range, which are exposed via properties that allow for both mutation and retrieval of these core components. A string representation method generates the axiom in functional syntax, facilitating debugging or serialization by explicitly listing annotations, the subject property, and the target range.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_data_property_axiom_data_property_range_OWLDataPropertyRange.png
       :alt: UML Class Diagram for OWLDataPropertyRange
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataPropertyRange**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_data_property_axiom_data_property_range_OWLDataPropertyRange.pdf
       :alt: UML Class Diagram for OWLDataPropertyRange
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataPropertyRange**

.. py:class:: OWLDataPropertyRange(property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, data_range: pyowl2.abstracts.data_range.OWLDataRange, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.property_range.OWLPropertyRange`, :py:obj:`pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.data_property_axiom.data_property_range.OWLDataPropertyRange
      :parts: 1
      :private-bases:


   This class represents an axiom within an ontology that defines the permissible types of literal values for a specific data property. It functions by associating a data property expression with a data range, thereby enforcing constraints such as requiring a property to hold only integers, strings, or values satisfying specific facet restrictions. Users can instantiate this entity to declare these type restrictions, optionally attaching annotations to provide additional metadata or context regarding the axiom itself.

   :parm data_property_expression: The data property expression for which the range is being specified.
   :type data_property_expression: OWLDataPropertyExpression
   :parm data_range: The set of data values or data types permitted for the associated data property.
   :type data_range: OWLDataRange


   .. py:method:: __str__() -> str

      Returns a string representation of the OWL data property range axiom, formatted according to a specific functional syntax. The representation always includes the axiom annotations, defaulting to an empty list if none are present, followed by the data property expression and the data range. This method does not modify the object's state and is primarily intended for debugging or display purposes.

      :return: A string representation of the axiom, including its annotations, data property expression, and data range.

      :rtype: str



   .. py:attribute:: _data_property_expression
      :type:  pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


   .. py:attribute:: _data_range
      :type:  pyowl2.abstracts.data_range.OWLDataRange


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Assigns the specified data property expression to this instance, replacing any previously held value. The method accepts an object of type `OWLDataPropertyExpression` and updates the internal state to reflect this change. This operation mutates the object in place and does not return a value.

      :param value: The data property expression to assign to this object.
      :type value: OWLDataPropertyExpression


   .. py:property:: data_range
      :type: pyowl2.abstracts.data_range.OWLDataRange


      Updates the data range associated with this OWL data property range axiom by assigning the provided value to the internal storage attribute. This operation overwrites any previously defined range without performing explicit validation. The method returns None and modifies the object's state in place.

      :param value: The data range to assign to the object.
      :type value: OWLDataRange

