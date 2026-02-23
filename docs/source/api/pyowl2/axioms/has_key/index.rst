pyowl2.axioms.has_key
=====================

.. py:module:: pyowl2.axioms.has_key



.. ── LLM-GENERATED DESCRIPTION START ──

Implements the OWL HasKey axiom to define unique identifiers for class instances using a combination of object and data properties.


Description
-----------


The software defines a structure for representing the OWL HasKey axiom, which asserts that a specific class expression is uniquely identified by a set of property expressions. By combining object and data properties, the axiom enforces a constraint that no two distinct individuals of the class can share identical values for all specified properties, thereby supporting efficient data retrieval and reasoning. The design ensures internal consistency by automatically sorting the provided property lists upon initialization and modification, maintaining a canonical order regardless of input sequence. Additionally, the implementation supports optional annotations for metadata and provides a string representation following a functional-style syntax to facilitate debugging and serialization.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.has_key.OWLHasKey


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_has_key_OWLHasKey.png
       :alt: UML Class Diagram for OWLHasKey
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLHasKey**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_has_key_OWLHasKey.pdf
       :alt: UML Class Diagram for OWLHasKey
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLHasKey**

.. py:class:: OWLHasKey(expression: pyowl2.abstracts.class_expression.OWLClassExpression, object_properties: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], data_properties: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_axiom.OWLClassAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.has_key.OWLHasKey
      :parts: 1
      :private-bases:


   This entity represents an OWL axiom used to declare that a specific class possesses a set of properties—comprising both object and data properties—that function as a unique key for its instances. By defining this key, the ontology asserts that no two distinct individuals of the specified class can share identical values for all the listed properties, thereby facilitating efficient retrieval and reasoning. To construct this axiom, provide the class expression to which the key applies, along with lists of the object and data property expressions that form the key; optional annotations may also be supplied to attach metadata. The implementation automatically sorts the provided property lists to maintain a canonical order.

   :parm class_expression: The class expression specifying the type of individuals for which the associated properties act as a unique key.
   :type class_expression: OWLClassExpression
   :parm object_property_expressions: A sorted list of object property expressions that form part of the key, used to uniquely identify instances by their relationships to other individuals.
   :type object_property_expressions: list[OWLObjectPropertyExpression]
   :parm data_property_expressions: A list of data property expressions that form part of the key, relating individuals to data values to uniquely identify instances of the class.
   :type data_property_expressions: list[OWLDataPropertyExpression]


   .. py:method:: __str__() -> str

      Returns a string representation of the HasKey axiom, formatted according to a functional-style syntax. The output string concatenates the axiom's annotations, the target class expression, and the sequences of object and data property expressions that define the key. If the axiom contains annotations, they are included in the string; otherwise, an empty list placeholder is used. This method relies on the string conversion of the internal components and does not modify the object's state.

      :return: Returns a functional-style string representation of the HasKey axiom, including the class expression, property expressions, and any annotations.

      :rtype: str



   .. py:attribute:: _class_expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:attribute:: _data_property_expressions
      :type:  list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


   .. py:attribute:: _object_property_expressions
      :type:  list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Updates the OWL class expression associated with this HasKey axiom. This method assigns the provided `OWLClassExpression` instance to the internal attribute, thereby modifying the state of the object to reflect the new class context for the key constraint.

      :param value: The OWL class expression to assign to the property.
      :type value: OWLClassExpression


   .. py:property:: data_property_expressions
      :type: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


      Updates the collection of data property expressions that define the key constraint by assigning a new list of `OWLDataPropertyExpression` objects. The input list is sorted prior to storage to ensure a consistent, canonical order, which means the order of elements in the provided argument does not affect the final internal state. This method modifies the object's internal state directly and returns nothing.

      :param value: A list of OWL data property expressions to assign to the object.
      :type value: list[OWLDataPropertyExpression]


   .. py:property:: object_property_expressions
      :type: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


      Updates the collection of object property expressions that constitute the key constraint for this axiom. It accepts a list of OWLObjectPropertyExpression instances and assigns them to the internal state. Notably, the provided list is sorted before storage, ensuring that the properties are maintained in a deterministic order regardless of the input sequence.

      :param value: A list of OWL object property expressions to assign.
      :type value: list[OWLObjectPropertyExpression]

