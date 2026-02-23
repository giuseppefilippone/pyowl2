pyowl2.axioms.object_property_axiom.object_property_range
=========================================================

.. py:module:: pyowl2.axioms.object_property_axiom.object_property_range



.. ── LLM-GENERATED DESCRIPTION START ──

A Python class representing an OWL axiom that constrains the range of an object property to a specific class expression.


Description
-----------


The implementation models a semantic constraint within an ontology by asserting that any individual serving as a value for a specific object property must belong to a defined class type. By inheriting from both ``OWLPropertyRange`` and ``OWLObjectPropertyAxiom``, the class integrates range restriction logic directly into the axiom structure, allowing for the enforcement of type safety across relationships. It encapsulates an object property expression and a class expression, storing them as internal attributes while supporting optional annotations for metadata enrichment. The design includes property accessors for modifying the constraint components and a string representation method that outputs the axiom in standard functional syntax for debugging or serialization.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_object_property_range_OWLObjectPropertyRange.png
       :alt: UML Class Diagram for OWLObjectPropertyRange
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyRange**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_object_property_range_OWLObjectPropertyRange.pdf
       :alt: UML Class Diagram for OWLObjectPropertyRange
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyRange**

.. py:class:: OWLObjectPropertyRange(property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, expression: pyowl2.abstracts.class_expression.OWLClassExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.property_range.OWLPropertyRange`, :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.object_property_range.OWLObjectPropertyRange
      :parts: 1
      :private-bases:


   This entity represents an axiom within an ontology that constrains the types of individuals which may serve as values for a specific object property. It asserts that for any pair of individuals related by the given property, the target individual must be an instance of the specified class expression, thereby enforcing type consistency across relationships. To utilize this component, instantiate it with the object property expression to be constrained, the class expression defining the allowable range, and an optional list of annotations for metadata. The class provides properties to access and modify the property expression, the range class expression, and any associated annotations, serving as a fundamental building block for defining type safety in object-oriented relationships.

   :parm object_property_expression: The object property expression whose range is defined by this axiom.
   :type object_property_expression: OWLObjectPropertyExpression
   :parm class_expression: The class expression defining the range of the object property, specifying the type of individuals that can be its values.
   :type class_expression: OWLClassExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the OWL object property range axiom, formatted according to a specific functional syntax. The output string encapsulates the axiom's annotations, the object property expression, and the class expression within parentheses. If the axiom contains annotations, they are included in the string; otherwise, an empty list representation is substituted in their place. This method does not modify the object's state and is primarily used for generating human-readable output or logging.

      :return: A string representation of the axiom in the format `ObjectPropertyRange([annotations] property range)`.

      :rtype: str



   .. py:attribute:: _class_expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Updates the range constraint of the object property by assigning a new `OWLClassExpression`. This setter replaces the existing class expression stored within the `OWLObjectPropertyRange` instance, effectively modifying the axiom's definition to reflect the new restriction. The change is immediate and affects the internal state of the object.

      :param value: The OWL class expression to assign to the object.
      :type value: OWLClassExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Assigns the specified object property expression to this instance, replacing any previously held value. The input must be a valid OWLObjectPropertyExpression object. This method directly mutates the internal state of the object to reflect the new association.

      :param value: The object property expression to assign.
      :type value: OWLObjectPropertyExpression

