pyowl2.class_expression.object_complement_of
============================================

.. py:module:: pyowl2.class_expression.object_complement_of



.. ── LLM-GENERATED DESCRIPTION START ──

Implements the logical negation of an OWL class expression to represent concepts that do not belong to a specific class.


Description
-----------


The software implements a logical construct for representing negation within an ontology, defining the set of all individuals that do not belong to a specified class expression. Acting as a wrapper around another expression, which may be a simple named class or a complex logical structure, this component inverts membership criteria to represent exclusionary concepts. It encapsulates the operand to be negated, providing mechanisms to access and modify this internal state dynamically to support flexible knowledge representation. Additionally, the implementation generates a human-readable string representation using functional syntax, facilitating debugging and logging by clearly displaying the logical structure of the negation.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_complement_of.OWLObjectComplementOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_object_complement_of_OWLObjectComplementOf.png
       :alt: UML Class Diagram for OWLObjectComplementOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectComplementOf**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_object_complement_of_OWLObjectComplementOf.pdf
       :alt: UML Class Diagram for OWLObjectComplementOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectComplementOf**

.. py:class:: OWLObjectComplementOf(expression: pyowl2.abstracts.class_expression.OWLClassExpression)

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.object_complement_of.OWLObjectComplementOf
      :parts: 1
      :private-bases:


   This class represents a logical negation within an ontology, defining the set of all individuals that do not belong to a specified class expression. It serves as a wrapper around another class expression, which may be a simple named class or a complex logical construct, effectively inverting its membership criteria to represent concepts such as "non-human" or "not a parent." To utilize this functionality, an instance is created by passing the target class expression to the constructor, and the internal expression can be accessed or modified via the corresponding property, enabling the dynamic definition of exclusionary constraints in knowledge representation.

   :parm expression: The class expression acting as the operand for the complement operation, representing the specific class being negated.
   :type expression: OWLClassExpression


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object complement using a functional syntax style. The output is constructed by concatenating the class name with the string representation of the internal expression, enclosed in parentheses. This method is primarily used for debugging and logging, and it relies on the nested expression having a valid string conversion method, though it does not modify the object's state.

      :return: A string representation of the object, formatted as "ObjectComplementOf(expression)".

      :rtype: str



   .. py:attribute:: _expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:property:: expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Updates the class expression that serves as the operand for this object complement. The method accepts a single argument, `value`, which should be an instance of `OWLClassExpression`. Assigning this value modifies the internal state of the object, specifically replacing the stored expression with the new one provided.

      :param value:
      :type value: OWLClassExpression

