pyowl2.expressions.inverse_object_property
==========================================

.. py:module:: pyowl2.expressions.inverse_object_property



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing the inverse of an OWL object property to model reciprocal relationships between individuals.


Description
-----------


The implementation provides a mechanism to express the inverse of a specific object property within an ontology, effectively reversing the direction of the relationship between two individuals. By wrapping an existing property, the logic allows systems to infer reciprocal connections, such as deriving a parent relationship from a child relationship, without requiring explicit assertions for both directions. The design includes methods to verify whether the underlying property corresponds to the universal top or bottom properties, ensuring consistency with OWL semantics. Additionally, the structure supports standard functional syntax output, enabling clear serialization and debugging of the logical constructs.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.expressions.inverse_object_property.OWLInverseObjectProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_expressions_inverse_object_property_OWLInverseObjectProperty.png
       :alt: UML Class Diagram for OWLInverseObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLInverseObjectProperty**

.. only:: latex

    .. figure:: /_uml/pyowl2_expressions_inverse_object_property_OWLInverseObjectProperty.pdf
       :alt: UML Class Diagram for OWLInverseObjectProperty
       :align: center
       :width: 11.6cm
       :class: uml-diagram

       UML Class Diagram for **OWLInverseObjectProperty**

.. py:class:: OWLInverseObjectProperty(property: pyowl2.expressions.object_property.OWLObjectProperty)

   Bases: :py:obj:`pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression`

   .. autoapi-inheritance-diagram:: pyowl2.expressions.inverse_object_property.OWLInverseObjectProperty
      :parts: 1
      :private-bases:


   This class represents an expression that defines the inverse of a specific object property, effectively reversing the direction of the relationship between two individuals. It is constructed by wrapping an existing `OWLObjectProperty`, allowing the ontology to infer that if the original property relates individual A to individual B, this expression relates B to A. This mechanism is essential for modeling reciprocal relationships—such as deriving "isParentOf" from "hasChild"—thereby enhancing the expressiveness and reasoning capabilities of the ontology without requiring explicit assertions for both directions.

   :parm object_property: The object property that is being inverted to represent the relationship in the opposite direction.
   :type object_property: OWLObjectProperty


   .. py:method:: __str__() -> str

      Returns a string representation of the inverse object property formatted according to functional syntax conventions. The output explicitly wraps the underlying object property within the "ObjectInverseOf" constructor, providing a human-readable depiction of the logical structure. This method does not alter the state of the object and relies on the string conversion of the internal object property attribute.

      :return: A string representation of the object, formatted as 'ObjectInverseOf({object_property})'.

      :rtype: str



   .. py:method:: is_bottom_object_property() -> bool

      Checks if the underlying object property is the top object property. The method returns True if the `object_property` attribute of the current instance is equal to the universal top object property, and False otherwise. This operation does not modify the state of the object or have any side effects.

      :return: True if the object property is the top object property, False otherwise.

      :rtype: bool



   .. py:method:: is_top_object_property() -> bool

      Determines whether the underlying object property is the bottom object property. This method compares the internal object property reference against the standard bottom property defined in the OWL ontology. It returns True if the properties are identical, indicating that this inverse property represents the bottom property.

      :return: True if the object property is the bottom object property, False otherwise.

      :rtype: bool



   .. py:attribute:: _object_property
      :type:  pyowl2.expressions.object_property.OWLObjectProperty


   .. py:property:: object_property
      :type: pyowl2.expressions.object_property.OWLObjectProperty


      Updates the internal state of the `OWLInverseObjectProperty` instance by assigning a new object property. This setter accepts an instance of `OWLObjectProperty` and stores it in the private `_object_property` attribute, effectively defining or modifying the property involved in the inverse relationship. The method modifies the instance in place and returns `None`.

      :param value: The OWL object property to set.
      :type value: OWLObjectProperty

