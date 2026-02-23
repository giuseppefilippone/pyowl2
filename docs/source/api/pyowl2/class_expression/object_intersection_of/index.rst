pyowl2.class_expression.object_intersection_of
==============================================

.. py:module:: pyowl2.class_expression.object_intersection_of



.. ── LLM-GENERATED DESCRIPTION START ──

Represents the logical intersection of multiple OWL class expressions, ensuring a canonical representation through sorting.


Description
-----------


Designed to model the set of individuals that belong to every specified operand, this implementation enforces a strict requirement that the input list contains at least two class expressions. To guarantee that the order of input does not affect the internal state or logical equality, the constituent expressions are automatically sorted during initialization and modification. This canonical sorting mechanism ensures that two intersections defined with the same operands in different orders are treated identically. The resulting structure provides a string representation in functional syntax, wrapping the sorted operands within a standard ``ObjectIntersectionOf`` format for readability and debugging.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_object_intersection_of_OWLObjectIntersectionOf.png
       :alt: UML Class Diagram for OWLObjectIntersectionOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectIntersectionOf**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_object_intersection_of_OWLObjectIntersectionOf.pdf
       :alt: UML Class Diagram for OWLObjectIntersectionOf
       :align: center
       :width: 11.5cm
       :class: uml-diagram

       UML Class Diagram for **OWLObjectIntersectionOf**

.. py:class:: OWLObjectIntersectionOf(expressions: list[pyowl2.abstracts.class_expression.OWLClassExpression])

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.object_intersection_of.OWLObjectIntersectionOf
      :parts: 1
      :private-bases:


   This class expression models the logical intersection of multiple class expressions, defining a set of individuals that belong to all specified operands. It is constructed using a list of `OWLClassExpression` instances, which must contain at least two elements to form a valid intersection. Upon initialization or modification, the constituent expressions are automatically sorted to ensure a canonical representation, meaning the order of input does not affect the internal state or equality.

   :parm classes_expressions: A sorted list of class expressions representing the operands of the intersection, guaranteed to contain at least two elements.
   :type classes_expressions: list[OWLClassExpression]


   .. py:method:: __str__() -> str

      Returns a string representation of the object intersection using a functional syntax format. The method converts each constituent class expression to a string, joins them with spaces, and wraps the result in 'ObjectIntersectionOf(...)'. This provides a readable textual representation suitable for debugging or display purposes.

      :return: A string representation of the object intersection, formatted as 'ObjectIntersectionOf(...)' with the constituent class expressions joined by spaces.

      :rtype: str



   .. py:attribute:: _classes_expressions
      :type:  list[pyowl2.abstracts.class_expression.OWLClassExpression]


   .. py:property:: classes_expressions
      :type: list[pyowl2.abstracts.class_expression.OWLClassExpression]


      Sets the list of class expressions that define this intersection. The provided list is sorted before being assigned to the internal state to ensure a canonical representation, meaning the original order of the input list is not preserved. This operation modifies the object in place and requires that the elements in the list support comparison operations to be sorted successfully.

      :param value: The list of OWL class expressions to assign. The list will be sorted before being stored.
      :type value: list[OWLClassExpression]

