pyowl2.axioms.data_property_axiom.sub_data_property_of
======================================================

.. py:module:: pyowl2.axioms.data_property_axiom.sub_data_property_of



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing an OWL axiom that asserts one data property is a sub-property of another.


Description
-----------


The class ``OWLSubDataPropertyOf`` models a specific type of axiom within the Web Ontology Language (OWL) used to define a hierarchical relationship where one data property is a specialization of another. By storing references to both the sub-property and super-property expressions, the implementation ensures that any logical inference or validation involving the sub-property automatically applies to the super-property as well. Construction of the object requires these two property expressions, and it optionally accepts a list of annotations to attach metadata or contextual information, which are managed through inheritance from the base axiom class. To facilitate debugging or serialization, the logic includes a string representation method that outputs the relationship in standard OWL functional syntax, explicitly handling the presence or absence of annotations in the output format.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_data_property_axiom_sub_data_property_of_OWLSubDataPropertyOf.png
       :alt: UML Class Diagram for OWLSubDataPropertyOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSubDataPropertyOf**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_data_property_axiom_sub_data_property_of_OWLSubDataPropertyOf.pdf
       :alt: UML Class Diagram for OWLSubDataPropertyOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSubDataPropertyOf**

.. py:class:: OWLSubDataPropertyOf(sub_property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, super_property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.data_property_axiom.sub_data_property_of.OWLSubDataPropertyOf
      :parts: 1
      :private-bases:


   This axiom defines a hierarchical relationship between two data properties within an OWL ontology, asserting that the first property is a subproperty of the second. By establishing this relationship, it implies that any individual associated with a specific value via the subproperty is also implicitly associated with that same value via the superproperty. To construct this axiom, provide the specific subproperty expression and the general superproperty expression, optionally including a list of annotations to attach metadata or contextual information to the statement.

   :parm sub_data_property_expression: The data property expression declared as the subproperty, representing the more specific property in the relationship.
   :type sub_data_property_expression: OWLDataPropertyExpression
   :parm super_data_property_expression: The data property expression that serves as the superproperty (the more general property) in the subproperty relationship.
   :type super_data_property_expression: OWLDataPropertyExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the OWL sub-data-property axiom in a functional syntax format. The representation includes the axiom annotations, the sub-data property expression, and the super-data property expression. If no annotations are present, an empty list is explicitly rendered in the output string.

      :return: Returns a string representation of the axiom in functional syntax, including the sub-property, super-property, and any associated annotations.

      :rtype: str



   .. py:attribute:: _sub_data_property_expression
      :type:  pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


   .. py:attribute:: _super_data_property_expression
      :type:  pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


   .. py:property:: sub_data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Sets the sub-data property expression for this OWL sub-data property axiom. This method accepts an `OWLDataPropertyExpression` object and assigns it to the internal state, overwriting any existing value stored for the sub-property. As a setter, it directly modifies the object's internal representation to reflect the new hierarchical relationship between data properties.

      :param value: The OWL data property expression to assign as the sub-data-property expression.
      :type value: OWLDataPropertyExpression


   .. py:property:: super_data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Sets the super data property expression for this `OWLSubDataPropertyOf` axiom, defining the parent property in the sub-property relationship. This method accepts an instance of `OWLDataPropertyExpression` and updates the internal state by overwriting the existing value stored in the private attribute. It serves as the setter for the corresponding property, ensuring that the axiom reflects the specified hierarchical relationship between data properties.

      :param value: The data property expression to assign as the super property.
      :type value: OWLDataPropertyExpression

