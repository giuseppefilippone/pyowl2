pyowl2.axioms.object_property_axiom.equivalent_object_properties
================================================================

.. py:module:: pyowl2.axioms.object_property_axiom.equivalent_object_properties



.. ── LLM-GENERATED DESCRIPTION START ──

Models an OWL axiom declaring that a collection of object properties are semantically equivalent to one another.


Description
-----------


The implementation ensures that any relationship defined by one property in the group holds true for all others, which is a fundamental concept in ontology engineering for defining synonyms or interchangeable relations. To maintain data integrity, the logic requires at least two object property expressions upon initialization, preventing the creation of trivial or malformed axioms. A key design choice involves automatically sorting the internal list of expressions whenever the object is created or modified, which guarantees a canonical representation and simplifies comparison operations. Optional annotations can be attached to the axiom to provide metadata, and the string representation is formatted to resemble standard functional syntax for easier debugging and logging.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_equivalent_object_properties_OWLEquivalentObjectProperties.png
       :alt: UML Class Diagram for OWLEquivalentObjectProperties
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLEquivalentObjectProperties**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_equivalent_object_properties_OWLEquivalentObjectProperties.pdf
       :alt: UML Class Diagram for OWLEquivalentObjectProperties
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLEquivalentObjectProperties**

.. py:class:: OWLEquivalentObjectProperties(expressions: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.equivalent_object_properties.OWLEquivalentObjectProperties
      :parts: 1
      :private-bases:


   This class models an axiom used to declare that a group of object properties are semantically equivalent, implying that any relationship defined by one property holds true for the others. To utilize this class, instantiate it with a list containing at least two object property expressions; providing fewer than two will raise an assertion error. The input expressions are automatically sorted upon initialization and modification to maintain a consistent internal order, and optional annotations may be attached to provide additional context or metadata about the equivalence statement.

   :parm object_property_expressions: Internal storage for the sorted list of object property expressions declared to be equivalent. The list is guaranteed to contain at least two expressions.
   :type object_property_expressions: list[OWLObjectPropertyExpression]


   .. py:method:: __str__() -> str

      Returns a string representation of the equivalent object properties axiom, formatted to resemble a functional syntax or constructor call. The representation includes the axiom's annotations, displaying an empty list if no annotations are present, followed by the sequence of object property expressions joined by spaces. This method ensures a consistent textual format for debugging or logging purposes without modifying the underlying object state.

      :return: A string representation of the object, formatted as 'EquivalentObjectProperties(...)' including the annotations and object property expressions.

      :rtype: str



   .. py:attribute:: _object_property_expressions
      :type:  list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


   .. py:property:: object_property_expressions
      :type: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


      Updates the collection of object property expressions that constitute this equivalence axiom. The provided list of expressions is sorted before being assigned to the internal state, ensuring a canonical order is maintained. This method replaces the existing set of properties and creates a new list instance, meaning subsequent modifications to the input list will not affect the object's state.

      :param value: A list of OWL object property expressions to assign. The list will be sorted internally before storage.
      :type value: list[OWLObjectPropertyExpression]

