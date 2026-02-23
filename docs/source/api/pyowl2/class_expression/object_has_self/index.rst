pyowl2.class_expression.object_has_self
=======================================

.. py:module:: pyowl2.class_expression.object_has_self



.. ── LLM-GENERATED DESCRIPTION START ──

OWLObjectHasSelf models a Web Ontology Language (OWL) class expression that restricts individuals to those related to themselves via a specific object property.


Description
-----------


It represents a specific type of existential restriction where an individual must satisfy a relationship with itself using a designated object property. The implementation encapsulates an object property expression, which can range from a simple property to more complex constructs like inverse properties, serving as the criteria for the self-relation. By providing getter and setter mechanisms, the design allows the underlying property expression to be modified dynamically after instantiation, altering the semantic definition of the restriction. A string representation method is included to generate a human-readable format, typically used for debugging or displaying the structure of the ontology concept.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_has_self.OWLObjectHasSelf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_object_has_self_OWLObjectHasSelf.png
       :alt: UML Class Diagram for OWLObjectHasSelf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectHasSelf**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_object_has_self_OWLObjectHasSelf.pdf
       :alt: UML Class Diagram for OWLObjectHasSelf
       :align: center
       :width: 14.8cm
       :class: uml-diagram

       UML Class Diagram for **OWLObjectHasSelf**

.. py:class:: OWLObjectHasSelf(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.object_has_self.OWLObjectHasSelf
      :parts: 1
      :private-bases:


   This class models a specific type of existential restriction in the Web Ontology Language (OWL) where an individual is required to be related to itself via a designated object property. It encapsulates a property expression, which can be a simple property or a complex inverse or chain, to define the criteria for self-relation. To utilize this restriction, instantiate it with the desired object property expression; the resulting object can then be used within class expressions to define concepts such as "self-connected" entities. The property expression is mutable, allowing for dynamic modification of the restriction's definition after instantiation.

   :parm object_property_expression: The object property expression that defines the relationship an individual must have with itself to satisfy the restriction.
   :type object_property_expression: OWLObjectPropertyExpression


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object restriction, formatted as "ObjectHasSelf" followed by the associated object property expression in parentheses. This method relies on the string representation of the underlying object property expression and is typically used for debugging or display purposes.

      :return: A string representation of the object, displaying the class name and the value of `object_property_expression`.

      :rtype: str



   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Updates the object property expression used to define this self-restriction. The method assigns the provided OWLObjectPropertyExpression to the internal state, overwriting any existing value. This modification directly alters the semantic definition of the class expression, affecting how it evaluates individuals in the ontology.

      :param value: The OWL object property expression to assign.
      :type value: OWLObjectPropertyExpression

