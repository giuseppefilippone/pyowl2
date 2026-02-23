pyowl2.axioms.object_property_axiom.transitive_object_property
==============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.transitive_object_property



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a representation of the Web Ontology Language axiom used to declare a specific object property as transitive.


Description
-----------


The software models the logical concept of transitivity within the Web Ontology Language by providing a structure to assert that a specific relationship holds transitively between individuals. By inheriting from a base axiom class, it leverages existing functionality for handling metadata annotations while focusing on storing the specific object property expression that is being characterized. The implementation ensures that if a property relates entity A to B and B to C, the ontology can infer that the property also relates A to C, which is a fundamental requirement for complex reasoning tasks. A string representation method generates output resembling OWL functional syntax, allowing the axiom to be easily serialized or debugged in a human-readable format that explicitly lists annotations and the target property.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_transitive_object_property_OWLTransitiveObjectProperty.png
       :alt: UML Class Diagram for OWLTransitiveObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLTransitiveObjectProperty**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_transitive_object_property_OWLTransitiveObjectProperty.pdf
       :alt: UML Class Diagram for OWLTransitiveObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLTransitiveObjectProperty**

.. py:class:: OWLTransitiveObjectProperty(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.transitive_object_property.OWLTransitiveObjectProperty
      :parts: 1
      :private-bases:


   This class represents an axiom in the Web Ontology Language (OWL) that declares a specific object property to be transitive. By defining a property as transitive, the ontology enables logical inference where if the property relates individual A to individual B and individual B to individual C, it must also relate individual A to individual C. To use this class, instantiate it with the target `OWLObjectPropertyExpression` that requires this characteristic, optionally providing a list of annotations to attach metadata or context to the axiom.

   :parm object_property_expression: The object property expression that is declared to be transitive.
   :type object_property_expression: OWLObjectPropertyExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the axiom, formatted in a style resembling OWL functional syntax. The output string encapsulates the annotations and the object property expression within a "TransitiveObjectProperty" declaration. If the instance contains annotations, they are included in the string; otherwise, an empty list is substituted to maintain a consistent format.

      :return: A string representation of the transitive object property axiom, including its annotations and the object property expression.

      :rtype: str



   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Assigns the object property expression to which the transitivity rule applies. This method accepts an instance of OWLObjectPropertyExpression and updates the internal state of the axiom, overwriting any previously defined property. It effectively defines the specific property that is being asserted as transitive within the ontology structure.

      :param value: The OWL object property expression to assign to the instance.
      :type value: OWLObjectPropertyExpression

