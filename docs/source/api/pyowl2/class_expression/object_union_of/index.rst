pyowl2.class_expression.object_union_of
=======================================

.. py:module:: pyowl2.class_expression.object_union_of



.. ── LLM-GENERATED DESCRIPTION START ──

An implementation of the OWL object union construct that represents the logical disjunction of multiple class expressions.


Description
-----------


OWLObjectUnionOf models the logical disjunction of multiple class expressions within an ontology, representing individuals that belong to at least one of the constituent classes. The implementation enforces a canonical internal representation by automatically sorting the provided list of expressions during initialization and modification, which ensures consistency for comparisons and hashing regardless of the input order. It requires a minimum of two class expressions to construct a valid union, preventing the creation of degenerate logical structures. Furthermore, the logic provides a string representation that adheres to standard functional syntax, outputting the union operator followed by the sorted components.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_union_of.OWLObjectUnionOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_object_union_of_OWLObjectUnionOf.png
       :alt: UML Class Diagram for OWLObjectUnionOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectUnionOf**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_object_union_of_OWLObjectUnionOf.pdf
       :alt: UML Class Diagram for OWLObjectUnionOf
       :align: center
       :width: 11.5cm
       :class: uml-diagram

       UML Class Diagram for **OWLObjectUnionOf**

.. py:class:: OWLObjectUnionOf(expressions: list[pyowl2.abstracts.class_expression.OWLClassExpression])

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.object_union_of.OWLObjectUnionOf
      :parts: 1
      :private-bases:


   This class models a logical union (disjunction) of class expressions, defining a group of individuals that belong to at least one of the constituent classes. It is used to construct complex, inclusive definitions within an ontology by combining multiple class criteria. When initializing or modifying this object, a list of at least two `OWLClassExpression` instances must be provided; the list is automatically sorted to ensure a consistent internal representation.

   :parm classes_expressions: Sorted list of class expressions comprising the union, containing at least two elements.
   :type classes_expressions: list[OWLClassExpression]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object union expression. The output is formatted by concatenating the literal "ObjectUnionOf(" with the string representations of the constituent class expressions, which are joined by single spaces, and terminating with a closing parenthesis. This method provides a standard functional syntax view of the logical structure without modifying the object's state.

      :return: A string representation of the object union, formatted as "ObjectUnionOf(...)" containing the string representations of the constituent class expressions.

      :rtype: str



   .. py:attribute:: _classes_expressions
      :type:  list[pyowl2.abstracts.class_expression.OWLClassExpression]


   .. py:property:: classes_expressions
      :type: list[pyowl2.abstracts.class_expression.OWLClassExpression]


      Assigns a new list of class expressions to serve as the operands for this union. The input list is sorted before being stored internally to maintain a consistent, canonical order, regardless of the order provided by the caller. This method replaces the existing collection of expressions rather than modifying it in place.

      :param value: A list of OWL class expressions to assign. The list will be sorted before storage.
      :type value: list[OWLClassExpression]

