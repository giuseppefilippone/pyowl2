pyowl2.class_expression.object_some_values_from
===============================================

.. py:module:: pyowl2.class_expression.object_some_values_from



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a Python class representing the OWL ObjectSomeValuesFrom existential restriction, which describes individuals connected to a specific class via an object property.


Description
-----------


The software implements a specific construct from the Web Ontology Language known as an existential restriction, defining a set of individuals that must participate in at least one relationship defined by a specific object property with an individual belonging to a particular class. By inheriting from the base class expression type, this implementation integrates into the broader ontology framework, allowing for the creation of complex class definitions based on the properties of related entities rather than intrinsic data. Internally, the structure maintains references to both the object property expression that defines the relationship type and the class expression that acts as the constraint or filler, exposing these components through managed properties to ensure encapsulation. A string representation method is provided to generate a human-readable format of the restriction, facilitating debugging and serialization by combining the string forms of the property and the class expression.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_object_some_values_from_OWLObjectSomeValuesFrom.png
       :alt: UML Class Diagram for OWLObjectSomeValuesFrom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectSomeValuesFrom**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_object_some_values_from_OWLObjectSomeValuesFrom.pdf
       :alt: UML Class Diagram for OWLObjectSomeValuesFrom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectSomeValuesFrom**

.. py:class:: OWLObjectSomeValuesFrom(property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, expression: pyowl2.abstracts.class_expression.OWLClassExpression)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.object_some_values_from.OWLObjectSomeValuesFrom
      :parts: 1
      :private-bases:


   This class models an existential restriction within the Web Ontology Language (OWL), defining a set of individuals that must be connected to at least one member of a specific class through a particular object property. It serves as a complex class expression that constrains the existence of relationships, enabling the definition of classes based on the properties of their neighbors rather than their intrinsic attributes. To utilize this restriction, one must provide an object property expression, which defines the nature of the relationship, and a class expression, which specifies the type of the related individual. This construct is fundamental for creating nuanced ontological definitions, such as describing a "Parent" as an entity that has at least one child who is a "Person".

   :parm object_property_expression: The object property expression defining the relationship between the subject individual and the class expression, which may be a simple property or a complex expression involving inverses.
   :type object_property_expression: OWLObjectPropertyExpression
   :parm class_expression: The class expression defining the type of individuals that the subject individual must be related to via the object property expression.
   :type class_expression: OWLClassExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the OWL existential restriction defined by this object. The representation follows the format "ObjectSomeValuesFrom({property} {class})", where {property} corresponds to the object property expression and {class} corresponds to the class expression associated with the restriction. This method does not modify the object's state and relies on the string representations of the internal property and class expressions to construct the output.

      :return: A string representation of the object, formatted as 'ObjectSomeValuesFrom(property_expression class_expression)'.

      :rtype: str



   .. py:attribute:: _class_expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Assigns a new class expression to this `OWLObjectSomeValuesFrom` restriction, replacing the existing filler. The provided value, which must be an instance of `OWLClassExpression`, is stored internally and defines the range of the existential restriction. This operation modifies the object's state in place and does not return a value.

      :param value: The OWL class expression to assign.
      :type value: OWLClassExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Assigns the specified object property expression to this existential restriction instance. This method serves as the setter for the `object_property_expression` attribute, updating the internal state to reflect the new property relationship defined by the provided `OWLObjectPropertyExpression`. It directly modifies the underlying private attribute, potentially altering the semantic meaning of the class expression within the ontology structure.

      :param value: The object property expression to assign.
      :type value: OWLObjectPropertyExpression

