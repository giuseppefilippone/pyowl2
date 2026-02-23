pyowl2.axioms.object_property_axiom.irreflexive_object_property
===============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.irreflexive_object_property



.. ── LLM-GENERATED DESCRIPTION START ──

Models an OWL axiom that declares a specific object property to be irreflexive, meaning no individual can be related to itself through that property.


Description
-----------


The implementation extends the base object property axiom class to encapsulate the logic required for irreflexivity constraints within an ontology. By storing a specific object property expression, the software ensures that the relationship defined by that expression cannot hold between an entity and itself, which is crucial for modeling distinct entities such as parent-child relationships. Optional annotations are supported to allow users to attach metadata or human-readable descriptions directly to the axiom, inheriting this capability from the parent class structure. A string representation method generates the functional syntax output, dynamically including any associated annotations to facilitate serialization or debugging of the ontology structure.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_irreflexive_object_property_OWLIrreflexiveObjectProperty.png
       :alt: UML Class Diagram for OWLIrreflexiveObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLIrreflexiveObjectProperty**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_irreflexive_object_property_OWLIrreflexiveObjectProperty.pdf
       :alt: UML Class Diagram for OWLIrreflexiveObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLIrreflexiveObjectProperty**

.. py:class:: OWLIrreflexiveObjectProperty(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.irreflexive_object_property.OWLIrreflexiveObjectProperty
      :parts: 1
      :private-bases:


   This class models an axiom within the Web Ontology Language (OWL) that declares a specific object property to be irreflexive. By asserting this axiom, a user specifies that no individual in the ontology can be related to itself through the given property expression. It is typically used to define constraints for relationships where self-reference is logically impossible or undesirable, such as "hasParent" or "isPredecessorOf". The class accepts the target property expression and an optional list of annotations to provide metadata about the axiom itself.

   :parm object_property_expression: The property expression that is asserted to be irreflexive by this axiom.
   :type object_property_expression: OWLObjectPropertyExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the irreflexive object property axiom in a functional syntax format. The method checks for the presence of axiom annotations, including them in the output if they exist, or substituting an empty list otherwise. The resulting string always contains the specific object property expression associated with the axiom.

      :return: A string representation of the axiom, formatted as `IrreflexiveObjectProperty([annotations] object_property_expression)`.

      :rtype: str



   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Updates the object property expression associated with this irreflexive object property axiom. It assigns the provided `OWLObjectPropertyExpression` instance to the internal storage, overwriting any previously held value. This setter allows the specific property being defined as irreflexive to be modified after the axiom's initialization.

      :param value: The object property expression to assign to the entity.
      :type value: OWLObjectPropertyExpression

