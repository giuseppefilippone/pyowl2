pyowl2.axioms.object_property_axiom.asymmetric_object_property
==============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.asymmetric_object_property



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a data structure for representing the Web Ontology Language axiom that declares an object property to be asymmetric.


Description
-----------


The logic encapsulated here enforces a semantic constraint where if an individual A is related to individual B via a specific property, B cannot be related back to A using that same property. This structure stores the target object property expression and optionally accepts a list of annotations to attach metadata or context to the logical statement. By inheriting from a base object property axiom class, the implementation integrates seamlessly into the ontology structure while delegating the management of annotations to the parent initialization. A string representation method generates a functional syntax format, which is useful for debugging, logging, or serializing the axiom in a human-readable form that explicitly lists annotations and the property expression.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.asymmetric_object_property.OWLAsymmetricObjectProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_asymmetric_object_property_OWLAsymmetricObjectProperty.png
       :alt: UML Class Diagram for OWLAsymmetricObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAsymmetricObjectProperty**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_asymmetric_object_property_OWLAsymmetricObjectProperty.pdf
       :alt: UML Class Diagram for OWLAsymmetricObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAsymmetricObjectProperty**

.. py:class:: OWLAsymmetricObjectProperty(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.asymmetric_object_property.OWLAsymmetricObjectProperty
      :parts: 1
      :private-bases:


   This class represents an axiom in the Web Ontology Language (OWL) that declares a specific object property to be asymmetric. Semantically, this constraint ensures that if an individual A is related to an individual B through the specified property, then B cannot be related to A through the same property, effectively defining a one-way relationship. It is commonly used to model concepts such as parenthood or temporal precedence where reciprocity is logically impossible. To use this class, instantiate it with the target `OWLObjectPropertyExpression` and, optionally, a list of `OWLAnnotation` objects to attach metadata or context to the axiom.

   :param object_property_expression: The object property expression that is declared to be asymmetric.
   :type object_property_expression: OWLObjectPropertyExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the asymmetric object property axiom, formatted to resemble a functional syntax declaration. The output string includes the axiom annotations followed by the object property expression. If the axiom contains annotations, they are listed explicitly; otherwise, an empty list is displayed in their place. This method is primarily used for debugging or logging purposes to provide a readable snapshot of the object's state.

      :return: A string representation of the asymmetric object property axiom, including its annotations and object property expression.

      :rtype: str



   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Sets the object property expression for this asymmetric object property axiom, identifying the specific property that is subject to the asymmetry constraint. This operation overwrites the existing property expression stored in the instance with the provided value.

      :param value: The object property expression to assign.
      :type value: OWLObjectPropertyExpression

