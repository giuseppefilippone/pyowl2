pyowl2.axioms.object_property_axiom.inverse_object_properties
=============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.inverse_object_properties



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a data structure representing an OWL axiom that declares two object properties to be inverses of one another.


Description
-----------


The software models a specific type of Web Ontology Language (OWL) axiom used to define reciprocal relationships between two object properties. By storing references to two distinct object property expressions, it establishes a logical constraint where the existence of a relationship defined by the first property implies the existence of a relationship defined by the second property in the opposite direction. This structure allows reasoning systems to infer bidirectional connections between entities, such as linking a "hasParent" property with an "isChildOf" property. In addition to holding the core property expressions, the implementation supports the attachment of metadata annotations and provides a string representation formatted according to OWL functional syntax for serialization or debugging purposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_inverse_object_properties_OWLInverseObjectProperties.png
       :alt: UML Class Diagram for OWLInverseObjectProperties
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLInverseObjectProperties**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_inverse_object_properties_OWLInverseObjectProperties.pdf
       :alt: UML Class Diagram for OWLInverseObjectProperties
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLInverseObjectProperties**

.. py:class:: OWLInverseObjectProperties(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, inverse_expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.inverse_object_properties.OWLInverseObjectProperties
      :parts: 1
      :private-bases:


   This class represents an axiom within an ontology that declares two object properties to be inverses of one another. It establishes a logical rule where if the first property relates an individual A to an individual B, the second property must necessarily relate B to A. To use this class, instantiate it with the two property expressions that form the inverse pair, optionally providing a list of annotations to attach metadata to the axiom. This structure is essential for defining reciprocal relationships, such as linking "hasParent" with "isChildOf", thereby allowing reasoning systems to infer bidirectional connections between entities.

   :parm object_property_expression: The object property expression declared to be the inverse of the second property expression.
   :type object_property_expression: OWLObjectPropertyExpression
   :parm inverse_object_property_expression: The object property expression that is declared to be the inverse of the first property expression.
   :type inverse_object_property_expression: OWLObjectPropertyExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the inverse object properties axiom, formatted to display the annotations and the two related object property expressions. The output string starts with the identifier "InverseObjectProperties" and includes the list of annotations, the primary object property expression, and the inverse object property expression. If the axiom has associated annotations, they are rendered within the string; otherwise, an empty list is explicitly included to preserve the structural format.

      :return: Returns a string representation of the inverse object properties axiom in functional syntax.

      :rtype: str



   .. py:attribute:: _inverse_object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: inverse_object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Sets the object property expression that constitutes the inverse relationship within this axiom. This method updates the internal attribute to the provided `OWLObjectPropertyExpression`, overwriting any previous value.

      :param value: The OWL object property expression to assign.
      :type value: OWLObjectPropertyExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Assigns the specified object property expression to this instance, effectively updating one side of the inverse relationship defined by the axiom. The provided value, which must be an instance of `OWLObjectPropertyExpression`, replaces the existing property expression stored internally. This method modifies the object's state in place and does not return a value.

      :param value: The OWL object property expression to assign to the instance.
      :type value: OWLObjectPropertyExpression

