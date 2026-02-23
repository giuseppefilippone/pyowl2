pyowl2.axioms.object_property_axiom.reflexive_object_property
=============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.reflexive_object_property



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing an OWL axiom that asserts a specific object property relates every individual to itself.


Description
-----------


The software implements a representation of the Web Ontology Language (OWL) concept of reflexivity, specifically for object properties. By extending the base axiom class, it allows logical reasoners to infer that for any individual, a relationship exists between that individual and itself via the specified property. The design encapsulates a target object property expression, which can be a named property or an inverse property, along with optional metadata annotations that provide context or human-readable information. Functionality includes managing the internal state of the property expression through property accessors and generating a human-readable string representation that displays the axiom type and its components for debugging or logging purposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.reflexive_object_property.OWLReflexiveObjectProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_reflexive_object_property_OWLReflexiveObjectProperty.png
       :alt: UML Class Diagram for OWLReflexiveObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLReflexiveObjectProperty**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_reflexive_object_property_OWLReflexiveObjectProperty.pdf
       :alt: UML Class Diagram for OWLReflexiveObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLReflexiveObjectProperty**

.. py:class:: OWLReflexiveObjectProperty(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.reflexive_object_property.OWLReflexiveObjectProperty
      :parts: 1
      :private-bases:


   This class represents an axiom in the Web Ontology Language (OWL) that declares a specific object property to be reflexive, meaning that every individual in the ontology is necessarily related to itself through that property. It is typically used to model relationships where self-reference is a universal truth, such as a 'hasIdentity' property. To utilize this class, instantiate it with the target `OWLObjectPropertyExpression` and, optionally, a list of `OWLAnnotation` objects to provide metadata about the axiom. Once asserted, this axiom enables logical reasoners to infer that for any individual $x$, the statement $P(x, x)$ holds true.

   :parm object_property_expression: The object property expression that is asserted to be reflexive, meaning it relates every individual to itself.
   :type object_property_expression: OWLObjectPropertyExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the reflexive object property axiom, formatted to display the axiom type, its annotations, and the associated object property expression. The output string follows the pattern 'ReflexiveObjectProperty([annotations] property_expression)', where the annotations list is populated if annotations exist or displayed as an empty list otherwise. This method does not modify the object's state and is primarily used for generating human-readable output for debugging or display.

      :return: A string representation of the reflexive object property axiom, including its annotations and object property expression.

      :rtype: str



   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Assigns the specified object property expression to this axiom, defining the property that is asserted to be reflexive. This method updates the internal state by replacing the existing property expression with the provided `OWLObjectPropertyExpression` instance. It serves as the setter for the corresponding property, allowing the subject of the reflexive axiom to be modified after initialization.

      :param value: The object property expression to assign.
      :type value: OWLObjectPropertyExpression

