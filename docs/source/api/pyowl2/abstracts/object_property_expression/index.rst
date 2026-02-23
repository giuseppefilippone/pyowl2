pyowl2.abstracts.object_property_expression
===========================================

.. py:module:: pyowl2.abstracts.object_property_expression



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class defining the interface for object property expressions in an OWL ontology, encompassing both named properties and complex constructs like inverse properties.


Description
-----------


By extending the base ``OWLObject`` class and utilizing the Abstract Base Class module, the structure ensures that all concrete implementations adhere to a consistent interface for representing relationships between individuals. It serves as a polymorphic type that unifies simple named properties with more complex constructs, such as inverse properties, allowing the reasoning system to treat them uniformly. The design mandates that subclasses provide specific logic to identify whether an expression represents the universal top property or the empty bottom property, which are essential logical constants for semantic reasoning. This abstraction facilitates the manipulation and evaluation of property hierarchies without exposing the underlying complexity of specific property types.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_abstracts_object_property_expression_OWLObjectPropertyExpression.png
       :alt: UML Class Diagram for OWLObjectPropertyExpression
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyExpression**

.. only:: latex

    .. figure:: /_uml/pyowl2_abstracts_object_property_expression_OWLObjectPropertyExpression.pdf
       :alt: UML Class Diagram for OWLObjectPropertyExpression
       :align: center
       :width: 14.7cm
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyExpression**

.. py:class:: OWLObjectPropertyExpression

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression
      :parts: 1
      :private-bases:


   This abstract base class defines the interface for expressions that represent relationships between individuals in an OWL ontology, covering both simple named properties and complex constructs such as inverse properties. It acts as a common type for any entity functioning as an object property, allowing the system to treat various property forms uniformly. Furthermore, it mandates the implementation of methods to identify if the expression corresponds to the universal (top) or empty (bottom) property, which are specific logical constants used in reasoning.


   .. py:method:: is_bottom_object_property() -> bool
      :abstractmethod:


      Determines whether this object property expression represents the bottom object property, which is the property that no pair of individuals can satisfy. In the context of the Web Ontology Language (OWL), this corresponds to `owl:bottomObjectProperty` and acts as the logical equivalent of "false" for property expressions. The method returns True if the expression is the bottom property and False otherwise, serving as a read-only check that does not alter the state of the object.

      :return: True if this property is the bottom object property (the property that relates no individuals), False otherwise.

      :rtype: bool



   .. py:method:: is_top_object_property() -> bool
      :abstractmethod:


      Determines whether this object property expression corresponds to the universal top object property, which is the property that relates every possible pair of individuals in the ontology. This method returns True if the expression is the top property, and False for any other property, including named properties or complex expressions like inverse or property chains. The check is purely evaluative and does not produce any side effects or modifications to the ontology.

      :return: True if the property is the top object property in the hierarchy, otherwise False.

      :rtype: bool



   .. py:attribute:: __slots__
      :value: ()


