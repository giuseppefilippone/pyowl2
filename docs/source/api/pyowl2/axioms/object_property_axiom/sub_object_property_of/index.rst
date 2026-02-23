pyowl2.axioms.object_property_axiom.sub_object_property_of
==========================================================

.. py:module:: pyowl2.axioms.object_property_axiom.sub_object_property_of



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing the OWL SubObjectPropertyOf axiom to establish hierarchical relationships between object properties.


Description
-----------


The implementation models the logical assertion that a specific object property or a chain of properties is a sub-property of a more general object property. By accepting either a simple property expression or a complex property chain as the sub-property, the design accommodates both straightforward hierarchies and intricate logical rules where a sequence of relationships implies a broader connection. Optional annotations can be attached to the axiom to provide metadata, which are managed through inheritance from the base axiom class. A string representation method generates the axiom in functional syntax, ensuring consistent textual output that includes the sub-property, super-property, and any associated annotations.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_sub_object_property_of_OWLSubObjectPropertyOf.png
       :alt: UML Class Diagram for OWLSubObjectPropertyOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSubObjectPropertyOf**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_sub_object_property_of_OWLSubObjectPropertyOf.pdf
       :alt: UML Class Diagram for OWLSubObjectPropertyOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSubObjectPropertyOf**

.. py:class:: OWLSubObjectPropertyOf(sub_property: Union[pyowl2.axioms.object_property_axiom.object_property_chain.OWLObjectPropertyChain, pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], super_property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.sub_object_property_of.OWLSubObjectPropertyOf
      :parts: 1
      :private-bases:


   This class represents an axiom in the Web Ontology Language (OWL) that asserts a hierarchical relationship between two object properties, indicating that the first is a subproperty of the second. It is used to define that any relationship defined by the sub-property expression necessarily implies a relationship defined by the super-property expression. The implementation supports both simple property hierarchies and complex property chains, allowing for the expression of intricate logical rules where a sequence of properties implies a more general property. To use this entity, instantiate it with the specific sub-property expression, the general super-property expression, and an optional list of annotations for metadata.

   :parm sub_object_property_expression: The object property expression or property chain that serves as the subproperty in the relationship.
   :type sub_object_property_expression: typing.Union[OWLObjectPropertyChain, OWLObjectPropertyExpression]
   :parm super_object_property_expression: The object property expression declared to be the superproperty, serving as the more general property in the subproperty relationship.
   :type super_object_property_expression: OWLObjectPropertyExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the sub-object property axiom formatted according to a specific functional syntax. The output string includes the axiom annotations, or an empty list if none are present, followed by the sub-property and super-property expressions. This method ensures that the annotation field is always represented, providing a consistent textual format for the axiom regardless of whether it is annotated.

      :return: A string representation of the axiom in functional syntax format, including the sub-property, super-property, and any annotations.

      :rtype: str



   .. py:attribute:: _sub_object_property_expression
      :type:  Union[pyowl2.axioms.object_property_axiom.object_property_chain.OWLObjectPropertyChain, pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


   .. py:attribute:: _super_object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: sub_object_property_expression
      :type: Union[pyowl2.axioms.object_property_axiom.object_property_chain.OWLObjectPropertyChain, pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


      Sets the sub-property expression for this OWL sub-object property axiom to the provided value. The value can be either a single object property expression or a chain of object properties, accommodating both simple and complex sub-property relationships. This method updates the internal state of the axiom instance to reflect the new sub-property definition.

      :param value: The object property expression or property chain to set as the sub-property.
      :type value: typing.Union[OWLObjectPropertyChain, OWLObjectPropertyExpression]


   .. py:property:: super_object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Sets the super object property expression for this `SubObjectPropertyOf` axiom to the provided value. This operation updates the internal state of the object, effectively defining the parent property in the sub-property relationship by assigning the given `OWLObjectPropertyExpression` to the underlying private attribute.

      :param value: The object property expression to set as the super property.
      :type value: OWLObjectPropertyExpression

