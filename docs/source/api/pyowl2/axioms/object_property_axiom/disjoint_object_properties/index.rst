pyowl2.axioms.object_property_axiom.disjoint_object_properties
==============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.disjoint_object_properties



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing an OWL axiom that asserts a collection of object properties are mutually exclusive and cannot relate the same pair of individuals.


Description
-----------


It models the semantic constraint where specific relationship types within an ontology cannot overlap, ensuring that if one property links two individuals, no other property in the defined set can link the same pair. The implementation enforces a canonical internal representation by automatically sorting the provided list of property expressions, which simplifies comparison and structural consistency regardless of the input order. Validation logic ensures that at least two property expressions are supplied during initialization, as disjointness is a relationship that requires multiple entities to be meaningful. Inheritance from the base object property axiom class allows for the attachment of optional annotations, providing a mechanism to add metadata or contextual information to the logical constraint.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_disjoint_object_properties_OWLDisjointObjectProperties.png
       :alt: UML Class Diagram for OWLDisjointObjectProperties
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDisjointObjectProperties**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_disjoint_object_properties_OWLDisjointObjectProperties.pdf
       :alt: UML Class Diagram for OWLDisjointObjectProperties
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDisjointObjectProperties**

.. py:class:: OWLDisjointObjectProperties(expressions: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.disjoint_object_properties.OWLDisjointObjectProperties
      :parts: 1
      :private-bases:


   This class models a semantic axiom asserting that a collection of object properties are mutually exclusive, meaning no single pair of individuals can be related by more than one of these properties simultaneously. It is typically used to define strict separation between relationship types within an ontology, such as ensuring that a "parent of" relationship cannot also be a "sibling of" relationship for the same entities. When constructing an instance, users must provide a list of at least two object property expressions; the class automatically sorts this list to ensure a canonical internal representation. Additionally, optional annotations may be supplied to attach metadata or contextual information to the axiom.

   :parm object_property_expressions: The sorted list of object property expressions declared to be disjoint, indicating that they cannot relate the same pair of individuals.
   :type object_property_expressions: list[OWLObjectPropertyExpression]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the disjoint object properties axiom, formatted to resemble a functional syntax constructor. The string includes the axiom annotations, defaulting to an empty list representation if none are present, followed by the string representations of the object property expressions involved in the disjointness relationship. This method has no side effects and does not alter the state of the object.

      :return: A string representation of the disjoint object properties axiom, including any annotations and the list of object property expressions.

      :rtype: str



   .. py:attribute:: _object_property_expressions
      :type:  list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


   .. py:property:: object_property_expressions
      :type: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


      Replaces the current collection of object property expressions involved in this disjointness axiom with the provided list. The input list is sorted before being stored internally to ensure a canonical ordering, which means the sequence of properties in the input does not affect the internal representation. This method directly modifies the internal state of the object.

      :param value: A list of object property expressions to assign. The list will be sorted before storage.
      :type value: list[OWLObjectPropertyExpression]

